
__author__ = "Maximilian Geitner"
__date__ = "10.12.2023"

import numpy as np

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
OUTSIDE = 2

def has_connection(letter, direction):
    if direction == 'S':
        return True
    if direction == NORTH:
        return letter == '|' or letter == 'L' or letter == 'J'
    elif direction == EAST:
        return letter == '-' or letter == 'L' or letter == 'F'
    elif direction == SOUTH:
        return letter == '|' or letter == '7' or letter == 'F'
    elif direction == WEST:
        return letter == '-' or letter == 'J' or letter == '7'
    # all other cases
    return False


def get_pos(x, y, direction):
    if direction == NORTH:
        return x, y - 1
    elif direction == EAST:
        return x + 1, y
    elif direction == SOUTH:
        return x, y + 1
    elif direction == WEST:
        return x - 1, y


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example_2.txt"

    # The pipes are arranged in a two-dimensional grid of tiles:
    #
    #     | is a vertical pipe connecting north and south.
    #     - is a horizontal pipe connecting east and west.
    #     L is a 90-degree bend connecting north and east.
    #     J is a 90-degree bend connecting north and west.
    #     7 is a 90-degree bend connecting south and west.
    #     F is a 90-degree bend connecting south and east.
    #     . is ground; there is no pipe in this tile.
    #     S is the starting position of the animal; there is a pipe on this tile,
    #     but your sketch doesn't show what shape the pipe has.

    # 1.) read input
    lines = []
    col_count = 0
    with open(filename) as file:

        for line in file:
            line = line.replace("\n", "")
            lines.append(line)
            col_count = max(len(line), col_count)
    row_count = len(lines)

    # 2) Perform algorithm from part one
    distances = np.zeros(shape=(row_count, col_count), dtype=int)
    start_x, start_y = 0, 0
    for i in range(col_count):
        for j in range(row_count):
            if lines[j][i] == 'S':
                start_x, start_y = (i, j)
                break

    symbols = ['|', '-', 'L', 'J', '7', 'F']
    solution_dist = None
    sol_dist = None
    sol_pipes = None
    valid_tile = None

    for symbol in symbols:
        # reset distances
        distances = np.zeros(shape=(row_count, col_count), dtype=int)
        # is_valid = np.zeros(shape=(cols_count, rows_count), dtype=int)
        valid_tiles = []
        for i in range(col_count):
            for j in range(row_count):
                if i == start_x and j == start_y:
                    distances[j][i] = 0
                else:
                    distances[j][i] = -1

        list1 = list(lines[start_y])
        list1[start_x] = symbol
        lines[start_y] = ''.join(list1)

        # find all pipes in main loop
        current_stack = [(start_x, start_y)]
        distance = 0
        while len(current_stack) > 0:
            next_stack = []
            distance += 1
            for pos_x, pos_y in current_stack:
                # find connecting pipes
                for dir_source in range(4):
                    if has_connection(lines[pos_y][pos_x], dir_source):
                        # look at dest pipe
                        next_x, next_y = get_pos(pos_x, pos_y, dir_source)
                        if has_connection(lines[next_y][next_x], (dir_source + 2) % 4):
                            # both pipes are connected
                            if distances[next_y][next_x] == -1:
                                # print(next_x, next_y, distance)
                                distances[next_y][next_x] = distance
                                next_stack.append((next_x, next_y))
                            elif distances[next_y][next_x] == distance:
                                # visit twice from different directions
                                valid_tiles.append((next_x, next_y))
            current_stack = next_stack

        for pos_x, pos_y in valid_tiles:
            found_distance = distances[pos_y][pos_x]
            # evaluate run
            if solution_dist is None:
                solution_dist = found_distance
                sol_dist = distances
                sol_pipe = symbol
                valid_tile = pos_x, pos_y
            else:
                solution_dist = max(solution_dist, found_distance)
                sol_dist = distances
                sol_pipe = symbol
                valid_tile = pos_x, pos_y
    # 3.)  Identify other related pipe belonging to the main loop
    # 3.a) Setup level
    list1 = list(lines[start_y])
    list1[start_x] = sol_pipe
    lines[start_y] = ''.join(list1)

    current_stack = [valid_tile]
    valid_tiles = np.zeros(shape=(row_count, col_count), dtype=int)
    while current_stack:
        next_stack = []
        for pos_x, pos_y in current_stack:
            valid_tiles[pos_y][pos_x] = 1
            cur_dist = sol_dist[pos_y][pos_x]
            for i in range(4):
                if has_connection(lines[pos_y][pos_x], i):
                    next_x, next_y = get_pos(pos_x, pos_y, i)
                    if sol_dist[next_y][next_x] + 1 == cur_dist and valid_tiles[next_y][next_x] == 0:
                        valid_tiles[next_y][next_x] = 1
                        next_stack.append((next_x, next_y))
        # identify predecessor with less distance to start
        current_stack = next_stack

    # 4.) Create larger more precise representation of map
    prec_level = np.zeros(shape=(row_count * 3, col_count * 3), dtype=int)
    for i in range(col_count):
        for j in range(row_count):
            if lines[j][i] != '.' and valid_tiles[j][i] == 1:
                center_x, center_y = i * 3 + 1, j * 3 + 1
                prec_level[center_y][center_x] = 1
                symbol = lines[j][i]
                # directions
                if has_connection(symbol, NORTH):
                    prec_level[center_y - 1][center_x] = 1
                if has_connection(symbol, EAST):
                    prec_level[center_y][center_x + 1] = 1
                if has_connection(symbol, SOUTH):
                    prec_level[center_y + 1][center_x] = 1
                if has_connection(symbol, WEST):
                    prec_level[center_y][center_x - 1] = 1

    # 5.) identify all outside tiles
    current_stack = [(0, 0)]
    while current_stack:
        next_stack = []
        for pos_x, pos_y in current_stack:
            prec_level[pos_y][pos_x] = OUTSIDE
            for i in range(4):
                next_x, next_y = get_pos(pos_x, pos_y, i)
                if (3 * col_count) > next_x >= 0 and (3 * row_count) > next_y >= 0:
                    # valid tile
                    if prec_level[next_y][next_x] == 0:
                        prec_level[next_y][next_x] = OUTSIDE  # set TO OUTSIDE
                        next_stack.append((next_x, next_y))

        current_stack = next_stack
    # 6.) Identify all inside tiles
    inside_tile_count = 0
    for i in range(col_count):
        for j in range(row_count):
            center_x, center_y = 3 * i + 1, 3 * j + 1
            if prec_level[center_y][center_x] == 0:
                inside_tile_count += 1

    print("Solution Day 10 Part Two: ", inside_tile_count)
