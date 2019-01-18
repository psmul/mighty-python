
class Card(object):
    figure: str = ""
    color: str = ""
    value: int

    def __init__(self, figure, value, color):
        self.figure = figure
        self.value = value
        self.color = color

    @property
    def label(self):
        return self.color + self.figure
