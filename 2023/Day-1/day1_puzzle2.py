def check_letters(letters):
    number_words = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    for word, number in number_words.items():
        if word in letters:
            return number

    return -1


def compute_line(input: str):
    line = input.strip()
    first_letters = ""
    last_letters = ""
    first_number = -1
    last_number = -1

    for index, character in enumerate(line):
        if first_number == -1:
            if character.isdigit():
                first_number = int(character)
            else:
                first_letters += character
                first_number = check_letters(first_letters)
        if last_number == -1:
            last_character = line[-index-1]
            if last_character.isdigit():
                last_number = int(last_character)
            else:
                last_letters += last_character
                last_number = check_letters(last_letters[::-1])

        if first_number != -1 and last_number != -1:
            break

    return first_number * 10 + last_number


print(sum(map(lambda line: compute_line(line), open("day1.txt").readlines())))
