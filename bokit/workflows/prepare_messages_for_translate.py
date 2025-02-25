def prepare_messages_for_translate(strings: list, prefix: str = '') -> list:

    '''
    Prepare messages for translation by formatting the strings with a specified prefix.

    Args:
        strings (list): The list of strings to prepare.
        prefix (str): The prefix to prepend to each string.

    Returns:
        list: The formatted messages.
    '''

    out = []

    for i, line in enumerate(strings):

        out.append({"role": "user", "content": [{"type": "text", "text": prefix + line}]})

    return out
