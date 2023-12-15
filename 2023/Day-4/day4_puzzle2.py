from collections import defaultdict

lines = open("day4.txt").readlines()

copies = defaultdict(int)

for line in lines:
    card_str, numbers = line.strip().split(":")
    _, card_id = card_str.split()
    winning, mine = numbers.split("|")
    amount_of_winning = sum([
        1 if x in winning.split(" ") else 0 for x in mine.split(" ") if x])
    for x in range(1, amount_of_winning + 1):
        copies[int(card_id) + x] += copies[int(card_id)] + 1


print(sum(copies.values()) + len(lines))
