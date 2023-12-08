
__author__ = "Maximilian Geitner"
__date__ = "04.12.2023"

if __name__ == '__main__':
    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    total_points = 0
    # Day 4 Part One
    # Idea: 1.) Count winning numbers in each line
    #       2.) One winning number counts as one point. For each additional number, double the amount points.
    #       3.) Sum up over all the number of points
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            line_parts = line.split(":")
            numbers_parts = line_parts[1].split("|")
            winning_numbers_str = numbers_parts[0].strip().replace("  ", " ").replace("  ", " ").split(" ")

            own_numbers_str = numbers_parts[1].strip().replace("  ", " ").replace("  ", " ").split(" ")

            # convert to numbers

            winning_numbers = list(map(lambda number_str: int(number_str.strip()), winning_numbers_str))
            own_numbers = list(map(lambda number_str: int(number_str.strip()), own_numbers_str))

            wins_round = 0
            for num in own_numbers:
                if num in winning_numbers:
                    wins_round += 1
            if wins_round > 0:
                total_points += 2 ** (wins_round - 1)

        print("Solution Part One: ", total_points)

        # Day 4 Part Two
        # Idea: 1.) Count amount of winning numbers for each card.
        #       2.) The amount of winning numbers translate into more scratchcards for the following card evaluations.
        #       4.) Solution is the computation of the amount of scratchcards including the original cards.
        total_instances = 0
        instances = {}
        with open(filename) as file:

            for index, line in enumerate(file):
                card_number = index + 1
                card_instances = 1
                if card_number in instances.keys():
                    card_instances += instances[card_number]
                total_instances += card_instances

                instances[card_number] = card_instances
                line = line.replace("\n", "")
                line_parts = line.split(":")
                numbers_parts = line_parts[1].split("|")
                winning_numbers_str = numbers_parts[0].strip().replace("  ", " ").replace("  ", " ").split(" ")

                own_numbers_str = numbers_parts[1].strip().replace("  ", " ").replace("  ", " ").split(" ")

                # convert to numbers

                winning_numbers = list(map(lambda number_str: int(number_str.strip()), winning_numbers_str))
                own_numbers = list(map(lambda number_str: int(number_str.strip()), own_numbers_str))

                wins_round = 0
                for num in own_numbers:
                    if num in winning_numbers:
                        # winning scratch card
                        wins_round += 1

                # do scratch card round
                if wins_round > 0:
                    # generate copies
                    copies = []
                    for index in range(wins_round):
                        copies.append(card_number + 1 + index)
                    # process copies
                    for num in copies:
                        if num in instances.keys():
                            instances[num] = instances[num] + card_instances
                        else:
                            instances[num] = card_instances

        print("Solution Part Two: ", total_instances)
