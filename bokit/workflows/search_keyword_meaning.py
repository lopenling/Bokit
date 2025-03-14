def search_keyword_meaning(api_key: str,
                           message: str,
                           context: dict) -> str:
    
    '''
    Search for the meaning of a keyword in a given context.
    
    Args:
        api_key (str): The API key for the Anthropic API.
        message (str): The keyword to search for.
        context (dict): The context in which the keyword appears.
    
    Returns:
        str: The meaning of the keyword in the given context.
    '''

    import anthropic

    system = " ".join(f"{key}: {value}; " for key, value in context.items())

    client = anthropic.Anthropic(api_key=api_key)
    
    message = client.messages.create(model="claude-3-opus-20240229",
                                     max_tokens=800,
                                     temperature=0.05,
                                     system=system,
                                     messages=message,
                                     stream=False)

    return message
