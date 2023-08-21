"""
d888888P dP
   88    88
   88    88d888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b.
   88    88'  `88 88ooood8 88'`88'`88 88ooood8 88'  `88 88'  `88
   88    88    88 88.  ... 88  88  88 88.  ... 88       88.  .88
   dP    dP    dP `88888P' dP  dP  dP `88888P' dP       `88888P8

Themera Independent Constants File
PySimpleGUI Theme Code Generator
Copyright 2023 Divine Afam-Ifediogor
"""

# IMPORTS ______________________________________________________________________________________________________________
from darkdetect import isLight
from PySimpleGUI import LOOK_AND_FEEL_TABLE, running_mac, running_windows

from version_and_copyright import __version__

# CONSTANTS ____________________________________________________________________________________________________________
APP_ID = (
    f'divineafamifediogor.themera.v{__version__.split(".", 1)[0]}'  # Major version only
)

DEFAULT_SETTINGS_PATH = f"./.themerasettings"
THEMES = ["Themera Light", "Themera Dark"] + sorted(
    [
        theme
        for theme in LOOK_AND_FEEL_TABLE.keys()
        if "1234567890" not in LOOK_AND_FEEL_TABLE[theme].values()
    ]
)
DEFAULT_THEME = (
    (THEMES[0] if isLight() else THEMES[1]) if isLight() is not None else THEMES[0]
)
EXTERNAL_LINK_ICON = "⇗"  # '🔗'
GEAR_ICON = "⚙"
DOWN_ICON = "▼"
UP_ICON = "▲"
PENCIL_ICON = "✎"
WARNING_ICON = "⚠"
BORDER_UPPER_LIMIT = 100001
BATCH_ACTIONS = [
    "-- Choose an action --",
    "Select Color",
    "Shuffle",
    "Interpolate",
    "Random Color (All)",
    "Random Color (Individual)",
    "Brighten Colors",
    "Darken Colors",
]
LAST_USED_BATCH_ACTION = BATCH_ACTIONS[0]
DISPLAY_TO_THEMEDICT = {
    "Background": "BACKGROUND",
    "Text": "TEXT",
    "Input Background": "INPUT",
    "Input Text": "TEXT_INPUT",
    "Button Background": "BUTTON[1]",
    "Button Text": "BUTTON[0]",
    "Slider": "SCROLL",
    "Progress Bar Trough": "PROGRESS[1]",
    "Progress Bar Indicator": "PROGRESS[0]",
    "Border": "BORDER",
    "Slider Border": "SLIDER_DEPTH",
    "Progress Bar Border": "PROGRESS_DEPTH",
    "Accent 1": "ACCENT1",
    "Accent 2": "ACCENT2",
    "Accent 3": "ACCENT3",
    "Accent 4": "ACCENT4",
}
SAFE_TO_EXPAND = ["BUTTON", "PROGRESS"]
EXPANSION_FORMAT = "[<index>]"
INDEX_MARKERS = EXPANSION_FORMAT.split("<index>")
THEMEDICT_TO_DISPLAY = {value: key for key, value in DISPLAY_TO_THEMEDICT.items()}
CTRL = "Cmd" if running_mac() else "Ctrl"
CTRL_EVENT = "Command" if running_mac() else "Control"
ALT = "Option" if running_mac() else "Alt"
IMAGE_PREVIEW_SIZE = (320, 130)
CREATE_BUTTON_PADDING = ((3, 2), 3)
BACK_BUTTON_PADDING = ((2, 5), 3)
IMAGE_FILETYPES = [
    (
        "All Images",
        ("*.png", "*.jpg", "*.jpeg", "*.gif", "*.webp", "*.bmp", "*.ico", "*.icns"),
    ),
    ("PNG Images", ("*.png")),
    ("JPEG Images", ("*.jpg", "*.jpeg")),
    ("GIF Images", ("*.gif")),
    ("WEBP Images", ("*.webp")),
    ("Bitmaps", ("*.bmp")),
    ("Windows Icons", ("*.ico")) if running_windows() else ("Mac Icons", ("*.icns")),
]
DEFAULT_COLOR_THEME_FIELDS = [
    key
    for key in THEMEDICT_TO_DISPLAY.keys()
    if "Border" not in THEMEDICT_TO_DISPLAY[key]
]
DEFAULT_NON_COLOR_THEME_FIELDS = {
    "BORDER": 0,
    "SLIDER_DEPTH": 0,
    "PROGRESS_DEPTH": 0,
}

