NUMBER_OF_BOXES = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def get_id_count(line: str):
    id_str, games_str = line.split(":")
    for game in games_str.split(";"):
        for boxes_str in game.split(","):
            num, color = boxes_str.strip().split(" ")
            if NUMBER_OF_BOXES[color] < int(num):
                break
        else:
            continue
        break
    else:
        _, num_str = id_str.strip().split(" ")
        return int(num_str)
    return 0


print(sum(map(lambda line: get_id_count(line), open("day2.txt").readlines())))
