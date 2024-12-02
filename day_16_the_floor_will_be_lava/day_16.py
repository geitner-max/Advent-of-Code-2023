
__author__ = "Maximilian Geitner"
__date__ = "16.12.2023"

import numpy as np

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def get_next_direction(tile, direction):
    result = []
    if tile == '.':
        result.append(direction)
    elif tile == '/':
        res_m1 = [EAST, NORTH, WEST, SOUTH]
        result.append(res_m1[direction])
    elif tile == '\\':
        res_m2 = [WEST, SOUTH, EAST, NORTH]
        result.append(res_m2[direction])
    elif tile == '-':
        if direction == WEST or direction == EAST:
            result.append(direction)
        else:
            result.append(WEST)
            result.append(EAST)
    elif tile == '|':
        if direction == NORTH or direction == SOUTH:
            result.append(direction)
        else:
            result.append(NORTH)
            result.append(SOUTH)
    else:

        pass
    return result
def get_next_pos(cur_x, cur_y, direction):
    if direction == NORTH:
        return cur_x, cur_y - 1
    elif direction == EAST:
        return cur_x + 1, cur_y
    elif direction == SOUTH:
        return cur_x, cur_y + 1
    else:
        return cur_x - 1, cur_y

# empty space (.), mirrors (/ and \), and splitters (| and -).
if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    lines = []
    with open(filename) as file:

        for line in file:
            line = line.replace("\n", "")

            lines.append(line)

    rows = len(lines)
    cols = len(lines[0])

    beam_start_conf = [(0, 0, EAST), (0, 0, SOUTH), (0, rows - 1, EAST), (0, rows - 1, NORTH), (cols - 1, 0, SOUTH), (cols - 1, 0, WEST),
                       (cols - 1, rows - 1, WEST), (cols - 1, rows - 1, NORTH)]

    visited = np.zeros(shape=(rows, cols), dtype=int)

    beams = [(0, 0, EAST)]

    while beams:
        beams_next = []
        for pos_x, pos_y, cur_dir in beams:
            # mark current position as visited
            marker = 1 << cur_dir
            visited[pos_y][pos_x] = visited[pos_y][pos_x] | marker
            # process next direction
            next_dirs = get_next_direction(lines[pos_y][pos_x], cur_dir)

            # move next
            for next_dir in next_dirs:
                next_x, next_y = get_next_pos(pos_x, pos_y, next_dir)
                marker_next = 1 << next_dir
                # if valid pos, add to next stack
                if 0 <= next_x < cols and 0 <= next_y < rows and visited[next_y][next_x] & marker_next == 0:
                    beams_next.append((next_x, next_y, next_dir))

        beams = beams_next

    total = 0
    for i in range(cols):
        for j in range(rows):
            if visited[j][i] > 0:
                total += 1

    print("Solution Day 16 Part 1: ", total)
