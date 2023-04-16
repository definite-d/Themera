"""
d888888P dP
   88    88
   88    88d888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b.
   88    88'  `88 88ooood8 88'`88'`88 88ooood8 88'  `88 88'  `88
   88    88    88 88.  ... 88  88  88 88.  ... 88       88.  .88
   dP    dP    dP `88888P' dP  dP  dP `88888P' dP       `88888P8

Themera Independent Functions File
PySimpleGUI Theme Code Generator
Copyright 2023 Divine Afam-Ifediogor
"""

# IMPORTS ______________________________________________________________________________________________________________
from _tkinter import TclError
from random import randint
from typing import Dict, List, Optional, Union, Tuple

import colour
import PySimpleGUI as sg
from PIL import Image
from psg_reskinner import reskin

from constants import DISPLAY_TO_THEMEDICT, EXPANSION_FORMAT, INDEX_MARKERS, SAFE_TO_EXPAND, THEMEDICT_TO_DISPLAY


# FUNCTIONS ____________________________________________________________________________________________________________
def rint(value: Union[int, float]) -> int:
    """
    Stands for "Rounded Integer"; rounds the given value to an integer.

    :param value: An integer or floating point value
    :return: An integer
    """
    return int(round(value, 0))


def flatten_themedict(themedict: Dict, targets=SAFE_TO_EXPAND) -> Dict:
    """
    Reduces themedicts with nested expandable iterable values (e.g. the value for BUTTON in most themedicts) to a new
    dict in which each nested value has its own key (e.g. BUTTON[0]: '#ffffff')

    :param themedict: The themedict to work on.
    :param targets: This is a list of keys that will be expanded as part of the flattening process. It defaults to the
    SAFE_SAFE_TO_EXPAND list.
    :return: A flattened Python dictionary.
    """
    new = {}
    for key in themedict.copy():
        if key in targets:
            for index, item in enumerate(themedict.copy()[key]):
                _key = str(key) + EXPANSION_FORMAT.replace('<index>', str(index))
                new[_key] = item
            continue
        new[key] = themedict.copy()[key]
    return new


def unflatten_themedict(themedict: Dict, original_themedict=Optional[Dict]) -> Dict:
    """
    Reverses the effects of the `flatten_themedict()` function and returns a Dict similar to a proper PySimpleGUI
    themedict.

    :param themedict: The flattened themedict to un-flatten.
    :param original_themedict: The original themedict that was fed into the `flatten_themedict()` function. Not
    required, but if given, it will be used as a guide to obtain the right iterable type.
    :return: An un-flattened themedict.
    """
    new = {}
    for key in themedict:
        if INDEX_MARKERS[0] in key and key.endswith(INDEX_MARKERS[1]):
            prefix, index = key.rstrip(INDEX_MARKERS[1]).rsplit(INDEX_MARKERS[0], 1)
            try:
                index = int(index)
            except TypeError:
                new[key] = themedict[key]
                continue
            try:
                new[prefix].insert(index, themedict[key])
            except KeyError:
                new[prefix] = [themedict[key]]
            continue
        new[key] = themedict[key]
    if original_themedict:
        for key in new:
            try:
                new[key] = type(original_themedict[key])(new[key])
            except (TypeError, ValueError):
                pass
    return new


def get_display_name(themedict_name: str) -> str:
    """
    "Converts" a given flattened-themedict key to a proper name for displaying in the UI, e.g. BUTTON[0] becomes
    'Button Text'.

    :param themedict_name: A key name from any flattened themedict.
    :return: A string.
    """
    try:
        return THEMEDICT_TO_DISPLAY[themedict_name]
    except KeyError:
        return str(' ').join([part.capitalize() for part in (themedict_name).split('_')])


def get_themedict_name(display_name: str) -> str:
    """
    "Converts" a given proper name for displaying in the UI to a flattened-themedict key, e.g. 'Button Text' becomes
    BUTTON[0].

    :param display_name: Any display name e.g. 'Accent 1'
    :return: A string
    """
    try:
        return DISPLAY_TO_THEMEDICT[display_name]
    except KeyError:
        return str('_').join([part.upper() for part in (display_name).split(' ')])


def check_if_color(value: str) -> bool:
    """
    Checks if the given value is a valid hex-format color or a valid color name.

    :param value: Any string.
    :return: True if the value is a valid color, else False.
    """
    v = str(value)
    if (v == '') or (' ' in v):
        return False
    try:
        colour.Color(v)
        return True
    except (ValueError, AttributeError):
        return False


def random_color() -> str:
    """
    Generates a random color.

    :return: A hex color string or valid color name.
    """
    color = '#'
    for n in range(3):
        color += str(format((randint(0, 255)), 'x').zfill(2))
    return colour.hex2web(color)


def alter_luminance(color: str, factor: float) -> str:
    """
    This function takes a color, adjusts its luminance value by a given factor (ranging from 0 to 1),
    and returns the resulting color.

    :param color: The color to work on.
    :param factor: The factor to alter the color's luminance by.
    :return: A new color with the luminance alteration applied.
    """
    color = colour.Color(color)
    val = color.get_luminance() * factor if color.get_luminance() else factor
    color.set_luminance(val if 0 <= val <= 1 else (0 if color.get_luminance() <= 0.5 else 1))
    return color.get_web()


def invert(color: str) -> str:
    """
    Inverts a given color (e.g. black becomes white)

    :param color: Any valid hex color or color name
    :return: An inverted color string
    """
    color = colour.Color(str(color))
    color.set_rgb((1 - color.get_red(), 1 - color.get_green(), 1 - color.get_blue()))
    return color.get_web()


