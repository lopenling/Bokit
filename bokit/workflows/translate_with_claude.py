def translate_with_claude(api_key: str,
                          system: str,
                          messages: list,
                          model: str,
                          chunk_size: int = 10) -> list:
    
    '''
    Translate a list of messages using the Claude model.
    
    Args:
        api_key (str): The API key for the Anthropic API.
        system (str): The system in which the messages appear.
        messages (list): The messages to translate.
        model (str): The model to use for translation.
        chunk_size (int): The number of messages to translate in each chunk.
    
    Returns:
        list: The translated messages.
    '''

    out = []

    import anthropic
    
    client = anthropic.Anthropic(api_key=api_key)

    for i in range(0, len(messages), chunk_size):
        chunk = messages[i:i + chunk_size]
        message = client.messages.create(model=model,
                                         max_tokens=4096,
                                         temperature=0,
                                         system=system,
                                         messages=chunk)
        out.append(message.content[0])

    return out
