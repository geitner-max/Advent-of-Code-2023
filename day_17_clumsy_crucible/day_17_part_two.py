
__author__ = "Maximilian Geitner"
__date__ = "17.12.2023"

import numpy as np

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def get_next_pos(cur_x, cur_y, direction):
    if direction == NORTH:
        return cur_x, cur_y - 1
    elif direction == EAST:
        return cur_x + 1, cur_y
    elif direction == SOUTH:
        return cur_x, cur_y + 1
    else:
        return cur_x - 1, cur_y

# apply rule about turns here
def generate_next_directions(straight_turns_count, direction_last_move):
    result = []
    if straight_turns_count < 10:
        result.append(direction_last_move)
    if straight_turns_count >= 4:
        # left turn
        result.append((direction_last_move + 3) % 4)
        # right turn
        result.append((direction_last_move + 1) % 4)
    return result

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

    # straight, left or right
    # max 3 turns in a row straight

    cols = len(lines[0])
    rows = len(lines)
    visited = {}
    heat_loss_matrix = np.zeros(shape=(rows, cols), dtype=int)
    for i in range(cols):
        for j in range(rows):
            heat_loss_matrix[j][i] = int(lines[j][i])

    # pos_x, pos_y, heat_loss, amount straight, direction last move
    stack = [(0, 0, -heat_loss_matrix[0][0], 0, SOUTH), (0, 0, -heat_loss_matrix[0][0], 0, EAST)]
    min_heat_loss = -1
    while stack:
        next_stack = []
        for pos_x, pos_y, heat_loss, straight_turn_count, direction_last_move in stack:
            cur_heat_loss = heat_loss + heat_loss_matrix[pos_y][pos_x]
            next_turn_dirs = generate_next_directions(straight_turn_count, direction_last_move)
            if pos_x == cols - 1 and pos_y == rows - 1:
                if min_heat_loss == -1:
                    min_heat_loss = cur_heat_loss
                else:
                    min_heat_loss = min(min_heat_loss, cur_heat_loss)
                continue
            for next_dir in next_turn_dirs:
                next_x, next_y = get_next_pos(pos_x, pos_y, next_dir)
                if 0 <= next_x < cols and 0 <= next_y < rows:
                    straight_count = 1
                    if direction_last_move == next_dir:
                        straight_count = max(straight_turn_count + 1, straight_count)
                    visited_key = (next_x, next_y, straight_count, next_dir)
                    if visited_key in visited.keys():
                        prev_heat_loss = visited[visited_key]
                        if cur_heat_loss < prev_heat_loss:
                            visited[visited_key] = cur_heat_loss

                            # Case: better approx than before
                            next_stack.append((next_x, next_y, cur_heat_loss, straight_count, next_dir))
                    else:
                        # Case: not previously visited
                        visited[visited_key] = cur_heat_loss

                        next_stack.append((next_x, next_y, cur_heat_loss, straight_count, next_dir))
        stack = next_stack

    print("Solution Day 17 Part Two: ", min_heat_loss)
    # correct answer: 997
    # runtime: 2-3 minutes
