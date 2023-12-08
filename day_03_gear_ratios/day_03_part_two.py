__author__ = "Maximilian Geitner"
__date__ = "03.12.2023"

# Idea: 1.) Identify all numbers in the given input and remember the value, the column_index of the first and last
#           character as well as the row_index
#       2.) Identify all star symbols in the input with its column and row index
#       3.) For each identified star, look for amount of adjacent numbers
#           a) If two adjacent numbers are next to a given star, multiply the numbers with each other and add the result
#              to solution value
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
    numbers_parsed = []  # style: (value, index_x_start, index_x_end, index_y)
    symbol_stars = []  # style: (index x, index_y)
    for row_index, line in enumerate(lines):
        cur_number = ""
        for i in range(len(line)):
            if '0' <= line[i] <= '9':
                cur_number += line[i]
                # check above line[i]
            else:
                # not a digit, process number
                if cur_number != "":
                    # process number
                    num_val = int(cur_number)
                    numbers_parsed.append((num_val, i - len(cur_number), i - 1, row_index))
                cur_number = ""
            if line[i] == '*':
                symbol_stars.append((i, row_index))
        # process end of line
        if cur_number != "":
            # process number
            num_val = int(cur_number)
            numbers_parsed.append((num_val, len(line) - len(cur_number), len(line) - 1, row_index))
        else:
            cur_number = ""
    print(numbers_parsed)
    print(symbol_stars)
    for index_x_star, index_y_star in symbol_stars:
        # filter values by position
        # value, x_s, x_e, y
        numbers_adjacent = list(filter(lambda item: ((index_x_star - 1 <= item[1] <= index_x_star + 1) or
                                                     (item[1] < index_x_star < item[2]) or
                                                     (index_x_star - 1 <= item[2] <= index_x_star + 1))
                                                    and
                                                    (
                                                            item[3] - 1 == index_y_star or
                                                            item[3] == index_y_star or
                                                            item[3] + 1 == index_y_star),
                                       numbers_parsed))
        print(numbers_adjacent)
        if len(numbers_adjacent) == 2:
            print(numbers_adjacent[0][0], numbers_adjacent[1][0])
            total += (numbers_adjacent[0][0] * numbers_adjacent[1][0])
    print("Solution Day 3 Part Two: ", total)

