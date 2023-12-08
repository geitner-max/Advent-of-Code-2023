
__author__ = "Maximilian Geitner"
__date__ = "02.12.2023"


# Idea: For each revealed set of cubes, parse the amount of red, green and blue cubes Compare whether the revealed
# set fullfils the requirement of a maximum of 12 red cubes, 13 green cubes, blue cubes The game is playable if all
# revealed sets fullfil the requirement above Sum up all game ids to compute the solution
if __name__ == '__main__':
    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14
    possible_games_total = 0

    with open(filename) as file:
        for line in file:
            req_red = 0
            req_green = 0
            req_blue = 0
            line = line.replace("\n", "")
            game_possible = True

            parts = line.split(": ")
            game_id = int(parts[0].split(" ")[1])
            revealed_sets = parts[1].split("; ")
            for set_items in revealed_sets:
                parts_cubes_shown = set_items.split(", ")
                for item in parts_cubes_shown:
                    item_splited = item.split(" ")
                    amount_shown, cube_type = int(item_splited[0]), item_splited[1]

                    # print(game_id, amount_shown, cube_type)
                    if cube_type == "blue":
                        if amount_shown > blue_cubes:
                            game_possible = False
                            continue
                    elif cube_type == "red":
                        if amount_shown > red_cubes:
                            game_possible = False
                            continue
                    elif cube_type == "green":
                        if amount_shown > green_cubes:
                            game_possible = False
                            continue
            if game_possible:
                possible_games_total += game_id

    # Solution
    print("Solution Day 2 Part One: ", possible_games_total)

