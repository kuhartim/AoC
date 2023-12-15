def get_id_count(line: str):
    _, games_str = line.split(":")
    blue, red, green = 0, 0, 0
    for game in games_str.split(";"):
        for boxes_str in game.split(","):
            num, color = boxes_str.strip().split(" ")
            if color == "blue" and blue < int(num):
                blue = int(num)
            if color == "green" and green < int(num):
                green = int(num)
            if color == "red" and red < int(num):
                red = int(num)

    return blue * red * green


print(sum(map(lambda line: get_id_count(line), open("day2.txt").readlines())))
