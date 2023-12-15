import numpy as np
from itertools import combinations


def expand(lines):
    for (index, ), line in list(np.ndenumerate(lines))[::-1]:
        line = line.strip()
        if len(set(line)) == 1 and line[0] == ".":
            lines = np.insert(lines, index, line)

    return lines


def get_indices(lines):
    indices = []
    for (i, ), row in np.ndenumerate(lines):
        for j, char in enumerate(row):
            if char == '#':
                indices.append((i, j))
    return np.array(indices)


lines = np.array(open("test.txt", "r").readlines())
lines = expand(lines)
lines = np.transpose(lines)
lines = expand(lines)

indices = get_indices(lines)

print(indices)
print(sum([sum(abs(combination[1] - combination[0]))
      for combination in combinations(indices, 2)]))
