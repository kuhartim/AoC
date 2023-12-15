def get_prediction(sequence):
    if all(el == 0 for el in sequence):
        return 0

    sub_list = [sequence[i + 1] - sequence[i]
                for i in range(len(sequence) - 1)]
    sub_list_prediction = get_prediction(sub_list)

    return sequence[-1] + sub_list_prediction


print(sum([get_prediction(list(map(lambda x: int(x), line.split())))
      for line in open("day9.txt", "r").readlines() if line.strip()]))

# part 2


def get_prediction(sequence):
    if all(el == 0 for el in sequence):
        return 0

    sub_list = [sequence[i + 1] - sequence[i]
                for i in range(len(sequence) - 1)]
    sub_list_prediction = get_prediction(sub_list)

    return sequence[0] - sub_list_prediction


print(sum([get_prediction(list(map(lambda x: int(x), line.split())))
      for line in open("day9.txt", "r").readlines() if line.strip()]))
