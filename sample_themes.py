'''
# Sample Themes.

 #######
 #     #
 #        ####### #     # ####### #       ####### #######
 #######  #     # ##   ## #     # #       #       #
      ##  ####### # # # # ####### #       ####    #######
 #    ##  #     # #  #  # #       #       #             #    ##   ##   ##
 #######  #     # #     # #       ####### ####### #######    ##   ##   ##

=======================================================================================================================

Here lies a multitude of themes generated with LookyFeely, ready for use. Simply copy the definition of the required
theme and paste for use in your own PySimpleGUI project. If you use the themes, a little credit would be nice, but is
not required.

Some of these were generated entirely from LookyFeely's random color choices, others were tweaked a little bit once I
saw a bit of potential. As you may notice from the background colors below, I love dark themed GUIs. That may be
observed in form of bright colors on total darkness.

'''

import PySimpleGUI as sg
icon = b'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\n'

# =======================================================================

'''
Y8b Y88888P                      ,e,                       d88       e88 88e
 Y8b Y888P   ,e e,  888,8,  dP"Y  "   e88 88e  888 8e     d888      d888 888b
  Y8b Y8P   d88 88b 888 "  C88b  888 d888 888b 888 88b   d"888     C8888 8888D
   Y8b Y    888   , 888     Y88D 888 Y888 888P 888 888     888 d8b  Y888 888P
    Y8P      "YeeP" 888    d,dP  888  "88 88"  888 888     888 Y8P   "88 88"
'''

# =======================================================================
# Custom HighlighterGreen LookAndFeel Theme.
# Generated using LookyFeely.
sg.LOOK_AND_FEEL_TABLE['HighlighterGreen'] = {'BACKGROUND': '#000000',
    'TEXT': '#b0e00f',
    'INPUT': '#b0e00f',
    'TEXT_INPUT': '#050500',
    'SCROLL': '#222220',
    'BUTTON': ('#b0e00f', '#191917'),
    'PROGRESS': '#b0e00f',
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 1}

sg.ChangeLookAndFeel('HighlighterGreen')

# =======================================================================
# Custom HighlighterYellow LookAndFeel Theme.
# Generated using LookyFeely.
sg.LOOK_AND_FEEL_TABLE['HighlighterYellow'] = {'BACKGROUND': '#000000',
    'TEXT': '#E0CC10',
    'INPUT': '#E0CC10',
    'TEXT_INPUT': '#050500',
    'SCROLL': '#222220',
    'BUTTON': ('#E0CC10', '#191917'),
    'PROGRESS': '#c637a7',
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 1}

sg.ChangeLookAndFeel('HighlighterYellow')

