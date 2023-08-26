"""
d888888P dP
   88    88
   88    88d888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b.
   88    88'  `88 88ooood8 88'`88'`88 88ooood8 88'  `88 88'  `88
   88    88    88 88.  ... 88  88  88 88.  ... 88       88.  .88
   dP    dP    dP `88888P' dP  dP  dP `88888P' dP       `88888P8

Themera Launcher Function File
PySimpleGUI Theme Code Generator
Copyright 2023 Divine Afam-Ifediogor
"""

# IMPORTS ______________________________________________________________________________________________________________
from base64 import b64decode, b64encode
from io import BytesIO
from random import getrandbits
from tkinter import StringVar
from typing import Dict, List, Tuple, Union

import PySimpleGUI as sg
from bytecode import BANNER, SIDEBAR
from colour import Color
from constants import (
    BACK_BUTTON_PADDING,
    CREATE_BUTTON_PADDING,
    DEFAULT_COLOR_THEME_FIELDS,
    DEFAULT_NON_COLOR_THEME_FIELDS,
    IMAGE_FILETYPES,
    IMAGE_INDEX,
    IMAGE_PREVIEW_SIZE,
    THEMES,
)
from filters import index_filter
from fonts import FONTS
from functions import (
    clamp,
    get_colors_from_image,
    mini_preview_window_layout,
    reskin_mini_preview_window,
    unflatten_themedict,
)
from open_docs import open_docs
from PIL import Image, ImageTk, UnidentifiedImageError
from preview_panel import PreviewPanel
from version_and_copyright import COPYRIGHT, __version__
from window import Window


# FUNCTIONS ____________________________________________________________________________________________________________
def action_button_row(key: str) -> List[sg.Element]:
    """
    UI utility function.
    Generates a row of action buttons for the launcher; `Create` and `Back`.

    :param key: A string from which the action buttons will derive their keys.
    :return: A list (row) containing a `Push` element and 2 `Button` elements.
    """
    return [
        sg.Push(),
        sg.Button("Create", k=f"{key}_start", pad=CREATE_BUTTON_PADDING),
        sg.Button("Back", k=f"{key}_back", pad=BACK_BUTTON_PADDING),
    ]


def theme_name_row(key: str) -> List[sg.Element]:
    """
    UI utility function.
    Generates a row for the theme name entry box.

    :param key: The element key.
    :return: A list containing a text element and the input itself.
    """
    return [sg.Text("Theme Name", size=(12, 1)), sg.Input(k=f"{key}_themename")]


def image_action(image: Image.Image) -> Dict[str, Union[str, Tuple, List]]:
    """
    This function gets invoked when a new theme is to be created from an image via the launcher.
    It gets the colors from the image, makes a themedict out of them and sorts them.

    :param image: A `PIL.Image.Image` object to work on.
    :return: A themedict of colors extracted from the image.
    """
    colors = get_colors_from_image(image, len(DEFAULT_COLOR_THEME_FIELDS))
    themedict = unflatten_themedict(dict((zip(DEFAULT_COLOR_THEME_FIELDS, colors))))
    themedict.update(DEFAULT_NON_COLOR_THEME_FIELDS)
    themedict = index_filter(themedict, IMAGE_INDEX)
    return themedict


def existing_validation(code: str) -> bool:
    """
    This function checks if the given theme code is valid or not and returns True or False.

    :param code: A string containing user theme code.
    :return: True if the theme code is valid else False.
    """
    if "{" not in code and "}" not in code:
        return False
    code = "{" + code.rsplit("{", 1)[1]
    code = code.split("}", 1)[0] + "}"
    try:
        exec(code, {}, {})
    except SyntaxError:
        return False
    return True


def existing_action(code):
    code = "{" + code.rsplit("{", 1)[1]
    code = code.split("}", 1)[0] + "}"
    return eval(code, {}, {})


def new_action(theme: str) -> Dict[str, Union[str, Tuple, List]]:
    """
    This function is invoked when a new theme (based on builtin PySimpleGUI themes) is to be created via the launcher.
    It simply obtains the appropriate themedict from the `LOOK_LOOK_AND_FEEL_TABLE`.

    :param theme: The name of the builtin PySimpleGUI theme.
    :return: The themedict for the given theme.
    """
    return sg.LOOK_AND_FEEL_TABLE[theme]


