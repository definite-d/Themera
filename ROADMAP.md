#Coming Soon to LookyFeely: 

##Theme modifier: 

Paste pre-existing theme code from anywhere, click a button and use 
it as new input for LookyFeely. Expected to feature Python's exec function, so mind 
the code you paste.

##Handle more than just themes: 

LookyFeely will get the ability to take care of most 
styling-related parameters by generating the `SetOptions()` function of PySimpleGUI. 
Yes, icons will be taken care of too. Wouldn't it be nice to send in a filepath to 
your .png/.ico/.icns file and not only have your theme possibly fashioned after it, 
but also have it set as your program icon automatically and even converted to a 
bytestring?

##GitHub filesystem changes: 

Rather than having everything about the LookyFeely 
project exposed on the first page, a compiled executable will be made available 
instead, as expected of a desktop app. The source code and other things will be 
tucked into deeper directories. PyInstaller will be used for compiling, as usual. 
The main caveat here is; I'm a Windows user, so Mac and Linux support looks bleak. 
This is an open source project though, so perhaps someone could volunteer to provide 
builds for those OSes or just compile the source yourself with PyInstaller or 
cxFreeze.
