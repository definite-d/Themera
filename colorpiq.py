'''
Colorpiq
 ____            ___
/\  _`\         /\_ \                          __
\ \ \/\_\    ___\//\ \     ___   _ __   _____ /\_\     __
 \ \ \/_/_  / __`\\ \ \   / __`\/\`'__\/\ '__`\/\ \  /'__`\
  \ \ \L\ \/\ \L\ \\_\ \_/\ \L\ \ \ \/ \ \ \L\ \ \ \/\ \L\ \
   \ \____/\ \____//\____\ \____/\ \_\  \ \ ,__/\ \_\ \___, \
    \/___/  \/___/ \/____/\/___/  \/_/   \ \ \/  \/_/\/___/\ \
                                          \ \_\           \ \_\
                                           \/_/            \/_/

Color picker extension module for the PySimpleGUI SDK
by definite_d (https://www.github.com/definite-d/).
This is NOT a standalone color picker app.
It can be imported and used via its functions, or modified under the terms of the LGPLv3.

Code Sample for Using Colorpiq:

import colorpiq
import PySimpleGUI as sg
sg.ChangeLookAndFeel('DarkTeal11')
window = sg.Window(title='Hello World', layout=[[sg.Text('Color Chosen:'), sg.InputText(key='color'), sg.Button('Choose Color', key='choose')]])
while True:
    events, values = window.Read
    if events is 'choose':
        window[color].Update(colorpiq.colorpiqr())

'''

from PySimpleGUI import *
import colour as col
import random

DEFAULT_ICON = '\\colorpiq_icon.ico'
screen_location = DEFAULT_WINDOW_LOCATION

def colorpiqr(title='Pick a color...', confirm_button_text='OK', no_titlebar=False, slider_width=30, slider_step=1, slider_value=160, preview_box_height=1, preview_box_width=45, output_size=(11, 1), icon=DEFAULT_ICON, location=screen_location):
    color_format = 'RGB'
    
    accepted_color_formats = ['RGB']
    if color_format not in accepted_color_formats:
        given_format = color_format
        color_format = accepted_color_formats[0]
        raise ValueError(('The '+str(given_format)+' color format is not supported.'))
    
    slider_layout = []
    for i in color_format:
        a = str(i)
        i = color_format.index(i)
        slider_layout.append([Text(color_format[i]),
                              Slider(range=(0, 255), default_value=slider_value, size=(slider_width, 10), resolution=slider_step,
                                     orientation='h', key=a)])
    colorpiqr_layout = [
        [Text('Please adjust the sliders to pick a color.')],
        [Column(slider_layout, pad=(0, 0))],
        [DummyButton('', size=(preview_box_width, preview_box_height), key='PreviewBox', disabled=True, pad=(2, (6, 2)))],
        [InputText('', key='Color', size=output_size), Button(confirm_button_text, size=(12, 1), key='Confirm', focus=True, bind_return_key=True, pad=((68, 1), 2)), Button('Cancel', size=(12, 1), key='Cancel')]
    ]
    colorpiqr_window = Window(title=title, layout=colorpiqr_layout, no_titlebar=no_titlebar, icon=DEFAULT_ICON, location=location)
    while True:
        e, v = colorpiqr_window.Read(timeout=10)
        try:
            colorpiqr_window_sliders = []
            for i in color_format:
                colorpiqr_window_sliders = colorpiqr_window_sliders + [v[i]]
            
            for i in colorpiqr_window_sliders:
                colorpiqr_window_sliders[colorpiqr_window_sliders.index(i)] = float(i / 255)
            sliders_color = col.rgb2hex(((colorpiqr_window_sliders[0], colorpiqr_window_sliders[1], colorpiqr_window_sliders[2])), force_long=True)
            
            colorpiqr_window['PreviewBox'](button_color=(sliders_color, sliders_color))
            colorpiqr_window['Color'](sliders_color)
            if e in (None, 'Cancel'):
                colorpiqr_window.Close()
                return 'None'
            if e is 'Confirm':
                colorpiqr_window.Close()
                return sliders_color
        except:
            return None
            pass
