'''
Loc8 Quick Intro

Loc8 is a PySimpleGUI extension module that enables easy translocation of PySimpleGUI windows in relation to a reference
window without fiddling with screen coordinates. It's built to kill the stress of manually calculating window locations
to improve your program's aesthetic value; having all windows pinned by their upper-left corner gets old after a while.

To put it in exact terms, this module enables you obtain a screen location coordinate in relation to a reference/parent
window which you can pass as the location parameter of a window. When used right, your windows will appear in more
logical locations, rather than the center of the screen.

PSG_Loc8 is distributed under the MIT license. See its GitHub repo for details of that:

https://github.com/definite-d/PSG-Loc8/

------------------------------------------------------------------------------------------------------------------------

Usage Instructions:

~ As a rule of thumb, have your layouts defined in individual variables, before the Window() call.

~ Create your first window.

~ Choose a reference window; preferably the first window that comes up when your program is run. It's also probably the window you just created.

~ Within the event loop of the reference window, advisably immediately after the Read call, declare a variable of the Locator class.

~ In between the layout and Window class variable declarations of the other window you wish to locate (or probably anywhere else), call the get_ideal_location() function of the Locator class with the layout variable being passed.

~ That function will return the ideal location for the window to be shown, so you can go ahead and specfiy that as the location value of the Window declaration, or Move your window.

'''

__version__ = '1.16'

from random import choice as rc
from string import ascii_letters, punctuation, ascii_lowercase, ascii_uppercase, digits

import PySimpleGUI as sg

created_keys = []
def generate_unique_key(length=20, created_keys=created_keys):
	'''
	This function creates unique identifiers when called. These identifiers can be used as
	PySimpleGUI Element keys with no issue.
	
	:param length: (int) The character length of the generated key. The default 20 will
	ensure a maximum number of possibly unique keys so high that it would be a very strange
	thing to require any value higher than that.
	:param created_keys: (list) A list in which to store all keys generated. This will help avoid duplicates, even when nested.
	:return: (str) Unique Key id.
	'''
	choice_pool = [rc([rc(ascii_letters), rc(digits)]) for iterator in range(int(length*1.5))]
	key = ''
	for n in range(length):
		key += rc(choice_pool)
	if key not in created_keys:
		created_keys.append(key)
		return key
	else:
		generate_unique_key(length)
		
def change_up_text(text):
	'''
	This function takes in text and returns a string of the same length, but with a different value.
	
	:param text: (str) Text to change up.
	:return: (str) Changed text.
	'''
	if type(text) == str and str(text) not in (None, ''):
		trans = str.maketrans((digits+ascii_lowercase+ascii_uppercase+punctuation+' '), '9753102468zxvtrpnljhfdbacegikmoqsuwyZXVTRPNLJHFDBACEGIKMOQSUWY~|`^\@><:.,*(&$"!#%\')+-/;=?[] {} ')
		changed_text = text.translate(trans)
		return changed_text
	else:
		return text

