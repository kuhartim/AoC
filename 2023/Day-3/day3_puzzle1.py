import re

lines = open("day3.txt").readlines()

sum = 0
for line_index, line in enumerate(lines):
    numbers_arr = re.findall(r'\d+', line)
    for number in numbers_arr:
        index = re.search(f"(^|[^0-9]){number}($|[^0-9])", line).start()
        if not line[index].isdigit():
            index += 1

        for index_i in range(index - 1, index + len(number) + 1):
            if index_i < 0 or index_i >= len(line.strip()):
                continue
            for index_j in range(line_index - 1, line_index + 2):
                if index_j < 0 or index_j >= len(lines):
                    continue
                char_to_check = lines[index_j][index_i]
                if not char_to_check.isdigit() and char_to_check != ".":
                    sum += int(number)
                    # print(f"\033[92m YES: {number}")
                    break
            else:
                continue
            break
        else:
            # print(f"\033[91m NOT: {number}")
            pass


print(f"\033[0m {sum}")
