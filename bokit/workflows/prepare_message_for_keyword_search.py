def prepare_message_for_keyword_search(strings: list) -> list:

    '''
    Prepare a list of messages for keyword search.

    Args:
        strings (list): A list of strings to prepare for keyword search.

    Returns:
        list: A list of formatted messages for keyword search.
    '''

    out = []

    for _, line in enumerate(strings):

        out.append({"role": "user",
                    "content": [{"type": "text", "text": line}],
                    })

    return out
