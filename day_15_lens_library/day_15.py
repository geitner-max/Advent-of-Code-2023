
__author__ = "Maximilian Geitner"
__date__ = "15.12.2023"

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    with open(filename) as file:
        total = 0

        for line in file:
            line = line.replace("\n", "")

            steps = line.split(",")
            # start with 0 for each sequence
            for step in steps:
                current_value = 0
                for char in step:
                    val = ord(char)
                    current_value = ((current_value + val) * 17 % 256) # apply hash function
                total += current_value

        print("Day 15 Part 1", total)
