
__author__ = "Maximilian Geitner"
__date__ = "12.12.2023"

def count_arrangements(input_string, index_input, index_cur_spring, spring_sizes):
    if len(input_string) == index_input:
        # count backwards to last .
        index_spring_start = index_input
        for i in range(index_spring_start - 1, -1, -1):
            if input_string[i] == '#':
                index_spring_start = i
            else:
                break
        len_spring = index_input - index_spring_start

        if index_cur_spring == len(spring_sizes) and len_spring == 0:
            # print("".join([str(i) for i in input]))
            return 1
        if index_cur_spring == len(spring_sizes):
            return 0
        if len_spring == spring_sizes[index_cur_spring] and index_cur_spring == len(spring_sizes) - 1:
            # print("".join([str(i) for i in input]))
            return 1
        else:
            return 0

    else:
        if input_string[index_input] == '.':
            # evaluate previous spring
            # count backwards to last .
            index_spring_start = index_input
            for i in range(index_spring_start - 1, -1, -1):
                if input_string[i] == '#':
                    index_spring_start = i
                else:
                    break
            len_spring = index_input - index_spring_start
            if index_cur_spring == len(spring_sizes):
                if len_spring > 0:
                    return 0
                else:
                    return count_arrangements(input_string, index_input + 1, index_cur_spring, spring_sizes)
            if len_spring == spring_sizes[index_cur_spring]:
                return count_arrangements(input_string, index_input + 1, index_cur_spring + 1, spring_sizes)
            elif len_spring == 0:
                return count_arrangements(input_string, index_input + 1, index_cur_spring, spring_sizes)
            else:
                return 0

            # return count_arrangements(input, index_input + 1, index_cur_spring, spring_sizes)
        elif input_string[index_input] == '#':
            return count_arrangements(input_string, index_input + 1, index_cur_spring, spring_sizes)
        elif input_string[index_input] == '?':
            total = 0
            symbols = ['.', '#']
            for symbol in symbols:
                input_string[index_input] = symbol
                total += count_arrangements(input_string, index_input, index_cur_spring, spring_sizes)
            input_string[index_input] = '?'
            return total
    return 0


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    total_arrangements = 0
    with open(filename) as file:

        for line in file:
            line = line.replace("\n", "")

            parts = line.split(' ')
            springs = parts[0]

            spring_s = list(map(lambda item: int(item), parts[1].split(",")))

            # calculate arrangements
            found_arrangements = count_arrangements(list(parts[0]), 0, 0, spring_s)
            total_arrangements += found_arrangements
    print('Solution Day 12 Part 1: ', total_arrangements)
