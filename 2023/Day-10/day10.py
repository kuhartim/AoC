import math

lines = [f".{line.strip()}." for line in open(
    "day10.txt", "r").readlines() if line.strip()]
lines.append("." * len(lines[0]))
lines.insert(0, lines[-1])


def coordinate_to_string(coordinate: tuple[int, int]):
    return f"({str(coordinate[0])},{str(coordinate[1])})"


start_coordinates = next(((j.index("S"), i) for i, row in enumerate(
    lines) if 'S' in row for j in [row]))

top_connected = ["|", "7", "F", "S"]
bottom_connected = ["|", "L", "J", "S"]
left_connected = ["-", "F", "L", "S"]
right_connected = ["-", "J", "7", "S"]

visited = []
chars = []

current_coordinates = start_coordinates
counter = 0
while True:
    char = lines[current_coordinates[1]][current_coordinates[0]]
    visited.append(current_coordinates)
    chars.append(char)

    top_coordinates = list(current_coordinates)
    top_coordinates[1] -= 1
    top_coordinates = tuple(top_coordinates)

    bottom_coordinates = list(current_coordinates)
    bottom_coordinates[1] += 1
    bottom_coordinates = tuple(bottom_coordinates)

    right_coordinates = list(current_coordinates)
    right_coordinates[0] += 1
    right_coordinates = tuple(right_coordinates)

    left_coordinates = list(current_coordinates)
    left_coordinates[0] -= 1
    left_coordinates = tuple(left_coordinates)

    if char in bottom_connected and lines[top_coordinates[1]][top_coordinates[0]] in top_connected and top_coordinates not in visited:
        current_coordinates = top_coordinates
        counter += 1
        continue

    if char in left_connected and lines[right_coordinates[1]][right_coordinates[0]] in right_connected and right_coordinates not in visited:
        current_coordinates = right_coordinates
        counter += 1
        continue

    if char in top_connected and lines[bottom_coordinates[1]][bottom_coordinates[0]] in bottom_connected and bottom_coordinates not in visited:
        current_coordinates = bottom_coordinates
        counter += 1
        continue

    if char in right_connected and lines[left_coordinates[1]][left_coordinates[0]] in left_connected and left_coordinates not in visited:
        current_coordinates = left_coordinates
        counter += 1
        continue

    break

print(math.ceil(counter / 2.0))

# part 2


# def print_grid(grid):
#     for row in grid:
#         for char in row:
#             if char == 1:
#                 print(f"\033[92m {char}", end="")
#             elif char == 2:
#                 print(f"\033[91m {char}", end="")
#             else:
#                 print(f"\033[0m {char}", end="")
#         print("\033[0m\n")


def change_start():
    is_top_connected = lines[start_coordinates[1] -
                             1][start_coordinates[0]] in top_connected
    is_right_connected = lines[start_coordinates[1]
                               ][start_coordinates[0] + 1] in right_connected
    is_bottom_connected = lines[start_coordinates[1] +
                                1][start_coordinates[0]] in bottom_connected
    is_left_connected = lines[start_coordinates[1]
                              ][start_coordinates[0] - 1] in left_connected

    index_of_start = chars.index("S")

    if is_top_connected and is_right_connected:
        chars[index_of_start] = "L"
        return
    if is_top_connected and is_bottom_connected:
        chars[index_of_start] = "|"
        return
    if is_top_connected and is_left_connected:
        chars[index_of_start] = "J"
        return
    if is_right_connected and is_bottom_connected:
        chars[index_of_start] = "F"
        return
    if is_right_connected and is_left_connected:
        chars[index_of_start] = "-"
        return
    if is_bottom_connected and is_left_connected:
        chars[index_of_start] = "7"
        return


def upscale_grid():
    upscaled_grid = [[0 for _ in range(
        len(lines[0]) * 3)] for _ in range(len(lines) * 3)]
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            is_loop = (x, y) in visited
            if not is_loop:
                continue
            char = chars[visited.index((x, y))]

            upscaled_grid[y * 3] = upscaled_grid[y * 3][:x * 3] + (
                [0, 1, 0] if char in bottom_connected else [0, 0, 0]) + upscaled_grid[y * 3][x*3 + 3:]

            upscaled_grid[y * 3 + 1] = upscaled_grid[y * 3 + 1][:x * 3] + (
                [1, 1, 1] if char == "-" else [0, 1, 0] if char == "|" else [1, 1, 0] if char in right_connected else [0, 1, 1] if char in left_connected else [0, 0, 0]) + upscaled_grid[y * 3 + 1][x*3 + 3:]

            upscaled_grid[y * 3 + 2] = upscaled_grid[y * 3 + 2][:x * 3] + (
                [0, 1, 0] if char in top_connected else [0, 0, 0]) + upscaled_grid[y * 3 + 2][x*3 + 3:]

    return upscaled_grid


def fill(grid, coordinates):
    stack = [coordinates]

    while stack:
        x, y = stack.pop()

        if grid[y][x] == 0:
            grid[y][x] = 2

            neighbors = [
                (x-1, y), (x+1, y), (x-1, y-1), (x+1, y+1),
                (x-1, y+1), (x+1, y-1), (x, y-1), (x, y+1)
            ]

            for neighbor in neighbors:
                nx, ny = neighbor
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    stack.append(neighbor)


def get_not_filled(upscaled_grid):
    counter = 0
    for y in range(0, len(upscaled_grid), 3):
        for x in range(0, len(upscaled_grid[0]), 3):
            for y1 in range(y, y+3):
                for x1 in range(x, x+3):
                    if upscaled_grid[y1][x1] != 0:
                        break
                else:
                    continue
                break
            else:
                counter += 1

    return counter


# visualized = [["1" if (x, y) in visited else "0" for x in range(len(lines[0]))]
#               for y in range(len(lines))]

# print_grid(visualized)
# print("\n")
change_start()
upscaled = upscale_grid()
# print_grid(upscaled)
fill(upscaled, (0, 0))
# print("\n")
# print_grid(upscaled)
print(get_not_filled(upscaled))
