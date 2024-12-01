
__author__ = "Maximilian Geitner"
__date__ = "13.12.2023"


# modification: only one column can have a small difference (one . or # is flipped) compared to the opposite column
def is_valid_column_reflection(level, start_col_index):
    rows_inner = len(level)
    cols_inner = len(level[0])
    second_col = start_col_index + 1
    amount_not_matching = 0
    for offset in range(0, cols_inner):
        if start_col_index - offset < 0 or second_col + offset >= cols_inner:
            if amount_not_matching == 1:
                return True
            else:
                return False

        for j in range(rows_inner):
            if level[j][start_col_index - offset] != level[j][second_col + offset]:
                amount_not_matching += 1
                if amount_not_matching >= 2:
                    return False

    return False

def is_valid_row_reflection(level, start_row_index):
    rows_inner = len(level)
    cols_inner = len(level[0])

    # for second_row in range(start_row_index + 1, rows_inner):
    second_row = start_row_index + 1
    amount_not_matching = 0
    has_error = False
    for offset in range(0, rows_inner):  # start_row_index + 1

        if start_row_index - offset < 0 or second_row + offset >= rows_inner:
            if amount_not_matching == 1 and not has_error:
                return True
            else:
                return False

        for i in range(cols_inner):
            if level[start_row_index - offset][i] != level[second_row + offset][i]:
                amount_not_matching += 1
                if amount_not_matching >= 2:
                    has_error = True
                    break
        if has_error:
            return False
    return False

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) read input
    # ash (.) and rocks (#)

    current_levels = []
    input_string = ""
    with open(filename) as file:
        current_level = []
        for line in file:
            input_string += line
            line = line.replace("\n", "")

            if line == '':
                current_levels.append(current_level)
                current_level = []
            else:
                current_level.append(line)
        current_levels.append(current_level)

    # 2.) solve puzzle similar to part one with modified helper functions
    total = 0
    for current_level in current_levels:
        rows = len(current_level)
        cols = len(current_level[0])
        # find two columns next to each other that match
        highest_col = None
        highest_row = None
        for col_index in range(cols - 1):
            # similar pattern found
            if is_valid_column_reflection(current_level, col_index):#
                highest_col = col_index

        if highest_col is not None:
            total += highest_col + 1
        # keep highest value

        for row_index in range(rows - 1):
            # similar pattern found
            if is_valid_row_reflection(current_level, row_index):
                highest_row = row_index
        if highest_row is not None:
            total += (100 * (highest_row + 1))

    print("Solution Day 13 Part Two: ", total)
