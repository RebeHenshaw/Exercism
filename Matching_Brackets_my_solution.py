BRACKETS = {
    '(': ')',
    '{': '}',
    '[': ']'
           }
opener = BRACKETS.keys()
closer = BRACKETS.values()
def is_paired(to_check: str)-> bool:
    """Check if brackets are correctly opened and closed."""
    bracket_stack = []
    if to_check:
        for bracket in to_check:
            if bracket in opener:
                bracket_stack.append(bracket)
            elif bracket in closer:
                if len(bracket_stack)== 0:
                    return False
                last = bracket_stack.pop()
                if bracket != BRACKETS[last]:
                    return False
    return len(bracket_stack) == 0
