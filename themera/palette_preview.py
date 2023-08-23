"""
d888888P dP
   88    88
   88    88d888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b.
   88    88'  `88 88ooood8 88'`88'`88 88ooood8 88'  `88 88'  `88
   88    88    88 88.  ... 88  88  88 88.  ... 88       88.  .88
   dP    dP    dP `88888P' dP  dP  dP `88888P' dP       `88888P8

Themera Palette Preview Functionality Script
PySimpleGUI Theme Code Generator
Copyright 2023 Divine Afam-Ifediogor
"""
import PySimpleGUI as sg
from colour import Color
from fonts import FONTS
from functions import (
    check_if_color,
    clamp,
    colorbox_text_color,
    flatten_themedict,
    invert,
)
from pyperclip import copy
from version_and_copyright import __version__
from window import Window


def palette_block(color):
    return sg.Button(
        color,
        key=f"{color}_color",
        size=(8, 5),
        expand_x=True,
        expand_y=True,
        button_color=(colorbox_text_color(color), color),
        pad=(0, 0),
        font=FONTS["medium"],
    )


def palette_preview(theme_name, themedict):
    """
    Displays a card type preview of the colors used in the theme.
    """
    flat = flatten_themedict(themedict)
    layout = [
        [sg.Text(f"{theme_name} Palette Preview", font=FONTS["icon"])],
        [
            palette_block(Color(_color).get_web())
            for _color in sorted(set(flat.values()), key=lambda x: Color(x).get_hue())
            if check_if_color(_color)
        ],
        [sg.Text("Click on a button to copy its color.", key="instruction")],
    ]
    window = Window(
        f"Palette Preview of {theme_name} | Themera v{__version__}",
        layout,
        modal=True,
    )
    while True:
        e, v = window.read()
        if e in (None, "Exit"):
            window.close()
            break
        if e.endswith("_color"):
            color = e.rsplit("_", 1)[0]
            copy(color)
            window[e]("Copied!")
            window["instruction"](f'Color "{color}" copied to clipboard.')

            def _action():
                window[e](color)
                window["instruction"]("Click on a button to copy its color.")

            window[e].widget.after(2000, _action)
