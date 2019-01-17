from Card import Card


def generate_new_deck() -> list:
    deck = []

    for color in ['h', 't', 'c', 'p']:
        for num in range(1, 14):
            label = ""
            if num <= 10:
                label = str(num)
            if num == 11:
                label = "J"
            if num == 12:
                label = "Q"
            if num == 13:
                label = "K"
            if num == 14:
                label = "A"

            deck.append(Card(label, num, color))

    return deck


def shuffledeck(deck: list) -> list:
    return deck.shuffle()
