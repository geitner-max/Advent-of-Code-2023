
__author__ = "Maximilian Geitner"
__date__ = "08.12.2023"

# Day 8 Part One:
# Idea:
#       1.) Read input sequence and graph configuration:
#           Each node saves the next node after moving left or right, dictionary with the following items:
#           key: <source_node>, value: (<node_after_moving_left>, <node_after_moving_right>)
#       2.) Simulate moving according to the given input sequence starting at 'AAA' until it reaches 'ZZZ'
#       3.) Solution: Amount of steps
#
# Day 8 Part Two:
#       Note:
#       -   Steps != Cycles
#       -   One Cycle: One complete consumption of the input sequence
#       Observation: Nodes take X amount of cycles to reach a valid exit node ending with 'Z',
#                    and need additional X amount of cycles to reach the same exit node again
#                    -->  X cycles for one round trip
#                    The value X differs for each node starting with 'A' and are prime numbers for the input
#       1.) Read input sequence and graph configuration (similar as in part one)
#       2.) For each node, compute destination node after consuming one input sequence cycle
#       3.) Find all starting nodes starting with 'A'
#       4.) Simulate for each starting node the input sequence and compute the number of required input sequence cycles
#           are required to find an exit
#           and how long the cycle to the same exit nodes takes
#       5.) Find the least common multiple between of all given cycle values
#       6.) Solution = least_common_multiple * steps_for_one_cycle
#           steps_for_one_cycle = len(input_sequence)

if __name__ == '__main__':
    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    input_sequence = ""
    with open(filename) as file:
        # line 1: input sequence
        is_first_line = True
        graph = {}
        for line in file:
            line = line.replace("\n", "")
            if is_first_line:
                is_first_line = False
                input_sequence = line
            elif line == "":
                continue
            else:
                # Format:
                # PND = (LHJ, NLX)
                parts = line.replace(" ", "").replace("(", "").replace(")", "").split("=")
                source = parts[0]
                dest = parts[1].split(",")
                graph[source] = dest

    cur_pos = 'AAA'
    cur_index = 0
    steps = 0
    while cur_pos != 'ZZZ':
        next_instr = input_sequence[cur_index]
        cur_index = (cur_index + 1) % len(input_sequence)
        steps += 1
        if next_instr == 'L':
            cur_pos = graph[cur_pos][0]
        else:
            cur_pos = graph[cur_pos][1]
    print("Solution Day 8 Part One: ", steps)

    # Other Example for part Two
    if use_example:
        filename = "example_2.txt"

    # Part Two
    input_sequence = ""
    with open(filename) as file:
        # line 1: input sequence
        is_first_line = True
        graph = {}
        for line in file:
            line = line.replace("\n", "")
            if is_first_line:
                is_first_line = False
                input_sequence = line
            elif line == "":
                continue
            else:
                parts = line.replace(" ", "").replace("(", "").replace(")", "").split("=")
                source = parts[0]
                dest = parts[1].split(",")
                graph[source] = dest

    graph_cycle = {}
    for source in graph.keys():
        # for each source process one input sequence cycle, record destination and solutions
        solutions = []
        pos = source
        if source.endswith('Z'):
            solutions.append(0)
        for index, direction in enumerate(input_sequence):
            if direction == 'L':
                pos = graph[pos][0]
            else:
                pos = graph[pos][1]
            if pos.endswith('Z'):
                solutions.append(index + 1)
        graph_cycle[source] = (pos, solutions)

    cur_positions = []
    # add starting pos
    for source in graph.keys():
        if source.endswith('A'):
            cur_positions.append(source)

    cur_index = 0
    cur_positions2 = []
    # contains, start pos, offset to first goal and steps between two similar goals
    for source in cur_positions:
        # find steps to first goal
        # identify steps between repetition
        pos = source
        goals_visited = {}
        cycles = 0
        while True:
            pos = graph_cycle[pos][0]
            cycles += 1
            if pos.endswith('Z'):
                if pos in goals_visited.keys():
                    # second visit occured
                    offset = goals_visited[pos]
                    cycle_steps = cycles - offset
                    cur_positions2.append((source, offset, cycle_steps))
                    break
                else:
                    goals_visited[pos] = cycles  # mark first visit
    # kgv(19637, 18023, 21251, 16409, 11567, 14257)
    # 14449445933179
    result = 1
    for source, offset, cycle in cur_positions2:
        result *= cycle
    print('Solution Day 8 Part Two: ', result * len(input_sequence))