IMAGE_INDEX = [0.3, 1, 0.7, 0.1, 0.2, 0, 0.6, 0.4, 0.5, 0.3, 0.7, 0.8, 0.6]
AUTOCONTRAST_INDEX_DARK = [0.99, 0.8, 0.2, 0.1, 0.99, 0.7, 0.8, 0.3, 0.5, 0.6, 0.2, 0.4]
AUTOCONTRAST_INDEX_LIGHT = [0.3, 0.7, 0.3, 0.8, 0.23, 0.3, 0.4, 0.7, 0.2, 0.9, 0.1, 0.6]
DARK_MODE_INDEX = [0.1, 0.9, 0.8, 0.1, 0.3, 0.2, 0.7, 0.8, 0.3, 0.2, 0.4, 0.6, 0.8]
LIGHT_MODE_INDEX = [0.9, 0.1, 0.3, 0.8, 1, 0.9, 0.4, 0.6, 0.2, 0.8, 0.6, 0.4, 0.2]

DEFAULT_ALIAS = "sg"
DEFAULT_SETTINGS_DICT = {
    "psg_alias": DEFAULT_ALIAS,
    "theme": DEFAULT_THEME,
    "colorboxes": True,
    "full_preview_mode": "default",
    "image_index": IMAGE_INDEX,
    "autocontrast_index_dark": AUTOCONTRAST_INDEX_DARK,
    "autocontrast_index_light": AUTOCONTRAST_INDEX_LIGHT,
    "dark_mode_index": DARK_MODE_INDEX,
    "light_mode_index": LIGHT_MODE_INDEX,
}

CONTRAST_THRESHOLD = 0.5
CONTRAST_THRESHOLD_MULTIPLIER = 3

CRASH_REPORT_TITLE_PREFIX = "[Crash]"

LINK_DEVELOPER = "https://github.com/definite-d"
LINK_GITHUB_REPO = f"{LINK_DEVELOPER}/themera"
LINK_GITHUB_ISSUES = f"{LINK_GITHUB_REPO}/issues"
LINK_NEW_GITHUB_ISSUE = f"{LINK_GITHUB_ISSUES}/new"
LINK_PYSIMPLEGUI_SITE = "https://pysimplegui.org/"
LINK_PYSIMPLEGUI_REPO = "https://github.com/pysimplegui/pysimplegui/"
LINK_DOCS_DL = f"{LINK_GITHUB_REPO}/blob/main/src/help/help.rtf"

HELP_PATH = "help/help.rtf"

DEFAULT_LAYOUT = """# Sample Layout Code
[
    [Column([
           [Column([
               [Column([
                    [Column([
                        [
                            Image(data=EMOJI_BASE64_HAPPY_BIG_SMILE, k=f'tb_icon'),
                            # Icon and Title
                            Text('Quick Preview', k=f'tb_title'),
                        ]
                    ], pad=(0, 0), k=f'tb_title_and_icon')],
                    [Column([
                        [Text('Sample Text; Lorem ipsum dolor sit amet...', k=f'element_text', expand_x=True)],
                        [Input('Hello world', k=f'element_input', expand_x=True)],
                        [Button('Button', k=f'element_button')]
                    ], k=f'element_bg', pad=(0, 0), expand_x=True)]
                ], expand_x=True, k=f'tb_container', pad=(2, (0, 2)))],
            ], k=f'tb_maincolumn', element_justification='c', pad=(1, 1), expand_x=True)]
    ], k=f'visibility_wrap', expand_x=True)]
]"""
