__author__ = "Maximilian Geitner"
__date__ = "05.12.2023"


# Day 5 Part One
# Idea:
#       1.) Read all numbers ("the seeds") from the first line
#       2.) Interpret the following mappings as conversion rules with a given source interval and the offset
#           after the translation
#       3.) Do the translation for each seed from the first to the last translation layer
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


if __name__ == '__main__':
    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    with open(filename) as file:

        state_input = 0
        seeds = []
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
                seeds = list(map(lambda parts_str: int(parts_str), parts_num))
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

        # apply rules to each seed
        min_value = None
        for val in seeds:
            cur_val = val
            for converter in converters:
                cur_val = converter.convert_item(cur_val)
            if min_value is None:
                min_value = cur_val
            elif min_value > cur_val:
                min_value = cur_val

        print('Solution Day 5 Part One: ', min_value)
