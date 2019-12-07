import PySimpleGUI as sg

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
# Custom HighlighterGreen LookAndFeel Theme.
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

preview_layout = [[sg.Text('Theme Preview')],
						[sg.Text('This window does nothing.')],
						[sg.Text('Only the exit button works.')],
						[sg.InputText('...just a textbox', size=(60, 8))],
						[sg.Exit(' Exit ', key='Exit')]]
preview = sg.Window(title=('Preview Popup'), layout=preview_layout, resizable=False)
while True:
						preview_events, preview_values = preview.Read()
						if preview_events in (None, 'Exit'):
							preview.Close()
							break