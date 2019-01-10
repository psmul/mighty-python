
def search4letters(phrase:str, letters:str='asd') -> set:
    return set(letters).intersection(set(phrase))
