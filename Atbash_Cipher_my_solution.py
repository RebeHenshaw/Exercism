import string
import textwrap
CODE_PAIRS = {letter: opposite_letter for letter, opposite_letter in zip(string.ascii_lowercase, string.ascii_lowercase[::-1])}
CODE_PAIRS.update({i: i for i in string.digits})

def encode(plain_text: str) -> str:
    """Encode to an Atbash-ciphered string."""
    return ' '.join(textwrap.wrap(decode(plain_text), 5))
def decode(ciphered_text: str) -> str:
    """Decode from an Atbash-ciphered string."""
    ciphered_text = ciphered_text.lower()
    decoded = [CODE_PAIRS.get(letter, '') for letter in ciphered_text]
    return ''.join(decoded)
