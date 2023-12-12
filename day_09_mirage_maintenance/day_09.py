
__author__ = "Maximilian Geitner"
__date__ = "09.12.2023"

# Day 9 Part One:
# Idea:
#       1.) Read input of numbers
#       2.) Recreate scenario by creating the following layers by computing the difference between two values
#       3.) Start at the layer containing only zeros and compute the new layers for all other layers
#       4.) Solution: Sum of the last computed value in the first layer of each input sequence
#
# Day 9 Part Two:
# Difference compared to part one:
#       -   Different computation formula and place in layer for computing the unknown value


if __name__ == '__main__':
    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    total = 0
    total_part_two = 0
    with open(filename) as file:

        for line in file:
            line = line.replace("\n", "")
            parts = line.split(" ")
            numbers = list(map(lambda val: int(val), parts))

            cur_row = numbers
            rows = []
            rows.append(cur_row)
            only_zeros = True
            # 1.) generate new rows until only zeros appear
            while True:
                only_zeros = True
                next_row = []

                for i in range(len(cur_row) - 1):
                    diff = cur_row[i + 1] - cur_row[i]
                    if diff != 0:
                        only_zeros = False
                    next_row.append(diff)
                cur_row = next_row
                rows.append(cur_row)
                if only_zeros:
                    break
            # calculate next value by interpolating from layer with only zeros
            next_val = 0
            for i in range(len(rows) - 1, 0, -1):
                diff = rows[i][-1]
                next_val = rows[i - 1][-1] + diff
                rows[i - 1].append(next_val)
            total += next_val

            # Part Two: Extrapolate Backwards
            cur_diff = 0
            # calculate next value by interpolating from layer with only zeros
            prev_value = 0
            for i in range(len(rows) - 1, 0, -1):
                val_layer_above = rows[i - 1][0]
                prev_value = val_layer_above - cur_diff
                cur_diff = prev_value
                rows[i - 1].append(prev_value)
            total_part_two += prev_value

        print("Solution Day 9 Part One: ", total)
        print("Solution Day 9 Part Two: ", total_part_two)
