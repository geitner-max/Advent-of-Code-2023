
__author__ = "Maximilian Geitner"
__date__ = "02.12.2023"


# Idea: For each revealed set of cubes, parse the amount of red, green and blue cubes
#       For each game, count the minimum of required red, green and blue cubes
#       Multiply these three counters with each other and sum up all these values for each game to compute the solution
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

                    if cube_type == "blue":
                        req_blue = max(req_blue, amount_shown)
                    elif cube_type == "red":
                        req_red = max(req_red, amount_shown)
                    elif cube_type == "green":
                        req_green = max(req_green, amount_shown)
            # print((req_red * req_green * req_blue))
            possible_games_total += (req_red * req_green * req_blue)

    # Solution
    print("Solution Day 2 Part Two: ", possible_games_total)


