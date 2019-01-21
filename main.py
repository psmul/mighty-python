import sys
import deck_utilities
import random

start_new = False


def pick_random_card_and_get_value(d, cards):
    rand = random.randint(1, len(d) - 1)
    rand_card = d.pop(rand)
    cards.append(rand_card)
    return rand_card.value


def check_win_conditionals(p_score, p_cards, o_score, o_cards):
    over = True
    if len(p_cards) == 2 and p_cards[0].figure == 'A' and p_cards[1].figure == 'A':
        print("You won with Persian Eye!")
    elif len(o_cards) == 2 and o_cards[0].figure == 'A' and o_cards[1].figure == 'A':
        print("Your opponent won with Persian Eye.")
    elif p_score == 21:
        print("You have 21 points. You won.")
    elif o_score == 21:
        print("Opponent got 21 points. You lost.")
    elif o_score > 21:
        print("Opponent exceeded 21 points. You won.")
    elif p_score > 21:
        print("You have exceeded 21 points. You lost.")
    else:
        over = False
    return over


def print_current_sate_of_game(p_score, o_score, d):
    print("\n------------------------------------------------------------")
    print("Current score:          " + str(p_score) + " : " + str(
        o_score) + "          Opponent score")
    print("Cards left in deck: " + str(len(d)))
    print("------------------------------------------------------------\n")


def start_game():
    deck = deck_utilities.generate_new_deck()
    game_over = False
    player_score = 0
    player_cards = []
    opponent_score = 0
    opponent_cards = []

    deck_utilities.shuffle_deck(deck)

    print("************************************************************")
    print("**                  Basic Blackjack Game                  **")
    print("************************************************************\n")

    while not game_over:
        input_label = "1 - Take card\n2 - Pass\n"
        if len(player_cards) > 0:
            input_label += "3 - Check your cards\n"
        input_label += "Select: "

        decision = input(input_label)

        if decision == '1':
            if opponent_score < 19:
                opponent_score += pick_random_card_and_get_value(deck, opponent_cards)
            player_score += pick_random_card_and_get_value(deck, player_cards)
            print_current_sate_of_game(player_score, opponent_score, deck)
            game_over = check_win_conditionals(player_score, player_cards, opponent_score, opponent_cards)

        if decision == '2':
            if opponent_score < 19:
                opponent_score += pick_random_card_and_get_value(deck, opponent_cards)

            print_current_sate_of_game(player_score, opponent_score, deck)

            game_over = check_win_conditionals(player_score, player_cards, opponent_score, opponent_cards)

        if decision == '3':
            print("\n")
            for card in player_cards:
                print(card.label + "\n")

    return game_over


while not start_new:
    player_input = input("Start new game? Submit (y/n): ").lower()
    if player_input == 'y':
        start_game()
    if player_input == 'n':
        sys.exit()
