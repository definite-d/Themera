"""
d888888P dP
   88    88
   88    88d888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b.
   88    88'  `88 88ooood8 88'`88'`88 88ooood8 88'  `88 88'  `88
   88    88    88 88.  ... 88  88  88 88.  ... 88       88.  .88
   dP    dP    dP `88888P' dP  dP  dP `88888P' dP       `88888P8

Themera Custom Layout Preview Functionality Script
PySimpleGUI Theme Code Generator
Copyright 2023 Divine Afam-Ifediogor
"""
from typing import Dict, List, Optional, Any, Union
from fonts import FONTS

from PySimpleGUI import EMOJI_BASE64_HAPPY_BIG_SMILE, Element, LOOK_AND_FEEL_TABLE, Window, theme, \
    Text, Input, Push, Button, theme, theme_add_new, PopupError

ELEMENTS = {element.__name__: element for element in Element.__subclasses__()}
GLOBALS = {'EMOJI_BASE64_HAPPY_BIG_SMILE': EMOJI_BASE64_HAPPY_BIG_SMILE}
GLOBALS.update(ELEMENTS)

DEFAULT_LAYOUT = '''
# Sample Layout Code
[
    [Column([
           [Column([
               [Column([
                    [Column([
                        [
                            Image(data=EMOJI_BASE64_HAPPY_BIG_SMILE, k=f'tb_icon'),
                            # Icon and Title
                            Text('Quick Preview', k=f'tb_title'),
                        ]
                    ], pad=(0, 0), k=f'tb_title_and_icon')],
                    [Column([
                        [Text('Sample Text; Lorem ipsum dolor sit amet...', k=f'element_text', expand_x=True)],
                        [Input('Hello world', k=f'element_input', expand_x=True)],
                        [Button('Button', k=f'element_button')]
                    ], k=f'element_bg', pad=(0, 0), expand_x=True)]
                ], expand_x=True, k=f'tb_container', pad=(2, (0, 2)))],
            ], k=f'tb_maincolumn', element_justification='c', pad=(1, 1), expand_x=True)]
    ], k=f'visibility_wrap', expand_x=True)]
]
'''


def get_custom_layout_from_user(
        present_theme: str,
        present_themedict: Dict[str, Union[int, str, tuple, list]],
        user_theme_name: str,
        user_themedict: Dict[str, Union[int, str, tuple, list]],
):
    """
    Gets the custom layout to preview from the user.
    """
    theme_add_new(present_theme, present_themedict)
    theme(present_theme)
    layout = [
        [Text('Enter your layout', font=FONTS['theme_name'])],
        [Text('Please enter the layout code to preview')],
        [Text('All PySimpleGUI elements are available;\nno need for aliases or imports.')],
        [Input(DEFAULT_LAYOUT, k='user_layout')],
        [Push(), Button('Preview'), Button('Cancel')]
    ]
    window = Window(
        'Custom Layout Entry',
        layout,
    )
    while True:
        e, v = window.read()
        if e in (None, 'Exit'):
            window.close()
            break
        try:
            custom_layout_preview(v['custom_layout'], user_theme_name, user_themedict)
        except Exception as e:
            PopupError('There was ')


def custom_layout_preview(
        layout: str,
        theme_name: str,
        themedict: Optional[Dict] = None,
):
    """
    Provide your layout without any alias to PySimpleGUI; use the elements themselves only.
    The provided layout will be used to create a custom preview window.
    Use with caution; this function relies on `eval()`.
    :param layout: A string representing the layout code.
    :param theme_name: The name of the theme that the preview is working with.
    :param themedict: The themedict of the given theme, mainly required if it's not a standard theme.
    """
    if theme_name not in LOOK_AND_FEEL_TABLE and themedict is None:
        message = f'The theme {theme_name} was not found within the LOOK_AND_FEEL_TABLE, ' \
            f'and its themedict wasn\'t supplied either.'
        raise KeyError(message)

    existing_theme: str = theme()

    theme(theme_name)

    layout: List[List[Element]] = eval(layout, GLOBALS)
    window: Window = Window(
        f'Custom Layout Preview for \'{theme_name}\' Theme.',
        layout
    )
    while True:
        e, v = window.read()
        if e in (None, 'Exit'):
            window.close()
            break
    theme(existing_theme)

custom_layout_preview(DEFAULT_LAYOUT, 'Default')