# =======================================================================
# Custom Rhubarb LookAndFeel Theme.
# Generated using LookyFeely.
sg.LOOK_AND_FEEL_TABLE['Rhubarb'] = {'BACKGROUND': '#000000',
    'TEXT': '#6dbc7f',
    'INPUT': '#3ec803',
    'TEXT_INPUT': '#0c0242',
    'SCROLL': '#eb367f',
    'BUTTON': ('#000000', '#f52c6e'),
    'PROGRESS': ('#d096ca', '#0b18c7'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 1}

sg.ChangeLookAndFeel('Rhubarb')

# =======================================================================
# Custom TealOrange LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg
sg.LOOK_AND_FEEL_TABLE['TealOrange'] = {'BACKGROUND': '#59cbae',
    'TEXT': '#3a121b',
    'INPUT': '#92a3a2',
    'TEXT_INPUT': '#352843',
    'SCROLL': '#668bdc',
    'BUTTON': ('#ddeeff', '#de8303'),
    'PROGRESS': ('#44df46', '#1988fe'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 1}

sg.ChangeLookAndFeel('TealOrange')

# =======================================================================
# Custom Underwater Barney LookAndFeel Theme.
# Generated using LookyFeely.
sg.LOOK_AND_FEEL_TABLE['UnderwaterBarney'] = {'BACKGROUND': '#0f80bd',
    'TEXT': '#9ecdf7',
    'INPUT': '#b92a69',
    'TEXT_INPUT': '#8888ff',
    'SCROLL': '#5f8a75',
    'BUTTON': ('#39200c', '#0c948c'),
    'PROGRESS': ('#b64724', '#49d463'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 1}

sg.ChangeLookAndFeel('UnderwaterBarney')

# =======================================================================
# Custom IrisOfTheDesert LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg
sg.LOOK_AND_FEEL_TABLE['IrisOfTheDesert'] = {'BACKGROUND': '#deb54d',
    'TEXT': '#9b3d6d',
    'INPUT': '#73493f',
    'TEXT_INPUT': '#66ac55',
    'SCROLL': '#546c54',
    'BUTTON': ('#ad469c', '#e0c05c'),
    'PROGRESS': ('#24e651', '#4993ae'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 1}

sg.ChangeLookAndFeel('IrisOfTheDesert')
# This one fully randomly generated. No alteration whatsoever.
# =======================================================================
# =======================================================================

'''
o     o                      o                .oPYo.    .oPYo.
8     8                                           `8    8  .o8
8     8 .oPYo. oPYo. .oPYo. o8 .oPYo. odYo.      oP'    8 .P'8
`b   d' 8oooo8 8  `' Yb..    8 8    8 8' `8   .oP'      8.d' 8
 `b d'  8.     8       'Yb.  8 8    8 8   8   8'        8o'  8
  `8'   `Yooo' 8     `YooP'  8 `YooP' 8   8   8ooooo 88 `YooP'
:::..::::.....:..:::::.....::..:.....:..::..::.........::.....:
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
'''

# =======================================================================
# =======================================================================
# Custom CementNGreen LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['CementNGreen'] = {'BACKGROUND': '#217e59',
    'TEXT': '#e8e5e4',
    'INPUT': '#e8e5e4',
    'TEXT_INPUT': '#217e59',
    'SCROLL': '#c2c7a1',
    'BUTTON': ('#217e59', 'white'),
    'PROGRESS': ('#d5d1c4', '#e8e5e4'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('CementNGreen')

# =======================================================================
# Custom BigBlue LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['BigBlue'] = {'BACKGROUND': '#182b9b',
    'TEXT': '#eae8e5',
    'INPUT': '#eae8e5',
    'TEXT_INPUT': '#182b9b',
    'SCROLL': '#b1cea2',
    'BUTTON': ('#182b9b', 'white'),
    'PROGRESS': ('#2a8db8', '#eae8e5'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('BigBlue')

# =======================================================================
# Custom ClassyCoffeeJoint LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['ClassyCoffeeJoint'] = {'BACKGROUND': '#f0e68c',
    'TEXT': '#000000',
    'INPUT': '#e0c466',
    'TEXT_INPUT': 'black',
    'SCROLL': '#9c6e3d',
    'BUTTON': ('khaki', 'black'),
    'PROGRESS': ('#42302a', '#e0c466'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('ClassyCoffeeJoint')
# =======================================================================
# Custom AshCool LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['AshCool'] = {'BACKGROUND': '#495a4c',
    'TEXT': '#e7e6e6',
    'INPUT': '#637461',
    'TEXT_INPUT': 'white',
    'SCROLL': '#9fa296',
    'BUTTON': ('white', '#495a4c'),
    'PROGRESS': ('#e7e6e6', '#637461'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('AshCool')
# =======================================================================
# Custom TracesOfGold LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['TracesOfGold'] = {'BACKGROUND': '#121212',
    'TEXT': 'darkgray',
    'INPUT': '#262626',
    'TEXT_INPUT': 'gold',
    'SCROLL': '#98631e',
    'BUTTON': ('#121212', '#7d7d7d'),
    'PROGRESS': ('#5a3a2d', '#262626'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('TracesOfGold')
# =======================================================================
# Custom MindMadness LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['MindMadness'] = {'BACKGROUND': 'Black',
    'TEXT': 'Blue',
    'INPUT': 'Red',
    'TEXT_INPUT': '#0f6',
    'SCROLL': 'blue',
    'BUTTON': ('black', '#0f6'),
    'PROGRESS': ('#1f7a43', 'Red'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('MindMadness')
# =======================================================================
# Custom HeartOfPurple LookAndFeel Theme.
# (Fully) Generated using LookyFeely.
import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['HeartOfPurple'] = {'BACKGROUND': 'indigo',
    'TEXT': 'gainsboro',
    'INPUT': '#0c18a2',
    'TEXT_INPUT': 'gainsboro',
    'SCROLL': '#b8c699',
    'BUTTON': ('indigo', 'gainsboro'),
    'PROGRESS': ('#3dca94', '#0c18a2'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('HeartOfPurple')

# Custom HeartOfPurple - Light LookAndFeel Theme.
# Generated using LookyFeely.
#import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['HeartOfPurpleLight'] = {'BACKGROUND': 'gainsboro',
   'TEXT': '#0c18a2',
   'INPUT': '#cec8be',
   'TEXT_INPUT': 'indigo',
   'SCROLL': '#b8c699',
   'BUTTON': ('indigo', '#cec8be'),
   'PROGRESS': ('#71c56e', '#cec8be'),
   'BORDER': 1,
   'SLIDER_DEPTH': 1,
   'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('HeartOfPurpleLight')
# =======================================================================
# Custom Wasp LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['Wasp'] = {'BACKGROUND': 'yellow',
    'TEXT': 'black',
    'INPUT': 'black',
    'TEXT_INPUT': 'yellow',
    'SCROLL': 'black',
    'BUTTON': ('yellow', 'black'),
    'PROGRESS': ('black', 'black'),
    'BORDER': 2,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('Wasp')
# =======================================================================
# Custom JustLime LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['JustLime'] = {'BACKGROUND': 'olivedrab',
    'TEXT': 'chartreuse',
    'INPUT': '#709c20',
    'TEXT_INPUT': 'chartreuse',
    'SCROLL': '#7edc0d',
    'BUTTON': ('olivedrab', 'chartreuse'),
    'PROGRESS': ('#79bb18', '#709c20'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('JustLime')
# =======================================================================
# Custom BurnInHell LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['BurnInHell'] = {'BACKGROUND': 'orangered',
    'TEXT': 'black',
    'INPUT': '#391c1c',
    'TEXT_INPUT': 'red',
    'SCROLL': 'orangered',
    'BUTTON': ('white', 'darkred'),
    'PROGRESS': ('#555', '#391c1c'),
    'BORDER': 4,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('BurnInHell')
# =======================================================================
# Custom CreamyLatte LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['CreamyLatte'] = {'BACKGROUND': '#ccbb8e',
    'TEXT': '#1a1817',
    'INPUT': '#1a1817',
    'TEXT_INPUT': '#b79d72',
    'SCROLL': '#56463e',
    'BUTTON': ('#1a1817', '#b79d72'),
    'PROGRESS': ('#b79d72', '#1a1817'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('CreamyLatte')
# =======================================================================
# Custom PurpleBarbie LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['PurpleBarbie'] = {'BACKGROUND': 'thistle',
    'TEXT': 'darkviolet',
    'INPUT': '#ac0de2',
    'TEXT_INPUT': 'thistle',
    'SCROLL': '#ce8bd4',
    'BUTTON': ('darkviolet', 'thistle'),
    'PROGRESS': ('#c34bdc', '#ac0de2'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('PurpleBarbie')

# Custom PurpleBarbie - Dark LookAndFeel Theme.
# Generated using LookyFeely.
#import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['PurpleBarbieDark'] = {'BACKGROUND': 'DarkViolet',
    'TEXT': '#d3a7d4',
    'INPUT': '#ac0de2',
    'TEXT_INPUT': 'thistle',
    'SCROLL': '#bc26e5',
    'BUTTON': ('thistle', '#ac0de2'),
    'PROGRESS': ('#c34bdc', '#ac0de2'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('PurpleBarbieDark')

# Custom PurpleBarbie - Light LookAndFeel Theme.
# Generated using LookyFeely.
#import PySimpleGUI as sg  # Please change 'sg' to your liking.
sg.LOOK_AND_FEEL_TABLE['PurpleBarbieLight'] = {'BACKGROUND': 'thistle',
    'TEXT': '#ac0de2',
    'INPUT': '#d3a7d4',
    'TEXT_INPUT': 'DarkViolet',
    'SCROLL': '#ce8bd4',
    'BUTTON': ('DarkViolet', '#d3a7d4'),
    'PROGRESS': ('#c96cd7', '#d3a7d4'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.ChangeLookAndFeel('PurpleBarbieLight')
# =======================================================================
# =======================================================================
# =======================================================================
# =======================================================================
# =======================================================================

theme_name = str(sg.theme())
# theme_name = 'theme'

preview_layout = [[sg.Text((f'This is the {theme_name} theme.'))],
                        [sg.Text('This window does nothing.')],
                        [sg.Text('Only the exit button works.')],
                        [sg.InputText('...just a textbox', size=(60, 8))],
                        [sg.Exit(' Exit ', key='Exit')]]
preview = sg.Window(title=(f'{theme_name} Theme Preview'), layout=preview_layout, icon=icon, resizable=False)
while True:
    preview_events, preview_values = preview.Read()
    if preview_events in (None, 'Exit'):
        preview.Close()
        break
