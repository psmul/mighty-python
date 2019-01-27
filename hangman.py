import random
import sys

start_new = False


def get_random_word_from_file():
    with open('random_words.txt') as some_tasks:
        words = some_tasks.read().splitlines()
        rand = random.randint(1, len(words) - 1)
        return words.pop(rand)


def get_word_template(word):
    template = ""
    for i in list(word):
        template += "_"
    return template


def format_template_with_spaces(template):
    list_with_spaces = []
    for t in template:
        list_with_spaces.append(t)
        list_with_spaces.append(" ")
    return list_with_spaces


def get_char_positions(word, char):
    positions = []
    for i, j in enumerate(list(word)):
        if j == char:
            positions.append(i)
    return positions


def start_game():
    max_attempts = 8
    attempts = 0
    game_over = False
    random_word = get_random_word_from_file()
    tmpl = list(get_word_template(random_word))

    while not game_over:
        user_input = input("\nPlease input character.\nSubmit: ")
        if isinstance(user_input, str) and len(user_input) == 1:
            is_in_list = user_input in list(random_word)
            if is_in_list:
                pos = get_char_positions(random_word, user_input)
                for i in pos:
                    tmpl[i] = user_input.upper()
                print("".join(format_template_with_spaces(tmpl)))
            elif attempts < 8:
                attempts += 1
                print("Miss. Attempts: " + str(attempts) + "/" + str(max_attempts))

            if attempts == 8:
                print("Game over. The word was: " + random_word)
                game_over = True

        if isinstance(user_input, str) and len(user_input) > 1 and user_input == random_word:
            print("\nWow! You hit it!")
            print("".join(format_template_with_spaces(user_input.upper())))

        if isinstance(user_input, str) and len(user_input) > 1 and user_input != random_word:
            attempts += 1
            print("Miss. Attempts: " + str(attempts) + "/" + str(max_attempts))


while not start_new:
    player_input = input("Start new game? Submit (y/n): ").lower()
    if player_input == 'y':
        start_game()
    if player_input == 'n':
        sys.exit()

