import string
letters_count = {y:x for x, y in enumerate(string.ascii_uppercase, 1)}
count_letters = {y:x for x, y in letters_count.items()}
def rows(letter: str) -> list[str]:
    """Create a diamond shape with letter at the center."""
    side = letters_count[letter] -1
    middle = 1
    row_letter = 'A'
    final = []
    for each in range(1, letters_count[letter]+1):
        if row_letter == 'A':
            final.append((' ' * side) + row_letter + (' ' * side))
            if row_letter == letter:
                return final
            else:
                side -= 1
                row_letter = count_letters[each +1]
        else:
            final.append((' ' * side) + row_letter + (middle * ' ') + row_letter + (' ' * side))
            if row_letter == letter:
                return final + final[0:-1][::-1]
            middle += 2
            side -= 1
            row_letter = count_letters[each +1]
