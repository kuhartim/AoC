def get_card_worth(line: str):
    _, numbers = line.strip().split(":")
    winning, mine = numbers.split("|")
    amount_of_winning = sum([
        1 if x in winning.split(" ") else 0 for x in mine.split(" ") if x])
    if not amount_of_winning:
        return 0
    return pow(2, amount_of_winning - 1)


print(sum(map(lambda line: get_card_worth(line), open("day4.txt").readlines())))
