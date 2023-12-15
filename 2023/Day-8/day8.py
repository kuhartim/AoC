import math
file = open("day8.txt", "r")

directions = file.readline().strip()
lines = file.readlines()

legend = {}
for line in lines:
    if not line.strip():
        continue
    key, direction_keys = line.strip().split(" = ")
    left, right = direction_keys[1:-1].split(", ")
    legend[key] = (left, right)

current = "AAA"
last = "ZZZ"

count = 0
while current != last:
    for direction in directions:
        direction_legend = legend[current]
        current = direction_legend[0] if direction == "L" else direction_legend[1]
        count += 1
        if current == last:
            break

print(count)

# part 2

counts = []
for start in filter(lambda x: x[-1] == "A", legend.keys()):
    current = start
    count = 0
    while current[-1] != "Z":
        for direction in directions:
            direction_legend = legend[current]
            current = direction_legend[0] if direction == "L" else direction_legend[1]
            count += 1
            if current[-1] == "Z":
                break
    counts.append(count)

print(math.lcm(*counts))
