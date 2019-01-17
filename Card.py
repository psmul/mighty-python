
class Card(object):
    label: str = ""
    color: str = ""
    value: int

    def __init__(self, label, value, color):
        self.label = label
        self.value = value
        self.color = color
