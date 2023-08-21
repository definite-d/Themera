"""
d888888P dP
   88    88
   88    88d888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b.
   88    88'  `88 88ooood8 88'`88'`88 88ooood8 88'  `88 88'  `88
   88    88    88 88.  ... 88  88  88 88.  ... 88       88.  .88
   dP    dP    dP `88888P' dP  dP  dP `88888P' dP       `88888P8

Themera Custom Window Class File
PySimpleGUI Theme Code Generator
Copyright 2023 Divine Afam-Ifediogor
"""

# IMPORTS ______________________________________________________________________________________________________________
import PySimpleGUI as sg


# LOGIC ________________________________________________________________________________________________________________
class Window(sg.Window):
    open_windows = list()

    def __init__(self, *args, **kwargs):
        self.editor_object = None
        super().__init__(*args, **kwargs)
        self.open_windows.append(self)

    def close(self):
        self.open_windows.remove(self)
        return super().close()
