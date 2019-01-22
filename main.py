import sys
import deck_utilities
import random

start_new = False


def pick_random_card_and_get_value(d, cards):
    rand = random.randint(1, len(d) - 1)
    rand_card = d.pop(rand)
    cards.append(rand_card)
    return rand_card.value


def check_win_conditionals(p_score, p_cards, o_score, o_cards, p_pass, o_pass):
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
    elif p_pass and o_pass:
        if p_score == o_score:
            print("Weird situation, but it's DRAW.")
        elif p_score > o_score:
            print("You won with score " + str(p_score) + ".")
        elif p_score < o_score:
            print("Opponent won with score " + str(o_score) + ".")
    else:
        over = False
    return over


def print_current_state_of_game(d, p_score, o_score, round_num):
    print("\n----------------------- Round " + str(round_num) + " ----------------------------")
    print("Current score:          " + str(p_score) + " : " + str(o_score) + "          Opponent score")
    print("Cards left in deck: " + str(len(d)))
    print("------------------------------------------------------------\n")


def player_move(deck, cards, score):
    end_move = False

    while not end_move:
        input_label = "1 - Take card\n2 - Pass\n"
        if len(cards) > 0:
            input_label += "3 - Check your cards\n"
        input_label += "Select: "
        decision = input(input_label)

        if decision == '1':
            score = pick_random_card_and_get_value(deck, cards)
            print(score)
            end_move = True

        if decision == '2':
            score = 0
            end_move = True

        if decision == '3':
            print("\n")
            for card in cards:
                print(card.label)

    return score


def opponent_move(deck, cards, score):
    result = 0
    if score < 16:
        result = pick_random_card_and_get_value(deck, cards)

    return result


def start_game():
    deck = deck_utilities.generate_new_deck()
    game_over = False
    player_score = 0
    player_cards = []
    opponent_score = 0
    opponent_cards = []
    round_num = 1
    player_pass = False
    opponent_pass = False

    deck_utilities.shuffle_deck(deck)
    opponent_score += opponent_move(deck, opponent_cards, opponent_score)

    print("************************************************************")
    print("**                  Basic Blackjack Game                  **")
    print("************************************************************\n")

    while not game_over:
        if not player_pass:
            p_score_this_turn = player_move(deck, player_cards, player_score)
            player_pass = not bool(p_score_this_turn)
            player_score += p_score_this_turn

        if not opponent_pass:
            o_score_this_turn = opponent_move(deck, opponent_cards, opponent_score)
            opponent_pass = not bool(o_score_this_turn)
            opponent_score += o_score_this_turn

        print_current_state_of_game(deck, player_score, opponent_score, round_num)

        game_over = check_win_conditionals(player_score, player_cards, opponent_score, opponent_cards, player_pass, opponent_pass)
        round_num += 1

    return game_over


while not start_new:
    player_input = input("Start new game? Submit (y/n): ").lower()
    if player_input == 'y':
        start_game()
    if player_input == 'n':
        sys.exit()
