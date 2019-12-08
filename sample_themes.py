'''
# Sample Themes.
=======================================================================================================================

Here lies a multitude of themes generated with LookyFeely, ready for use. Simply copy the definition of the required
theme and paste for use in your own PySimpleGUI project.

Some of these were generated entirely from LookyFeely's random color choices, others were tweaked a little bit once I
saw a bit of potential. As you may notice from the background colors below, I love dark themed GUIs. That may be
observed in form of bright colors on total darkness.

'''

import PySimpleGUI as sg

# =======================================================================
# Custom HighlighterGreen LookAndFeel Theme.
theme = 'HighlighterGreen'
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
theme = 'HighlighterYellow'
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
theme = 'Rhubarb'
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
theme = 'TealOrange'
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
theme = 'Underwater Barney'
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
theme = 'IrisOfTheDesert'
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
# This one was fully randomly generated. No alteration whatsoever.
# =======================================================================
# Custom TrueBarney LookAndFeel Theme.
# Generated using LookyFeely.
import PySimpleGUI as sg
theme = 'TrueBarney'
sg.LOOK_AND_FEEL_TABLE['TrueBarney'] = {'BACKGROUND': '#5e195a',
    'TEXT': '#efc5ed',
    'INPUT': '#388616',
    'TEXT_INPUT': '#ffb0ff',
    'SCROLL': '#9ff45b',
    'BUTTON': ('#1a1339', '#e247dc'),
    'PROGRESS': ('#4b2082', '#81cfaf'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 1}

sg.ChangeLookAndFeel('TrueBarney')
=========================================================================


sg.ChangeLookAndFeel(theme, force=True)
preview_layout = [[sg.Text((theme+' is live.'))],
						[sg.Text('This window does nothing.')],
						[sg.Text('Only the exit button works.')],
						[sg.InputText('...just a textbox', size=(60, 8))],
						[sg.Exit(' Exit ', key='Exit')]]
preview = sg.Window(title=('Theme Preview for '+theme+' Theme.'), layout=preview_layout, resizable=False)
while True:
						preview_events, preview_values = preview.Read()
						if preview_events in (None, 'Exit'):
							preview.Close()
							break
