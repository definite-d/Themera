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
from colour import Color


# LOGIC ________________________________________________________________________________________________________________
def hexify(color: str):
    color = Color(color).get_hex_l()
    color = f"0x00{color[5]}{color[6]}{color[3]}{color[4]}{color[1]}{color[2]}"
    color = eval(color)
    return color


class Window(sg.Window):
    open_windows = list()

    def __init__(self, *args, **kwargs):
        # Make all windows inherit the last known location.
        if len(self.open_windows) > 1:
            kwargs.setdefault(
                "location", self.open_windows[-1].current_location(more_accurate=True)
            )
        self.editor_object = None
        super().__init__(*args, **kwargs)
        self.open_windows.append(self)
        self.finalize()

        # Windows-only titlebar customization.
        self.customize_titlebar()

    def close(self):
        self.open_windows.remove(self)
        return super().close()

    def customize_titlebar(self):
        # Windows-only titlebar customization.
        if not sg.running_windows():
            return
        from platform import win32_ver

        try:
            version = int(win32_ver()[0])
        except ValueError:
            version = None
        if version < 10:
            return
        import ctypes

        bg = hexify(sg.theme_background_color())
        fg = hexify(sg.theme_text_color())
        try:
            hwnd = ctypes.windll.user32.GetParent(self.TKroot.winfo_id())
            ctypes.windll.dwmapi.DwmSetWindowAttribute(
                hwnd,
                35,
                ctypes.byref(ctypes.c_int(bg)),
                ctypes.sizeof(ctypes.c_int),
            )
            ctypes.windll.dwmapi.DwmSetWindowAttribute(
                hwnd,
                36,
                ctypes.byref(ctypes.c_int(fg)),
                ctypes.sizeof(ctypes.c_int),
            )
        except Exception as e:
            print("Failed to set custom titlebar color.")
            raise e
        self.TKroot.update()
