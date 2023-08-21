"""
d888888P dP
   88    88
   88    88d888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b.
   88    88'  `88 88ooood8 88'`88'`88 88ooood8 88'  `88 88'  `88
   88    88    88 88.  ... 88  88  88 88.  ... 88       88.  .88
   dP    dP    dP `88888P' dP  dP  dP `88888P' dP       `88888P8

Themera Main File
PySimpleGUI Theme Code Generator
Copyright 2023 Divine Afam-Ifediogor
"""

# Greetings to whoever can see the console.
from .version_and_copyright import __version__

print(f"Themera v{__version__} started successfully.")


# (OTHER) IMPORTS ______________________________________________________________________________________________________
from os.path import abspath, isfile
from random import shuffle
from tkinter import colorchooser
from typing import Dict, List, Optional, Tuple, Union
from webbrowser import open_new_tab as open_link

import colour
import PySimpleGUI as sg
from _tkinter import TclError
from pyperclip import copy

from .bytecode import THEMERA_LOGO
from .color_shorthands import COLOR_SHORTHANDS
from .constants import (
    ALT,
    APP_ID,
    BATCH_ACTIONS,
    BORDER_UPPER_LIMIT,
    CONTRAST_THRESHOLD,
    CONTRAST_THRESHOLD_MULTIPLIER,
    CTRL,
    CTRL_EVENT,
    EXTERNAL_LINK_ICON,
    GEAR_ICON,
    HELP_PATH,
    LINK_DEVELOPER,
    LINK_DOCS_DL,
    LINK_GITHUB_REPO,
    LINK_NEW_GITHUB_ISSUE,
    LINK_PYSIMPLEGUI_SITE,
    PENCIL_ICON,
    WARNING_ICON,
)
from .crash import handle_crash
from .custom_preview import custom_preview
from .filters import FILTER_MAPPING, FILTERS
from .fonts import FONTS
from .functions import (
    alter_luminance,
    check_if_color,
    flatten_themedict,
    get_display_name,
    invert,
    mini_preview_window_layout,
    random_color,
    reskin_mini_preview_window,
    rint,
    unflatten_themedict,
)
from .launcher import Launcher
from .settings import SETTINGS
from .themes import DarkTheme, LightTheme
from .window import Window

# SETTINGS.save_settings()

# FUNCTIONS AND UI _____________________________________________________________________________________________________
sg.set_options(dpi_awareness=True)
if sg.running_windows():
    import ctypes
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            APP_ID
        )  # Adapted from PySimpleGUI source.
    except Exception as e:
        print("Failed to set App ID for Windows.")

sg.theme_add_new("Themera Light", LightTheme)
sg.theme_add_new("Themera Dark", DarkTheme)
sg.theme(SETTINGS["theme"])
sg.set_options(font=FONTS["regular"], icon=THEMERA_LOGO, border_width=0)


# This variable is used to tell Themera whether to run again after being exited. It is used for returning to the
# launcher while avoiding event loop nesting.
relaunch_options: Optional[List[Union[Window, str]]] = None


def menudef_to_shortcut_router_dict(menudef):
    return {
        tuple(subsection.split("(")[1].lstrip(" ")[0:-1].split("+")): subsection.split(
            " ("
        )[0].replace("&", "")
        for section in menudef
        for subsection in section[1]
        if subsection.endswith(")")
    }


def get_proper_colorbox_textcolor(color):
    bg_color = colour.Color(color)
    text_color = colour.Color(invert(color))
    if abs(bg_color.get_luminance() - text_color.get_luminance()) <= CONTRAST_THRESHOLD:
        if text_color.get_luminance() > bg_color.get_luminance():
            sign = 1
        else:
            sign = -1
        text_color.set_luminance(
            min(
                1,
                text_color.get_luminance()
                + (CONTRAST_THRESHOLD * CONTRAST_THRESHOLD_MULTIPLIER * sign),
            )
            if sign == 1
            else max(
                0,
                text_color.get_luminance()
                + (CONTRAST_THRESHOLD * CONTRAST_THRESHOLD_MULTIPLIER * sign),
            )
        )
    return text_color.get_web()


