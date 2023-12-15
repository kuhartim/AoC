from collections import defaultdict

players = list(map(lambda line: (line.strip().split()[0], int(
    line.strip().split()[1])), open("day7.txt", "r").readlines()))


def five_of_a_kind(hand):
    return len(set(hand)) == 1


def four_of_a_kind(hand):
    return any(hand.count(char) == 4 for char in set(hand))


def full_house(hand):
    return len(set(hand)) == 2


def three_of_a_kind(hand):
    return any(hand.count(char) == 3 for char in set(hand))


def two_pair(hand):
    return len([char for char in set(hand) if hand.count(char) == 2]) == 2


def one_pair(hand):
    return len([char for char in set(hand) if hand.count(char) == 2]) == 1


def high_card(hand):
    return len(set(hand)) == 5


def step_one(players):
    step_one_plays = defaultdict(list)

    for player in players:
        hand = player[0]

        if five_of_a_kind(hand):
            step_one_plays["five_of_a_kind"].append(player)
            continue
        if four_of_a_kind(hand):
            step_one_plays["four_of_a_kind"].append(player)
            continue
        if full_house(hand):
            step_one_plays["full_house"].append(player)
            continue
        if three_of_a_kind(hand):
            step_one_plays["three_of_a_kind"].append(player)
            continue
        if two_pair(hand):
            step_one_plays["two_pair"].append(player)
            continue
        if one_pair(hand):
            step_one_plays["one_pair"].append(player)
            continue
        if high_card(hand):
            step_one_plays["high_card"].append(player)

    return step_one_plays


cards = "23456789TJQKA"


def step_two(plays: list, index_to_check=0):
    if index_to_check > 4:
        return plays
    sorted_plays = sorted(
        plays, key=lambda e: cards.index(e[0][index_to_check]), reverse=True)
    output = []
    for card in cards[::-1]:
        output.extend(step_two(list(filter(
            lambda element: element[0][index_to_check] == card, sorted_plays)), index_to_check + 1))
    return output


plays = step_one(players)
result = step_two(plays["five_of_a_kind"]) + step_two(plays["four_of_a_kind"]) + step_two(plays["full_house"]) + step_two(
    plays["three_of_a_kind"]) + step_two(plays["two_pair"]) + step_two(plays["one_pair"]) + step_two(plays["high_card"])

print(sum(map(lambda enumerated_element: (enumerated_element[0] + 1) *
      enumerated_element[1][1], enumerate(result[::-1]))))

# part 2


def five_of_a_kind(hand):
    hand_set = set(hand)
    return len(hand_set) == 1 or (len(hand_set) == 2 and "J" in hand_set)


def four_of_a_kind(hand):
    amount_of_J = hand.count("J")
    return any(hand.count(char) >= (4 - amount_of_J) for char in set(hand) if char != "J") or amount_of_J == 4


def full_house(hand):
    hand_set = set(hand)
    return len(hand_set) == 2 or (len(hand_set) == 3 and "J" in hand_set)


def three_of_a_kind(hand):
    amount_of_J = hand.count("J")
    return any(hand.count(char) >= (3 - amount_of_J) for char in set(hand) if char != "J") or amount_of_J == 3


def two_pair(hand):
    return len([char for char in set(hand) if hand.count(char) == 2]) == 2 or (len([char for char in set(hand) if hand.count(char) == 2]) == 1 and "J" in set(hand)) or hand.count("J") == 2


def one_pair(hand):
    return len([char for char in set(hand) if hand.count(char) == 2]) == 1 or "J" in set(hand)


def high_card(hand):
    return len(set(hand)) == 5


cards = "J23456789TQKA"

plays = step_one(players)
result = step_two(plays["five_of_a_kind"]) + step_two(plays["four_of_a_kind"]) + step_two(plays["full_house"]) + step_two(
    plays["three_of_a_kind"]) + step_two(plays["two_pair"]) + step_two(plays["one_pair"]) + step_two(plays["high_card"])

print(sum(map(lambda enumerated_element: (enumerated_element[0] + 1) *
      enumerated_element[1][1], enumerate(result[::-1]))))
