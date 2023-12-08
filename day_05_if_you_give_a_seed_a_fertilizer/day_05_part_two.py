
__author__ = "Maximilian Geitner"
__date__ = "05.12.2023"

# Day 5 Part Two
# Idea:
#       1.) Read all numbers ("the seeds") from the first line and create intervals (offset and length)
#       2.) Interpret the following mappings as conversion rules with a given source interval and the offset
#           after the translation
#       3.) Do the translation for each interval from the first to the last translation layer, this involves
#       splitting up intervals due to different conversion rules for individual values
#       4.) Solution is the smallest value of all completely translated seeds
class Converter:
    def __init__(self, conversion_rules):
        self.conversion_rules = conversion_rules

    def convert_item(self, value):
        for dest, source, length in self.conversion_rules:
            if source <= value < source + length:
                # conversion rule applies
                offset = value - source
                return dest + offset
        return value

    def convert_item_range(self, list_ranges):
        output = []
        for start_index, length_index in list_ranges:
            expected_len = length_index

            output_current = []
            converted_intervals = []
            for dest, source, length_con in self.conversion_rules:
                # interval smaller than conversion rule interval
                if source <= start_index and start_index + length_index - 1 < source + length_con:
                    offset = start_index - source
                    output_current.append((dest + offset, length_index))
                    converted_intervals.append((start_index, start_index + length_index))
                elif source < start_index and source+ length_con > start_index and source + length_con < start_index + length_index:
                    # start_index lies within the conversion rule
                    offset = start_index - source
                    new_len = length_con - offset
                    if new_len < 0 or new_len > length_index:
                        print("Err")
                    output_current.append((dest + offset, new_len))
                    converted_intervals.append((start_index, start_index + new_len))
                elif source >= start_index and source < start_index + length_index and start_index + length_index < source + length_con:
                    # end of interval lies within conversion rule
                    new_len = start_index + length_index - source
                    output_current.append((dest, new_len))
                    if new_len < 0 or new_len > length_index:
                        print("Err")
                    converted_intervals.append((source, source + new_len))
                elif source >= start_index and source + length_con < start_index + length_index:
                    # complete conversion rule lies within output
                    output_current.append((dest, length_con))
                    converted_intervals.append((source, source + length_con))
                else:
                    pass  # conversion rule does not overlap with given interval
            # add remaining, not converted intervals to output
            converted_intervals.sort(key=lambda item: item[0])
            # add start_index --> first_interval to output
            if len(converted_intervals) >= 1:
                new_len = converted_intervals[0][0] - start_index
                if new_len > expected_len:
                    print("Err")
                if new_len > 0:
                    output_current.append((start_index, new_len))
                new_len = (start_index + length_index) - converted_intervals[-1][1]
                if new_len > expected_len:
                    print("Err")
                if new_len > 0:
                    output_current.append((converted_intervals[-1][1], new_len))
            else:
                # no conversion rule applies, add current interval to output
                output_current.append((start_index, length_index))
                output += output_current
                continue
            for i in range(len(converted_intervals) - 1):
                # values between intervals
                interval_start = converted_intervals[i][1]
                interval_end = converted_intervals[i + 1][0]
                new_len = interval_end - interval_start
                if new_len > 0:
                    output_current.append((interval_start, new_len))
            # add output_current to output
            #print("Before: ", output)
            actual_len = 0
            for _, len_output in output_current:
                actual_len += len_output
            if expected_len != actual_len:
                print("Err")
            output = output + output_current
            #print("After: ", output)
            # print('After ', start_index, length_index, ": ", output, output_current)
        if len(list_ranges) > len(output):
            print("Error")
        return output

if __name__ == '__main__':
    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"



    with open(filename) as file:

        state_input = 0
        set_seeds = []
        seeds = []
        seeds_initial = []
        # conversions
        seed_to_soil_map = []
        soil_to_fertilizer_map = []
        fertilizer_to_water_map = []
        water_to_light_map = []
        light_to_temperature_map = []
        temperature_to_humidity_map = []
        humidity_to_location_map = []

        converters = []

        conversion_rules = []
        for line in file:

            line = line.replace("\n", "")
            if line.startswith("seeds: "):
                parts_num = line.replace("seeds: ", "").split(" ")
                seeds_initial = list(map(lambda parts_str: int(parts_str), parts_num))
            elif line == '':
                if state_input != 0:
                    converters.append(Converter(conversion_rules))
                    conversion_rules = []
                state_input += 1
            elif "map" in line:
                continue
            else:
                # read line
                parts_conversion = line.split(" ")  # destination, source, range
                conversion = list(map(lambda parts_str: int(parts_str), parts_conversion))
                conversion_rules.append(conversion)
        # add last converter seperately
        converters.append(Converter(conversion_rules))
        # transform initial input to seeds
        start_seed = 0
        for index, val in enumerate(seeds_initial):
            if index % 2 == 1:
                # length value
                seeds.append((start_seed, val))
            else:
                start_seed = val
        # apply rules to each seed
        min_value = None
        cur_val = seeds
        for converter in converters:
            print("Processing next stage with ", len(cur_val), " intervals")
            cur_val = converter.convert_item_range(cur_val)

        for start, len in cur_val:
            if min_value is None:
                min_value = start
            elif min_value > start:
                min_value = start
        print('Solution Day 5 Part Two: ', min_value)
