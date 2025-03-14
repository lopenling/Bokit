def normalize_spaces(text):

    import re
    
    return re.sub(r'\s+', ' ', text).strip()
