import math
lines = open('day6.txt').readlines()
combinations_part1 = zip(*[map(lambda element: int(element), elements.split(":")[1].strip().split())
                           for elements in lines])


def calculate_score(combinations):
    result = 1
    for time, record in combinations:
        wins = 0
        is_even = time % 2 == 0
        for index in range(math.ceil(time / 2)):
            game_result = index * (time - index)
            if game_result > record:
                wins += 1
        wins *= 2
        result *= wins + (1 if is_even else 0)
    return result


print(calculate_score(combinations_part1))

combinations_part2 = [tuple(
    int("".join(elements.split(":")[1].strip().split())) for elements in lines)]

print(calculate_score(combinations_part2))
