def is_valid(isbn: str)-> bool:
    """Validate International Standard Book Number."""
    if not isbn:
        return False
    onlydigits = list(isbn.replace('-', ''))
    if onlydigits[-1] == 'X':
        onlydigits[-1] = '10'  # String '10' avoids line 12 error when converting str to int
    if len(onlydigits) != 10:
        return False
    if not all(char.isdigit() for char in onlydigits):
        return False