def duplicate_layout(layout):
	'''
	This function is responsible for generating a duplicated layout from one supplied.
	
	It is built to bypass the inability to reuse elements in layouts when you simply need
	to find out details of how a Window will work with your layout before a Read, as is 
	the case here.

	:param layout: (list) A list-in-list layout.
	:return: (list) A duplicated layout
	'''
	duplicated_layout = []
	# I'm feeling a bit lazy about this, so if you find any unsupported elements which you need in your layout,
	#   please alert me on GitHub.
	supported_elements = [sg.Text, sg.Tab, sg.TabGroup, sg.Column, sg.Button, sg.InputText, sg.Slider, sg.Frame,
	                      sg.Radio, sg.ProgressBar, sg.Checkbox, sg.Multiline]
	for row in layout:
		new_row = []
		for element in row:
			element_index = row.index(element)
			pad = element.Pad
			size = element.Size
			font = element.Font
			auto_size_text = element.AutoSizeText
			text_input_default = element.TextInputDefault
			key = f'dummykey_{generate_unique_key()}'  # Hopefully, a user-supplied layout won't include a key as convoluted as this.
			# Measures to ensure that there are no duplicate keys. We don't care about the keys themselves here; just duplicates.
			if element.Key != key:
				pass
			else:
				# Run the process again if the user's key was in fact convoluted.
				key = f'dummykey_{generate_unique_key()}'
			if element.Visible:
				# print(element)
				# print(element.Type)
				# print(type(element))
				if type(element) == sg.Text:
					text = change_up_text(element.Get())
					relief = element.Relief
					border_width = element.BorderWidth
					justification = element.Justification
					copied_element = sg.Text(
						text = text,
						size = size,
						auto_size_text = auto_size_text,
						relief = relief,
						font = font,
						border_width = border_width,
						justification = justification,
						pad = pad,
						key=key,
						metadata = key
					)
				if type(element) == sg.Tab:
					title = change_up_text(element.Title)
					layout = duplicate_layout(element.Rows)
					border_width = element.BorderWidth
					copied_element = sg.Tab(
						title = title,
						layout = layout,
						font = font,
						pad = pad,
						border_width = border_width,
						key = key,
						metadata=key
					)
				if type(element) == sg.TabGroup:
					layout = duplicate_layout(element.Rows)
					border_width = element.BorderWidth
					copied_element = sg.TabGroup(
						layout = duplicate_layout(layout),
						font = font,
						pad = pad,
						metadata=key,
						border_width = border_width,
						key = key
					)
				if type(element) == sg.Column:
					layout = duplicate_layout(element.Rows)
					scrollable = element.Scrollable
					vertical_scroll_only = element.VerticalScrollOnly
					justification = element.Justification
					el_justification = element.ElementJustification
					copied_element = sg.Column(
						layout = layout,
						size = size,
						scrollable= scrollable,
						justification = justification,
						element_justification= el_justification,
						vertical_scroll_only = vertical_scroll_only,
						pad = pad,
						metadata = generate_unique_key(),
						key = key
					)
				if type(element) == sg.Frame:
					title = element.Title
					relief = element.Relief
					title_location = element.TitleLocation
					layout = duplicate_layout(element.Rows)
					border_width = element.BorderWidth
					el_justification = element.ElementJustification
					copied_element = sg.Frame(
						title = change_up_text(title),
						title_location = title_location,
						layout = layout,
						relief = relief,
						size = size,
						font = font,
						border_width=border_width,
						element_justification=el_justification,
						pad = pad,
						metadata=key,
						key = key
					)
				if type(element) == sg.Button:
					button_text = change_up_text(element.ButtonText)
					image_filename = element.ImageFilename
					image_data = element.ImageData
					image_subsample = element.ImageSubsample
					image_size = element.ImageSize
					border_width = element.BorderWidth
					auto_size_button = element.AutoSizeButton
					copied_element = sg.Button(
						button_text = button_text,
						image_filename = image_filename,
						image_data = image_data,
						image_size = image_size,
						image_subsample = image_subsample,
						border_width = border_width,
						size = size,
						auto_size_button = auto_size_button,
						font = font,
						pad = pad,
						metadata=key,
						key = key
					)
				if type(element) == sg.Radio:
					text = change_up_text(element.Text)
					group_id =  element.GroupID
					copied_element = sg.Radio(
						text = text,
						group_id = group_id,
						key = key,
						font = font,
						metadata=key,
						pad = pad,
					)
				if type(element) == sg.Checkbox:
					text = change_up_text(element.Text)
					copied_element = sg.Checkbox(
						text = text,
						size = size,
						auto_size_text = auto_size_text,
						key = key,
						font = font,
						metadata=key,
						pad = pad,
					)
				if type(element) == sg.InputText:
					default_text = change_up_text(text_input_default)
					border_width = element.BorderWidth
					password_character = element.PasswordCharacter
					copied_element = sg.InputText(
						default_text = default_text,
						size = size,
						font = font,
						border_width = border_width,
						key = key,
						metadata=key,
						pad = pad,
					)
				if type(element) == sg.Multiline:
					default_text = change_up_text(element.DefaultText)
					border_width = element.BorderWidth
					copied_element = sg.Multiline(
						default_text = default_text,
						size = size,
						auto_size_text = auto_size_text,
						font = font,
						border_width = border_width,
						metadata=key,
						key = key,
						pad = pad,
					)
				if type(element) == sg.Slider:
					slider_range = element.Range
					orientation = element.Orientation
					disable_number_display = element.DisableNumericDisplay
					relief = element.Relief
					copied_element = sg.Slider(
						range = slider_range,
						orientation = orientation,
						disable_number_display=disable_number_display,
						border_width = border_width,
						relief = relief,
						size=size,
						font = font,
						key = key,
						metadata=key,
						pad = pad
					)
				if type(element) == sg.ProgressBar:
					max_value = element.MaxValue
					orientation = element.Orientation
					style = element.BarStyle
					border_width = element.BorderWidth
					relief = element.Relief
					copied_element = sg.ProgressBar(
						max_value = max_value,
						orientation = orientation,
						size = size,
						auto_size_text = auto_size_text,
						style = style,
						border_width = border_width,
						relief = relief,
						key = key,
						metadata=key,
						pad = pad
					)
				elif type(element) not in supported_elements:
					raise NotImplementedError(f'The element type: \'{str(type(element))}\' has not been implemented yet.')
				new_row.append(copied_element)
			else:
				pass
		duplicated_layout.append(new_row)
	return duplicated_layout

