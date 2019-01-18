from Card import Card
import random


def generate_new_deck() -> list:
    deck = []

    for color in ['h', 't', 'c', 'p']:
        for num in range(2, 15):
            figure = ""
            value = num
            if num <= 10:
                figure = str(num)
            if num == 11:
                figure = "J"
                value = 2
            if num == 12:
                figure = "Q"
                value = 3
            if num == 13:
                figure = "K"
                value = 4
            if num == 14:
                figure = "A"
                value = 11

            deck.append(Card(figure=figure, value=value, color=color))

    return deck


def shuffle_deck(deck: list) -> list:
    return random.shuffle(deck)
