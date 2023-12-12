__author__ = "Maximilian Geitner"
__date__ = "06.12.2023"


# Day 6 Part One
# Idea:
#       1.) Read input with all distances and durations
#       2.) For each scenario, evaluate for each valid button hold time [1, duration - 1] the travelled distance
#           and count amount of scenarios beating the given record
#
# Day 6 Part Two
# Idea: 1.) Read input with all distances and durations
#       2.) Find lower and upper bound of valid record beating hold times with binary search
#       Note: This version might not work with all inputs, some improved version to narrow the interval might help.
#             Formula Solution Part Two = <Upper_Bound> - <Lower_Bound> + 1

def beats_record(dist_record, timestamp, hold_time):
    rem_time_f = timestamp - hold_time
    dist_travelled_f = rem_time_f * hold_time  # button_hold_time equals speed
    if dist_travelled_f > dist_record:
        return True
    else:
        return False


if __name__ == '__main__':
    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    timestamps = []
    distances = []
    solution = 1
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")

            race_stats = []

            if line.startswith("Time: "):
                line = line.replace("Time: ", "").replace("  ", " ").strip().replace("  ", " ").replace("  ", " ")
                timestamps = list(map(lambda value: int(value), line.split(" ")))

            else:
                line = line.replace("Distance: ", "").replace("  ", " ").strip().replace("  ", " ").replace("  ", "")

                distances = list(map(lambda value: int(value), line.split(" ")))

    for i in range(len(timestamps)):
        win_options = 0
        cur_dist = distances[i]
        for button_hold_time in range(1, timestamps[i] - 1):
            rem_time = timestamps[i] - button_hold_time
            dist_travelled = rem_time * button_hold_time  # button_hold_time equals speed
            if dist_travelled > cur_dist:
                win_options += 1
        solution *= win_options
    print("Solution Part One: ", solution)
    print("--------------------------------------------")
    # Part Two
    timestamps = []
    distances = []
    solution = 1
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            race_stats = []

            if line.startswith("Time: "):
                line = line.replace("Time: ", "").replace(" ", "").strip()
                timestamps = list(map(lambda value: int(value), line.split(" ")))

            else:
                line = line.replace("Distance: ", "").replace(" ", "").strip()

                distances = list(map(lambda value: int(value), line.split(" ")))

    for i in range(len(timestamps)):
        win_options = 0
        cur_dist = distances[i]
        start_value = None
        # start value
        button_hold_time_smin = 1
        button_hold_time_smax = timestamps[i] - 1
        while True:
            if button_hold_time_smin == button_hold_time_smax or button_hold_time_smin + 1 == button_hold_time_smax:
                print("Beats record with ", button_hold_time_smin, ": ",
                      beats_record(cur_dist, timestamps[i], button_hold_time_smin))
                print("Beats record with ", button_hold_time_smax, ": ",
                      beats_record(cur_dist, timestamps[i], button_hold_time_smax))
                start_value = button_hold_time_smax
                break
            # print(button_hold_time_smin, button_hold_time_smax)
            time_to_test = (button_hold_time_smin + button_hold_time_smax) // 2
            if beats_record(cur_dist, timestamps[i], time_to_test):
                # search in upper range
                # print("Beats Record --> Max lower")
                button_hold_time_smax = time_to_test
            else:
                # print("Doesnt Beats Record --> Min higher")
                button_hold_time_smin = time_to_test

        end_value = None
        button_hold_time_smin = 1
        button_hold_time_smax = timestamps[i] - 1
        while True:
            if button_hold_time_smin == button_hold_time_smax or button_hold_time_smin + 1 == button_hold_time_smax:
                print("Beats record with ", button_hold_time_smin, ": ",
                      beats_record(cur_dist, timestamps[i], button_hold_time_smin))
                print("Beats record with ", button_hold_time_smax, ": ",
                      beats_record(cur_dist, timestamps[i], button_hold_time_smax))
                end_value = button_hold_time_smin
                break
            # print(button_hold_time_smin, button_hold_time_smax)
            time_to_test = (button_hold_time_smin + button_hold_time_smax) // 2
            if beats_record(cur_dist, timestamps[i], time_to_test):
                # search in upper range
                # print("Beats Record --> Min higher")
                button_hold_time_smin = time_to_test
            else:
                # print("Doesnt Beats Record --> Max Lower")
                button_hold_time_smax = time_to_test

        win_options_part_two = end_value - start_value + 1
        print("Solution Part Two: ", win_options_part_two)