def themedict_entry(name, value, name_size=16, value_size=10):
    if check_if_color(value):
        text = (
            get_proper_colorbox_textcolor(value)
            if SETTINGS["colorboxes"]
            else sg.theme_input_text_color()
        )
        bg = value if SETTINGS["colorboxes"] else sg.theme_input_background_color()
        return (
            sg.Checkbox(
                f"{get_display_name(name)}",
                k=f"{name}_entryname",
                enable_events=True,
                pad=(0, 0),
                size=(name_size, 1),
                tooltip=f"{get_display_name(name)}",
            ),
            sg.Text(
                WARNING_ICON,
                k=f"{name}_warning",
                font=FONTS["icon"],
                pad=(0, 0),
                text_color=sg.theme_background_color(),
            ),
            sg.Input(
                value,
                k=f"{name}_value",
                size=(value_size, 1),
                expand_x=True,
                metadata="is_color",
                text_color=text,
                background_color=bg,
            ),
            sg.Text(
                PENCIL_ICON,
                k=f"{name}_pickcolor",
                font=FONTS["icon"],
                enable_events=True,
                pad=((0, 3), 0),
            ),
        )
    if type(value) == int:
        return (
            sg.Text(
                f"{get_display_name(name)}",
                k=f"{name}_entryname",
                pad=((23, 0), 0),
                size=(name_size, 1),
                tooltip=f"{get_display_name(name)}",
            ),
            sg.Text(
                WARNING_ICON,
                k=f"{name}_warning",
                font=FONTS["icon"],
                pad=(0, 0),
                text_color=sg.theme_background_color(),
            ),
            sg.Spin(
                [n for n in range(0, BORDER_UPPER_LIMIT)],
                value,
                k=f"{name}_value",
                expand_x=True,
                size=(value_size, 1),
                metadata=type(value),
            ),
        )
    if type(value) == float:
        return (
            sg.Text(
                f"{get_display_name(name)}",
                k=f"{name}_entryname",
                pad=((23, 0), 0),
                size=(name_size, 1),
                tooltip=f"{get_display_name(name)}",
            ),
            sg.Text(
                WARNING_ICON,
                k=f"{name}_warning",
                font=FONTS["icon"],
                pad=(0, 0),
                text_color=sg.theme_background_color(),
            ),
            sg.Spin(
                [n / 10 for n in range(0, BORDER_UPPER_LIMIT)],
                value,
                k=f"{name}_value",
                expand_x=True,
                size=(value_size, 1),
                metadata=type(value),
            ),
        )
    return (
        sg.Text(
            f"{get_display_name(name)}",
            k=f"{name}_entryname",
            pad=((23, 0), 0),
            size=(name_size, 1),
            tooltip=f"{get_display_name(name)}",
        ),
        sg.Text(
            WARNING_ICON,
            k=f"{name}_warning",
            font=FONTS["icon"],
            pad=(0, 0),
            text_color=sg.theme_background_color(),
        ),
        sg.Input(
            str(value),
            k=f"{name}_value",
            expand_x=True,
            size=(value_size, 1),
            metadata=type(value),
        ),
    )


