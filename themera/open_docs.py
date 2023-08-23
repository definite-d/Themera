"""
d888888P dP
   88    88
   88    88d888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b.
   88    88'  `88 88ooood8 88'`88'`88 88ooood8 88'  `88 88'  `88
   88    88    88 88.  ... 88  88  88 88.  ... 88       88.  .88
   dP    dP    dP `88888P' dP  dP  dP `88888P' dP       `88888P8

Themera Help Functionality File
PySimpleGUI Theme Code Generator
Copyright 2023 Divine Afam-Ifediogor
"""
from os.path import abspath, isfile

import PySimpleGUI as sg
from constants import HELP_PATH, LINK_DOCS_DL
from window import Window


def open_docs():
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
