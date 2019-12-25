# Welcome...
# ... to the code of LookyFeely.
# https://www.github.com/definite-d/Looky-Feely/

version = 'v2.1.9.3'

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

wow... i typed that by hand.
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
sg.SetGlobalIcon('icon\\lf_ico.ico')  # Had no befitting icon. So I made one :)...

# Random color generator.
def random_color():
    h = str('#')
    color = ''
    for i in range(6):
        color = color + str(rc([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                'a', 'b', 'c', 'd', 'e', 'f']))
    color = str(h + color)
    if DebugMode is on:
        print('Randomly Generated Color: ' + color)
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
color_names_list = []
for i in colour.RGB_TO_COLOR_NAMES:  # I refuse to type all 450 color names in here. By hand.
    for j in colour.RGB_TO_COLOR_NAMES[i]:
        color_names_list.append(str(j))

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
        unsupported_entry = False
        no_name = False
        if window_1_values['name'] is '' or window_1_values['name'].isspace() is True:
            sg.Popup('You didn\'t specify a name for the theme!', title='Warning: No Name!', button_type='Cancel',
                     location=(window_1_c[0]+90, window_1_c[1]+50))
            no_name = True  # What masterpiece didn't have a name?
        for i in window_1_values:
            if '_c' in i and window_1_values[str(i)] not in ('...color value', 'None') and window_1_values[str(i)] not in color_names_list and window_1_values[str(i)].startswith('#') is False and window_1_values[str(i)].isspace() is False and window_1_values[str(i)] is not '':
                sg.Popup(('The color name '+str((window_1_values[str(i)]))+' is not supported.\nYou should use the hex value of the intended color instead.'), title='Warning: Unsupported Color!', button_type='Cancel',
                         location=(window_1_c[0] + 40, window_1_c[1] + 50))
                unsupported_entry = True  # To avoid unforeseen error-stances.
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
                        selected.append(color_values.index(o))
                sel_colors = selected
                sel_colors1 = []
                for s in sel_colors:
                    if sel_colors.count(s) > 1:
                        for n in range((sel_colors.count(s) - 1)):
                            sel_colors.remove(s)  # Removing the duplicates...
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
                                    for i in sel_colors:
                                        i = color_values[i]
                                        sel_colors1.append(i)
                                    sel_colors = sel_colors1
                                    del sel_colors1  # It was a disposable variable. So disposed it is.
                                    sel_colors_shades = []
                                    number = -1*(8//(-1*(len(sel_colors))))  # Phew. What a number.
                                    number = int(number)
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
                                            if colour.Color(sel_colors[0]).luminance > 0.5:
                                                other_shade = colour.Color('black')
                                                signal = 'black'
                                            if colour.Color(sel_colors[0]).luminance < 0.45:
                                                other_shade = colour.Color('white')
                                                signal = 'white'
                                            else:  # Yeah.
                                                other_shade = colour.Color(i)
                                                other_shade.set_luminance((other_shade.get_luminance())/2)
                                                signal = 'depends'
                                            print('Other shade:', other_shade)
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
                                    if len(sel_colors) is 1:  # I found that pure mono themes need this little spice-up.
                                        if signal is 'white':
                                            shade_list = [sorted_list[1], sorted_list[5], sorted_list[0], sorted_list[5],
                                                          sorted_list[3], sorted_list[0], sorted_list[7], sorted_list[6]]
                                        if signal is 'black':
                                            shade_list = [sorted_list[0], sorted_list[6], sorted_list[7], sorted_list[1],
                                                          sorted_list[3], sorted_list[1], sorted_list[6], sorted_list[6]]
                                        if signal is 'depends':
                                            shade_list = [sorted_list[0], sorted_list[7], sorted_list[7], sorted_list[2],
                                                          sorted_list[3], sorted_list[7], sorted_list[0], sorted_list[6]]
                                    else:
                                        if selected[0] is not 0:
                                            shade_list = [sorted_list[6], sorted_list[0], sorted_list[7], sorted_list[1], sorted_list[5], sorted_list[7], sorted_list[0], sorted_list[3]]
                                        else:
                                            shade_list = [sorted_list[0], sorted_list[1], sorted_list[7], sorted_list[1], sorted_list[5], sorted_list[0], sorted_list[7], sorted_list[3]]
                                        print(shade_list)
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
                            color_values[color_values.index(i)] = str(i).capitalize()
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
                                    print('Error!')
    
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
                cmd('python -m pip install PySimpleGUI --upgrade')  # What did the chick say to the Python? Pip!
                confirmation.Close()                                # And it got eaten for such a terrible joke.
                break
    
    if window_1_events is 'col_name_view':
        color_names = []
        for j in color_names_list:
            color_names.append(([sg.Text(text=(str(j)), text_color=sg.LOOK_AND_FEEL_TABLE[str(random_theme)]['TEXT_INPUT'], background_color=sg.LOOK_AND_FEEL_TABLE[str(random_theme)]['INPUT'])]))
        viewer_layout = [
            [sg.Text(text=('These are the names of '+str(len(color_names))+' valid color names.'))],
            [sg.Text('Just for reference.')],
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
        print(window_1_events)
        print(window_1_values)

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
# Well, that's all people. Just over 560 lines total. Comments included.
# PyCharm helped. Nothing more than a 'weak warning' came up.
