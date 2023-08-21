"""
d888888P dP
   88    88
   88    88d888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b.
   88    88'  `88 88ooood8 88'`88'`88 88ooood8 88'  `88 88'  `88
   88    88    88 88.  ... 88  88  88 88.  ... 88       88.  .88
   dP    dP    dP `88888P' dP  dP  dP `88888P' dP       `88888P8

Themera Settings File
PySimpleGUI Theme Code Generator
Copyright 2023 Divine Afam-Ifediogor
"""

# IMPORTS ______________________________________________________________________________________________________________
from os.path import isfile
from pathlib import Path
from pickle import UnpicklingError, dump, load
from typing import Dict, Optional, Union

from psg_reskinner import reskin

from .constants import DEFAULT_SETTINGS_DICT, DEFAULT_SETTINGS_PATH, THEMES
from .functions import invert
from .window import Window


# SETTINGS _____________________________________________________________________________________________________________
class Settings:
    """
    This class loads Themera settings from a filepath or gets defaults from the `constants` module.
    """

    def __init__(self, filepath: Optional[Union[str, Path]] = None) -> None:
        filepath = filepath or DEFAULT_SETTINGS_PATH
        if isfile(filepath):
            print("Getting settings from file.")
            self.settings_dict = self.parse_settings_file(filepath)
        if not isfile(filepath) or not self.settings_dict:
            print("Using default settings.")
            self.settings_dict = self.get_defaults()
        self.previous_settings = self.settings_dict.copy()

    def __getitem__(self, setting):
        return self.settings_dict.get(setting)

    def __setitem__(self, key, value):
        self.settings_dict.__setitem__(key, value)

    def save_settings(self, filepath: Optional[Union[str, Path]] = None):
        with open(filepath or DEFAULT_SETTINGS_PATH, "wb") as settings_file:
            dump(self.settings_dict, settings_file)

    @staticmethod
    def parse_settings_file(filepath: Optional[Union[str, Path]]) -> Dict:
        with open(filepath or DEFAULT_SETTINGS_PATH, "rb") as settings_file:
            settings_dict = None
            try:
                settings_dict: Dict = load(settings_file)
            except (UnpicklingError, EOFError, ValueError):
                return None
            if type(settings_dict) != dict:
                return None
            return settings_dict

    @staticmethod
    def get_defaults() -> Dict:
        settings_dict = DEFAULT_SETTINGS_DICT.copy()
        return settings_dict

    def edit(self, sg, editor):
        # import PySimpleGUI as sg
        layout = [
            [
                sg.Frame(
                    "Import Alias",
                    [
                        [
                            sg.Text("import PySimpleGUI as "),
                            sg.Input(
                                self["psg_alias"], k="psg_alias_setting", size=(10, 1)
                            ),
                        ]
                    ],
                    expand_x=True,
                ),
                sg.Frame(
                    "UI Theme",
                    [
                        [
                            sg.DropDown(
                                THEMES,
                                self["theme"],
                                k="theme_setting",
                                enable_events=True,
                                readonly=True,
                            )
                        ],
                    ],
                    expand_x=True,
                ),
            ],
            [
                sg.Frame(
                    "Full Preview Mode",
                    [
                        [
                            sg.Radio(
                                "Default",
                                group_id="full_preview_mode",
                                default=True
                                if self["full_preview_mode"] == "default"
                                else False,
                                k="full_preview_mode_default",
                            ),
                            sg.Radio(
                                "Custom",
                                group_id="full_preview_mode",
                                default=True
                                if self["full_preview_mode"] == "custom"
                                else False,
                                k="full_preview_mode_custom",
                            ),
                        ]
                    ],
                    expand_x=True,
                ),
                sg.Frame(
                    "Colorboxes",
                    [
                        [
                            sg.Checkbox(
                                "Enabled",
                                default=self["colorboxes"],
                                k="colorboxes_setting",
                            ),
                        ]
                    ],
                    expand_x=True,
                ),
            ],
            [
                sg.Frame(
                    "Filter Indexes",
                    [
                        [
                            sg.Text(f"Images", size=(15, 1)),
                            sg.Input(
                                str(self["image_index"]),
                                k="image_index_setting",
                                expand_x=True,
                            ),
                        ],
                        [
                            sg.Text("Auto Contrast (Dark)", size=(15, 1)),
                            sg.Input(
                                str(self["autocontrast_index_dark"]),
                                k="autocontrast_index_dark_setting",
                                expand_x=True,
                            ),
                        ],
                        [
                            sg.Text("Auto Contrast (Light)", size=(15, 1)),
                            sg.Input(
                                str(self["autocontrast_index_light"]),
                                k="autocontrast_index_light_setting",
                                expand_x=True,
                            ),
                        ],
                        [
                            sg.Text("Dark Mode", size=(15, 1)),
                            sg.Input(
                                str(self["dark_mode_index"]),
                                k="dark_mode_index_setting",
                                expand_x=True,
                            ),
                        ],
                        [
                            sg.Text("Light Mode", size=(15, 1)),
                            sg.Input(
                                str(self["light_mode_index"]),
                                k="light_mode_index_setting",
                                expand_x=True,
                            ),
                        ],
                    ],
                    expand_x=True,
                )
            ],
            [sg.HSep()],
            [
                sg.Push(),
                sg.Button("Save"),
                sg.Button("Apply"),
                sg.Button("Cancel"),
            ],
        ]
        settings_window = Window("Themera Settings", layout, modal=True)
        while True:
            e, v = settings_window()

            if e in (None, "Cancel"):
                settings_window.close()
                break

            if e == "theme_setting":
                reskin(
                    settings_window,
                    v["theme_setting"],
                    sg.theme,
                    sg.LOOK_AND_FEEL_TABLE,
                    target_element_keys=["theme_setting"],
                    reskin_background=False,
                )
                settings_window["theme_setting"].ParentRowFrame.configure(
                    background=sg.theme_background_color()
                )

            if e in ("Apply", "Save"):
                if v["theme_setting"] != self["theme"]:
                    reskin(
                        settings_window,
                        v["theme_setting"],
                        sg.theme,
                        sg.LOOK_AND_FEEL_TABLE,
                        True,
                        honor_previous=False,
                    )

                for window in settings_window.open_windows:
                    if v["theme_setting"] != self["theme"]:
                        reskin(
                            window,
                            v["theme_setting"],
                            sg.theme,
                            sg.LOOK_AND_FEEL_TABLE,
                            True,
                            honor_previous=False,
                        )
                        sg.set_options(border_width=0)

                    if window.editor_object:
                        if v["theme_setting"] != self["theme"]:
                            window.editor_object.update_quick_preview(
                                editor.preview_themedict
                            )

                        if v["psg_alias_setting"] != self["psg_alias"]:
                            self["psg_alias"] = v["psg_alias_setting"]
                            window.editor_object.update_theme_code(
                                window.editor_object.generate_theme_code(
                                    window.editor_object.themedict
                                )
                            )

                        for k in window.key_dict.keys():
                            if v["theme_setting"] != self["theme"]:
                                if str(k).endswith("_warning"):
                                    window[k](text_color=sg.theme_background_color())
                            if (
                                v["colorboxes_setting"] != self["colorboxes"]
                                or v["theme_setting"] != self["theme"]
                            ):
                                if (
                                    str(k).endswith("value")
                                    and window[k].metadata == "is_color"
                                ):
                                    if v["colorboxes_setting"]:
                                        window.editor_object._update_color_value(
                                            k, window[k].widget.get()
                                        )
                                    else:
                                        fg = sg.theme_input_text_color()
                                        bg = sg.theme_input_background_color()
                                        window[k](background_color=bg, text_color=fg)

                errors = False
                for _k, _v in v.items():
                    if _k.endswith("_setting"):
                        if str(v[_k]).startswith("["):
                            try:
                                v[_k] = eval(v[_k])
                            except (NameError, SyntaxError) as error:
                                sg.PopupError(
                                    f"Invalid entry:\n{v[_k]}", title="Invalid entry!"
                                )
                                errors = True
                                break
                        if not errors:
                            self[_k[:-8]] = v[_k]
                self["full_preview_mode"] = (
                    "default" if v["full_preview_mode_default"] else "custom"
                )
                # print(self.settings_dict)

                if e == "Save" and not errors:
                    if self.settings_dict != self.previous_settings:
                        self.save_settings()
                    settings_window.close()
                    break


# SETTINGS OBJECT ______________________________________________________________________________________________________
SETTINGS = Settings()
