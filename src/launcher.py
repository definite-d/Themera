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
from PIL import Image, UnidentifiedImageError

from bytecode import BANNER, GRID, SIDEBAR
from constants import BACK_BUTTON_PADDING, CREATE_BUTTON_PADDING, DEFAULT_COLOR_THEME_FIELDS, IMAGE_FILETYPES, \
    IMAGE_INDEX, IMAGE_PREVIEW_SIZE, THEMES, DEFAULT_NON_COLOR_THEME_FIELDS
from filters import index_filter
from fonts import FONTS
from functions import get_colors_from_image, mini_preview_window_layout, reskin_mini_preview_window, unflatten_themedict
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
    return [sg.Push(), sg.Button('Create', k=f'{key}_start', pad=CREATE_BUTTON_PADDING),
            sg.Button('Back', k=f'{key}_back', pad=BACK_BUTTON_PADDING)]


def theme_name_row(key: str) -> List[sg.Element]:
    """
    UI utility function.
    Generates a row for the theme name entry box.

    :param key: The element key.
    :return: A list containing a text element and the input itself.
    """
    return [sg.Text('Theme Name', size=(10, 1)), sg.Input(k=f'{key}_themename')]


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
    if '{' not in code and '}' not in code:
        return False
    code = '{' + code.rsplit('{', 1)[1]
    code = code.split('}', 1)[0] + '}'
    try:
        exec(code, {}, {})
    except SyntaxError:
        return False
    return True


def existing_action(code):
    code = '{' + code.rsplit('{', 1)[1]
    code = code.split('}', 1)[0] + '}'
    return eval(code, {}, {})


def new_action(theme: str) -> Dict[str, Union[str, Tuple, List]]:
    """
    This function is invoked when a new theme (based on builtin PySimpleGUI themes) is to be created via the launcher.
    It simply obtains the appropriate themedict from the `LOOK_LOOK_AND_FEEL_TABLE`.

    :param theme: The name of the builtin PySimpleGUI theme.
    :return: The themedict for the given theme.
    """
    return sg.LOOK_AND_FEEL_TABLE[theme]


