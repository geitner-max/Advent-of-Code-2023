
__author__ = "Maximilian Geitner"
__date__ = "03.12.2023"

# Idea: Identify number in each line and look for any adjacent symbols
# Solution: Sum of all numbers that are adjacent to numbers
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

    # read input again, for each number, that is adjacent to a symbol, add it to total
    total = 0
    for row_index, line in enumerate(lines):
        cur_number = ""
        adjacent_to_symbol = False
        for i in range(len(line)):
            if '0' <= line[i] <= '9':
                cur_number += line[i]
                # check above line[i]
                pos_to_check = [(i - 1, row_index - 1), (i, row_index - 1), (i + 1, row_index - 1),
                                (i - 1, row_index), (i + 1, row_index), (i - 1, row_index + 1),
                                (i, row_index + 1), (i + 1, row_index + 1)]
                for index_x, index_y in pos_to_check:
                    if 0 <= index_y < len(lines) and 0 <= index_x < len(lines[index_y]):
                        if lines[index_y][index_x] != "." and not ('0' <= lines[index_y][index_x] <= '9'):
                            adjacent_to_symbol = True
                # current row, neighbor pos
            else:
                # not a digit, process number
                if cur_number != "":
                    # process number
                    num_val = int(cur_number)
                    cur_number = ""
                    if adjacent_to_symbol:
                        total += num_val
                        adjacent_to_symbol = False
                else:
                    cur_number = ""
                    adjacent_to_symbol = False
        # process end of line
        if cur_number != "":
            # process number
            num_val = int(cur_number)
            if adjacent_to_symbol:
                total += num_val
                adjacent_to_symbol = False
        else:
            cur_number = ""
            adjacent_to_symbol = False
    print('Solution Day 3 Part One', total)
