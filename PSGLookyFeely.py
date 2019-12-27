# Welcome...
# ... to the code of LookyFeely.
# https://www.github.com/definite-d/Looky-Feely/

version = 'v2.1.14'

'''

  /%                                    %**%
 / %                                    %  %
%  %                                    %  %
%  %                                    %  %
%  %             %*****\     %*****\    %  % %*%    %**%  %**%
%  %            % %***\ %   % %***\ %   %  %% %     %  %  %  %
%  %            % %   % %   % %   % %   %     \     %  %  %  %
%  %,,,,,,,,,   % \,,,% %   % \,,,% %   %  %\  \    %  \,,%  %
%,,,,,,,,,,,/    \,,,,,%     \,,,,,%    %,,% \,,\   \,,,,,,  %
                                                           % %
                                                    ,,,,,,,% %
                                                   /,,,,,,,,%
fffffffffffff                       lll
fff                                 lll
fff                                 lll
fff                                 lll
ffffffffff   eeeeeee     eeeeeee    lll       yyy   yyy
fff         eee   eee   eee   eee   lll       yyy   yyy
fff         eeeeeeee    eeeeeeee    lll       yyy   yyy
fff         eee         eee         lll       yyy   yyy
fff         eee   eee   eee   eee   lll  lll  yyy   yyy
fff          eeeeee      eeeeee      llllll    yyyyyyyy
                                                    yyy
                                            yyy	    yyy
                                              yyyyyyy

wow... I typed that by hand.
(EDIT: Just found out there was a Python module to automatically type this stuff. [14/12/2019])

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
# Development began on 29/11/2019, bare minimum was completed on 1/12/2019.
# ===================================================================================
# ___...:::---=== Code Starts Here. ===---:::...___

# Necessary import calls.
import colorpiq
import colour
import PySimpleGUI as sg  # I'm calling it 'sg' to comply with the PySimpleGUI Docs.
from PySimpleGUI import Print as Print  # Also, since I want to showcase PySimpleGUI features,
# I'll use the PySimpleGUI Debug Window.
from os import getlogin as user
from os import system as cmd
from random import choice as rc
import _tkinter

sg.SetOptions(font=('Helvetica', 9),
              auto_size_text=True,
              element_padding=(8, 2),
              ttk_theme='default')

# Had no befitting icon. So I made one :)... PEP-8... The things I do for PEP-8... About 744 lines could have been
# taken up by the icon in Base64 form. Thanks to PEP-8. Nuh-uh; I'm NOT filling paragraph, PyCharm.
colorpiq.DEFAULT_ICON = b64icon = b'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\n'
sg.SetGlobalIcon(b64icon)

# Random color generator.
def random_color():
    h = str('#')
    color = ''
    for i in range(6):
        color = color + str(rc([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']))  # Ha ha. Hex.
    color = str(h + color)
    if DebugMode is on:
        Print('Randomly Generated Color: ' + color)
    return color


# To avoid the 'nagging' at all costs...
look_and_feel_values = sg.ListOfLookAndFeelValues()
for t in look_and_feel_values:
    if 'Default' in str(t):
        look_and_feel_values.remove(t)  # I declare war upon any theme bearing the surname of Default.
random_theme = str(rc(look_and_feel_values))
# 'Cause I figured the master of colors should have all the colors.
sg.ChangeLookAndFeel(random_theme)

# I like to make a custom debug mode when I make apps.
# So, here's a shameless boolean debug switch and aliases.
on = True
off = False
DebugMode = off  # Powerful line here... powerful.
if DebugMode is on:
    # Just for fun.
    Print('@'+str(user())+', do you read me?')
    Print('LookyFeely is live.')
    Print('LookyFeely is live.')
    Print('I repeat, LookyFeely is live.')

# Yeah, I gotta know what colors could possibly be valid.
raw_list = colour.RGB_TO_COLOR_NAMES
color_names_list = []
lowercase_color_names_list = []
for i in raw_list:  # I refuse to type all 450 color names in here. By hand.
    for j in raw_list[i]:
        color_names_list.append(str(j))
        lowercase_color_names_list.append((str(j)).lower())
luminance_list = []
# To sort from Darkest to Lightest...
for i in color_names_list:
    i_c = colour.Color(i)
    i_c_l = i_c.get_luminance()
    luminance_list.append(i_c_l)
sorter_list = list(zip(luminance_list, color_names_list))
sorter_list = sorted(sorter_list, key=lambda color: color[0])
color_names_list = sorted_list = [i[1] for i in sorter_list]

# This is the code for the first window you'll see when running this code.
# Ironically, you can only change the LookAndFeel for windows like this from the code itself.

tab_layout = [
    [sg.Tab(title='Specifier',
            layout=[
                [sg.Text('')],
                [sg.Text('Theme Name: '), sg.InputText(key='name', size=(20, 1))],
                [sg.Text('Background Color: ', size=(16, 1)), sg.InputText('...color value', key='bg_c', size=(16, 1)),
                 sg.Button(target='bg_c', button_text='Choose Color', key='bg_c_choose')],
                [sg.Text('Text Color: ', size=(16, 1)), sg.InputText('...color value', key='txt_c', size=(16, 1)),
                 sg.Button(target='txt_c', button_text='Choose Color', key='txt_c_choose')],
                [sg.Text('Text Input Color: ', size=(16, 1)), sg.InputText('...color value', key='in_c', size=(16, 1)),
                 sg.Button(target='in_c', button_text='Choose Color', key='in_c_choose')],
                [sg.Text('Input Color: ', size=(16, 1)), sg.InputText('...color value', key='txt_in_c', size=(16, 1)),
                 sg.Button(target='txt_in_c', button_text='Choose Color', key='txt_in_c_choose')],
                [sg.Text('Scroll Color: ', size=(16, 1)), sg.InputText('...color value', key='scr_c', size=(16, 1)),
                 sg.Button(target='scr_c', button_text='Choose Color', key='scr_c_choose')],
                [sg.Text('Button Text Color: ', size=(16, 1)), sg.InputText('...color value', key='bt_txt_c', size=(16, 1)),
                 sg.Button(target='bt_txt_c', button_text='Choose Color', key='bt_txt_c_choose')],
                [sg.Text('Button Color: ', size=(16, 1)), sg.InputText('...color value', key='bt_c', size=(16, 1)),
                 sg.Button(target='bt_c', button_text='Choose Color', key='bt_c_choose')],
                [sg.Text('Progress Bar Color: ', size=(16, 1)), sg.InputText('...color value', key='pb_c', size=(16, 1)),
                 sg.Button(target='pb_c', button_text='Choose Color', key='pb_c_choose')],
                [sg.Text('Border Width: ', size=(10, 1)),
                 sg.Spin(initial_value='1',values=[x for x in range(0, 1000)], key='bor_w', size=(3, 1)),
                 sg.Text(' || '), sg.Text('Slider Depth: ', size=(10, 1)),
                 sg.Spin(initial_value=1,
                         values=[x for x in range(0, 1000)], key='sl_bor_w', size=(3, 1))],
                [sg.Text('Progress Meter Depth: ', size=(17, 1)),
                 sg.Spin(initial_value=0, values=[x for x in range(0, 1000)], key='pb_w', size=(3, 1))]],
            element_justification='canter')],
    [sg.Tab(title='Other Options',
            layout=[[sg.Column(layout=[
                    [sg.Text(text='Have a feature proposal to add to these options?\nGot a complaint?\nOpen up an '
                                  'issue on the LookyFeely GitHub repository.', text_color=sg.LOOK_AND_FEEL_TABLE[
                        str(random_theme)]['TEXT_INPUT'], background_color=sg.LOOK_AND_FEEL_TABLE[str(random_theme)][
                        'INPUT'])],
                    [sg.Frame(title='Dark/Light Modes',
                              layout=[[sg.Text('Automatically make a...')],
                                      [sg.Checkbox('Dark Mode Theme', key='dark')],
                                      [sg.Checkbox('Light Mode Theme', key='light')],
                                      [sg.Text('...along with the theme currently being made.')]],
                              tooltip='May not always work as expected. Majorly dependent on your color choices.')],
                    [sg.Frame(title='Color Options', layout=[[sg.Button('View valid color names.', key='col_name_view')]])],
                    [sg.Frame(title='PySimpleGUI Options', layout=[[sg.Text('Probably unrelated, but useful.')], [sg.Button('Preview all PySimpleGUI themes', key='preview', tooltip=('This may take a while to initialize.\nAfter all, there are '+str(len(sg.ListOfLookAndFeelValues()))+ ' built-in themes.'))],  # That list sure grows fast.
                                     [sg.Button('Update / Install PySimpleGUI', key='update',
                                                tooltip='Requires Python and pip.')]],
                              element_justification='center')],
                    [sg.Frame(title='External Links', layout=[[sg.Button('Check out definite_d\'s GitHub page', key='checkout_me', tooltip='Come on, don\'t be shy!')], [sg.Button('Check out the LookyFeely GitHub page', key='checkout_lookyfeely', tooltip='Whoo! GitHub!')], [sg.Button('Check out the PySimpleGUI GitHub page', key='checkout_psg', tooltip='Whoo! GitHub! Again!')]], element_justification='center')]
                    ], element_justification='center', scrollable=True, vertical_scroll_only=True, size=(340, 315), background_color=sg.LOOK_AND_FEEL_TABLE[str(random_theme)]['SCROLL'])]],
            element_justification='center')]
]
window_1_layout = [
    [sg.Text('LookyFeely!')],
    [sg.Text('PySimpleGUI Look And Feel Code Generator.')],
    [sg.Text('by definite_d')],
    [sg.Text('Hover over this text for help.', tooltip='Specifying your theme\'s parameters is done using\nthe Specifier tab.\nSimply click the buttons or type them in to choose colors.\nTkinter color names also work.\nIf no color is given, LookyFeely will work with a random color.\nDon\'t forget to check out the other options in the\nOther Options tab.',)],  # Tsk. PEP-8. [sg.Text(('*'*70))],
    [sg.TabGroup(layout=tab_layout)],
    [sg.Button(button_text=' Generate LookAndFeel Code ', key='gen', bind_return_key=True)],
    [sg.Text(('\"'*100))],
    [sg.Text('Current Theme: '+str(random_theme))]
]
window_1 = sg.Window(('LookyFeely'+' - '+version), layout=window_1_layout, element_justification='center',
                     grab_anywhere=False, resizable=False)

while True:
    window_1_events, window_1_values = window_1.Read()
    try:
        window_1_c = window_1.CurrentLocation()
    except:
        break
        pass
    if 'choose' in window_1_events:
        window_1[window_1_events.replace('_choose', '')].Update(colorpiq.colorpiqr(preview_box_width=53, location=(window_1.CurrentLocation()[0]+4, window_1.CurrentLocation()[1]+150)))
    
    if window_1_events is 'gen':
        unsupported_entry = False
        no_name = False
        if window_1_values['name'] is '' or window_1_values['name'].isspace() is True:
            sg.Popup('You didn\'t specify a name for the theme!', title='Warning: No Name!', button_type='Cancel',
                     location=(window_1_c[0]+90, window_1_c[1]+50))
            no_name = True  # What masterpiece didn't have a name?
        for i in window_1_values:
            # I found that 'Navajo White' (unsupported color) isn't the same as 'NavajoWhite' (supported color).
            if '_c' in i and window_1_values[str(i)] not in ('...color value', 'None'):
                given_value = str(window_1_values[str(i)])
                window_1_values[str(i)] = (str(window_1_values[str(i)])).replace(' ', '')
            if '_c' in i and window_1_values[str(i)] not in ('...color value', 'None') and str(window_1_values[str(i)]).lower() not in lowercase_color_names_list and window_1_values[str(i)].startswith('#') is False and window_1_values[str(i)].isspace() is False and window_1_values[str(i)] is not '':
                sg.Popup(('The color name \''+given_value+'\' is not supported.\nYou should use the hex value of the '
                'intended color instead.'), title='Warning: Unsupported Color!', button_type='Cancel',
                         location=(window_1_c[0] + 40, window_1_c[1] + 50))
                unsupported_entry = True  # To avoid unforeseen error-stances.
        
        # What's a world without color?
        name = str(window_1_values['name'])
        bg_c = str(window_1_values['bg_c'])
        txt_c = str(window_1_values['txt_c'])
        txt_in_c = str(window_1_values['txt_in_c'])
        in_c = str(window_1_values['in_c'])
        scr_c = str(window_1_values['scr_c'])
        bt_txt_c = str(window_1_values['bt_txt_c'])
        bt_c = str(window_1_values['bt_c'])
        pb_c = str(window_1_values['pb_c'])
        bor_w = str(window_1_values['bor_w'])
        sl_bor_w = str(window_1_values['sl_bor_w'])
        pb_w = str(window_1_values['pb_w'])
        color_values = [bg_c, txt_c, in_c, txt_in_c, scr_c, bt_txt_c, bt_c, pb_c]
        
        if no_name is False and unsupported_entry is False:
            # Selected is a list of indexes of all colors selected (NOT their identifiers),
            #  in order of hierarchy on the color_values list.
            # Cleaning up the list of all... space wasters.
            for o in color_values:
                if (o.isspace() is True) or (o is ''):
                    color_values[color_values.index(o)] = 'None'
            # Now, to fetch my 'Selected' list.
            selected = []
            for e in color_values:
                if e not in ('...color value', 'None'):
                    selected.append(color_values.index(e))
            sel_colors = selected
            sel_colors1 = []
            for s in sel_colors:
                if sel_colors.count(s) > 1:
                    for n in range((sel_colors.count(s) - 1)):
                        sel_colors.remove(s)  # Removing the duplicates...
            for i in sel_colors:
                i = color_values[i]
                sel_colors1.append(i)
            sel_colors = sel_colors1
            # Dealing with unspecified color values.
            done = False
            if color_values.count(('...color value' or 'None')) > 0:
                unspecified = True
            else:
                unspecified = False
                done = True
    
            if unspecified is False:
                # These lists are used for sorting colors by brightness.
                luminance_list = []
                for i in color_values:
                    i_c = colour.Color(i)
                    i_c_l = i_c.get_luminance()
                    luminance_list.append(i_c_l)
                sorter_list = list(zip(luminance_list, color_values))
                sorter_list = sorted(sorter_list, key=lambda color: color[0])
                sorted_list = [i[1] for i in sorter_list]
                if window_1_values['dark'] is True:
                    dark_list = [sorted_list[0], sorted_list[6], sorted_list[2], sorted_list[0], sorted_list[2],
                                 sorted_list[7], sorted_list[1], sorted_list[3]]
                if window_1_values['light'] is True:
                    light_list = [sorted_list[5], sorted_list[0], sorted_list[1], sorted_list[7], sorted_list[0],
                                  sorted_list[7], sorted_list[2], sorted_list[2]]
                done = True
            if unspecified is True:
                unspec_no = len(color_values) - len(selected)
                if unspec_no is not 1:
                    unspec_title = str(unspec_no)+' color values were not specified!'
                else:
                    unspec_title = 'A color value was not specified!'
                if unspec_no is 8:
                    unspec_no = 'any'
                    unspec_title = 'No color value was specified!'
                unspec_opts_layout = [
                    [sg.Text(text=('You didn\'t specify '+str(unspec_no)+' color values.'))],  # I'm so fancy...
                    [sg.Text(text='What should be done about that?')],
                    [sg.Button('Fill in random colors.', key='Randomize', tooltip='Make it crazy random!'),
                     sg.Button('Base other colors off those given.', key='Mono', tooltip='Good for mono-color themes.'),
                     sg.Button('Cancel; Let me change that.', key='Cancel', tooltip='Have it your way.')]]
                try:
                    unspec_opts = sg.Window(title=unspec_title, layout=unspec_opts_layout,
                                            location=(window_1_c[0]-60, window_1_c[1]+50))
                except:
                    break
                    pass
                done = False
                while True:
                    try:
                        unspec_opts_events, unspec_opts_values = unspec_opts.Read()
                        if unspec_opts_events is 'Randomize':  # The most straightforward task for colors.
                            for c in color_values:
                                if c in ('None', '...color value'):
                                    color_values[color_values.index(c)] = random_color()
                            #Sort things out...
                            luminance_list = []
                            for i in color_values:
                                i_c = colour.Color(i)
                                i_c_l = i_c.get_luminance()
                                luminance_list.append(i_c_l)
                            sorter_list = list(zip(luminance_list, color_values))
                            sorter_list = sorted(sorter_list, key=lambda color: color[0])
                            sorted_list = [i[1] for i in sorter_list]
                            color_values = sorted_list
                            done = True
                            unspec_opts.Close()
                            break
                        if unspec_opts_events is 'Mono':
                            # Here comes the mono...
                            try:
                                if not selected:
                                    selected = [0]
                                    color_values[0] = random_color()
                                    sel_colors = [color_values[0]]
                                    number = len(color_values)  # That should be 8.
                                number = int(-1 * (8 // (-1 * (len(sel_colors)))))  # Phew. What a number.
                                sel_colors_shades = []
                                # Just in case anybody dropped in some Tkinter colors.
                                for tk in sel_colors:
                                    sel_colors[sel_colors.index(tk)] = colour.Color(tk).get_web()
                                # I'm gonna expand the list of selected colors to 8, by creating a list of
                                #   transitioning colors between all selected colors.
                                if len(sel_colors) > 1:
                                    transition = []
                                    for n in sel_colors[0:(len(sel_colors)-1)]:
                                        next_color = sel_colors[((sel_colors.index(n))+1)]
                                        n = colour.Color(n)
                                        next_color = colour.Color(next_color)
                                        shadegradient = list(n.range_to(next_color, number*2))
                                        transition.extend(shadegradient)
                                        for s in transition:
                                            if transition.count(s) > 1:
                                                for h in range((transition.count(s) - 1)):
                                                    transition.remove(s)
                                if len(sel_colors) == 1:  # Mono el mono.
                                    for i in sel_colors:
                                        # Who wants a theme where every color is black? Or annoyingly bright?
                                        if colour.Color(sel_colors[0]).luminance >= 0.6:
                                            other_shade = colour.Color('black')
                                            signal = 'black'
                                        if colour.Color(sel_colors[0]).luminance <= 0.5:
                                            other_shade = colour.Color('white')
                                            signal = 'white'
                                        if colour.Color(sel_colors[0]).luminance > 0.5 and colour.Color(sel_colors[0]).luminance < 0.6:  # Yeah.
                                            other_shade = colour.Color(i)
                                            other_shade.set_luminance((other_shade.get_luminance())/2)
                                            signal = 'depends'
                                        i = colour.Color(i)
                                        # I have to get a list of colors that's sorted from darkest to brightest by
                                        #   default. So...
                                        if other_shade.luminance < i.luminance:  # Darker/Blacker to Lighter.
                                            transition = list(other_shade.range_to(i, number))
                                        else:  # Darker to Whiter/Lighter.
                                            transition = list(i.range_to(other_shade, number))
                                sel_colors_shades.extend(transition)
                                # Dark and Light modes... I nearly got confused about where to put their code.
                                # Sort things out...
                                luminance_list = []
                                for i in sel_colors_shades:
                                    i_c = colour.Color(i)
                                    i_c_l = i_c.get_luminance()
                                    luminance_list.append(i_c_l)
                                sorter_list = list(zip(luminance_list, sel_colors_shades))
                                sorter_list = sorted(sorter_list, key=lambda color: color[0])
                                sorted_list = [i[1] for i in sorter_list]
                                if window_1_values['dark'] is True:
                                    dark_list = [sorted_list[0], sorted_list[6], sorted_list[7],
                                                 sorted_list[1], sorted_list[2], sorted_list[7],
                                                 sorted_list[1], sorted_list[3]]
                                if window_1_values['light'] is True:
                                    light_list = [sorted_list[7], sorted_list[1], sorted_list[0],
                                                  sorted_list[6], sorted_list[5], sorted_list[0],
                                                  sorted_list[6], sorted_list[4]]
                                # Now, to make the 'neutral' theme. No light or dark tilts.
                                if len(sel_colors) == 1:  # I found that pure mono themes need this little spice-up.
                                    if signal is 'white':
                                        if selected[0] != 0:
                                            shade_list = [sorted_list[1], sorted_list[5], sorted_list[0], sorted_list[5], sorted_list[3], sorted_list[0], sorted_list[7], sorted_list[6]]
                                        else:
                                            shade_list = [sorted_list[1], sorted_list[5], sorted_list[0], sorted_list[5], sorted_list[3], sorted_list[0], sorted_list[7], sorted_list[6]]
                                    if signal is 'black':
                                        if selected[0] != 0:
                                            shade_list = [sorted_list[0], sorted_list[7], sorted_list[6], sorted_list[1], sorted_list[3], sorted_list[1], sorted_list[6], sorted_list[6]]
                                        else:
                                            shade_list = [sorted_list[0], sorted_list[1], sorted_list[6], sorted_list[1], sorted_list[3], sorted_list[1], sorted_list[6], sorted_list[6]]
                                    if signal is 'depends':
                                        if selected[0] != 0:
                                            shade_list = [sorted_list[2], sorted_list[7], sorted_list[7], sorted_list[2], sorted_list[3], sorted_list[7], sorted_list[0], sorted_list[6]]
                                        else:
                                            shade_list = [sorted_list[2], sorted_list[0], sorted_list[7], sorted_list[0], sorted_list[3], sorted_list[7], sorted_list[0], sorted_list[6]]
                                            
                                else:
                                    if selected[0] is not 0:
                                        shade_list = [sorted_list[6], sorted_list[0], sorted_list[7], sorted_list[1], sorted_list[5], sorted_list[7], sorted_list[0], sorted_list[3]]
                                    else:
                                        shade_list = [sorted_list[0], sorted_list[6], sorted_list[7], sorted_list[1], sorted_list[5], sorted_list[0], sorted_list[7], sorted_list[3]]
                                for i in selected:
                                    shade_list[i] = color_values[i]
                                color_values = shade_list
                                done = True
                                unspec_opts.Close()
                                break
                            except:
                                unspec_opts.Close()
                                done = False
                                break
                        if unspec_opts_events in (None, 'Cancel'):
                            done = False
                            unspec_opts.Close()
                            break
                    except:
                        break
                        pass
            # This is where the real code generation happens.
            if done is True:  # Yep. Real shameless signal system.
                # Set the names of colors just right...
                for i in color_values:
                    if str(i).startswith('#') is False:
                        color_values[color_values.index(i)] = str(i).lower()  # Lowercase doesn't discriminate.
                # Reset all colors to their values in the color_values list.
                bg_c = str(color_values[0])
                txt_c = str(color_values[1])
                txt_in_c = str(color_values[2])
                in_c = str(color_values[3])
                scr_c = str(color_values[4])
                bt_txt_c = str(color_values[5])
                bt_c = str(color_values[6])
                pb_c = str(color_values[7])
                theme = str('# Custom '+name+' LookAndFeel Theme.\n# Generated using LookyFeely.\n'
                                             'import PySimpleGUI as sg  # Please change \'sg\' to your liking.\n'
                                             'sg.LOOK_AND_FEEL_TABLE[\''+name+'\'] = {\'BACKGROUND\': \''+bg_c+'\',\n    \''
                                                                                                               'TEXT\': \''+txt_c+'\',\n    \'INPUT\': \''+in_c+'\',\n    \''
                                                                                                                                                                'TEXT_INPUT\': \''+txt_in_c+'\',\n    \'SCROLL\': \''+scr_c+'\',\n    \''
                                                                                                                                                                                                                            'BUTTON\': (\''+bt_txt_c+'\', \''+bt_c+'\'),\n    \''
                                                                                                                                                                                                                                                                   'PROGRESS\': (\''+pb_c+'\', \''+in_c+'\'),\n    \'BORDER\': '+str(bor_w)+',\n    \''
                                                                                                                                                                                                                                                                                                                                            'SLIDER_DEPTH\': '+str(sl_bor_w)+',\n    \'PROGRESS_DEPTH\': '+str(pb_w)+'}\n\n'
                                                                                                                                                                                                                                                                                                                                                                                                                     'sg.ChangeLookAndFeel(\''+name+'\')\n\n')
                # Dark and Light modes implementation.
                if window_1_values['dark'] is True:
                    bg_c = str(dark_list[0])
                    txt_c = str(dark_list[1])
                    txt_in_c = str(dark_list[2])
                    in_c = str(dark_list[3])
                    scr_c = str(dark_list[4])
                    bt_txt_c = str(dark_list[5])
                    bt_c = str(dark_list[6])
                    pb_c = str(dark_list[7])
                    theme = theme + str('# Custom '+name+' - Dark LookAndFeel Theme.\n# Generated using LookyFeely.\n#import PySimpleGUI as sg  # Please change \'sg\' to your liking.\n#sg.LOOK_AND_FEEL_TABLE[\'' + name + 'Dark\'] = {\'BACKGROUND\': \'' + bg_c + '\',\n#    \'TEXT\': \'' + txt_c + '\',\n#    \'INPUT\': \'' + in_c + '\',\n#    \'TEXT_INPUT\': \'' + txt_in_c + '\',\n#    \'SCROLL\': \'' + scr_c + '\',\n#    \'BUTTON\': (\'' + bt_txt_c + '\', \'' + bt_c + '\'),\n#    \'PROGRESS\': (\'' + pb_c + '\', \'' + in_c + '\'),\n#    \'BORDER\': ' + str(bor_w) + ',\n#    \'SLIDER_DEPTH\': ' + str(sl_bor_w) + ',\n#    \'PROGRESS_DEPTH\': ' + str(pb_w) + '}\n\n#sg.ChangeLookAndFeel(\'' + name + 'Dark\')\n\n')
                if window_1_values['light'] is True:
                    bg_c = str(light_list[0])
                    txt_c = str(light_list[1])
                    txt_in_c = str(light_list[2])
                    in_c = str(light_list[3])
                    scr_c = str(light_list[4])
                    bt_txt_c = str(light_list[5])
                    bt_c = str(light_list[6])
                    pb_c = str(light_list[7])
                    theme = theme + str('# Custom '+name+' - Light LookAndFeel Theme.\n# Generated using LookyFeely.\n#import PySimpleGUI as sg  # Please change \'sg\' to your liking.\n#sg.LOOK_AND_FEEL_TABLE[\'' + name + 'Light\'] = {\'BACKGROUND\': \'' + bg_c + '\',\n#    \'TEXT\': \'' + txt_c + '\',\n#    \'INPUT\': \'' + in_c + '\',\n#    \'TEXT_INPUT\': \'' + txt_in_c + '\',\n#    \'SCROLL\': \'' + scr_c + '\',\n#    \'BUTTON\': (\'' + bt_txt_c + '\', \'' + bt_c + '\'),\n#    \'PROGRESS\': (\'' + pb_c + '\', \'' + in_c + '\'),\n#    \'BORDER\': ' + str(bor_w) + ',\n#    \'SLIDER_DEPTH\': ' + str(sl_bor_w) + ',\n#    \'PROGRESS_DEPTH\': ' + str(pb_w) + '}\n\n#sg.ChangeLookAndFeel(\'' + name + 'Light\')\n\n')
                # I decided to add a progress meter for the code generation because... why not?
                prog_l = [[sg.Text('Please wait...')],
                          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')]]
                prog = sg.Window('Generating Theme...', prog_l, location=window_1_c)
                for i in range(10000):
                    prog_e, prog_v = prog.Read(timeout=0)
                    try:
                        prog_location = prog.CurrentLocation()
                    except _tkinter.TclError:
                        break
                        pass
                    if prog_e is None:
                        prog.Close()
                        break
                    prog['progbar'].UpdateBar(i + 1)
                sg.PopupOK('All done!', 'Your theme code is ready.', location=prog.CurrentLocation(), auto_close=True,
                           auto_close_duration=5)
                prog.Close()
                # Dole out the code for the user's harvest.
                output_window_layout = [
                    [sg.Text('Code for '+str(name)+' Look and Feel theme.')],
                    [sg.Text('Please copy and paste the code below into your source code.')],
                    [sg.Text('This output is directly modifiable.')],
                    [sg.Multiline(default_text=theme, key='output', size=(70, 8))],
                    [sg.Button(' Exit ', key='Exit'), sg.Button(' Preview Theme ', key='preview')]
                ]
                try:  # I've found that these 'weirdly positioned' try and except blocks stop all error breaks.
                    output_window = sg.Window(title=('Look and Feel Theme - '+str(name)), layout=output_window_layout,
                                              grab_anywhere=False, element_justification='center',
                                              location=window_1_c)
                except _tkinter.TclError:
                    break
                    pass
                while True:
                    output_window_events, output_window_values = output_window.Read()
                    if output_window_events in (None, 'Exit'):
                        output_window.Close()
                        break
                    if output_window_events in 'preview':
                        try:
                            user_output = output_window_values['output']
                            if user_output == theme:    # This guy here and his alternate allow for
                                exec(theme)             # on-the-fly editing of the theme code even from the
                            if user_output != theme:    # output panel.
                                theme = user_output     # Tried and tested :).
                                exec(theme)             # Nifty as ever for adjusting the background color in a pinch.
                    
                            # Let's give 'em a feel of their custom theme.
                            previewtimer = 60
                            preview_layout = [[sg.Text(' '*40), sg.Text('Theme Preview')],
                                              [sg.Text(' '*19),
                                               sg.Text('This is how your theme will look when used.')],
                                              [sg.Text(' '*5),
                                               sg.Text('This window serves no other purpose than being a mannequin.')],
                                              [sg.Text('Only the exit button works.')],
                                              [sg.InputText('...just a textbox', size=(60, 8))],
                                              [sg.Multiline('This is just a Multiline element. Play with it as you '
                                                            'deem fit.\n\nHave some Latin too.\nLorem ipsum '
                                                            'dolor sit amet, consectetur adipisici elit, '
                                                            'sed eiusmod\n tempor incidunt ut labore et dolore magna '
                                                            'aliqua. Ut enim ad minim\n veniam, quis nostrud '
                                                            'exercitation ullamco laboris nisi ut aliquid\n ex ea '
                                                            'commodi consequat. Quis aute iure reprehenderit in '
                                                            'voluptate\n velit esse cillum dolore eu fugiat nulla '
                                                            'pariatur. Excepteur sint\n obcaecat cupiditat non '
                                                            'proident, sunt in culpa qui officia deserunt\n mollit '
                                                            'anim id est laborum.', size=(58, 5))],
                                              # Yeah, that's Latin. Copied obviously.
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
                                preview.Close()
                            # Change back to the previous LookyFeely theme.
                            sg.ChangeLookAndFeel(random_theme)
                        except:
                            sg.ChangeLookAndFeel(random_theme)
                            sg.Popup('An error occured! Please check your entries! You may have typed in an '
                                     'unsupported character or put in a wrong color value format.', title='Error!')
                            if DebugMode is on:
                                Print('Error!')
    
    if window_1_events is 'preview':
        sg.preview_all_look_and_feel_themes(columns=3)
    
    if window_1_events is 'update':  # This one was longer than expected. Phew.
        confirmation = sg.Window('Are you sure?', layout=[
            [sg.Text('You chose to update PySimpleGUI.')],
            [sg.Text('Are you sure about this?')],
            [sg.Button('I\'m Sure.', key='Sure'), sg.Button('Cancel', key='Cancel')]
        ], element_justification='center', location=(window_1_c[0]+90, window_1_c[1]+90))
        while True:
            conf_e = confirmation.Read()[0]
            confirmation.NonBlocking = True
            if conf_e in (None, 'Cancel'):
                confirmation.Close()
                break
            if conf_e is 'Sure':
                cmd('python -m pip install PySimpleGUI --upgrade --no-cache')
                confirmation.Close()
                break
    
    if window_1_events is 'col_name_view':
        color_names = []
        for j in color_names_list:
            color_names.append(([sg.Text(text=(str(j)),
                                         size=(20, 1),
                                         text_color=sg.LOOK_AND_FEEL_TABLE[str(random_theme)]['TEXT_INPUT'],
                                         background_color=sg.LOOK_AND_FEEL_TABLE[str(random_theme)]['INPUT']),
                                 sg.DummyButton('', disabled=True,
                                                button_color=('#000000', str(colour.Color(str(j)).get_hex_l())),
                                                size=(10, 1))]))
        
        viewer_layout = [
            [sg.Text(text=('These are the names of '+str(len(color_names))+' valid color names.'))],
            [sg.Text('Just for reference.')],
            [sg.Text('Ranked from darkest to lightest.')],
            [sg.Column(layout=color_names, size=(250, 200), scrollable=True, vertical_scroll_only=True, background_color=sg.LOOK_AND_FEEL_TABLE[str(random_theme)]['INPUT'])],
            [sg.Button('Exit')]
        ]
        viewer = sg.Window('Valid Color Name List', layout=viewer_layout, location=(window_1.CurrentLocation()[0]+60, window_1.CurrentLocation()[1]+100))
        while True:
            viewer_e = viewer.Read()[0]
            viewer.NonBlocking = True
            if viewer_e in (None, 'Exit'):
                viewer.Close()
                break
    
    if 'checkout' in window_1_events:
        # I don't want to go importing this big dog if I'm not going to use him.
        from webbrowser import open_new_tab as hyp_lnk
        if window_1_events is 'checkout_me':
            hyp_lnk('https://www.github.com/definite-d/')
        if window_1_events is 'checkout_lookyfeely':
            hyp_lnk('https://www.github.com/definite-d/PSG-LookyFeely/')
        if window_1_events is 'checkout_psg':
            hyp_lnk('https://www.github.com/PySimpleGUI/PySimpleGUI/')
    
    if window_1_events in (None, 'Exit', 'Cancel'):  # The customary exit route.
        try:
            output_window.Close()
            preview.Close()
            window_1.Close()
            break
        except(Exception):
            pass
            break
    
    if DebugMode is on:
        Print(window_1_events)
        Print(window_1_values)

'''

This code is distributed under the...

:::          ::::::::   :::::::::   :::          ::::::::
:+:         :+:    :+:  :+:    :+:  :+:         :+:    :+:       :+:
+:+         +:+         +:+    +:+  +:+                +:+       +:+
+#+         :#:         +#++:++#+   +#+             +#++:   +#++:++#++:++
+#+         +#+   +#+#  +#+         +#+                +#+       +#+
#+#         #+#    #+#  #+#         #+#         #+#    #+#       #+#
##########   ########   ###         ##########   ########

...license.

(I made my own!!! Whooo!)
'''
# Well, that's all people. PyCharm helped. Nothing more than a 'weak warning' came up.