def get_preview_colors():
    col = Color(sg.theme_background_color())
    lum = col.get_luminance()
    if lum >= 0.5:
        col.set_luminance(clamp(lum * 0.8))
        preview_bg = col.get_hex()
        # col.set_saturation(0.2)
        col.set_luminance(lum)
        preview_fg = col.get_hex()
    else:
        col.set_luminance(clamp(lum * 1.8))
        preview_bg = col.get_hex()
        col.set_saturation(0.2)
        col.set_luminance(clamp(lum * 4))
        preview_fg = col.get_hex()
    del col, lum
    return preview_bg, preview_fg


def sidebar():
    """
    Compound element function. Returns the sidebar used in multiple layouts.
    """
    return sg.Column(
        [
            [
                sg.Image(
                    data=SIDEBAR,
                    subsample=3,
                    pad=(0, 0),
                    expand_y=True,
                )
            ]
        ],
        pad=(0, 0),
        expand_y=True,
        expand_x=True,
    )


def Launcher(set_to: str = "main"):
    """
    This function is responsible for initializing a new launcher upon startup and when requested by the user.

    :return: None
    """
    themes, default_theme = (
        tuple(
            theme
            for theme in sorted(THEMES)
            if sg.COLOR_SYSTEM_DEFAULT not in sg.LOOK_AND_FEEL_TABLE[theme].values()
        ),
        "Black",
    )
    image: sg.Optional[Image.Image] = None
    preview_bg, preview_fg = get_preview_colors()
    layout = [
        [
            sg.Column(
                [
                    [sg.Image(data=BANNER, subsample=2, pad=(0, 0), expand_x=True)],
                    [
                        sg.Push(),
                        sg.Text(
                            "The PySimpleGUI Theme Editor",
                            font=FONTS["tagline"],
                        ),
                        sg.Push(),
                    ],
                    [
                        sg.Button(
                            "New Theme",
                            font=FONTS["medium"],
                            k="new_route",
                            pad=((10, 0), 5),
                            expand_x=True,
                        ),
                        sg.Button(
                            "Edit Existing Theme",
                            font=FONTS["medium"],
                            k="existing_route",
                            pad=(5, 5),
                            expand_x=True,
                        ),
                        sg.Button(
                            "Theme from Image",
                            font=FONTS["medium"],
                            k="image_route",
                            pad=((0, 10), 5),
                            expand_x=True,
                        ),
                    ],
                    [sg.Text(COPYRIGHT, pad=(0, (5, 10)))],
                ],
                k="main_panel",
                visible=set_to == "main",
                element_justification="center",
                expand_x=True,
                expand_y=True,
                pad=(0, 0),
            ),
            sg.Column(
                [
                    [
                        sidebar(),
                        sg.Column(
                            [
                                [
                                    sg.Text(
                                        "Create New Theme",
                                        font=FONTS["medium"],
                                        expand_x=True,
                                    )
                                ],
                                theme_name_row("new"),
                                [
                                    sg.Text("Based on", size=(9, 1)),
                                    sg.DropDown(
                                        themes,
                                        default_theme,
                                        readonly=True,
                                        expand_x=True,
                                        k="new_theme",
                                        enable_events=True,
                                    ),
                                ],
                                [sg.VPush()],
                                [
                                    mini_preview_window_layout(
                                        "new",
                                        sg.LOOK_AND_FEEL_TABLE[default_theme],
                                        "Some text",
                                        "Mini preview.",
                                    )
                                ],
                                [sg.VPush()],
                                action_button_row("new"),
                            ],
                            pad=(5, 5),
                            expand_x=True,
                            expand_y=True,
                        ),
                    ]
                ],
                k="new_panel",
                visible=set_to == "new",
                expand_y=True,
                expand_x=True,
                pad=(0, 0),
            ),
            sg.Column(
                [
                    [
                        sidebar(),
                        sg.Column(
                            [
                                # [sg.VPush()],
                                [sg.Text("Edit Existing Theme", font=FONTS["medium"])],
                                theme_name_row("existing"),
                                [
                                    sg.Multiline(
                                        "~ Your theme's value dict goes here. ~",
                                        k="existing_themecode",
                                        expand_x=True,
                                        expand_y=True,
                                    )
                                ],
                                action_button_row("existing"),
                                # [sg.VPush()],
                            ],
                            pad=(5, 5),
                            expand_x=True,
                            expand_y=True,
                        ),
                    ],
                ],
                k="existing_panel",
                visible=set_to == "existing",
                expand_y=True,
                expand_x=True,
                pad=(0, 0),
            ),
            sg.Column(
                [
                    [
                        sidebar(),
                        sg.Column(
                            [
                                # [sg.VPush()],
                                [
                                    sg.Text(
                                        "Theme from Image",
                                        font=FONTS["medium"],
                                        expand_x=True,
                                    )
                                ],
                                theme_name_row("image"),
                                [
                                    sg.Input(
                                        "~ No image selected. ~",
                                        expand_x=True,
                                        pad=(5, 2),
                                        size=(20, 1),
                                        enable_events=True,
                                        k="image_filepath",
                                    ),
                                    sg.FileBrowse(file_types=IMAGE_FILETYPES),
                                ],
                                # [sg.VPush()],
                                [
                                    # sg.Push(),
                                    sg.Canvas(
                                        expand_x=True,
                                        expand_y=True,
                                        k="image_preview",
                                        pad=(5, (0, 2)),
                                        background_color=preview_bg,
                                    ),
                                    # sg.Push(),
                                ],
                                # [sg.VPush()],
                                action_button_row("image"),
                                # [sg.VPush()],
                            ],
                            pad=(5, 5),
                            expand_x=True,
                            expand_y=True,
                        ),
                    ],
                ],
                k="image_panel",
                visible=set_to == "image",
                expand_y=True,
                expand_x=True,
                pad=(0, 0),
            ),
            sg.Column(
                [
                    [
                        sidebar(),
                        sg.Column(
                            [
                                [sg.VPush()],
                                [
                                    sg.Text(
                                        "Loading... Please be patient",
                                        font=FONTS["medium"],
                                        expand_x=True,
                                    )
                                ],
                                [sg.VPush()],
                            ],
                            pad=(5, 5),
                            expand_x=True,
                            expand_y=True,
                        ),
                    ]
                ],
                k="loading_panel",
                visible=set_to == "loading",
                expand_x=True,
                expand_y=True,
                pad=(0, 0),
            ),
        ],
    ]

    launcher = Window(
        f"Themera v{__version__}",
        layout,
        element_justification="center",
        margins=(0, 0),
        size=(500, 367),
        modal=False,
    ).finalize()

    launcher.TKroot.bind(
        "<KeyPress-F1>",
        lambda e: open_docs(),
    )

    center_coords = tuple(c / 2 for c in IMAGE_PREVIEW_SIZE)
    preview_panel: PreviewPanel = PreviewPanel(launcher["image_preview"], preview_fg)

    name_variable = StringVar(
        launcher.TKroot, f"NewTheme{getrandbits(16)}", "theme_name"
    )
    for element in launcher.element_list():
        if str(element.key).endswith("themename"):
            element.widget.configure(textvariable=name_variable)
    reskin_mini_preview_window(launcher, "new", sg.LOOK_AND_FEEL_TABLE[default_theme])
    launcher.set_min_size(launcher.size)
    themedict = {}
    while True:
        e, v = launcher()
        if e in (None, "Exit"):
            launcher.close()
            break

        if e == "new_theme":
            reskin_mini_preview_window(
                launcher, "new", sg.LOOK_AND_FEEL_TABLE[v["new_theme"]]
            )
            continue

        if e == "image_filepath":
            image = preview_panel.preview(v["image_filepath"])
            continue

        if e.endswith("route"):
            e = e.split("_", 1)[0]
            launcher["main_panel"](visible=False)
            launcher[f"{e}_panel"](visible=True)
            launcher[f"{e}_start"].BindReturnKey = True
            continue

        if e.endswith("back"):
            e = e.split("_", 1)[0]
            launcher[f"{e}_panel"](visible=False)
            launcher[f"main_panel"](visible=True)
            launcher[f"{e}_start"].BindReturnKey = False
            continue

        if e.endswith("start"):
            e = e.split("_", 1)[0]
            if e == "existing":
                if not existing_validation(v["existing_themecode"]):
                    sg.PopupError(
                        "Your themedict is invalid. Please correct it.",
                        title="Invalid theme dictionary!",
                    )
                    continue
                themedict = existing_action(v["existing_themecode"])
            if e == "new":
                themedict = new_action(v["new_theme"])
            if e == "image":
                if not image:
                    sg.PopupError("No valid image selected.", title="Invalid image!")
                    continue
                themedict = image_action(image)
            launcher["loading_panel"](visible=True)
            launcher[f"{e}_panel"](visible=False)
            break

    return name_variable.get(), themedict, launcher
