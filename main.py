import deckUtilities
import random

deck = deckUtilities.generate_new_deck()
game_over = False
player_score = 0
picked_cards = []

deckUtilities.shuffle_deck(deck)


while not game_over:
    decision = input("Take card? \n (Y/N): ").lower()
    if decision == 'y':
        rand = random.randint(1, len(deck)-1)
        rand_card = deck.pop(rand)
        picked_cards.append(rand_card)
        player_score += rand_card.value
        print("Card picked: " + rand_card.label)
        print("Current score: " + str(player_score))
        print("Cards left in deck: " + str(len(deck)))
        if player_score > 21 and not ( picked_cards[0].figure == 'A' and picked_cards[1].figure == 'A'):
            print("You lost.")
            game_over = True

    if decision == 'n':
        print("Game over. Your score: " + str(player_score))
        game_over = True

