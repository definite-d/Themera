"""
d888888P dP
   88    88
   88    88d888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b.
   88    88'  `88 88ooood8 88'`88'`88 88ooood8 88'  `88 88'  `88
   88    88    88 88.  ... 88  88  88 88.  ... 88       88.  .88
   dP    dP    dP `88888P' dP  dP  dP `88888P' dP       `88888P8

Crash Handling File
PySimpleGUI Theme Code Generator
Copyright 2023 Divine Afam-Ifediogor
"""
from datetime import datetime
from traceback import format_exception

from constants import CRASH_REPORT_TITLE_PREFIX, LINK_NEW_GITHUB_ISSUE, WARNING_ICON
from fonts import FONTS
from version_and_copyright import __version__
from window import Window


def run_crash_window(error_message, sg):
    """
    Runs the window that shows the "crashed" error message to the user.
    """
    main_layout = [
        [sg.Text(f"{WARNING_ICON} Fatal Error!", font=FONTS["icon"])],
        [sg.Text("Oh no!")],
        [sg.Text("It appears Themera has crashed fatally.")],
        [sg.Multiline(f"{error_message}", disabled=True, k="error_box", size=(50, 5))],
        [sg.HSep()],
        [sg.Text("Would you like to open a GitHub issue to report this?")],
        [sg.Push(), sg.Button("Yes"), sg.Button("No (and Exit)")],
    ]
    additional_info_layout = [
        [sg.Text(f"{WARNING_ICON} Report on Github", font=FONTS["icon"])],
        [
            sg.Text(
                "Please give any additional feedback on the issue.\n"
                "Your system information will be included automatically."
            )
        ],
        [
            sg.Multiline(
                "-- No additional feedback --", k="additional_info", size=(50, 7)
            )
        ],
        [sg.HSep()],
        [sg.Push(), sg.Button("Finish"), sg.Button("Back"), sg.Button("Cancel")],
    ]
    layout = [
        [
            sg.Column(main_layout, k="main_panel"),
            sg.Column(additional_info_layout, k="additional_info_panel", visible=False),
        ],
    ]
    window = Window(
        "Fatal Error!", layout, element_justification="center", size=(400, 250)
    )
    result = None
    while True:
        e, v = window()
        if e in ("No (and Exit)", None, "Cancel"):
            window.close()
            break
        if e == "Yes":
            window["main_panel"](visible=False)
            window["additional_info_panel"](visible=True)
        if e == "Back":
            window["main_panel"](visible=True)
            window["additional_info_panel"](visible=False)
        if e == "Finish":
            result = v["additional_info"]
            window.close()
            break
    return result


def handle_crash(exception, sg):
    """
    Handles the occurrence of a crash given the Exception and the PySimpleGUI Module instance.
    """
    # First close all windows.
    for window in Window.open_windows:
        window.close()

    title = f"{CRASH_REPORT_TITLE_PREFIX} {repr(exception)}"
    error = "".join(format_exception(exception, exception, exception.__traceback__))
    time_of_crash = datetime.now()

    issue_info = run_crash_window(error, sg)

    if issue_info:
        from platform import platform, processor
        from sys import version as sys_version
        from urllib import parse
        from webbrowser import open_new_tab as open_link

        from psg_reskinner import __version__ as r_version

        body = (
            f"### Error message:\n```shell\n{error}```\n"
            f"### User Report/Messages:\n{issue_info}\n"
            f"### Time of Crash:\n{time_of_crash}\n"
            f"### Platform info:\n{platform()}\n"
            f"### Processor:\n{processor()}\n"
            f"### Versions:\n"
            f"#### Themera Version:\n{__version__}\n"
            f"#### PySimpleGUI Version:\n{sg.__version__}\n"
            f"#### Reskinner Version:\n{r_version}\n"
            f"#### Python Version:\n{sys_version}\n\n"
        )

        # Adapted from PySimpleGUI's source.
        args = {"title": str(title), "body": str(body)}
        link = f"{LINK_NEW_GITHUB_ISSUE}?" + parse.urlencode(args).replace(
            "%5Cn", "%0D"
        )

        print("\nIt appears Themera has crashed fatally.")
        print(body)
        print(link)

        open_link(link)
