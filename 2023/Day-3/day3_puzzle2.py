import re

lines = open("day3.txt").readlines()


def get_number(x: int, y: int, direction, checked_indexes):
    if f"({x},{y})" in checked_indexes:
        return ""

    checked_indexes.append(f"({x},{y})")

    element = lines[y][x]

    if (x < 0 or x >= len(lines[y])) or (y < 0 or y >= len(lines)) or not element.isdigit():
        return ""

    return (get_number(x - 1, y, "left", checked_indexes) if direction != "right" else "") + element + (get_number(x + 1, y, "right", checked_indexes) if direction != "left" else "")


sum = 0
for line_index, line in enumerate(lines):
    for char_index, char in enumerate(line.strip()):
        if char != "*":
            continue

        checked_indexes = []
        numbers = []

        for index_i in range(char_index - 1, char_index + 2):
            if index_i < 0 or index_i >= len(line.strip()):
                continue
            for index_j in range(line_index - 1, line_index + 2):
                if index_j < 0 or index_j >= len(lines):
                    continue
                number = get_number(index_i, index_j, "both", checked_indexes)
                if number:
                    numbers.append(int(number))

        if len(numbers) == 2:
            sum += numbers[0] * numbers[1]

print(sum)
