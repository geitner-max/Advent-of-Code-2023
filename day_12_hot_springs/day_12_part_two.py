
__author__ = "Maximilian Geitner"
__date__ = "12.12.2023"

def count_spring_length(input):
    counter = 0
    for c in range(len(input) - 1, -1, -1):
        if c == '#':
            counter += 1
        else:
            break
    return counter


def process_input_dot(index_cur_spring: int, spring_len: int, amount_cases: int, spring_sizes, dict_next):
    if spring_len > 0 and index_cur_spring == len(spring_sizes):
        # new spring detected and all springs already visited --> invalid entry
        return dict_next
    elif spring_len == 0:
        # no new spring detected --> keep entry
        key = (index_cur_spring, 0)
        if key in dict_next.keys():
            dict_next[key] += amount_cases
        else:
            dict_next[key] = amount_cases
        return dict_next
    if spring_len == spring_sizes[index_cur_spring]:
        # create shortened entry
        key = (index_cur_spring + 1, 0)
        if key in dict_next.keys():
            dict_next[key] += amount_cases
        else:
            dict_next[key] = amount_cases
        return dict_next
    else:
        # spring_len does not match next item
        return dict_next


def count_arrangements(input_string: list, index_input: int, spring_sizes: list, dict_state: dict):
    dict_next = {}
    # dict_state: dict: key: (<index_spring>, <counter spring>), value: (amount of cases)
    if index_input == len(input_string):
        # evaluate dot on every item
        for key, amount_cases in dict_state.items():
            index_cur_spring, spring_len = key
            dict_next = process_input_dot(index_cur_spring, spring_len, amount_cases, spring_sizes, dict_next)
        # sum up all amount cases
        total = 0
        for key, amount_cases in dict_next.items():
            index_cur_spring, spring_len = key
            # only count entries that match all springs in spring_sizes
            if index_cur_spring == len(spring_sizes):
                total += amount_cases
        return total
    else:
        if input_string[index_input] == '.':
            # evalutate spring len
            for key, amount_cases in dict_state.items():
                index_cur_spring, spring_len = key
                dict_next = process_input_dot(index_cur_spring, spring_len, amount_cases, spring_sizes, dict_next)
            return count_arrangements(input_string, index_input + 1, spring_sizes, dict_next)
        elif input_string[index_input] == '#':
            # increment counter spring len
            for key, amount_cases in dict_state.items():
                index_cur_spring, spring_len = key
                key_next = (index_cur_spring, spring_len + 1)
                if key_next in dict_next.keys():
                    dict_next[key_next] += amount_cases
                else:
                    dict_next[key_next] = amount_cases
            return count_arrangements(input_string, index_input + 1, spring_sizes, dict_next)
        elif input_string[index_input] == '?':
            for key, amount_cases in dict_state.items():
                index_cur_spring, spring_len = key
                key1 = (index_cur_spring, spring_len + 1)  # case '#'
                if key1 in dict_next:
                    dict_next[key1] += amount_cases
                else:
                    dict_next[key1] = amount_cases
                # case '.'
                dict_next = process_input_dot(index_cur_spring, spring_len, amount_cases, spring_sizes, dict_next)
            return count_arrangements(input_string, index_input + 1, spring_sizes, dict_next)

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

            spring_counts = list(map(lambda item: int(item), parts[1].split(",")))

            # prepare string, multiply original input by 5 and add questionmarks between them
            input_str = []
            spring_count = []
            for i in range(5):
                input_str += parts[0]
                spring_count += spring_counts
                if i != 4:
                    input_str.append('?')

            # calculate arrangements
            found_arrangements = count_arrangements(input_str, 0, spring_count, {(0, 0): 1})
            total_arrangements += found_arrangements

    print('Solution Day 12 Part 2: ', total_arrangements)