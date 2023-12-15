file = open('day5.txt', 'r')

identifiers = [int(seed)
               for seed in file.readline().strip().split(": ")[1].split()]
lines = file.readlines()

indexes = [i for i in range(len(lines)) if lines[i] == "\n"] + [len(lines)]
groups = [(lambda x: [(lambda y: (int(y[0]), int(y[1]), int(y[2])))(element.strip().split()) for element in x])(lines[index+2:indexes[i+1]])
          for i, index in enumerate(indexes) if i+1 < len(indexes)]

end_results = []
for seed in identifiers:
    element = seed
    for group in groups:
        for sub_group in group:
            if element >= sub_group[1] and element <= sub_group[1] + sub_group[2]:
                element = element + sub_group[0] - sub_group[1]
                break
    end_results.append(element)

print(min(end_results))
