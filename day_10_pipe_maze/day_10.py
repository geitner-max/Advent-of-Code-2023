
__author__ = "Maximilian Geitner"
__date__ = "10.12.2023"

import numpy as np

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


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
        filename = "example.txt"

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
    lines: list = []
    cols_count = 0
    # 1.) read input
    with open(filename) as file:

        for line in file:
            line = line.replace("\n", "")
            lines.append(line)
            cols_count = max(len(line), cols_count)
    rows_count = len(lines)

    # 2.) Find start position
    distances = np.zeros(shape=(cols_count, rows_count), dtype=int)

    start_x, start_y = 0, 0
    for i in range(cols_count):
        for j in range(rows_count):
            if lines[j][i] == 'S':
                start_x, start_y = (i, j)
                break

    # 3.) Test each pipe type at the starting position and calculate farthest pipe away
    symbols = ['|', '-', 'L', 'J', '7', 'F']
    solution_dist = None
    sol_dist = None
    sol_pipes = None
    for symbol in symbols:
        # reset distances
        distances = np.zeros(shape=(cols_count, rows_count), dtype=int)

        valid_tiles = []
        for i in range(cols_count):
            for j in range(rows_count):
                if i == start_x and j == start_y:
                    distances[j][i] = 0
                else:
                    distances[j][i] = -1

        list1 = list(lines[start_y])
        list1[start_x] = symbol
        lines[start_y] = ''.join(list1)
        # Perform Breadth-first-search starting at location 'S'
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
            else:
                solution_dist = max(solution_dist, found_distance)
                sol_dist = distances
                sol_pipe = symbol

    # 4.) Print solution
    print("Solution Day 10 Part 1: ", solution_dist)