def get_colors_from_image(image_object: Image.Image, number_of_colors: int) -> List:
    """
    Extracts the colors in a given image.

    :param image_object: A `PIL.Image.Image` object
    :param number_of_colors: The number of colors to extract from the image.
    :return: A list of colors of length `number_of_colors`.
    """
    image = image_object.copy().resize((64, 64)).convert('RGBA')
    colors = image.getcolors(maxcolors = image_object.size[0]*image_object.size[1])
    result = []
    for n in range(number_of_colors):
        value = colors[(int((len(colors) * n) / number_of_colors))]
        value = (value[1][0]/255, value[1][1]/255, value[1][2]/255)
        result.append(colour.rgb2web(value))
    return result


def reskin_mini_preview_window(window, key: str, themedict: Dict[str, Union[str, Tuple, List]]) -> None:
    """
    UI utility function.
    Made to easily reskin the mini preview window within a given window, along with multiple minor tweaks.

    :param window: The PySimpleGUI window object that has the mini preview.
    :param key: The key that was used to instantiate the mini preview's layout.
    :param themedict: The current themedict; required to obtain relevant color info.
    :return: None
    """
    targets = [el.key for el in window.element_list() if f'{key}_element' in str(el.key)]
    tb_targets = [el.key for el in window.element_list() if f'{key}_tb' in str(el.key)]
    sg.theme_add_new('___temp_themera_theme_currently_in_use___', themedict)
    reskin(
        window,
        '___temp_themera_theme_currently_in_use___',
        sg.theme, sg.LOOK_AND_FEEL_TABLE,
        target_element_keys=targets, reskin_background=False
    )
    for target in tb_targets:
        # Dummy Titlebar elements.
        if 'maincolumn' in target:
            window[target].ParentRowFrame.configure(background=invert(themedict['BUTTON'][1]))
        else:
            window[target].ParentRowFrame.configure(background=themedict['BUTTON'][1])
        try:
            window[target].widget.configure(
                background=themedict['BUTTON'][1])  # Should work for all.
            window[target].widget.configure(foreground=themedict['BUTTON'][0])
        except TclError:  # Then the widget doesn't have text.
            pass
    del sg.LOOK_AND_FEEL_TABLE['___temp_themera_theme_currently_in_use___']


def titlebar_button(themedict: Dict[str, Union[str, Tuple, List]], symbol: str, key: str) -> sg.Text:
    """
    UI utility function.
    Returns a custom titlebar "button" element.

    :param themedict: The current theme dictionary; required to obtain the necessary colors.
    :param symbol: The symbol for the button.
    :param key: The element's key.
    :return: A PySimpleGUI text element.
    """
    return sg.Text(
        symbol,
        text_color=themedict['BUTTON'][0],
        background_color=themedict['BUTTON'][1],
        font=sg.CUSTOM_TITLEBAR_FONT, k=f'{key}_tb_{symbol}')

def mini_preview_window_layout(
        key: str,
        themedict: Dict[str, Union[str, Tuple, List]],
        input_message='This is a preview of your theme'
) -> sg.Column:
    """
    UI utility function.
    Generates a layout on demand for the mini preview windows.

    :param key: An string from which all generated elements will derive their key.
    :param themedict: The current themedict. Required to obtain the necessary colors.
    :param input_message: The message to display within the editable input box.
    :return: A PySimpleGUI column containing the entire mini preview window layout.
    """
    bc = themedict['BUTTON'][1]
    return sg.Column([  # Mini preview window
        [sg.Column([
            [sg.Column([
                # Dummy Custom Titlebar lifted from PySimpleGUI's source.
                [
                    sg.Column([
                        [
                            sg.Image(data=sg.DEFAULT_BASE64_ICON_16_BY_16,
                                     background_color=bc, k=f'{key}_tb_icon'),
                            # Icon and Title
                            sg.Text('Quick Preview', text_color=themedict['BUTTON'][0],
                                    background_color=bc, k=f'{key}_tb_title'),
                        ]
                    ], pad=(0, 0), background_color=bc, k=f'{key}_tb_title_and_icon'),
                    sg.Column([
                        [
                            titlebar_button(themedict, sg.SYMBOL_TITLEBAR_MINIMIZE, key),
                            titlebar_button(themedict, sg.SYMBOL_TITLEBAR_MAXIMIZE, key),
                            titlebar_button(themedict, sg.SYMBOL_TITLEBAR_CLOSE, key),
                        ]
                    ], element_justification='r', expand_x=True, pad=(0, 0),
                        background_color=bc, k=f'{key}_tb_buttons')],
                [sg.Column([
                    [sg.Text('Sample Text; Lorem ipsum dolor sit amet...',
                             k=f'{key}_element_text', expand_x=True)],
                    [sg.Input(input_message, k=f'{key}_element_input',
                              expand_x=True)],
                    [sg.Button('Button', k=f'{key}_element_button')]
                ], k=f'{key}_element_bg', pad=(0, 0), expand_x=True)]
            ],
                expand_x=True, background_color=bc, k=f'{key}_tb_container', pad=(2, (0, 2)))],
        ], k=f'{key}_tb_maincolumn', element_justification='c',
            background_color=bc, pad=(1, 1), expand_x=True)]
    ], k=f'{key}_visibility_wrap', expand_x=True,
        background_color=invert(bc))

