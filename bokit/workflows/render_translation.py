from IPython.display import display, HTML


#TODO move this to a css file and parse from there
source_style = "font-size: 18px; color: black; font-weight: regular; text-align: left; font-family: 'Noto Serif Tibetan', serif; line-height: 2.2;"
translation_style = "font-size: 16px; color: black; font-style: bold; text-align: left; font-family: 'Noto Serif', serif;"
spacing = "margin-bottom: 20px;"


def render_translation(source: str, translation: str) -> None:

    '''
    Render the source and translation in a side-by-side format.
    Args:
        source (str): The source text.
        translation (str): The translation text.
    '''

    html_content = f"""
    <div style="{spacing}">
        <div style="{source_style}">{source}</div>
        <div style="{translation_style}">{translation}</div>
    </div>
    """
    display(HTML(html_content))
