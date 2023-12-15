print(sum(map(lambda line: 10 * next(int(character)
      for character in line if character.isdigit()) + next(int(character)
      for character in reversed(line) if character.isdigit()), open("day1.txt").readlines())))
