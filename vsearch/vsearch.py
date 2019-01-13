def search4letters(phrase: str, letters: str = 'te') -> set:
    """ Return any letters defined in second parameter from phrase """
    return set(letters).intersection(set(phrase))