def get_editor_window_layout(
    theme_name: str,
    themedict: Dict[str, Union[str, Tuple, List]],
    shortcut_router: Dict[Tuple, Union[str, Tuple, List]],
):
    menu_layout = [
        [
            "&Theme",
            [
                f"&Create New Theme ({CTRL}+N)",
                f"&Edit Existing Theme ({CTRL}+Shift+N)",
                f"&Theme From Image ({CTRL}+{ALT}+N)",
                f"Return to &Launcher ({CTRL}+{ALT}+L)",
                f"&Settings ({CTRL}+Shift+S)",
                f"&Revert to Beginning ({CTRL}+{ALT}+R)",
            ],
        ],
        [
            "&Help",
            [
                "&Themera Help (F1)",
                f"&Report Issue on GitHub {EXTERNAL_LINK_ICON}",
                f"&PySimpleGUI Docs {EXTERNAL_LINK_ICON}",
                "&View valid color names",
            ],
        ],
        [
            "&Links",
            [
                f"&Visit Themera's GitHub Page {EXTERNAL_LINK_ICON}",
                f"&Developer's GitHub Profile {EXTERNAL_LINK_ICON}",
            ],
        ],
    ]
    shortcut_router.update(menudef_to_shortcut_router_dict(menu_layout))
    top_layout = [
        [
            sg.Column(
                [
                    [
                        sg.Text(theme_name, k="theme_name", font=FONTS["theme_name"]),
                        sg.Input(
                            theme_name,
                            k="theme_name_value",
                            font=FONTS["theme_name"],
                            visible=False,
                            size=(15, 1),
                        ),
                        sg.Text(
                            PENCIL_ICON,
                            k="edit_theme_name",
                            enable_events=True,
                            visible=False,
                            font=FONTS["icon"],
                        ),
                    ]
                ],
                pad=(0, 0),
                k="theme_name_container",
            ),
            sg.Push(),
            sg.Text(GEAR_ICON, k="Settings", font=FONTS["icon"], enable_events=True),
        ],
    ]
    edit_frame_layout = [
        [sg.Checkbox("Select All", k="select_all", enable_events=True, pad=(0, 0))]
    ]
    themedict_flat = flatten_themedict(themedict)
    max_name_size = rint(
        max([len(x) for x in [get_display_name(name) for name in themedict_flat]])
        * 0.83
    )
    for name, value in themedict_flat.items():
        edit_frame_layout.append(themedict_entry(name, value, max_name_size))
    edit_frame_layout.append(
        [
            sg.Column(
                [
                    [
                        sg.DropDown(
                            BATCH_ACTIONS,
                            BATCH_ACTIONS[0],
                            expand_x=True,
                            k="entry_action_dropdown",
                            readonly=True,
                            disabled=True,
                            enable_events=True,
                            tooltip="Batch Actions",
                        ),
                        sg.Button("Execute", k="execute_entry_action", disabled=True),
                    ]
                ],
                k="entry_action_container",
                pad=(0, 0),
                expand_x=True,
            )
        ]
    )
    left_layout = [
        [
            sg.Frame(
                "Theme Values",
                edit_frame_layout,
                k="edit_frame",
                element_justification="c",
                expand_x=True,
                expand_y=True,
            )
        ]
    ]
    right_layout = [
        [
            sg.Frame(
                "Theme Preview and Generation",
                [
                    [
                        sg.DropDown(
                            FILTERS,
                            FILTERS[0],
                            k="filter",
                            readonly=True,
                            expand_x=True,
                            pad=((5, 5), (2, 8)),
                            enable_events=True,
                        ),
                    ],
                    [mini_preview_window_layout("quickpreview", themedict)],
                    [
                        sg.Multiline(
                            expand_y=True, expand_x=True, k="theme_code", disabled=True
                        )
                    ],
                    [
                        sg.Button("Copy Theme Code", k="copy", pad=(4, 4)),
                        sg.Button("Full Preview", k="full_preview", pad=(4, 4)),
                        sg.Button(
                            "Apply Filter", k="apply_filter", pad=(4, 4), disabled=True
                        ),
                    ],
                ],
                expand_y=True,
                expand_x=True,
                element_justification="c",
            )
        ]
    ]
    return [
        [sg.Menu(menu_layout)],
        [sg.Column(top_layout, expand_x=True)],
        [
            sg.Column(left_layout, expand_y=True, expand_x=True, pad=((2, 1), 2)),
            sg.Column(
                right_layout,
                expand_y=True,
                expand_x=True,
                element_justification="c",
                pad=((1, 2), 2),
            ),
        ],
    ]


