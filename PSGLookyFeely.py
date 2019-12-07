# Welcome...
# ... to the code of LookyFeely.
# https://www.github.com/definite-d/Looky-Feely/

'''

%**%                                    %**%
%  %                                    %  %
%  %                                    %  %
%  %                                    %  %
%  %             %*****\     %*****\    %  % %*%    %**%  %**%
%  %            % %***\ %   % %***\ %   %  %% %     %  %  %  %
%  %            % %   % %   % %   % %   %     \     %  %  %  %
%  %,,,,,,,,,   % \,,,% %   % \,,,% %   %  %\  \    %  \,,%  %
%,,,,,,,,,,,/    \,,,,,%     \,,,,,%    %,,% \,,\   \,,,,,,  %
														   % %
													,,,,,,,% %
												   %,,,,,,,,%
FFFFFFFFFFFFF                       LLL
FFF                                 LLL
FFF                                 LLL
FFF                                 LLL
FFFFFFFFFF   EEEEEEE     EEEEEEE    LLL       YYY   YYY
FFF         EEE   EEE   EEE   EEE   LLL       YYY   YYY
FFF         EEEEEEEE    EEEEEEEE    LLL       YYY   YYY
FFF         EEE         EEE         LLL       YYY   YYY
FFF         EEE   EEE   EEE   EEE   LLL  LLL  YYY   YYY
FFF          EEEEEE      EEEEEE      LLLLLL    YYYYYYYY
												    YYY
											YYY	    YYY
							 	        	  YYYYYYY
												 
Wow... I typed that by hand.

'''

# ___________________________________________________________________________________
# LookyFeely is a utility created by definite_d (me) to make the creation of
# custom PySimpleGUI Look and Feel theme code a breeze, to be a christmas gift to
# PySimpleGUI users, and to act as a bigger 'Thank You' to MikeTheWatchGuy for
# PySimpleGUI ('bigger because I've already said 'Thank You' before).
#
# Well, it's a shameless code generator :).
# It depends on the PySimpleGUI Tkinter version; what I like to call PSG Vanilla.
# As for PEP8, I'll leave that to PyCharm to handle. Hopefully I'll adhere that way.
#
# Development began on 29/11/2019, bare minimum completed on 1/12/2019.
# ===================================================================================
# ___...:::---=== Code Starts Here. ===---:::...___

# Necessary import calls.
import PySimpleGUI as sg  # I'm calling it 'sg' to comply with the PySimpleGUI Docs.
from PySimpleGUI import Print as Print  # Also, since I want to showcase PySimpleGUI features,
# I'll use the PySimpleGUI Debug Window.
from os import getlogin as user
from random import choice as rc
import _tkinter

# 'Cause I figured the master of colors should have all the colors.
random_theme = str(rc(sg.ListOfLookAndFeelValues()))
sg.ChangeLookAndFeel(random_theme)
sg.SetGlobalIcon('\lf_ico.ico')  # Had no befitting icon. So I made one :)...

# I like to make a custom debug mode when I make apps.
# So, here's a shameless boolean debug switch and aliases.
on = True
off = False
DebugMode = off
if DebugMode is on:
	# Just for fun.
	Print('@'+str(user())+', do you read me?')
	Print('LookyFeely is live.')
	Print('LookyFeely is live.')
	Print('I repeat, LookyFeely is live.')

# I think it sucks that every builtin theme has the loader bar color as the same thing.
if sg.LOOK_AND_FEEL_TABLE[random_theme]['PROGRESS'] is sg.DEFAULT_PROGRESS_BAR_COLOR:
	sg.LOOK_AND_FEEL_TABLE[random_theme]['PROGRESS'] = sg.LOOK_AND_FEEL_TABLE[random_theme]['TEXT']

