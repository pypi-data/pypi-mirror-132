from random import shuffle, choice

import rethinkdb as r

from avalonBG.db_utils import db_get_value, resolve_key_id
from avalonBG.exception import AvalonBGError
from avalonBG.rules import get_rules


def game_put(payload):
    """
    This function adds rules and roles to players randomly.
        - method: PUT
        - route: /games
        - payload example: {
                               "players": [
                                    {
                                        "name": "name0",
                                        "avatar_index": 0
                                    },
                                    {
                                        "name": "name1",
                                        "avatar_index": 1
                                    },
                                    {
                                        "name": "name2",
                                        "avatar_index": 2
                                    },
                                    {
                                        "name": "name3",
                                        "avatar_index": 3
                                    },
                                    {
                                        "name": "name4",
                                        "avatar_index": 4
                                    }
                               ],
                               "roles": [
                                   "oberon",
                                   "perceval",
                                   "morgan"
                               ]
                           }
        - response example: {
                                "id": "2669a9fe-37c4-4139-ab78-8e3f0d0607d0",
                                "players": [
                                    {
                                        "avatar_index": 0,
                                        "id": "95763b27-de50-4d39-8ac2-2a7010281788",
                                        "name": "name0",
                                        "role": "assassin",
                                        "team": "red"
                                    },
                                    {
                                        ...
                                    },
                                    {
                                        "avatar_index": 4,
                                        "id": "83d21d25-f359-4ddc-9048-69ba1e6cf5b5",
                                        "name": "name4",
                                        "role": "morgan",
                                        "team": "red"
                                    }
                                ]
                            }
    """
    if not payload or set(payload) != {"players", "roles"}:
        raise AvalonBGError("Only 'players' and 'roles' are required!")

    for key, val in payload.items():
        if not isinstance(val, list):
            raise AvalonBGError("Both 'players' and 'roles' must be a list!")

        if key == "players":
            for player in val:
                if not isinstance(player, dict):
                    raise AvalonBGError("'player' must be an object!")

                if set(player) != {"name", "avatar_index"}:
                    raise AvalonBGError("'Only 'name' and 'avatar_index' are required for a player!")

                if not isinstance(player["name"], str):
                    raise AvalonBGError("'name' of a player must be a string!")

                if not isinstance(player["avatar_index"], int):
                    raise AvalonBGError("'avatar_index' of a player must be an int!")

        elif key == "roles":
            for elem in val:
                if not isinstance(elem, str):
                    raise AvalonBGError("Elements in 'roles' must be a string!")

    rules = get_rules()
    min_nb_player = int(min(rules, key=int))
    max_nb_player = int(max(rules, key=int))

    if not min_nb_player <= len(payload["players"]) <= max_nb_player:
        raise AvalonBGError("Player number should be between {} and {}!".format(min_nb_player, max_nb_player))

    if len(payload["players"]) != len(set([player["name"] for player in payload["players"]])):
        raise AvalonBGError("Players name should be unique!")

    for player in payload["players"]:
        if player["name"].isspace() or player["name"] == "":
            raise AvalonBGError("Players' name cannot be empty!")

    if len(payload["roles"]) != len(set(payload["roles"])):
        raise AvalonBGError("Players role should be unique!")

    available_roles = ("oberon", "morgan", "mordred", "perceval")  #TODO: should be a variable
    for role in payload["roles"]:
        if role not in available_roles:
            raise AvalonBGError("Players role should be {}, {}, {} or {}!".format(*available_roles))

    if "morgan" in payload["roles"] and "perceval" not in payload["roles"]:
        raise AvalonBGError("'morgan' is selected but 'perceval' is not!")

    if "perceval" in payload["roles"] and "morgan" not in payload["roles"]:
        raise AvalonBGError("'perceval' is selected but 'morgan' is not!")

    # find rules
    game_rules = rules[str(len(payload["players"]))]

    if len([role for role in payload["roles"] if role != "perceval"]) > game_rules["red"]:
        raise AvalonBGError("Too many red roles chosen!")

    # add roles to players
    players = roles_and_players(
        dict_names_roles=payload,
        max_red=game_rules["red"],
        max_blue=game_rules["blue"]
    )

    # find players
    list_id_players = r.RethinkDB().table("players").insert(players).run()["generated_keys"]

    # find quests
    list_id_quests = r.RethinkDB().table("quests").insert(game_rules["quests"]).run()["generated_keys"]

    inserted_game = r.RethinkDB().table("games").insert(
        {
            "players": list_id_players,
            "quests": list_id_quests,
            "current_id_player": list_id_players[choice(range(len(payload["players"])))],
            "current_quest": 0,
            "nb_quest_unsend": 0
        },
        return_changes=True
    )["changes"][0]["new_val"].run()

    inserted_game.update(
        {
            "players": resolve_key_id(table="players", list_id=inserted_game["players"]),
            "quests": resolve_key_id(table="quests", list_id=inserted_game["quests"])
        }
    )

    return inserted_game


