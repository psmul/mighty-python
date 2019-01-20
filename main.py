import deckUtilities
import random

deck = deckUtilities.generate_new_deck()
game_over = False
player_score = 0
player_cards = []
opponent_score = 0
opponent_cards = []

deckUtilities.shuffle_deck(deck)


def pick_random_card_and_get_value(d, cards):
    rand = random.randint(1, len(d) - 1)
    rand_card = d.pop(rand)
    cards.append(rand_card)
    return rand_card.value


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
        player_score += pick_random_card_and_get_value(deck, player_cards)
        opponent_score += pick_random_card_and_get_value(deck, opponent_cards)

        print("------------------------------------------------------------")
        print("Current score:          " + str(player_score) + " : " + str(opponent_score) + "          Opponent score")
        print("Cards left in deck: " + str(len(deck)))
        print("------------------------------------------------------------")

        if len(player_cards) == 2 and player_cards[0].figure == 'A' and player_cards[1].figure == 'A':
            print("You won with Persian Eye!")
            game_over = True
        elif len(opponent_cards) == 2 and opponent_cards[0].figure == 'A' and opponent_cards[1].figure == 'A':
            print("Your opponent won with Persian Eye.")
            game_over = True
        elif player_score > 21:
            print("You lost.")
            game_over = True

    if decision == '2':
        print("Game over. Your score: " + str(player_score))
        game_over = True

    if decision == '3':
        print("\n")
        for card in player_cards:
            print(card.label + "\n")
