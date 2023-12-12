
__author__ = "Maximilian Geitner"
__date__ = "07.12.2023"

# Day 7 Part One:
# Ranking Cards from highest to Lowest: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
# Idea:
#       1.) Read input: values of the five cards and the bid
#       2.) Identify card ranking by assigning the hand to the highest applicable type and sort hands by card strength
#           within each type bucket
#           Types:
#           -   Five of a kind
#           -   Four of a kind
#           -   Full House (Three of a kind + Two of a kind)
#           -   Three of a kind
#           -   Two Pair
#           -   One Pair
#           -   High Card
#       3.) Calculate total winnings by adding the multiplication of rank and bid of each hand
def get_rank(hand):
    rank = 0
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    for index, c in enumerate(hand):
        pos = cards.index(c)
        rank += pos * (14 ** (4 - index))
    return rank


def get_type(hand):
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    appearing_cards = set()
    # five of a kind
    for index, card in enumerate(cards):
        counter = 0

        for c in hand:
            appearing_cards.add(c)
            if card == c:
                counter += 1
        if counter == 5:
            return 0  # type 0: five of a kind
        if counter == 4:
            return 1  # type 1: four of a kind
    appearing_cards = list(appearing_cards)
    if len(appearing_cards) == 2:
        card0 = 0
        card1 = 0
        for c in hand:
            if appearing_cards[0] == c:
                card0 += 1
            if appearing_cards[1] == c:
                card1 += 1
        if (card0 == 3 and card1 == 2) or (card0 == 2 and card1 == 3):
            return 2  # type 2: full house

    for index, card in enumerate(cards):
        counter = 0
        for c in hand:
            if card == c:
                counter += 1
        if counter == 3:
            return 3  # type 3: three of a kind

    if len(appearing_cards) == 3:
        card0 = 0
        card1 = 0
        card2 = 0
        for c in hand:
            if appearing_cards[0] == c:
                card0 += 1
            if appearing_cards[1] == c:
                card1 += 1
            if appearing_cards[2] == c:
                card2 += 1
        if (card0 == 2 and card1 == 2 and card2 == 1) or (card0 == 2 and card1 == 1 and card2 == 2) or (
                card0 == 1 and card1 == 2 and card2 == 2):
            return 4  # type 2: two pair

    for index, card in enumerate(cards):
        counter = 0
        for c in hand:
            if card == c:
                counter += 1
        if counter == 2:
            return 5  # type 5: one pair

    return 6  # type 6: all cards distinct


if __name__ == '__main__':
    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "test.txt"

    with open(filename) as file:
        dict_bid_amount = {}
        hands = []
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(" ")
            dict_bid_amount[parts[0]] = int(parts[1])
            hands.append(parts[0])
    buckets = []
    for i in range(7):
        buckets.append([])

    for hand in hands:
        hand_type = get_type(hand)
        buckets[hand_type].append(hand)

    for i in range(len(buckets)):
        buckets[i].sort(key=lambda item: get_rank(item), reverse=False)

    ranking = []
    for i in range(len(buckets)):
        for hand in buckets[i]:
            ranking.append(hand)
    ranking.reverse()
    # calculate result
    solution = 0
    for index, hand in enumerate(ranking):
        solution += (index + 1) * dict_bid_amount[hand]
    print("Solution Day 7 Part One: ", solution)
