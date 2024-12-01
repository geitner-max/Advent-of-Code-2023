
__author__ = "Maximilian Geitner"
__date__ = "13.12.2023"

def is_valid_column_reflection(level, start_col_index):
    rows_inner = len(level)
    cols_inner = len(level[0])

    second_col = start_col_index + 1

# for second_col in range(start_col_index + 1, cols_inner):
    for offset in range(0, cols_inner):

        if start_col_index - offset < 0 or second_col + offset >= cols_inner:
            return True

        for j in range(rows_inner):
            if level[j][start_col_index - offset] != level[j][second_col + offset]:
                return False

def is_valid_row_reflection(level, start_row_index):
    rows_inner = len(level)
    cols_inner = len(level[0])

    # for second_row in range(start_row_index + 1, rows_inner):
    for second_row in range(start_row_index + 1, start_row_index + 2):
        for offset in range(0, cols_inner): # start_row_index + 1
            has_error = False
            if start_row_index - offset < 0 or second_row + offset >= rows_inner:
                return True

            for i in range(cols_inner):
                if level[start_row_index - offset][i] != level[second_row + offset][i]:
                    has_error = True
                    break
            if has_error:
                break
    return False

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"
    # 1.) read input
    # ash (.) and rocks (#)
    current_levels = []
    with open(filename) as file:
        current_level = []
        for line in file:
            line = line.replace("\n", "")

            if line == '':
                current_levels.append(current_level)
                current_level = []
            else:
                current_level.append(line)
        current_levels.append(current_level)

    # 2.) analyse each level

    total = 0
    for current_level in current_levels:
        rows = len(current_level)
        cols = len(current_level[0])
        # find two columns next to each other that match
        highest_col = None
        highest_row = None
        # 2a) check column reflection
        for col_index in range(cols - 1):
            # similar pattern found
            if is_valid_column_reflection(current_level, col_index):
                highest_col = col_index
        if highest_col is not None:
            total += highest_col + 1

        # 2b) check row reflections
        for row_index in range(rows - 1):
            # similar pattern found
            if is_valid_row_reflection(current_level, row_index):
                highest_row = row_index

        if highest_row is not None:
            total += (100 * (highest_row + 1))
    # 3.) output result
    print("Solution Day 13 Part 1: ", total)