POSITIONS = [
	'UC',
	'UL',
	'UR',
	'MC',
	'ML',
	'MR',
	'BC',
	'BL',
	'BR',
]

class Locator:
	'''
	The main class of this module. Does the heavy lifting.
	
	You have to create the locator object within the event loop of the reference window.
	'''
	
	def __init__(self, reference_window):
		'''
		Thsi class takes a single parameter upon initialization; the first reference window.
		
		:param reference_window: (PySimpleGUI.Window) Window object for the window which you wish others to reference for their location calculations.
		'''
		if type(reference_window) != sg.Window:
			raise TypeError('The reference window has to be a PySimpleGUI.Window object.')
		self.reference_window(reference_window)
	
	def reference_window(self, new_reference_window=None):
		'''
		If no window is passed as an argument, this function returns the current reference window object.
		However, passing a window will result in that window being set as the current reference window, and return None.
		
		:return: (Window or None) Either a PySimpleGUI.Window object or a None type value.
		'''
		if new_reference_window != None:
			self.reference_window = new_reference_window
			self.refresh_reference_window()
			return None
			
		if new_reference_window == None:
			return self.reference_window
	
	def refresh_reference_window(self):
		'''
		Calls the Refresh() function of the reference window, and re-registers the location and size values.
		
		:return: None
		'''
		self.reference_window.Refresh()
		try:
			self.reference_location = self.reference_window.CurrentLocation()
			self.reference_size = self.reference_window.Size
		except:
			self.reference_location = None
			self.reference_size = None
	
	def get_ideal_location(self, subject_layout, pin_to, handle, y_offset=0, x_offset=0):
		'''
		The biggest deal of this class ' functions. It calculates the best screen coordinate for the subject window to
		be for your requirements and returns those coordinates.
		
		:param subject_layout: (list) List-in-list layout for the subject window.
		:param pin_to: (str) An identifier for which part of the reference window to target. Can be any of the values in the POSITIONS constant.
		:param handle: (str) An identifier for which part of the subject window to be used as an anchor in positioning. Can be any out of the values in the POSITIONS constant.
		:param y_offset: (int) Desired space difference in pixels between the top of the reference window and the top of the subject window.
		:param x_offset: (int) Desired space difference in pixels between the left of the reference window and the left of the subject window.
		:return ideal_location: (tuple) A tuple containing the ideal screen location for the subject window to be moved to.
		'''
		# Dummy Window setup
		previous_theme = sg.theme()
		base_color = sg.theme_background_color()
		dummy_theme = {
			'BACKGROUND': base_color,
			'TEXT': base_color,
			'INPUT': base_color,
			'TEXT_INPUT': base_color,
			'SCROLL': base_color,
			'BUTTON': (base_color, base_color),
			'PROGRESS': (base_color, base_color),
			'BORDER': 0,
			'SLIDER_DEPTH': 0,
			'PROGRESS_DEPTH': 0,
		}
		sg.theme_add_new('Loc8_Dummy_Theme', dummy_theme)
		sg.theme('Loc8_Dummy_Theme')
		self.refresh_reference_window()
		reference_UL = (self.reference_location[0], self.reference_location[1])
		reference_UC = ((self.reference_location[0] + int(self.reference_size[0] / 2)), self.reference_location[1])
		reference_UR = ((self.reference_location[0] + self.reference_size[0]), self.reference_location[1])
		reference_ML = (self.reference_location[0], (self.reference_location[1] + int(self.reference_size[1] / 2)))
		reference_MC = ((self.reference_location[0] + int(self.reference_size[0] / 2)), (self.reference_location[1] + int(self.reference_size[1] / 2)))
		reference_MR = ((self.reference_location[0] + self.reference_size[0]), (self.reference_location[1] + int(self.reference_size[1] / 2)))
		reference_BL = (self.reference_location[0], (self.reference_location[1] + self.reference_size[1]))
		reference_BC = ((self.reference_location[0] + int(self.reference_size[0] / 2)), (self.reference_location[1] + self.reference_size[1]))
		reference_BR = ((self.reference_location[0] + self.reference_size[0]), (self.reference_location[1] + self.reference_size[1]))
		
		def pin_check():
			'''
			This process checks what the pin_to value is before carrying out further code execution.

			:return: None
			'''
			if pin_to == 'UL':
				chosen_reference = reference_UL
			if pin_to == 'UC':
				chosen_reference = reference_UC
			if pin_to == 'UR':
				chosen_reference = reference_UR
			if pin_to == 'ML':
				chosen_reference = reference_ML
			if pin_to == 'MC':
				chosen_reference = reference_MC
			if pin_to == 'MR':
				chosen_reference = reference_MR
			if pin_to == 'BL':
				chosen_reference = reference_BL
			if pin_to == 'BC':
				chosen_reference = reference_BC
			if pin_to == 'BR':
				chosen_reference = reference_BR
			return chosen_reference
		
		dummy_layout = duplicate_layout(subject_layout)
		dummy_window = sg.Window('Dummy Window', dummy_layout,
		                         alpha_channel=0, transparent_color=base_color,
		                         finalize=True)
		sg.theme(previous_theme)
		move_to_reference = pin_check()
		dummy_window.Move(move_to_reference[0], move_to_reference[1])
		dummy_window.Refresh()
		dummy_location = dummy_window.CurrentLocation()
		dummy_size = dummy_window.Size
		dummy_window.Refresh()
		dummy_UL = (dummy_location[0], dummy_location[1])
		dummy_UR = ((dummy_location[0] - dummy_size[0]), dummy_location[1])
		dummy_UC = ((dummy_location[0] - int(dummy_size[0] / 2)), dummy_location[1])
		dummy_ML = (dummy_location[0], (dummy_location[1] - int(dummy_size[1] / 2)))
		dummy_MC = ((dummy_location[0] - int(dummy_size[0] / 2)), (dummy_location[1] - int(dummy_size[1] / 2)))
		dummy_MR = ((dummy_location[0] - dummy_size[0]), (dummy_location[1] - int(dummy_size[1] / 2)))
		dummy_BL = (dummy_location[0], (dummy_location[1] - dummy_size[1]))
		dummy_BC = ((dummy_location[0] - int(dummy_size[0] / 2)), (dummy_location[1] - dummy_size[1]))
		dummy_BR = ((dummy_location[0] - dummy_size[0]), (dummy_location[1] - dummy_size[1]))
		
		def handle_check():
			'''
			This process checks what the handle value is before carrying out further code execution.

			:return: None
			'''
			if handle == 'UL':
				chosen_handle = dummy_UL
			if handle == 'UC':
				chosen_handle = dummy_UC
			if handle == 'UR':
				chosen_handle = dummy_UR
			if handle == 'ML':
				chosen_handle = dummy_ML
			if handle == 'MC':
				chosen_handle = dummy_MC
			if handle == 'MR':
				chosen_handle = dummy_MR
			if handle == 'BL':
				chosen_handle = dummy_BL
			if handle == 'BC':
				chosen_handle = dummy_BC
			if handle == 'BR':
				chosen_handle = dummy_BR
			return chosen_handle
		raw_result = handle_check()
		dummy_window.Move(raw_result[0], raw_result[1])
		dummy_window.Refresh()
		
		if y_offset != 0:
			offset_applied = (raw_result[0], (raw_result[1] + y_offset))
			
		if x_offset != 0:
			offset_applied = ((raw_result[0] + x_offset), raw_result[0])
			
		if (offset_applied[0] > sg.Window.get_screen_size()[0] or offset_applied[1] > sg.Window.get_screen_size()[1]) or \
				(offset_applied[0] < 0 or offset_applied[1] < 0):
			dummy_window.Move(move_to_reference[0], move_to_reference[1])
		else:
			dummy_window.Move(offset_applied[0], offset_applied[1])
		
		dummy_window.Refresh()
		result = dummy_window.CurrentLocation()
		dummy_window.Refresh()
		dummy_window.Close()
		return result
		
