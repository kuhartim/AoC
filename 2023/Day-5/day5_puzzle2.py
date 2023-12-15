file = open('day5.txt', 'r')

identifiers = [int(seed)
               for seed in file.readline().strip().split(": ")[1].split()]
paired_identifiers = [(identifiers[i], identifiers[i + 1])
                      for i in range(0, len(identifiers), 2)]

lines = file.readlines()

indexes = [i for i in range(len(lines)) if lines[i] == "\n"] + [len(lines)]
groups = [(lambda x: [(lambda y: (int(y[0]), int(y[1]), int(y[2])))(element.strip().split()) for element in x])(lines[index+2:indexes[i+1]])
          for i, index in enumerate(indexes) if i+1 < len(indexes)]


def compute_map(input: list, map: list):
    output = []
    for element in input:
        for dest, source, rng in map:
            element_start = element[0]
            element_end = element[0] + element[1] - 1
            source_start = source
            source_end = source + rng - 1

            if element_start > source_end or element_end < source_start:
                continue

            if element_start < source_start:
                range_start = element_start
                range_end = min(source_start-1, element_end)
                input.append((range_start, range_end-range_start+1))
            if element_end > source_end:
                range_start = max(source_end+1, element_start)
                range_end = element_end
                input.append((range_start, range_end-range_start+1))

            optional_range_start = max(element_start, source_start)
            optional_range_end = min(element_end, source_end)
            if optional_range_start <= optional_range_end:
                addition = dest - source
                range_start = optional_range_start + addition
                range_end = optional_range_end + addition
                output.append((range_start, range_end-range_start+1))
                break
        else:
            output.append(element)

    return output


input = paired_identifiers
for group in groups:
    input = compute_map(input, group)

print(min(input, key=lambda x: x[0])[0])