# This is the code for the first window you'll see when running this code.
# Ironically, you can only change the LookAndFeel for windows like this from the
# code itself.
window_1_layout = [
	[sg.Text('LookyFeely!')],
	[sg.Text('PySimpleGUI Look And Feel Code Generator.')],
	[sg.Text('by definite_d')],
	[sg.Text(('*'*70))],
	[sg.Text('Theme Name: ', size=(10, 1)), sg.InputText(key='name', size=(20, 1))],
	[sg.Text('Please click buttons to choose colors')],
	[sg.Text('All parameters with no color chosen will default')],
	[sg.Text('to randomly chosen colors.')],
	[sg.Text('Background Color: ', size=(14, 1)), sg.InputText('...color value', key='bg_c', size=(15, 1)),
	 sg.ColorChooserButton(target='bg_c', button_text='Choose Color', key='bg_c_choose')],
	[sg.Text('Text Color: ', size=(14, 1)), sg.InputText('...color value', key='txt_c', size=(15, 1)),
	 sg.ColorChooserButton(target='txt_c', button_text='Choose Color', key='txt_c_choose')],
	[sg.Text('Input Color: ', size=(14, 1)), sg.InputText('...color value', key='in_c', size=(15, 1)),
	 sg.ColorChooserButton(target='in_c', button_text='Choose Color', key='in_c_choose')],
	[sg.Text('Text Input Color: ', size=(14, 1)), sg.InputText('...color value', key='txt_in_c', size=(15, 1)),
	 sg.ColorChooserButton(target='txt_in_c', button_text='Choose Color', key='txt_in_c_choose')],
	[sg.Text('Scroll Color: ', size=(14, 1)), sg.InputText('...color value', key='scr_c', size=(15, 1)),
	 sg.ColorChooserButton(target='scr_c', button_text='Choose Color', key='scr_c_choose')],
	[sg.Text('Button Text Color: ', size=(14, 1)), sg.InputText('...color value', key='bt_txt_c', size=(15, 1)),
	 sg.ColorChooserButton(target='bt_txt_c', button_text='Choose Color', key='bt_txt_c_choose')],
	[sg.Text('Button Color: ', size=(14, 1)), sg.InputText('...color value', key='bt_c', size=(15, 1)),
	 sg.ColorChooserButton(target='bt_c', button_text='Choose Color', key='bt_c_choose')],
	[sg.Text('Progress Bar Color: ', size=(14, 1)), sg.InputText('...color value', key='pb_c', size=(15, 1)),
	 sg.ColorChooserButton(target='pb_c', button_text='Choose Color', key='pb_c_choose')],
	[sg.Text('Border Width: ', size=(10, 1)),
	 sg.Spin(initial_value='1',values=[x for x in range(0, 1000)], key='bor_w', size=(3, 1)),
	 # Just a divider.
	 sg.Text(' || '), sg.Text('Slider Depth: ', size=(10, 1)),
	 sg.Spin(initial_value=1, values=[x for x in range(0, 1000)], key='sl_bor_w', size=(3, 1))],
	[sg.Text('Progress Meter Depth: ', size=(17, 1)),
	 sg.Spin(initial_value=1, values=[x for x in range(0, 1000)], key='pb_w', size=(3, 1))],
	[sg.Button(button_text=' Generate LookAndFeel Code ', key='gen', bind_return_key=True)],
	[sg.Text(('\"'*70))],
	[sg.Text('Current Theme: '+str(random_theme))]
]
window_1 = sg.Window(('LookyFeely'+' - v1.9'), layout=window_1_layout, element_justification='center',
                     grab_anywhere=False, resizable=False)

