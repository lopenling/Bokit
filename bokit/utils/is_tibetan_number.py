def is_tibetan_number(s: str, clean_string=True) -> bool:

    '''
    Check if a string is a Tibetan number.
    
    # Parameters

    s (str): The string to check.
    clean_string (bool): Whether to clean the string by replacing
                         specific characters. Defaults to True.
    
    # Returns
    
    bool: True if the string is a Tibetan number, False otherwise.
    '''

    if clean_string:
        s = s.replace('་', '')
        s = s.replace('་', '།')
        
    if not s:
        return False
    for ch in s:
        if not ('\u0F20' <= ch <= '\u0F29'):
            return False
    return True
