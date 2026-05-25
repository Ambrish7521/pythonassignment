def is_valid_pattern(pattern):
    """
    Checks if the pattern is allowed.
    Rules:
    - '+' cannot be at the start or end
    - '+' cannot appear twice in a row
    """

    # '+' cannot be first or last in the pattern
    if pattern.startswith('+') or pattern.endswith('+'):
        return False

    # Check for '++' anywhere in the pattern
    for i in range(len(pattern) - 1):
        if pattern[i] == '+' and pattern[i + 1] == '+':
            return False

    return True


def regex_match(text, pattern):
    """
    Matches a text against a very simple pattern system.

    Pattern Rules:
    - A letter followed by '+' means: that letter must appear one or more times.
    - A normal letter means: match exactly that letter.
    """

    # If pattern breaks the rules, stop immediately
    if not is_valid_pattern(pattern):
        return "Invalid Pattern"

    t = 0  # pointer for text
    p = 0  # pointer for pattern

    # Go through the pattern from left to right
    while p < len(pattern):

        # If current pattern character is followed by '+'
        if p + 1 < len(pattern) and pattern[p + 1] == '+':
            letter = pattern[p]

            # The letter must appear at least once in the text
            if t >= len(text) or text[t] != letter:
                return False

            # Keep moving through all matching letters
            while t < len(text) and text[t] == letter:
                t += 1

            # Skip the letter and the '+' in the pattern
            p += 2

        else:
            # Normal character — must match exactly once
            if t >= len(text) or text[t] != pattern[p]:
                return False

            t += 1
            p += 1

    # Check that we used up the whole text
    return t == len(text)


# ------------- MAIN PROGRAM -------------

P = input("Enter String P: ")
Q = input("Enter Pattern Q: ")

result = regex_match(P, Q)

print("\nOutput:", result)