def roles_and_players(dict_names_roles, max_red, max_blue):
    """Check the validity of proposed roles.
    cases break rules: - 1. morgan in the game but Perceval is not
                       - 2. perceval in the game but Morgan is not
                       - 3. Unvalid role
                       - 4. Too many red in the game (or too many blue in the game, checked but impossible)"""

    nb_red, nb_blue = 0, 1
    list_roles = ["merlin"]
    for role in dict_names_roles["roles"]:
        if role in ["mordred", "morgan", "oberon"]:
            nb_red += 1
            list_roles.append(role)
        elif role == "perceval":
            nb_blue += 1
            list_roles.append(role)

    list_roles.extend(["red"]*(max_red-nb_red))
    list_roles.extend(["blue"]*(max_blue-nb_blue))

    shuffle(list_roles)

    bool_assassin = True
    list_players = []
    for ind, role in enumerate(list_roles):
        player = {
            "avatar_index": dict_names_roles["players"][ind]["avatar_index"],
            "name": dict_names_roles["players"][ind]["name"],
            "role": role,
            "team": "blue"
        }

        if role not in ("merlin", "perceval", "blue"):
            player["team"] = "red"
            if bool_assassin:
                bool_assassin = False
                player["assassin"] = True

        list_players.append(player)

    return list_players


def game_guess_merlin(game_id, payload):

    if len(payload) != 1:
        raise AvalonBGError("Only 1 vote required ('assassin')!")

    game = r.RethinkDB().table("games").get(game_id).run()
    if not game:
        raise AvalonBGError("Game's id {} does not exist!".format(game_id))

    if game["nb_quest_unsend"] == 5:
        raise AvalonBGError("Game is over because 5 consecutive laps have been passed : Red team won!")

    assassin_id = list(payload)[0]
    vote_assassin = payload[assassin_id]

    if assassin_id not in game["players"]:
        raise AvalonBGError("Player {} is not in this game!".format(assassin_id))

    if "assassin" not in r.RethinkDB().table("players").get(assassin_id).run():
        raise AvalonBGError("Player {} is not 'assassin'!".format(assassin_id))

    if vote_assassin not in game["players"]:
        raise AvalonBGError("Player {} is not in this game!".format(vote_assassin))

    game = r.RethinkDB().table("games").get(game_id).run()
    if not game:
        raise AvalonBGError("Game's id {} does not exist!".format(game_id))

    result = game.get("result")
    if not result:
        raise AvalonBGError("Game's status is not established!")

    if not result["status"]:
        raise AvalonBGError("Games's status should be 'true' (ie blue team won)!")

    if "guess_merlin_id" in result:
        raise AvalonBGError("Merlin already chosen!")

    result["guess_merlin_id"] = vote_assassin
    if db_get_value("players", vote_assassin, "role") == "merlin":
        result["status"] = False

    updated_game = r.RethinkDB().table("games").get(game_id).update(
        {"result": result},
        return_changes=True
    )["changes"][0]["new_val"].run()

    updated_game.update(
        {
            "players": resolve_key_id(table="players", list_id=updated_game["players"]),
            "quests": resolve_key_id(table="quests", list_id=updated_game["quests"])
        }
    )

    return updated_game