def Launcher(set_to: str = 'main'):
    """
    This function is responsible for initializing a new launcher upon startup and when requested by the user.

    :return: None
    """
    themes, default_theme = sorted(THEMES), 'Black'
    image: sg.Optional[Image.Image] = None
    layout = [
        [sg.Column(
            [
                [sg.Image(data=BANNER, subsample=2, pad=(0, 0))],
                [sg.Text('The PySimpleGUI Theme Editor', font=FONTS['tagline'], pad=(5, (10, 1)))],
                [
                    sg.Button('New Theme', font=FONTS['medium'], k='new_route', pad=(5, 5)),
                    sg.Button('Edit Existing Theme', font=FONTS['medium'], k='existing_route', pad=(5, 5)),
                    sg.Button('Theme from Image', font=FONTS['medium'], k='image_route', pad=(5, 5)),
                ],
                [sg.Text(COPYRIGHT, pad=(0, (5, 10)))]
            ],
            k='main_panel', visible=set_to=='main', element_justification='center', pad=(0, 0)),
        sg.Column(
            [
                [
                    sg.Column([[sg.Image(data=SIDEBAR, subsample=1, pad=(0, 0), expand_y=True)]], pad=(0, 0),
                              expand_y=True, expand_x=True),
                    sg.Column([
                        [sg.Text('Create New Theme', font=FONTS['medium'], expand_x=True)],
                        theme_name_row('new'),
                        [sg.Text('Based on', size=(10, 1)),
                         sg.DropDown(themes, default_theme, readonly=True, expand_x=True, k='new_theme',
                                     enable_events=True)],
                        [sg.VPush()],
                        [mini_preview_window_layout('new', sg.LOOK_AND_FEEL_TABLE[default_theme],
                                                    'This is a mini preview of the selected theme.')],
                        [sg.VPush()],
                        action_button_row('new'),
                    ], pad=(5, 5), expand_x=True, expand_y=True),
                ]
            ],
            k='new_panel', visible=set_to=='new', expand_y=True, expand_x=True, pad=(0, 0)),
        sg.Column(
            [
                [
                    sg.Column([[sg.Image(data=SIDEBAR, subsample=1, pad=(0, 0), expand_y=True)]], pad=(0, 0),
                              expand_y=True, expand_x=True),
                    sg.Column([
                        # [sg.VPush()],
                        [sg.Text('Edit Existing Theme', font=FONTS['medium'])],
                        theme_name_row('existing'),
                        [sg.Multiline('-- Paste your theme\'s value dictionary here. --', k='existing_themecode',
                                      expand_x=True, expand_y=True)],
                        action_button_row('existing'),
                        # [sg.VPush()],
                    ], pad=(5, 5), expand_x=True, expand_y=True),
                ],
            ],
            k='existing_panel', visible=set_to=='existing', expand_y=True, expand_x=True, pad=(0, 0)),
        sg.Column(
            [
                [
                    sg.Column([[sg.Image(data=SIDEBAR, subsample=1, pad=(0, 0), expand_y=True)]], pad=(0, 0),
                              expand_y=True, expand_x=True),
                    sg.Column([
                        # [sg.VPush()],
                        [sg.Text('Theme from Image', font=FONTS['medium'], expand_x=True)],
                        theme_name_row('image'),
                        [
                            sg.Input('-- No image selected. --', size=(38, 1), pad=((5, 1), 2),
                                     enable_events=True, k='image_filepath'),
                            sg.FileBrowse(file_types=IMAGE_FILETYPES)
                        ],
                        [sg.VPush()],
                        [
                            sg.Push(),
                            sg.Image(
                                GRID,
                                size=IMAGE_PREVIEW_SIZE,
                                expand_x=True,
                                expand_y=True,
                                k='image_preview',
                                pad=(0, 0),
                            ),
                            sg.Push()
                        ],
                        [sg.VPush()],
                        action_button_row('image'),
                        # [sg.VPush()],
                    ], pad=(5, 5), expand_x=True, expand_y=True),
                ],
            ],
            k='image_panel', visible=False, expand_y=True, expand_x=True, pad=(0, 0)),
        sg.Column(
            [
                [
                    sg.Column([[sg.Image(data=SIDEBAR, subsample=1, pad=(0, 0), expand_y=True)]], pad=(0, 0),
                              expand_y=True, expand_x=True),
                    sg.Column([
                        [sg.VPush()],
                        [sg.Text('Loading... Please be patient', font=FONTS['medium'], expand_x=True)],
                        [sg.VPush()],
                    ], pad=(5, 5), expand_x=True, expand_y=True),
                ]
            ],
            k='loading_panel', visible=False, expand_x=True, expand_y=True, pad=(0, 0)
        )
        ],
    ]
    launcher = Window(f'Themera v{__version__}', layout, element_justification='center', margins=(0, 0),
                         size=(476, 255), modal=False).finalize()
    name_variable = StringVar(launcher.TKroot, f'NewTheme{getrandbits(16)}', 'theme_name')
    for element in launcher.element_list():
        if str(element.key).endswith('themename'):
            element.widget.configure(textvariable=name_variable)
    reskin_mini_preview_window(launcher, 'new', sg.LOOK_AND_FEEL_TABLE[default_theme])
    launcher.set_min_size(launcher.size)
    themedict = {}
    while True:
        e, v = launcher()
        if e in (None, 'Exit'):
            launcher.close()
            break

        if e == 'new_theme':
            reskin_mini_preview_window(launcher, 'new', sg.LOOK_AND_FEEL_TABLE[v['new_theme']])

        if e == 'image_filepath':
            try:
                with Image.open(v['image_filepath']).convert('RGBA') as _thumbnail:
                    image = _thumbnail
                    thumbnail = BytesIO()
                    base: Image.Image = Image.open(BytesIO(b64decode(GRID)))
                    _thumbnail.thumbnail(IMAGE_PREVIEW_SIZE)
                    _thumbnail.mode = 'RGBA'
                    bbox = (
                        int((IMAGE_PREVIEW_SIZE[0] - _thumbnail.size[0]) / 2),
                        int((IMAGE_PREVIEW_SIZE[1] - _thumbnail.size[1]) / 2),
                    )
                    try:
                        base.paste(_thumbnail, bbox, _thumbnail)
                    except ValueError:
                        base.paste(_thumbnail, bbox)
                    base.save(thumbnail, 'png')
                    thumbnail = b64encode(thumbnail.getvalue())
                    launcher['image_preview'](source=thumbnail)
            except FileNotFoundError:
                continue
            except UnidentifiedImageError:
                sg.PopupError('No valid image selected.', title='Invalid image!')
                continue
            except OverflowError:
                sg.PopupError('There was a problem loading that image.', title='Problem with image!')
                continue
            except (ValueError, TypeError):
                sg.PopupError('An error occurred while trying to process',
                              'the image. Please try a different one.',
                              title='Error processing image.')

        if e.endswith('route'):
            e = e.split('_', 1)[0]
            launcher['main_panel'](visible=False)
            launcher[f'{e}_panel'](visible=True)
            launcher[f'{e}_start'].BindReturnKey = True
            continue

        if e.endswith('back'):
            e = e.split('_', 1)[0]
            launcher[f'{e}_panel'](visible=False)
            launcher[f'main_panel'](visible=True)
            launcher[f'{e}_start'].BindReturnKey = False
            continue

        if e.endswith('start'):
            e = e.split('_', 1)[0]
            if e == 'existing':
                if not existing_validation(v['existing_themecode']):
                    sg.PopupError('Your themedict is invalid. Please correct it.', title='Invalid theme dictionary!')
                    continue
                themedict = existing_action(v['existing_themecode'])
            if e == 'new':
                themedict = new_action(v['new_theme'])
            if e == 'image':
                if not image:
                    sg.PopupError('No valid image selected.', title='Invalid image!')
                    continue
                themedict = image_action(image)
            launcher['loading_panel'](visible=True)
            launcher[f'{e}_panel'](visible=False)
            break
    return name_variable.get(), themedict, launcher

