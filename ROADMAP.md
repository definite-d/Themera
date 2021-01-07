# Coming Soon to ~~LookyFeely~~ Themera: 
This document is a normal roadmap, and topics listed here will be deleted after a month or two after the feature or topic has been dealt with.

## A name change (Already here)
I think it's time to change the name of this project. Honestly, "LookyFeely" doesn't sound right. If anything, it probably sounds weird. It's my fault for naming it that, I know. With that in mind, the "LookyFeely" project has come to an end, to be continued under the name of *Themera*.

## Theme modifier (Done! Coming in Themera v1): 

Paste pre-existing theme code from anywhere, click a button and use it as new input for Themera. Expected to feature Python's exec function, so mind the code you paste.

## Handle more than just themes: (*Probably* coming in Themera v1.1)

Themera will get the ability to take care of most styling-related parameters by generating the `SetOptions()` function of PySimpleGUI. Yes, icons will be taken care of too. Wouldn't it be nice to send in a filepath to your .png/.ico/.icns file and not only have your theme possibly fashioned after it, but also have it set as your program icon automatically and even converted to a bytestring?

## GitHub filesystem changes (Done! Coming in Themera v1): 

Rather than having everything about the Themera project exposed on the first page, a compiled executable will be made available instead, as expected of a desktop app. The source code and other things will be tucked into deeper directories. PyInstaller will be used for compiling, as usual. The main caveat here is; I'm a Windows user, so Mac and Linux support looks bleak. This _is_ an open source project though, so perhaps someone could volunteer to provide builds for those OSes or just compile the source yourself with PyInstaller or cxFreeze.
