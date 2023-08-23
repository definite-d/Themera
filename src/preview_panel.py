"""
d888888P dP
   88    88
   88    88d888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b.
   88    88'  `88 88ooood8 88'`88'`88 88ooood8 88'  `88 88'  `88
   88    88    88 88.  ... 88  88  88 88.  ... 88       88.  .88
   dP    dP    dP `88888P' dP  dP  dP `88888P' dP       `88888P8

Themera Preview Panel Class File
PySimpleGUI Theme Code Generator
Copyright 2023 Divine Afam-Ifediogor
"""

from tkinter import Canvas
from typing import Tuple

import PySimpleGUI as sg
from colour import Color
from PIL import Image
from PIL.ImageTk import PhotoImage

from .constants import IMAGE_PREVIEW_SIZE
from .fonts import FONTS


class PreviewPanel:
    """
    This class handles the functionality behind the way the preview panel (for selecting images) works,
    and acts as a validator for said images, since if it previews, it'll work for our purposes.
    """

    def __init__(self, element: sg.Canvas, fg: str):
        self.canvas_element: sg.Canvas = element
        self.canvas: Canvas = self.canvas_element.TKCanvas
        self.size: Tuple[int, int] = IMAGE_PREVIEW_SIZE
        self.center: Tuple[int, int] = tuple((self.size[0] / 2, self.size[1] / 2))
        self.fg: str = fg
        self._clear: PhotoImage = PhotoImage(
            image=Image.new("RGBA", size=IMAGE_PREVIEW_SIZE, color=(0, 0, 0, 0))
        )
        self.image: int = self.canvas.create_image(*self.center, image=self._clear)
        self.directive: int = self.canvas.create_text(
            *self.center,
            text='Click "Browse" to select an image.',
            font=FONTS["medium"],
            fill=self.fg,
        )

    def set_directive(self, value: str):
        self.canvas.itemconfig(self.directive, text=value)

    def set_image(self, tkimage: PhotoImage):
        self.canvas.itemconfig(self.image, image=tkimage)

    def clear_directive(self):
        self.set_directive("")

    def clear_image(self):
        self.set_image(self._clear)

    def preview(self, filepath: str):
        try:
            img = Image.open(filepath).convert("RGBA")
        except FileNotFoundError:
            self.clear_image()
            self.set_directive('Click "Browse" to select an image.')
        except UnidentifiedImageError:
            self.clear_image()
            self.set_directive('Invalid Image.\nClick "Browse" to select an image.')
        except OverflowError:
            self.clear_image()
            self.set_directive(
                'There was a problem loading that\nimage. Click "Browse" to select\nan image.'
            )
        except (ValueError, TypeError):
            self.clear_image()
            self.set_directive(
                "An error occurred while trying\nto process the image. Please try"
                '\na different one. Click "Browse" to\nselect an image.'
            )
        else:
            global thumbnail
            thumbnail = img.copy()
            thumbnail.thumbnail(IMAGE_PREVIEW_SIZE)
            thumbnail = PhotoImage(image=thumbnail)
            self.set_image(thumbnail)
            self.set_directive("")
            return img