while True:
	window_1_events, window_1_values = window_1.Read()
	if window_1_events is 'gen':
		if window_1_values['name'] is '':
			sg.Popup('No Name!', 'You didn\'t specify a name for the theme!', button_type='Cancel',
			         location=window_1.CurrentLocation())
		else:
			name = str(window_1_values['name'])
			bg_c = str(window_1_values['bg_c'])
			txt_c = str(window_1_values['txt_c'])
			in_c = str(window_1_values['in_c'])
			txt_in_c = str(window_1_values['txt_in_c'])
			scr_c = str(window_1_values['scr_c'])
			bt_txt_c = str(window_1_values['bt_txt_c'])
			bt_c = str(window_1_values['bt_c'])
			pb_c = str('('+str(window_1_values['pb_c'])+', '+str(window_1_values['in_c']+')'))
			bor_w = str(window_1_values['bor_w'])
			sl_bor_w = str(window_1_values['sl_bor_w'])
			pb_w = str(window_1_values['pb_w'])
			
			# Random color generator.
			def random_color():
				h = str('#')
				color = ''
				for i in range(6):
					color = color + str(rc([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
					                        'a', 'b', 'c', 'd', 'e', 'f']))
				color = str(h + color)
				if DebugMode is on:
					print('Randomly Generated Color: '+color)
				return color
			
			# Changing the unspecified values to their defaults.
			if bg_c in ('...color value', None):
				bg_c = random_color()
			if txt_c in ('...color value', None):
				txt_c = random_color()
			if in_c in ('...color value', None):
				in_c = random_color()
			if txt_in_c in ('...color value', None):
				txt_in_c = random_color()
			if scr_c in ('...color value', None):
				scr_c = random_color()
			if bt_txt_c in ('...color value', None):
				bt_txt_c = random_color()
			if bt_c in ('...color value', None):
				bt_c = random_color()
			if ('...color value' or None) in pb_c:
				# 'Cause random is always fun.
				pb_c = str('(\''+random_color()+'\', \''+random_color()+'\')')
			# This is where the real code generation happens.
			theme = str('# Custom '+name+' LookAndFeel Theme.\n# Generated using LookyFeely.\n'
			            'import PySimpleGUI as sg\n'
						'sg.LOOK_AND_FEEL_TABLE[\''+name+'\'] = {\'BACKGROUND\': \''+bg_c+'\',\n    \''
						'TEXT\': \''+txt_c+'\',\n    \'INPUT\': \''+in_c+'\',\n    \''
						'TEXT_INPUT\': \''+txt_in_c+'\',\n    \'SCROLL\': \''+scr_c+'\',\n    \''
						'BUTTON\': (\''+bt_txt_c+'\', \''+bt_c+'\'),\n    \''
						'PROGRESS\': '+pb_c+',\n    \'BORDER\': '+str(bor_w)+',\n    \''
						'SLIDER_DEPTH\': '+str(sl_bor_w)+',\n    \'PROGRESS_DEPTH\': '+str(pb_w)+'}\n\n'
						'sg.ChangeLookAndFeel(\''+name+'\')')
			# I decided to add a progress meter for the code generation because... why not?
			prog_l = [[sg.Text('Please wait...')],
			          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')]]
			prog = sg.Window('Generating Theme...', prog_l, location=window_1.CurrentLocation(),
			                 progress_bar_color=pb_c)
			for i in range(10000):
				prog_e, prog_v = prog.Read(timeout=0)
				if prog_e is None:
					prog.Close()
					break
				prog.Element('progbar').UpdateBar(i + 1)
			sg.PopupOK('All done!', 'Your theme code is ready.', location=prog.CurrentLocation())
			prog.Close()
			# Dole out the code for the user's harvest.
			output_window_layout = [
				[sg.Text('Code for '+str(name)+' Look and Feel theme.')],
				[sg.Text('Please copy and paste the code below into your source code.')],
				[sg.Multiline(default_text=theme, key='output', size=(70, 8))],
				[sg.Button(' Exit ', key='Exit'), sg.Button(' Preview Theme ', key='preview')]
			]
			output_window = sg.Window(title=('Look and Feel Theme - '+str(name)), layout=output_window_layout,
			                          grab_anywhere=False, element_justification='center',
			                          location=window_1.CurrentLocation())
			while True:
				output_window_events, output_window_values = output_window.Read()
				if output_window_events in (None, 'Exit'):
					output_window.Close()
					break
				if output_window_events in 'preview':
					try:
						user_output = output_window_values['output']
						if user_output == theme:  # This guy here and his alternate allow for
							exec(theme)  # on-the-fly editing of the theme code even from the
						if user_output != theme:  #  output panel.
							theme = user_output  # Tried and tested :).
							exec(theme)

						# Let's give 'em a feel of their custom theme.
						preview_layout = [[sg.Text(' '*40), sg.Text('Theme Preview')],
							[sg.Text(' '*19),
							 sg.Text('This is how your theme will look when used.')],
							[sg.Text(' '*5),
							 sg.Text('This window serves no other purpose than being a mannequin.')],
							[sg.Text('Only the exit button works.')],
							[sg.InputText('...just a textbox', size=(60, 8))],
							[sg.Multiline('This is just a Multiline element. Play with it as you deem fit.',
							              size=(58, 10))],
							[sg.Button(' Button A '),
							 sg.Button(' Button B '),
							 sg.Button(' Button C '),
							 sg.Button(' Another useless button. ')],
							[sg.Exit(' Exit ', key='Exit')]]
						preview = sg.Window(title=(name+' Preview Popup'), layout=preview_layout, resizable=False,
						                    location=output_window.CurrentLocation(), progress_bar_color=pb_c)
						while True:
							preview_events, preview_values = preview.Read()
							if preview_events in (None, 'Exit'):
								preview.Close()
								break
						# Change back to the previous LookyFeely theme.
						sg.ChangeLookAndFeel(random_theme)
					except:
							sg.PopupCancel('An error occured! Please check your entries! Wrong color format!',
							               title='Error: Wrong color format!')
							if DebugMode is on:
								print('Error!')
			
	if DebugMode is on:
		print(window_1_events)
		print(window_1_values)
	# The customary exit route.
	if window_1_events in (None, 'Exit', 'Cancel'):
		window_1.Close()
		break

'''

This code is distributed under the...

888      .d8888b.  8888888b.  888      .d8888b.          
888     d88P  Y88b 888   Y88b 888     d88P  Y88b         
888     888    888 888    888 888          .d88P         
888     888        888   d88P 888         8888"    888   
888     888  88888 8888888P"  888          "Y8b. 8888888 
888     888    888 888        888     888    888   888   
888     Y88b  d88P 888        888     Y88b  d88P         
88888888 "Y8888P88 888        88888888 "Y8888P"          

...license.

(Okay, I copied that one from PySimpleGUI.)
'''

# Well, that's all people. Just over 270 lines total. Comments included.
# PyCharm helped. Nothing more than a 'weak warning' came up.
