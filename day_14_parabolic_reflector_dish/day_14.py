
__author__ = "Maximilian Geitner"
__date__ = "14.12.2023"

import numpy as np

# The rounded rocks (O) will roll when the platform is tilted, while the cube-shaped rocks (#) will stay in place.
# You note the positions of all of the empty spaces (.) and rocks (your puzzle input)
CUBE_SHAPED_ROCK = 1
ROUNDED_ROCK = 2
if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) read input
    input_lines = []
    with open(filename) as file:

        for line in file:
            line = line.replace("\n", "")
            input_lines.append(line)

    rows = len(input_lines)
    cols = len(input_lines[0])

    output = np.zeros(shape=(rows, cols), dtype=int)
    # 2.) All rounded rocks will move to the north (rowIndex decreases) as long as the next tile is empty
    for i in range(cols):
        for j in range(rows):
            cur_pos = j
            if input_lines[j][i] == '#':
                # stays at the same spot
                output[j][i] = CUBE_SHAPED_ROCK
            elif input_lines[j][i] == '.':
                continue
            else:
                # rounded rock
                while True:
                    next_pos = cur_pos - 1
                    if next_pos >= 0:
                        # valid pos
                        if output[next_pos][i] != 0:
                            # next_spot is blocked, stay at cur_pos
                            break
                        else:
                            cur_pos = next_pos
                    elif next_pos < 0:
                        break
                output[cur_pos][i] = ROUNDED_ROCK
    # 3.) Calculate load on support beam by counting rounded rocks
    total = 0
    # calculate solution
    for j in range(rows):
        load_row = rows - j
        for i in range(cols):
            if output[j][i] == ROUNDED_ROCK:
                total += load_row
    print('Solution Day 14 Part 1: ', total)
