import unicodedata as ud


def is_all_latin(word):
    
    """
    Checks if all characters in the given word belong to the Latin script.
    Allows common Latin-based symbols, numbers, and punctuation.
    """

    # Step 1: Define allowed symbols that are safe for Latin script
    allowed_symbols = set(".,!?-–—()[]{}:;'\" */<>#&@_=↑")

    # Step 2: Normalize input by stripping spaces
    cleaned_word = word.strip()

    # Step 3: Check each character in the word
    for char in cleaned_word:
        # If it's a letter, ensure it's from the Latin script
        if char.isalpha():
            if "LATIN" not in ud.name(char):
                return False  # Reject immediately if it's non-Latin
        
        # If it's not a letter, allow digits and predefined symbols
        elif not (char.isdigit() or char in allowed_symbols):
            return False  # Reject if it's an unknown character

    # Step 4: If all characters pass, return True
    return True
