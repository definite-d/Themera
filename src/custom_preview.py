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
from traceback import format_exception
from typing import Dict, List, Optional, Union

from pyperclip import paste
from PySimpleGUI import (
    EMOJI_BASE64_HAPPY_BIG_SMILE,
    LOOK_AND_FEEL_TABLE,
    Button,
    Element,
    Input,
    Multiline,
    Push,
    Text,
    Window,
    theme,
    theme_add_new,
)

from .constants import DEFAULT_LAYOUT
from .fonts import FONTS

ELEMENTS = {element.__name__: element for element in Element.__subclasses__()}
GLOBALS = {"EMOJI_BASE64_HAPPY_BIG_SMILE": EMOJI_BASE64_HAPPY_BIG_SMILE}
GLOBALS.update(ELEMENTS)


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
    if theme_name not in LOOK_AND_FEEL_TABLE:
        if themedict is None:
            message = (
                f"The theme {theme_name} was not found within the LOOK_AND_FEEL_TABLE, "
                f"and its themedict wasn't supplied either."
            )
            raise KeyError(message)
        if themedict:
            LOOK_AND_FEEL_TABLE[f"{theme_name}____Themera_temp"] = themedict

    existing_theme: str = theme()
    theme(f"{theme_name}____Themera_temp")
    try:
        layout: List[List[Element]] = eval(layout, GLOBALS)
    except Exception as _exception:
        theme(existing_theme)
        raise (_exception)
    window: Window = Window(f"Custom Layout Preview for '{theme_name}' Theme.", layout)
    theme(existing_theme)

    while True:
        e, v = window.read()
        if e in (None, "Exit"):
            window.close()
            break
    if f"{theme_name}____Themera_temp" in LOOK_AND_FEEL_TABLE:
        del LOOK_AND_FEEL_TABLE[f"{theme_name}____Themera_temp"]


def custom_preview(
    present_theme: str,
    present_themedict: Dict[str, Union[int, str, tuple, list]],
    user_theme_name: str,
    user_themedict: Dict[str, Union[int, str, tuple, list]],
):
    """
    Gets the custom layout to preview from the user and carries out the preview operation.
    """
    theme_add_new(present_theme, present_themedict)
    theme(present_theme)
    layout = [
        [Text("Enter your layout", font=FONTS["theme_name"])],
        [Text("Please enter the layout code to preview")],
        [
            Text(
                "All PySimpleGUI elements are available; no need for aliases or imports."
            )
        ],
        [Multiline(DEFAULT_LAYOUT, k="user_layout", size=(50, 5), expand_x=True)],
        [
            Push(),
            Button(
                "Paste",
                tooltip="Paste the contents of the clipboard into the layout code entrybox.",
            ),
            Button("Preview"),
            Button("Cancel"),
        ],
    ]
    window = Window(
        "Custom Layout Entry",
        layout,
    )
    while True:
        e, v = window.read()

        if e in (None, "Cancel"):
            window.close()
            break

        elif e == "Paste":
            window["user_layout"](paste())

        elif e == "Preview":
            try:
                custom_layout_preview(v["user_layout"], user_theme_name, user_themedict)
            except Exception as exception:
                error = format_exception(exception, exception, exception.__traceback__)[
                    -1
                ]
                error_window = Window(
                    "Layout Error",
                    [
                        [Text(f"Layout Error", font=FONTS["icon"])],
                        [
                            Text(
                                "There seems to be an issue with the custom layout supplied."
                            )
                        ],
                        [Multiline(error, disabled=True, k="error_box", size=(50, 3))],
                        [Push(), Button("Close")],
                    ],
                )
                while True:
                    e = error_window.read()[0]
                    if e in (None, "Close"):
                        error_window.close()
                        break
