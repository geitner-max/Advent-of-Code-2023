
__author__ = "Maximilian Geitner"
__date__ = "14.12.2023"

import numpy as np

# The rounded rocks (O) will roll when the platform is tilted, while the cube-shaped rocks (#) will stay in place.
# You note the positions of all of the empty spaces (.) and rocks (your puzzle input)
CUBE_SHAPED_ROCK = 1
ROUNDED_ROCK = 2
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
def get_next_pos(x, y, direction):
    if direction == NORTH:
        return x, y - 1
    elif direction == EAST:
        return x + 1, y
    elif direction == SOUTH:
        return x, y + 1
    else:
        return x - 1, y  # WEST

def compute_rock_movement(input_platform, output_platform, pos_x, pos_y, direction):
    cur_pos_x, cur_pos_y = pos_x, pos_y

    # initial check
    if input_platform[cur_pos_y][cur_pos_x] == CUBE_SHAPED_ROCK:
        # stays at the same spot
        output_platform[cur_pos_y][cur_pos_x] = CUBE_SHAPED_ROCK
    elif input_platform[cur_pos_y][cur_pos_x] == 0:
        return
    else:
        # rounded rock
        while True:
            next_pos_x, next_pos_y = get_next_pos(cur_pos_x, cur_pos_y, direction)
            if 0 <= next_pos_y < rows and 0 <= next_pos_x < cols:
                # valid pos
                if output_platform[next_pos_y][next_pos_x] != 0:
                    # next_spot is blocked, stay at cur_pos
                    break
                else:
                    cur_pos_x, cur_pos_y = next_pos_x, next_pos_y
            else:
                break
        output_platform[cur_pos_y][cur_pos_x] = ROUNDED_ROCK

def simulate_movement(input_platform, direction):
    output = np.zeros(shape=(rows, cols), dtype=int)
    if direction == NORTH:
        for i in range(cols):
            for j in range(rows):
                compute_rock_movement(input_platform, output, i, j, direction)
    elif direction == WEST:
        for j in range(rows):
            for i in range(cols):
                compute_rock_movement(input_platform, output, i, j, direction)
    elif direction == EAST:
        for j in range(rows):
            for i in range(cols - 1, -1, -1):
                compute_rock_movement(input_platform, output, i, j, direction)
    else:
        # SOUTH
        for i in range(cols):
            for j in range(rows - 1, -1, -1):
                compute_rock_movement(input_platform, output, i, j, direction)
    return output


def simulate_cycle(input_platform):
    # north, then west, then south, then east
    output = simulate_movement(input_platform, NORTH)
    output = simulate_movement(output, WEST)
    output = simulate_movement(output, SOUTH)
    output = simulate_movement(output, EAST)
    return output

def is_equal_state(outputs, cur_input):
    for index in range(len(outputs)):
        comp_level = outputs[index]
        is_equal = True
        for i in range(cols):
            for j in range(rows):
                if comp_level[j][i] != cur_input[j][i]:
                    is_equal = False
                    break
            if not is_equal:
                break
        if is_equal:
            return index
    return -1
if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) read input and initialize cur_input
    input_string = []
    with open(filename) as file:

        for line in file:
            line = line.replace("\n", "")
            input_string.append(line)

    rows = len(input_string)
    cols = len(input_string[0])


    cur_input = np.zeros(shape=(rows, cols), dtype=int)
    for x in range(cols):
        for y in range(rows):
            if input_string[y][x] == '#':
                cur_input[y][x] = CUBE_SHAPED_ROCK
            elif input_string[y][x] != '.':
                cur_input[y][x] = ROUNDED_ROCK

    outputs = [cur_input]
    cur_level = cur_input
    index_eq = None

    # 2.) simulate rotation until similar position as before appears
    while True:
        cur_level = simulate_cycle(cur_level)
        # compare state with previous iterations
        index_eq = is_equal_state(outputs, cur_level)
        if index_eq == -1:
            # not equal
            outputs.append(cur_level)
        else:
            outputs.append(cur_level)
            break

    # 3.) calculate offset
    # first_state --> cur_level --> ... --> cur_level
    offset = index_eq
    cycles = len(outputs) - 1 - offset

    # bring offset closest to 1000000000
    cycles_repeat = (1000000000 - offset) // cycles
    cur_index = offset + cycles * cycles_repeat
    for index in range(cur_index, 1000000000):
        cur_level = simulate_cycle(cur_level)


    total = 0
    # 4.) calculate solution
    for j in range(rows):
        load_row = rows - j
        for i in range(cols):
            if cur_level[j][i] == ROUNDED_ROCK:
                total += load_row
    print('Solution Day 14 Part 2: ', total)
    # correct answer: 95273