class Editor:
    def __init__(self, theme_name, themedict=None):
        self.copy_id = None
        self.theme_name = theme_name
        self.shortcut_router = {
            (CTRL, "Shift", "a"): "select_all_kb",
            (CTRL, "Shift", "c"): "copy",
            (CTRL, "Shift", "e"): "execute_entry_action",
        }
        self.shortcut_key = None
        self.color_shorthands = COLOR_SHORTHANDS.copy()
        self.original_themedict = (
            themedict.copy() if themedict else sg.LOOK_AND_FEEL_TABLE[theme_name].copy()
        )
        self.values = {
            f"{k}_value": v
            for k, v in flatten_themedict(self.original_themedict).items()
        }
        self.invalids = set()
        self.previous_themedict = self.original_themedict.copy()
        self.preview_themedict = self.original_themedict.copy()
        self.window = Window(
            f"'{self.theme_name}' Theme | Themera v{__version__} Editor",
            get_editor_window_layout(
                self.theme_name, self.original_themedict.copy(), self.shortcut_router
            ),
            modal=False,
            resizable=True,
        )
        self.window.editor_object = self
        self.window.finalize()

        for k, v in self.shortcut_router.items():
            k = k[:-1] + tuple(k[-1].upper())
            v = v[:-3] if v.endswith("_kb") else v
            if v in self.window.key_dict.keys():
                self.window[v].set_tooltip("+".join(k))

        self.window["theme_name"].widget.bind(
            "<Enter>", lambda e: self.window["edit_theme_name"](visible=True)
        )
        self.window["theme_name_container"].widget.bind(
            "<Leave>", lambda e: self.window["edit_theme_name"](visible=False)
        )

        self.window["edit_theme_name"].widget.bind(
            "<Button-1>", lambda e: self.edit_theme_name_action()
        )
        self.window["theme_name"].widget.bind(
            "<Button-1>", lambda e: self.edit_theme_name_action()
        )
        self.window["theme_name_container"].widget.bind(
            "<Button-1>", lambda e: self.edit_theme_name_action()
        )

        self.window["theme_name_value"].widget.bind(
            "<FocusOut>", lambda e: self.theme_name_value_action()
        )
        self.window["theme_name_value"].widget.bind(
            "<Return>", lambda e: self.theme_name_value_action()
        )
        self.window["theme_name_value"].widget.bind(
            "<Escape>", lambda e: self.theme_name_value_action()
        )
        for shortcut, key in self.shortcut_router.items():
            bindstr = (
                f"<"
                f'{f"{CTRL_EVENT}-" if CTRL in shortcut else ""}'
                f'{"Shift-" if "Shift" in shortcut else ""}'
                f'{f"{ALT}-" if ALT in shortcut else ""}'
            )
            # Bind for both caps and lower because Tk is quirky about case.
            self.window.TKroot.bind(
                bindstr + f"KeyPress-{shortcut[-1].upper()}>",
                lambda e, key=key: setattr(self, "shortcut_key", key),
            )
            try:
                self.window.TKroot.bind(
                    bindstr + f"KeyPress-{shortcut[-1].lower()}>",
                    lambda e, key=key: setattr(self, "shortcut_key", key),
                )
            except TclError:
                pass
        self.update_quick_preview(self.original_themedict)
        self.update_theme_code(self.generate_theme_code(self.original_themedict))
        self.window.bring_to_front()
        self.window.force_focus()

    def __call__(self, *args, **kwargs):
        self.read()

    def _update_color_value(self, key, new_value):
        self.window[key](new_value)
        if SETTINGS["colorboxes"]:
            text_color = get_proper_colorbox_textcolor(new_value)
            self.window[key].widget["insertbackground"] = text_color
            self.window[key].widget["background"] = new_value
            self.window[key].widget["foreground"] = text_color
            self.window[key].widget["highlightbackground"] = text_color
            self.window[key].widget["highlightcolor"] = new_value
            # self.window[key](
            #     background_color=new_value,
            #     text_color=text_color,
            # )
            # self.window[key].widget.configure(**config)
        else:
            self.window[key](
                background_color=sg.theme_input_background_color(),
                text_color=sg.theme_input_text_color(),
            )

    def color_picker(self, targets: List):
        if check_if_color(self.values[f"{targets[0]}_value"]):
            display_names = [get_display_name(name) for name in targets]
            title = (
                f"{display_names[0]} Color"
                if len(display_names) == 1
                else f'Color Picker ({", ".join(display_names)})'
            )
            color = colorchooser.askcolor(
                parent=self.window.TKroot,
                color=self.values[f"{targets[0]}_value"],
                title=title,
            )
            if color[1]:
                color = colour.hex2web(color[1])
                for target in targets:
                    self._update_color_value(f"{target}_value", color)

    def edit_theme_name_action(self):
        self.window["theme_name"](visible=False)
        self.window["edit_theme_name"](visible=False)
        self.window["theme_name_value"](visible=True)

    def theme_name_value_action(self):
        self.theme_name = self.window["theme_name_value"].TKStringVar.get()
        self.window["theme_name"](self.theme_name, visible=True)
        # self.window['edit_theme_name'](visible=True)
        self.window["theme_name_value"](visible=False)
        self.window.set_title(
            f"'{self.theme_name}' Theme | Themera v{__version__} Editor"
        )
        self.update_theme_code(self.generate_theme_code(self.themedict))

    def check_user_colors(self, value):
        try:
            return self.color_shorthands[str(value).lower()]
        except KeyError:
            return value

    def invalid_action(self, name):
        self.invalids.add(name)
        self.window[f"{name}_warning"].widget.configure(
            foreground=sg.theme_text_color()
        )

    def valid_action(self, name):
        try:
            self.invalids.remove(name)
        except KeyError:
            pass
        self.window[f"{name}_warning"].widget.configure(
            foreground=sg.theme_background_color()
        )

    def validate_theme_values(self):
        for name in flatten_themedict(self.themedict):
            key = f"{name}_value"
            value = self.values[key]

            if self.check_user_colors(value) != value:
                value = self.check_user_colors(value)
                self.values[key] = value
                self.window[key](value)

            if self.window[key].metadata == "is_color":
                if check_if_color(value):
                    self.valid_action(name)
                    self._update_color_value(key, value)
                else:
                    self.invalid_action(name)
                continue

            else:
                value_type = self.window[key].metadata
                try:
                    if value in (None, "", "-") or (
                        (issubclass(value_type, int) or issubclass(value_type, float))
                        and value_type(value) < 0
                    ):
                        self.invalid_action(name)
                        continue
                    value = eval(f"{value_type.__name__}({value})")
                except (ValueError, SyntaxError):
                    self.invalid_action(name)
                    continue

                self.valid_action(name)

    def write_themedict(self, themedict):
        flat = {f"{k}_value": str(v) for k, v in flatten_themedict(themedict).items()}
        for k, v in flatten_themedict(themedict).items():
            if self.window[f"{k}_value"].metadata == "is_color":
                self._update_color_value(f"{k}_value", v)
            else:
                self.window[f"{k}_value"](v)

    @property
    def themedict(self):
        flat = flatten_themedict(self.original_themedict)
        for key, value in flat.items():
            flat[key] = self.check_user_colors(value)
            widget = self.window[f"{key}_value"]
            value = self.values[f"{key}_value"]
            if widget.metadata != "is_color":
                try:
                    value = eval(f"{widget.metadata.__name__}({value})")
                except (ValueError, SyntaxError):
                    pass
            flat[key] = value
        result = unflatten_themedict(flat, self.original_themedict)
        return result

    def generate_theme_code(self, themedict):
        formatted_dict = "{\n"
        for k, v in themedict.copy().items():
            if isinstance(v, str) and v[0] not in ("{", "[", "("):
                # self.window.TKroot.tk.call('eval', f'Tk_GetColor {v}')
                v = f"'{self.check_user_colors(v)}'"
            if isinstance(k, str):
                k = f"'{k}'"
            formatted_dict += f"        {k}: {v}, \n"
        formatted_dict += "    }\n"
        return (
            f'{SETTINGS["psg_alias"]}.theme_add_new(\n    \'{self.theme_name}\', '
            f'\n    {formatted_dict})\n{SETTINGS["psg_alias"]}.theme(\'{self.theme_name}\')'
        )

    def update_theme_code(self, value: str):
        self.window["theme_code"](value)

    def update_quick_preview(self, themedict):
        current_filter = FILTER_MAPPING[FILTERS[self.window["filter"].widget.current()]]
        self.preview_themedict = (
            themedict.copy() if not current_filter else current_filter(themedict.copy())
        )
        reskin_mini_preview_window(self.window, "quickpreview", self.preview_themedict)

    def default_full_preview(self):
        _theme = sg.theme()
        preview_theme = f"{self.theme_name}_____fullpreview"
        sg.theme_add_new(preview_theme, self.preview_themedict.copy())
        sg.theme(preview_theme)
        preview_layout = [
            [sg.Text("Theme Preview", font=FONTS["theme_name"])],
            [sg.Text("This is how your theme will look when used.")],
            [sg.Text("This window serves no other purpose than being a mannequin.")],
            [sg.Text("Only the exit button works.")],
            [sg.InputText("...just a textbox", size=(60, 8))],
            [
                sg.Multiline(
                    f"# This is the code responsible for this window's theme.\n"
                    f"\n{self.generate_theme_code(self.themedict)}",
                    size=(58, 5),
                )
            ],
            [
                sg.Frame(
                    title="Progress Bar Preview",
                    layout=[
                        # [sg.Text('This bar is static though.')],
                        [
                            sg.ProgressBar(
                                max_value=1000,
                                orientation="h",
                                size=(35, 20),
                                key="p_bar",
                            )
                        ]
                    ],
                )
            ],
            [
                sg.Frame(
                    title="Slider Preview",
                    layout=[
                        [sg.Text("This is a useless slider.")],
                        [
                            sg.Slider(
                                range=(0, 1000),
                                size=(35, 10),
                                default_value=504,
                                orientation="h",
                            )
                        ],
                    ],
                )
            ],
            [
                sg.Frame(
                    title="Useless Buttons",
                    layout=[
                        [
                            sg.Button(" Button A ", key="btn_a"),
                            sg.Button(" Button B ", key="btn_b"),
                            sg.Button(" Button C ", key="btn_c"),
                            sg.Button(" Another useless button. ", key="btn_d"),
                        ]
                    ],
                )
            ],
            [sg.Button(" Exit ", key="Exit")],
        ]
        preview_window = Window(
            f"'{self.theme_name}' Full Preview | Themera v{__version__} Editor",
            preview_layout,
            element_justification="center",
            modal=True,
        )
        sg.theme(_theme)
        del sg.LOOK_AND_FEEL_TABLE[preview_theme]
        Window._move_all_windows = True
        while True:
            e, v = preview_window(timeout=30)
            if e in (None, "Exit"):
                preview_window.close()
                break
            if e == sg.TIMEOUT_EVENT:
                progbar_value = preview_window[
                    "p_bar"
                ].TKProgressBar.TKProgressBarForReal["value"]
                progbar_max_value = preview_window["p_bar"].MaxValue
                if progbar_value <= progbar_max_value:
                    preview_window["p_bar"](progbar_value + 5)
                else:
                    preview_window["p_bar"](0)
        Window._move_all_windows = False

    def read(self):
        global relaunch_options
        while True:
            if self.shortcut_key:
                event: str = self.shortcut_key
                self.shortcut_key = None
            else:
                event, self.values = self.window(timeout=350)
                if self.values:
                    self.validate_theme_values()

            if event in (None, "Exit", sg.WIN_CLOSED):
                self.window.close()
                break

            if (
                len(self.invalids) == 0 and self.previous_themedict != self.themedict
            ):  # No invalid values
                themedict = self.themedict.copy()
                theme_code = self.generate_theme_code(themedict)
                if self.values["theme_code"] != theme_code:
                    self.values["theme_code"] = theme_code
                    self.previous_themedict = themedict
                    self.update_theme_code(theme_code)
                    self.update_quick_preview(themedict)

            if event.endswith("pickcolor"):
                self.color_picker([event.rsplit("_", 1)[0]])

            if event == "full_preview":
                if SETTINGS["full_preview_mode"] == "default":
                    self.default_full_preview()
                elif SETTINGS["full_preview_mode"] == "custom":
                    current_theme = sg.theme()
                    custom_preview(
                        current_theme,
                        sg.LOOK_AND_FEEL_TABLE[current_theme],
                        self.theme_name,
                        self.themedict,
                    )

            if event.startswith("Settings"):
                SETTINGS.edit(sg, self)

            if event == "View valid color names":
                color_names = []
                for color in colour.COLOR_NAME_TO_RGB:
                    color_names.append(
                        (
                            [
                                sg.Text(
                                    text=color,
                                    size=(20, 1),
                                    text_color=sg.theme_input_text_color(),
                                    background_color=sg.theme_input_background_color(),
                                ),
                                sg.Button(
                                    "",
                                    key=f"{color}_col",
                                    tooltip=colour.web2hex(color),
                                    button_color=("#000000", colour.web2hex(color)),
                                    size=(10, 1),
                                ),
                            ]
                        )
                    )
                viewer_layout = [
                    [
                        sg.Text(
                            text=(
                                f"These are {len(colour.COLOR_NAME_TO_RGB)} valid color names."
                            )
                        )
                    ],
                    [sg.Text("Ranked from darkest to lightest.")],
                    [
                        sg.Column(
                            layout=color_names,
                            size=(270, 200),
                            scrollable=True,
                            vertical_scroll_only=True,
                            background_color=sg.theme_input_background_color(),
                            element_justification="center",
                        )
                    ],
                    [sg.Text("Clicking a color's button copies the color.")],
                    [sg.Button("Exit")],
                ]
                viewer = Window(
                    "Valid Color Name List",
                    layout=viewer_layout,
                    element_justification="center",
                    modal=False,
                )
                while True:
                    viewer_e = viewer()[0]
                    if "col" in str(viewer_e):
                        copy(viewer_e.rsplit("_", 1)[0])
                    if viewer_e in (None, "Exit"):
                        viewer.close()
                        break

            if event == f"Visit Themera's GitHub Page":
                open_link(LINK_GITHUB_REPO)
            if event == f"Developer's GitHub Profile":
                open_link(LINK_DEVELOPER)
            if event == f"Report Issue on GitHub":
                open_link(LINK_NEW_GITHUB_ISSUE)
            if event == f"PySimpleGUI Docs":
                open_link(LINK_PYSIMPLEGUI_SITE)

            if event.startswith("Themera Help"):
                _path = abspath(HELP_PATH)
                if isfile(_path):
                    if sg.running_windows():
                        from os import startfile

                        startfile(_path)
                    else:
                        from os import system

                        if sg.running_mac():
                            _open = "open"
                        else:
                            _open = "xdg-open"
                        system(f"{_open} {_path}")
                else:
                    not_found_window = Window(
                        "Error Opening Docs!",
                        [
                            [sg.Text("The built in help doc could not be opened.")],
                            [
                                sg.Push(),
                                sg.Button("Download the Docs", k="dl"),
                                sg.Button("Cancel"),
                            ],
                        ],
                        modal=True,
                    )
                    choice = not_found_window()[0]
                    if choice in (None, "Cancel"):
                        pass
                    if choice == "dl":
                        open_link(LINK_DOCS_DL)
                    not_found_window.close()

            if event == "execute_entry_action":
                value = self.values["entry_action_dropdown"]
                flat = flatten_themedict(self.themedict).keys()
                all_checkboxes = []
                for k in flat:
                    widget = self.window[f"{k}_entryname"]
                    if isinstance(widget, sg.Checkbox):
                        all_checkboxes.append(k)
                selected = [k for k in all_checkboxes if self.values[f"{k}_entryname"]]
                if value == "Select Color":
                    self.color_picker(selected)
                if value == "Interpolate":
                    begin = self.values[f"{selected[0]}_value"]
                    end = self.values[f"{selected[-1]}_value"]
                    colors = [
                        colour.hsl2hex(c)
                        for c in colour.color_scale(
                            colour.web2hsl(begin), colour.web2hsl(end), len(selected)
                        )
                    ]
                    self.window.fill(
                        dict(zip([f"{k}_value" for k in selected], colors))
                    )
                if value == "Shuffle":
                    colors = [self.values[f"{k}_value"] for k in selected]
                    shuffle(colors)
                    self.window.fill(
                        dict(zip([f"{k}_value" for k in selected], colors))
                    )
                if value == "Random Color (All)":
                    color = random_color()
                    for k in selected:
                        self._update_color_value(f"{k}_value", color)
                        self.values[f"{k}_value"] = color
                if value == "Random Color (Individual)":
                    for k in selected:
                        color = random_color()
                        self._update_color_value(f"{k}_value", color)
                        self.values[f"{k}_value"] = color
                if value == "Brighten Colors":
                    for k in selected:
                        color = alter_luminance(self.values[f"{k}_value"], 1.02)
                        self._update_color_value(f"{k}_value", color)
                        self.values[f"{k}_value"] = color
                if value == "Darken Colors":
                    for k in selected:
                        color = alter_luminance(self.values[f"{k}_value"], 0.98)
                        self._update_color_value(f"{k}_value", color)
                        self.values[f"{k}_value"] = color

            if event == "filter":
                self.update_quick_preview(self.themedict)
                if self.values["filter"] != FILTERS[0]:
                    self.window["apply_filter"](disabled=False)
                else:
                    self.window["apply_filter"](disabled=True)

            if event == "apply_filter":
                self.write_themedict(self.preview_themedict)
                self.window["filter"](FILTERS[0])
                self.window["apply_filter"](disabled=True)

            if event.startswith("select_all") or event.endswith("entryname"):
                # This portion powers the select all behaviour.
                flat = flatten_themedict(self.themedict).keys()
                all_checkboxes = []
                for k in flat:
                    widget = self.window[f"{k}_entryname"]
                    if isinstance(widget, sg.Checkbox):
                        all_checkboxes.append(k)
                if event.startswith("select_all"):
                    if event == "select_all_kb":
                        # Simulate the action from a click when using the kb shortcut on the select all checkbox.
                        self.values["select_all"] = not self.values["select_all"]
                        self.window["select_all"](value=self.values["select_all"])
                    for k in all_checkboxes:
                        # Set all checkboxes to the value of the select all checkbox.
                        self.window[f"{k}_entryname"](self.values["select_all"])
                        self.values[f"{k}_entryname"] = self.values["select_all"]

                elif not self.values[event]:
                    # If we're disabling an entry's checkbox, we also turn off the select all checkbox.
                    self.values["select_all"] = False
                    self.window["select_all"](False)

                # Count the number of selected entry checkboxes.
                selected = [k for k in all_checkboxes if self.values[f"{k}_entryname"]]

                if len(selected) == len(all_checkboxes):
                    # If all the checkboxes are selected, we tick the select all checkbox.
                    self.values["select_all"] = True
                    self.window["select_all"](True)

                if (
                    len(selected) >= 2
                ):  # If there's 2 or more selected, enable the batch options.
                    self.window["entry_action_dropdown"](disabled=False)

                else:  # If there's less than 2 selected, disable batch options, because what's getting batched?
                    self.window["entry_action_dropdown"](disabled=True)

            if event == "entry_action_dropdown":
                if self.values["entry_action_dropdown"] != BATCH_ACTIONS[0]:
                    self.window["execute_entry_action"](disabled=False)
                else:
                    self.window["execute_entry_action"](disabled=True)

            if event.startswith("Revert to Beginning") and (
                self.themedict != self.original_themedict
            ):
                self.write_themedict(self.original_themedict)

            if event == "copy":
                if self.copy_id:
                    self.window["copy"].widget.after_cancel(self.copy_id)
                copy(self.values["theme_code"])
                self.window["copy"]("Theme Code Copied"),
                self.copy_id = self.window["copy"].widget.after(
                    2000, lambda: self.window["copy"]("Copy Theme Code")
                )

            if event.startswith("Return to Launcher"):
                if (
                    sg.PopupYesNo(
                        "This action will close the editor. Continue?",
                        title="Are you sure?",
                    )
                    == "Yes"
                ):
                    relaunch_options = (self.window, "main")
                    break
                else:
                    continue

            if event.startswith("Create New Theme"):
                if (
                    sg.PopupYesNo(
                        "This action will close the editor. Continue?",
                        title="Are you sure?",
                    )
                    == "Yes"
                ):
                    relaunch_options = (self.window, "new")
                    break
                else:
                    continue

            if event.startswith("Edit Existing Theme"):
                if (
                    sg.PopupYesNo(
                        "This action will close the editor. Continue?",
                        title="Are you sure?",
                    )
                    == "Yes"
                ):
                    relaunch_options = (self.window, "existing")
                    break
                else:
                    continue

            if event.startswith("Theme From Image"):
                if (
                    sg.PopupYesNo(
                        "This action will close the editor. Continue?",
                        title="Are you sure?",
                    )
                    == "Yes"
                ):
                    relaunch_options = (self.window, "image")
                    break
                else:
                    continue


if __name__ == "__main__":
    try:
        # raise Exception('Testing the crash reporting system.')  # Do not uncomment unless you wish to test crashes.
        while True:
            set_launcher_to = "main"

            # Try to close any leftover editor windows in case we're restarting.
            if relaunch_options:
                previous_window, set_launcher_to = relaunch_options
                previous_window.close()
                relaunch_options = None

            # Run an instance of the launcher and follow it up with an Editor if successful.
            _name, _themedict, _launcher = Launcher(set_to=set_launcher_to)
            if _name and _themedict:  # Launcher completed successfully.
                _editor = eval("Editor(_name, _themedict)")
                _launcher.close()
                _editor()
            else:  # Launcher had issues.
                break

            # Check whether to restart after closing everything.
            if relaunch_options is None:
                break

    except Exception as e:
        handle_crash(e, sg)
