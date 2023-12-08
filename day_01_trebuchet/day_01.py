
__author__ = "Maximilian Geitner"
__date__ = "01.12.2023"

if __name__ == '__main__':
    filename = "input.txt"
    # Day 01 Part One
    # Idea: Find first and last digit character in each line, form a two-digit number and sum up these numbers.
    with open(filename) as file:
        total = 0
        for line in file:
            line = line.replace("\n", "")
            digits = ""
            # parse all characters in line, extract all digits
            for c in line:
                if '0' <= c <= '9':
                    digits += c
            # use first and last digit for computing the solution
            if digits != "":
                digits_i = int(digits[0] + digits[-1])
                total += digits_i
        print('Solution Part One: ', total)

    # Day 01 Part Two
    # Idea: Find first and last digit character in each line, or an equivalent text representation for the digit
    #       Then, form a two-digit number and sum up these numbers.
    total = 0
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            digits = ""
            digits_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            for index, c in enumerate(line):
                if '0' <= c <= '9':
                    digits += c
                else:
                    for index_val, text in enumerate(digits_str):
                        len_val = len(text)
                        if index + len_val <= len(line):
                            # compare substring with digits as text
                            if line[index:].startswith(text):
                                digits += str(index_val)
            # use first and last digit for computing the solution
            if digits != "":
                digits_i = int(digits[0] + digits[-1])
                total += digits_i
    print('Solution Part Two: ', total)