def test_run_with_windows():
	'''
	This function runs a couple of gibberish windows to demonstrate this module in action.
	
	:return: None
	'''
	ref = sg.Window('Ref Window', [[sg.Text('This is the reference window')], [sg.Button('Open sub window.', key='sub_open')]], finalize=True)
	loc8or = Locator(ref)
	while True:
		r_ev, r_val = ref.Read()
		if r_ev == 'sub_open':
			sub_layout = [
				[sg.TabGroup(
					[
						[sg.Tab('Some Fantastic Tab', [
							[sg.Text('This is the subject window. Have some gibberish text........asdfasdfsdfasdfasfdadsf')]
						]
						        )
						 ]
					]
				)
				],
				[sg.Text('asdgffasdfsadf')],
				[sg.Text('asdgffadasfasdfasdf sdfsadf')]
			]
			ideal_x, ideal_y = loc8or.get_ideal_location(sub_layout, 'UC', 'UC', 20)
			sub = sg.Window('Sub Window', sub_layout, location=(ideal_x, ideal_y))
			while True:
				s_ev, s_val = sub.Read()
				if s_ev in (None, 'Exit'):
					sub.Close()
					break
		if r_ev in (None, 'Exit'):
			ref.Close()
			break

if __name__ == '__main__':
	test_run_with_windows()
 