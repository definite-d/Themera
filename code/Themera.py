# Welcome...
# ... to the code of Themera.
# https://github.com/definite-d/Themera/
version = __version__ = 'v1.0.0'

'''
888888888888 88
     88      88
     88      88
     88      88,dPPYba,   ,adPPYba, 88,dPYba,,adPYba,   ,adPPYba, 8b,dPPYba, ,adPPYYba,
     88      88P'    "8a a8P_____88 88P'   "88"    "8a a8P_____88 88P'   "Y8 ""     `Y8
     88      88       88 8PP""""""" 88      88      88 8PP""""""" 88         ,adPPPPP88
     88      88       88 "8b,   ,aa 88      88      88 "8b,   ,aa 88         88,    ,88
     88      88       88  `"Ybbd8"' 88      88      88  `"Ybbd8"' 88         `"8bbdP"Y8

See the GitHub repo for more details.

'''
# Development began on 29/11/2019, bare minimum was completed on 1/12/2019.
# ===================================================================================
# ___...:::---=== Code Starts Here. ===---:::...___

# Necessary import calls.
from Loc8 import Locator
from os import getcwd as cwd
from os import getlogin as user
from os import system as cmd
from os.path import getsize as filesize
from os.path import isfile
from PIL import Image as img
from PIL_supported_image_types import rw_types
from pyperclip import copy
from PySimpleGUI import Print as Print
from random import choice as rc
from random import shuffle as rs
import _tkinter
import colorpiq
import colour
import PySimpleGUI as sg  # I'm calling it 'sg' to comply with the PySimpleGUI Docs.
import shelve

# User preferences.
prefs_path = f'{cwd()}/themera_config.themera'

preferences_file = shelve.open(prefs_path, writeback=True)

def theme_switch_registrar(theme_switch):
	'''This function creates and edits the theme switch shelve registry.'''
	preferences_file['theme_switch'] = f'{theme_switch}'

def check_theme_switch():
	theme_switch = None
	try:
		theme_switch = preferences_file['theme_switch']
	except KeyError:
		theme_switch_registrar('Themera Light Mode')
		theme_switch = preferences_file['theme_switch']
	return theme_switch

theme_switch = check_theme_switch()

# Icons
themera_img = b'iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAIAAAEMHXM7AAAABnRSTlMA/wD/AP83WBt9AAAACXBI\nWXMAAFxGAABcRgEUlENBAAAgAElEQVR4nO3dzY7cVBoGYLfUCkizQkLKLNgigWbZ18FcBuy4CC4h\nO7gNriNLlEizRSMhIc0KiWTTU4kTx+3yX9nHPsf+nmcBnXSn2q5z3u+zXf65f3x8rJ66u7urSnW9\ntPftP3xa9Ief91mgWzVL2KzJ/ZPvlbrcn3xcwsvS1utw3/z5AEvf9vBzvQ7vVuB4S197vw734z/z\n7K/frv/y7eu/t1miYQ8PQ9+5H6o5vYv+4VvffN58vdPKvHz57r99q/F+BK7mz8jSd39yxso8Pv5y\nd/f9zBccc1mNq3XomULzl777D1srU31cn8vSL3u1flfrMJGBNRIv+oDuCix++9vevHrRfdnNYrPh\nCAy5rMyqdXg6izKsQFpWIDcrkNsBVuD5d1/VX/zx6+/X3y10BZqF7vzl9TqUtQK9y935gc465F+B\nyYUel20FFi/3u0H476c/5lmBznbrGvmn0EppVuB683POD/zz3z+t/9VGIDcrkFuaFfjs2x/bf7yO\nbOcHLr74+sskv9oI5GYFcsu2Av/7z59JcmwEcrMCuVmB3KxAblYgNyuQW84VSLI9ZwRy22kFLrv5\nnf364+3UN+tQf0j8x+vflx2gfvf5wMPz5o+7TqHrwy31SSBrPiLYZAUu7/Tk4d625kOXyTUp/SOm\nevmGVuPD0o+frfL2H/9af77HZZZf5sbis1V6B6T3I8oq+Qi0z+JYsw61OVOrZwUWDMLQ2Sd1RodW\nY/5pXJ/e/uszth4fH6/PWpy/DnNOnElzvlk1cs5cn8s61F8Mrcl+5y4On7JYzclAsyZXr7tscdJ5\n+UNVr0DvLDqED2fuVodbh/fv/ZNzp6tmHQ7i09nr57l+4MlylzmXXv4weP3Ah2+UudyNZvHer8mn\nDBxj6dsui/pxHe4//dWxvF+H6sPp9wNLn78HN3qb8cgFEOMbQuVdP/DUTZuixV0/sGZv5npldjgD\nf6tdysvK3LRbPNc+F0CMXD+QPDPpV2D8jV978cCVso5KLGAFcjvgNTRPGYGNTR6cK3QF5h+vLmgF\nFlw8UJWwAjd9ONA5977KtQIrL3poyz8CK1mB9xZcP5Dk4oHKCORnBXJLf/1Ab6D7rh9I8puNQHZW\nIDcrkJsVyM0K5GYFlnIZ1gdWIDcrkJsVyM0KXJl55vfBrh/oXDxQrbh+oGPXCyA6f7Pg4oHO1Q9V\n3gzUZ7GsuXigKirE89ekbZMVWHnifbbrB9JePFC1LugYO/2+uxCLruDo/eS9OUurd02WXDzQZ+0F\nEIVeP1DQxQPV8PUD9WmX4+etl3vxwHutE18va3Osc1/fv/3VkwsgDrQO19cP1H8o+cT7tvZJ+D3X\nDzSOsj6HMPQ+91TRA1wIcTh9V27UngxA+Q+wOKqnV55UgxfQVN76jdVvb/8FQJV3fy89FzBVc9/9\nJNeqr3yF0o1eOvzxZz6MweDzTzqSPBPiw0sN3Oz4PAMzfLXVtVmX8CV898d+y/BdqMfHpjlakGyv\nO4l5wzB9PGifd39iGa7GZpNru7bQd9Fe28QAlPDut01e2lV/caBqVtAx6RG3zvfrxOQcktEQHGMA\nTswAZGYAMjMAmUUZgOTXvqcSZQB2MP6YsSEGYInxkzfq784cBgMwbdlpWL0Xa18zAE8kvCy7mheF\nuAOQ9r0e/0Wda/7bAg3AZUMo1XmpCQUagDIZgMwKGoD1h/hnvkKqW1ckUdAAxGQAMjMAmRmAzAoa\ngOt7xDRmdteRV2iUtitQ0ADEZAAyMwCZGYDMwg1AqhuepBJuAEpjADIzAJkZgMwMQGYRB6CoDaGI\nA1AUA5CZAcjMAGRmADIzAJkFHYBytkSDDkA5TjUAzT0+D+QYAzDznrDV6Bi8ff33bmdEz3eMAbjJ\nnKFacOfYxa5vOdt2wgGYo3Pn20baITnVFTLzq9BMvc/QTjgkJ7xGLPkYzNF5H+eMR/etX3O3lGU3\nA06rc1fkapenqA8Zj8hNF6jWphOw/xhMXlE9fmPnmVLd3WniTZ97w6bR++bWtzDebhgWX8Ne1i2y\nOmbesuzDjYtnmLwn9nxl3jUgjXnve6NVgmbfPHrwnt7zlXH375w+3v+6dffu6oA3IT+osbuP1/dV\nNwwb+Xjb+u6ti9t/+2kYKiORQvNmvjd28+7rn3AH+yRGnhEw9vyAhmFYZs57O7Yj5n1faeiZAW39\nA9Dz1msGN3la9zvPDGjrDoDHZ6TRfus+DkbzzIC2gSdoVN79dD4+tKHqi8KnAfAYh229f2BA/WU7\nCh5hsqNWFBr3PT/B9gaeIcMOPtaihc+QIYFWP5j7DJmOmz4SOPPR/8aNHwM0Zj1Dpm3BpzGdxymc\nczzqJ8ZUt43Eu6cozf/pVB9JtsfjhIMx8xFKH6vQ3AHY6APh0w7G1LN7GrMGYP/HWN06GPXpEWV9\nRj9vDAp9jNX8wch4jlASBzgzbmgwDvDWzwjBwZ4j1gzGYR7kNuUACeg42Fu/8kl6RZl86z1Jb0M3\nTfwDbd0eYwDWlJ1in59UO8YAnJgByCzEAJRchUIMQMkMQGYGIDMDkJkByMwAZGYAMjMAmRmAZDzQ\nOYPeW0fMfJJwzQAskfCuNlEGYP3hoJve9PkhiDIAiy2e7B5pvspud5czAJ8kf9PnhMAAbDvZxx8o\nX4UdgHLuXxlrAMp53xuBBqDAd78KNQBlMgCZGYDMDEBmpQxAknOe57zIP//90/pflFApAxCWAcjM\nAGRmADIzAJkZgMwMQGYGIDMDkFkpAzD+ALaZ+8mTT3Er5PGFbaUMQFgGIDMDkFmsASjnKbaNWANQ\nIAOQmQHIzABkZgAyMwCZGYDMDEBmBiAzA5CZAcjMAGQWbgBKOx4XbgBKYwAyMwCZGYDMDEBmBiAz\nA5CZAcjMAGRmADIzAJkZgMwiDkBRx+MiDkBRDEBmBiAzA5CZAcjMAGRmADIzAJkZgMwMQGYGILNw\nA1DOUaDaqQbgzasXQ3crePv6b3fO3UN9V4n2MDQPzmjuJF/USJxtAGqTN/e4u/u+2mUk3o36w/OR\nHzjGAFxmdJIbizYeH3+5jMHWmfAIk7kyVicD8EQ9EkmGwVOUJtRVqPdb6wNxwge5JW8DcywbidM+\nyjDLGNTmj8RN7351oAFY+Ry8VBI2idrEALz9x7+e/fVbql+2QOd9r6v2pXxnWpwPhgLRM/0fHsZf\nqtwEjEz5yzCsH4OhDnyT9kjcWnxq0wOwcwhmlppCotDof/enpn9VVAIWVPllw5Bk7k+b8e5XMwdg\n0xCs7647vaHbmJuALcagkA2b9ObN/drHAXj5Q/Xw8/iPXsbg8t8kw3Dat76a/e5f3vD37h8fH+/u\n7ua/fj0MjZvG45zv+y3zvePy5q9twp3xmLB8Uc/l4/SvnvSAGVWIhC7Tv6oH4FMVMgY7aE3/qknA\nrZ2AhT6++/X0r3o2Q+ufkIMtXL37VXsAnoRALUqu792vOgmov/epH1SikEKr6Hfe/ap3T7gbBRK5\nfveroUMRT6LAar1vfe1+5HuTjBAlWDOHbz4SYdJTms6cvCkPswIwMeltqJJL3zZ6M13nJGEiAP1T\n34ynEJ2p+DQPc5IwGICeqW/eU7hmivYlYe5RCFOfw+tLwmViTx8H7c5+U59Du0zgpxmohj4Kq8x+\nTqmexgOt4L79t91/A6dx1Qo+nY9Vmf1E0JeB+2qXz7Z2vr7vnCdfR7PiZPPh1/y5/4TQJz+RSMaL\nWp998/nQt2TjMF6+/PT1FmF4X/rvtyj/ea/nHjeUDcEoWhOG9Ul42gTuu99bp+SpP66cYNRXOh/6\nctsN1UlI1xCSXRt/3Kk/bp+tqXLusnAM6WKQJgBnnf3j1jcN836VSwxWZyBBAGLO/hGTwTDvk1md\ngbUBMPtnynV3QcatCoDZP2nxvK/biGNT09Y1gYJuEHcmqep9OcemzkoAUtptO6c3GFKxgAAkYys/\nmxVbQQJAaAJwHpftIltBtxIAQhMAQhMAQhMAQhMAQhOAU3Eg6FYCQGgCQGgCQLma52EvexbzHAJA\nKTqPf+98a6MMCAAZjMz1kX+yRQYEgG0tmOvjL5U2BgJwNhmPhCac6+O/JWEGBIAl9pnr4789SQwE\ngAl55/qIJK1AAPik2Lk+ZH0GBCCow831IR82h/678J8LQAinme7JCcAJPfvm8y++/jL3UhyDABCa\nABCaABCaABCaABCaAHQVcofDhIvxz3//lOqlzkcACE0ACE0ACE0ACE0ACE0ACE0ACE0ACE0ACE0A\nuj779sdl/zDtR8iLF6PNVQGTBIDQBIDQBIDQBODM/vefP+0GjBMAQhMAQhMAQhMAQhMAQhOAk3Mg\naJwAEJoAEJoAEJoAEJoAEJoAnJ8DQSMEgNAEgNAEgNAEgNAEgNAEgNAEIARHQocIAKEJAKEJAKEJ\nAKEJAKEJQBQOBPUSAEITAEITAEITAEITAEITAEITgEAcCb0mAIQmAIQmAIQmAIQmAIV68+pFkmdl\n1+z7DhGAZC7zNe3D4ldmwKSfQwCKVidqZgzevv67/cc/Xv9++e/z777aYsFOQwAOoNNYmjx0Zvy1\nx8dfmq/v7r6vvzhfJP749ffq4fmyfysAx7NsQ6sOwyUG76ZLy6Hz0FmXBQQgpeS7AcldYtC0gtr1\nHDpEJNZP/ZoAhHOdgY7yW0Sq2V8JQHLlN4FbFdUiEk79mgCkV34GJpvAuFwtYnD2Pzwsfk0B2ET5\nGUhohxaRvPA3VgXg7T/+9eyv31Itypm8ff13XWLbByLjSBuJ7WZ/pQOkMnRI/hKDmBnoWLbVNGvq\nr9j+qdYHIGwTmPwQqtFsbUtCY06L2LTwNxJ0gDgZmD/pe5WThDV7wBtZMt3X1f5amk2gs2Zg5Ywf\n0p5/+4ehwNm/RIrZX3UD8PKH6uHnZS90ycDlv0ePwUYzfsTIdFyWjZPM73GJZn+VfCf4cDHYf8bP\nF2Iq3yTdvG/cPz4+3t3dpX3ROgZVkUkoecbTL+28v2zmtFx1gBVbQdeaJNSy5MGMP6QNiv21S/W/\nr//3pAkkzUBbJw872eOd5CCelv+q6QC7ZQCyeTr7L3O+am8CyQBn1jf7q84+QE8GLsSAQxuY+rXu\nTnD9ba2AM7ja4u/M/mroc4D+VlDpBhzEjKlfG/wgrKcVVJJAwa4mfW1o6tcmPglu/vFgEhoiwc4G\nZnxtfN435p4KMZiEeUsD+5g57xs3nwt0/QuSn0kB89064zvuV/77hhiwp1TzdtXZoCY9ubTn3pow\nLAmAeU9R6gm5LAa3BcDUp1jLYjA3ADdMfcdD2c7UwcZbYzArABOz34xnN53JNpCH+TGYDsDg7Dfv\nya6ZhH1JuEzdyQyMBcDU5zDqOXkVg8kMDAagf/ab+pTsMj9vzEB/AMx+jqqvFYxkoCcAZj+Hd9UK\nhjIw4yiQqc8RzctANwDd8m/2c1wzMnDf+fYeiwW76dstbhvdBFL+OYGnGeg0gfv2N7r/DM7uQwDM\nfs5suAl4RBIxDOwM9AVA+efsmiZwXzn4QxB9TeCqA2xc/re7Q7rboJ/ELjdGrz42gZ32AXZ4MsCz\nbz5vvhaGA3v58sMXuyThftPtn1xPiBGGM6iTkDYGV1tBG3aAQp6PJAzHtkUMWp4GINEOQCFT/5ow\nHNUlBhtk4LL5k74DFDv7O9phqOShfNtkIHEAjjL7r2kOB7DB5lDKABx39ndkDEP9cGxPCN7Q0/3g\nZAE4zezv2DMMyx4NH07SbaE0ATjr7O/YLgym/m3SZcDJcAulCoOpv1CiDCQIQJDyP2JxGMz+7HSA\nxGYeXTX1E0jRBNYGQPkfd90cTP2i6AD7uYThzasXuZfiXFY3AQHYialfplUBsP0zh6lfMh1gW8tm\nf73n4IyMWdZtBQnAVtYXfqcn7UAA0ttim8e5qxsRgMT22eLXHFIRgGRy7ew2YZCEBZYHwCGgNod6\nDkoHIDQBIDQBIDQBIDQBIDQBIDQBIDQBIDQBIDQBIDQBOI9n33zudKBbCQChCQChCQChCQChCQCh\nCQChCQChCQChCQChCQChCQChCQDlev7dV5f//vHr79v9CgE4lXOcD1fP+/Yft8uAAFCEzqS//u5G\nGRAAchqf9zsQAPa2bNJv1AQEgJ2sL/ZbZEAA2FD2LZxJAkB628375E1AAEhjt2KfNgMCwCrlb+SM\nEwCWyDvvEzYBAWCuoop9qgwIABOKmvfJCQA9DjHpkzQBATibNefDHWLet63PgABEd7hJn5YABHWa\nef+uCfx3+T8XgEBOM+kTEoDzM+9HCMBpmfdzCMAJmfrzCQChCQChCQChCQChCQChCcAJ/e8/f37x\n9Ze5l+IYBIDQBIDQBIDQBIDQBKDrzasXuRch8TL8898/JXy1kxEAQhMAQhMAQhMAQhMAQhMAQhMA\nQhMAQhMAQhMAQhMAQhMAQhMAQhMAQhMAQhMAQhMAQhMAQhMAQhOArs++/XHBv0p7Fe+yZehwb6w5\nBOC03B9uDgEgNAEgNAEgNAEgNAEgNAEgNAEgNAEgNAEgNAEgNAEgNAEgNAE4M+fDTRIAQhMAQhMA\nQhMAQhMAQhMAQhMAQhMAQhMAQhMAQhMAQhMAQhOAk3M+3DgBIDQBIDQBIDQBIDQBIDQBIDQBIDQB\nIDQBIDQBIDQBIDQBIDQBOD/nw40QAEITAEITAEITAEITAEITAEITAEITAEITAEITAEITAEITgBCc\nDjREAAhNAAhNAAhNAAhNAAhNAAhNAAhNAAhNAAhNAAhNAAhNAAhNAKJwPlwvASA0ASA0ASA0AUjj\ns29/fPPqRe6l4GYCQGgCQGgCQGgCQGgCQGgCQGgCQGgCQGgCEIjz4a4JQInevHrx2bc/5l6KEASA\n0ASA0AQgEDsA1wQgBFN/iAAUKtV+sKk/TgDKtSYD5v1MAnA2b1///e5/X+dejoMQgKLVV5nN6QMf\n5v1Hf/z6e/3F8+++2mLBTkMADmB8W6gz9TvqJIjBEAFIZtPLgptXbpIwPu8vHh9/ab6+u/u+/uJ8\nSXiX8Ifni/+5ABzMsozVYbjE4GSbRs3qLCYAQZ0gCetnfyUAoVz6QLMt1DhBEtYQAD441u5ykvJf\nCUBa5d8eq7cJtB2iIaSa/ZUAMKTYJCSc/ZUABDTZBDqKTUISAsBcJewkpC3/lQAkV/5uwEoZG0Ly\n2V+tCcDbf/zr2V+/JVwUjmXnJGwx+ysdYAunbwIdOyRho9lfCcBGomWgdsTdZQEgvbS7y9uV/0oA\nNvL29d93d9+3z8csyq1HQpdJ0hCmZ//Dw+IXrwQgrc4pysVmYIfZ37Y4CZvW/tqqADgQ1Bg6O7/Y\nDGRR4E6CDrDK5FUplQz0mbOTMKv8r9v+qQRgsTlTvyEDvUYawg4bP7W1AYi2FXTTvG+rN7vFoFcn\nCbvN/ipJBwiSgcVTv62EVrDzHvBNbpv6q7d/KptAcySZ+g2tII0Us79KFYBTNoG0876jKcM7J6Hk\n8p9Fsg5wpgxsOvU79knC2eZ9ovJf2QRq23PeX7ueowsicbaJ3mvl7H/5Q/tPKQNw3CaQd+oPCTGb\nb5Wu9tcSd4BLBi7/PVAMypz69Es9+6uNNoHKbwXm/fFsMPsfHx+fBuCyefTwc5KXLrYVmPrHs8HU\nb2y7E1xOKzDvDyn51H+6B3xxf+kCd3d3iX9NS90KqnzdwNQ/ni1LfsdVB0i3FdTRJKGxaSTM+8PY\ncbq3XUp/lfdzgOtIpJTnXaVgV9s/VR2A7lbQZk0ASuOTYGJ4Wv7r7Z+qCYAmQEw6AAEMlP+qHQBN\ngHPq2/dtPOkAMsDZXM3+dvmvpjeBZIAT6cz+6joAPR8MywAHNbzp3+jpADLA4Y1u97f1bwLJAAfW\nN/t7y381sg/Qn4ELMaBkt8z+anwnuP9EUTGgTAObPSOzv5o8CjR4srQYUI5FU782/Ulw/SpjMagk\ngd1N7ebOmf3V/FMhJq6bmb3TDVubOfVrN5wLNNYKoAw3zf5qwclwYkCBbp33jYVngza/TxLIaPG8\nb9yvf4mVRAiIKXv53ft6GOUeoHZdD3duCZs3ABUfYKZOwdy6H2zVANR9gJWaQrpRJ0jcANbWfSfU\nAee26KzJjTpBmgawpO6r9UBAvaVvdldI2wlWNYCb676iD3CtXRvnNYMknWBhA7ih9Cv6APPd2Azq\narysDdzcAOaWfnUfYKWmkE51gmVt4IYGoPQD5FHX1dRtYG4DmK7+6j7ApubtEFzKdbLbwSn9AGWZ\n2iGYuSsw0QBUf4BCXcrvul2BwQag9AOUbt2uQH8DmKj+Sj9AOWa0gbkPBlb9AY5n9IhQbw/oNgDV\nH+CobuwB951vT7w0ACW7pQfct78x8aIAlG92D5h3IdgZq/+zv37LvQifvH39d+5FgMAeHnIvQWpT\nZ4jWPjSAsc3/A1b/oor7HM+++bz37zUG2MPLl9M/c7gmMdwDmp2A++r4T+86XLmfT2OAUlw3icO1\nhJa6B0wdAip48//EdX/SUGOo9AbYTdMSiu0EUweCRhtAedU/ctGfyU4D7K29c1BaMxjtAfdHOf6j\n9K+kMcAe6mZQWhvocyn+iR8Kn5y6vzVHkyC98o8OvVduA1D6s7PT0Hh8/KV6t8X0fe4F4WjK3iEY\nbgBZPwBQ/UsWpDHURR8SuLSBjD1g+GOA4vYAlP7jOsfRJHWfTRS5K1BWA1D9z6r8nQZ1nz3k3RW4\nUlADUP0DytsYFH0yKKkHFNEAlH46Nm0M6j6ZFXM4KH8DUP2Zb83HDOo+ZSlgVyB/A4AkenvDm1cv\n9l8SmCt3D8jcAGz+swV1H+bI2QBUf9JS9zmerDsBDgFxbIo+LJatAdj8Z40sdb/8qxk4pHw7AfYA\nOJIyt/fPcQk0AWkAlK7Moj+TnQZKpgFQqEPX/UkaAyXI0wB8AMCQc9f9SXVj0AbCyfQxgD0AgKA0\nAICgNACAoDQAgKA0ACjOs28+9zkwO9AAAILSAACC0gAAgtIAAILSAACC0gCgRE4EYgcaAEBQGgBA\nUBoAQFAaAEBQGgBAUBoAQFAaABTKmaBsTQMACEoDAAhKAwAISgMACEoDAFjl+Xdf/fHr77mXYgkN\nAMrlRKDSXGr90N8fsQdoAAA9hmr9yM8frgdoAEB0t9b6kdc5Vg/QAIBAUtX68dc/ShvQAIDT2rrc\nj/zeQ/QADQA4g1y1fsgheoAGABxMabV+SPmHgzQAKFrwM0GPUutHlLwroAEARThBrR9SbA/QAIC9\nnbjWDynzcJAGAGwoYK0fUdqugAYApKHWz1HUroAGANxMrV+pkF0BDQBKl/1EIOV+CyX0AA0A+ESt\n31P2w0EaAASl1hci466ABgDnp9YX7l0P+G+G36sBwKmo9cynAcBRqfWspAHAAaj1bEEDgAP433/+\n/OLrL3MvBWejAQAEpQEABKUBAASlAQAEpQEABKUBwDE4EYjkNACAoDQAgKA0AICgNACAoDQAJrx5\n9SL3IpSi2Lfin//+KfcicEgaAEBQGgBAUBoAQFAaAEBQGgBAUBoAQFAaAEBQGgBAUBoAQFAaAEBQ\nGgBAUBoAQFAaAEBQGgBAUBoAQFAaAEBQGgBAUBoAQFAaAEBQGgATPvv2xz1/XbHP3a12fytGfPH1\nl7kXgTPQAOB4/vefP/UA1tMAAILSAACC0gAAgtIAAILSAACC0gDgkJwIxHoaAEBQGgBAUBoAQFAa\nAEBQGgBAUBoAHJUTgVhJAwAISgMACEoDAAhKAwAISgMACEoDAAhKA4ADcyYoa2gAAEFpAABBaQAA\nQWkAAEFpAABBaQBwbE4EYjENACAoDQAgKA0AICgNACAoDQAgKA0AICgNAA7PmaAsowEABKUBAASl\nAQAEpQEABKUBAASlAcAZOBGIBTQAgKA0AICgNACAoDQAgKA0AICgNACAoDQAOAlngnIrDQAgKA0A\nICgNACAoDQAgKA0AICgNAM7DiUDcRAMACEoDAAhKAwAISgMACEoDAAhKA4BTcSIQ82kAAEFpAABB\naQAAQWkAAEFpAABBaQAAQWkAcDbOBGUmDQAgKA0AICgNgLJ89u2Pb169yL0UEIIGABCUBgAQlAYA\nJ+REIObQAACC0gAAgtIAAILSAACC0gAAgtIAAILSAGCuN69efPbtj7mXYi5ngjJJAwAISgMACEoD\nAAhKA4AbHOJjAIf+mUkDoDiF3xG6wB6g4rOMBgA3y94DVHyS0ABgiXofZbc2oOKzBQ0Altu0Dbx9\n/Xfz9R+vf29/6/l3X23xG4lGA4C1UrWBdsUf98evv3f+RktgAQ2AEhX+OXCvzgLP6QfzK/6kTkvQ\nDw7kw9g9PN//V2sAsImMDezu7nu7CEdxPVJ70gDgbB4ff6net4H2X9pFKE3e0l/TACjUEY8CFeXS\nBjo9oM0uQl4lVP9KA4ATG+8BHXYR9lFI6a9pAHBmN/WANrsIWyiq+lcaACVzFCiJxT2gwy7CGqWV\n/poGACxhF2GmMkt/TQOgaHYCkki1EzBOS7hWcvWvNADKpwccV+SjRoWX/lqeBvD2H/969tdvWX41\nR6QHrLfPTsC4OLsIN1f/h4dtFmSCPQCOQQ84pfPtIhxiw7+hAXAYesDpHX0X4VjVv9IAOBY9IJqj\n7CIcrvTXNAAOpj6QXd/uhpuU8DHASmXuIhy0+lcZG4DPgZmp957J2gC1vLsIaUp/pk+Aq7x7AHoA\nvebfJf/SBvSA+Y6++T/HnrsIR6/+lUNAFGLxo1HsCjBui5Zw3GM+HZkbgJ2AsBI+DKtqbdvqBExa\nc9QocenPuvlfZW8AlR4QRtqKP8QOAbeav4twsupfldAAKj3gpPap+L3sEFyL8AFAKte7COmP+RRQ\n/atCGkClB5xCxoo/pF31IjcD1X+Ns1b/qpwGUOkBB1RgxR8Rthmo/mUppvpXRTWA6n0PuPxXGyjZ\nsYr+kOuaeL6WoO4Xp6TSXyurAdS0gaKco+JPGiqXxTYG9f1Iyiv9teEG8PKH6uHnHZekyxGhXIJU\n/JnUWdbKXjtdi1YAAAHLSURBVP0vxXxAiXsAjXpXoLI3sDEVH9LLXvdnKLoBNBwUSkvFhw0dofTX\n7h8fH+/u7vq/mfsoUIcdgsVUfNhcmXV/+PjPpfgfYw+gQyeYpOLDTsqs+/O8awAH2gnoaDpBLXg/\nUPRhDweq+KOb/9VRPgOYqdMPqrO3BBUfNnegcn+7Dw3guDsB465bwqmceWYC60xt/lftPYCz9gCA\ncGZU/6pzCEgPADi8edW/uu0zAD0AoHDD1f9atwHU/WFsP+BCGwAozWjp72z71/r3AMaOBVV2BQAK\nc3v1r0YOAU33gMquAEBuU8d8hqp/Nf4ZwEQPqOwKAGS1ovpXkx8CT3wkUNkVAMhhXemvzToLaNau\nQE0nANjOvJN85lT/av5poNO7AjU7BABbSFr6a7fdC+i2NlDpBADrzD6v/6bSX1tyM7i5baDSCQAW\nueV6rgWlv7b8bqDNr7ytE1SaAUCfW4p+taLuNxLcDvqGHYLa9UpqCUA0N5b7tvWlv5bseQC37RB0\njL8R2gNwRCtKfK9Udb+R/oEw7UVc0gyupX4TAY4iedFv2/aJYOmbAcDZbVr02/Z7JGRnlfQDgNpu\nFb8j2zOBh1ZYYwDOKlehH/J/IZbVzvzzJKYAAAAASUVORK5CYII=\n'
eraser_icon = b'iVBORw0KGgoAAAANSUhEUgAAAB8AAAAfCAIAAAHny7H4AAAABnRSTlMA/wD/AP83WBt9AAAACXBI\nWXMAABJ0AAASdAHeZh94AAAFEklEQVR4nJ1WW0yaSRT+kR8Lv3KxeEFNjEZTq8Fkqza6al0UE5Ma\nL9GuLtliiQZr2qaNTz74Zpo00T6YPqkb3VQaG3HtKr54I0a21rpVa9xos65poLvqAqJyUQoI7vkB\nuQmW7RfyM3PmzDfnzJxzZtDT09PS0lLEDnRvby8xMXF8fHxnZxcFQU9P7/h47N27TXhna+svmcyu\nVl1dbTAYoEUkEtFIO2BOeXk5urg4oVJZTCYtroZh8TLZALQ6OztRtVrd1taGnEEk6uPzG3EtR39o\n6GcMi4QGgxHt5HIMHB5aEGT3zp16MpnstBKWgz+wCr5nQvvAzMxMR0cH4o3JyUlULBaDXy5RYWG/\nTNYAbqMu0fPn/ZcvR0kkkQUFardVYAlIoUEgEKanx3JySpy70t2NxMfHQhsMha9cLscHuNxMqXTF\nYFDxeI1uq+wzhra2kJUVp6iurg58QHU6HeyMp63Z2dmNjY2ozWZrbm5GgsPa2hqq0Wj8jr1//7tc\n/g+Kkpqa/hWLqTdu/ABCGo2G+uh9/Li1trZKJF7C7UVJ8O3tZZFI+3z+TyKR0L0fgIICODhrQgJG\nJNJ9WKzWcJGoxu31mbNW+H76dNzQYJyYYEHbZNLduvWjz2TnBL1eLxDwjMapZ880794xOByOS+5S\npVKp7gmODpVa8/gxkpcXcJfCw8PxuOnp6YEYD6h1BkeEoZAbeXl5jhUuAHC3traiZWVlGRkZX+QG\n9PX1oScnJ4GG376dm5//s7IyMyUl2yHxPS8XBgb6IyKirlyhKxQrDx4E1t7Y+GNzcxNU7T2MzdZf\nvy4KC+P70XZkApEY6pLo9TEtLbsPH86y2UWoh1QrlU450sMHVVXRubnxbm6l8rfR0Q+jo8i9e7E+\nqkbjQW1tvZfdT59+sHMgjx4pLZYYl6rVeuRSdWtXVNA2NnTQUChsLJYpJOSSxaKrquKFhIR4ruPU\nhgx48aLv9m08JLe395lMcl1dPXIOqH056/HxcXd3blrafH8/qlRW3rwZ6hmGiGckms3m9vZ2h7Sl\n5TwjJP+KVCrFtWEShULxyfxAQKEQDA8PB6Oq1WrRkpISLpcbqBx4Ai9AEN+Li4tdXV1QEoJZIUiA\nIUKhEL9MwEkmk/l1FMvLUwkJUcnJ30Ht9Ryi0+n4fYLYa8L/YrdYLK9evSSRSEQixmJB9B5UVv6N\nYRU0mlclg10JmG9+MTIyCLNCQ2kYFuGQqFQxiYma6Wnj5uZwR0fa1av5nvpBsUskYpPJTCbTQ0P9\nlB+zmVlY+Lm29nBubj01Vc7huMtpQHbwa2LiV53OAGYSCBQymXLB8gQCeXiYNTamfP36SCh8yWCU\nOWLElx2yRC5fpVA2BgeNk5NEDIsOxjnAycnng4MQgYCTnJzi3/b19dX795d5PKujq1BYa2rAnAjP\n0nSO1KTTafPzC1JSUs+PerHHxLDevDnl8dySkRHb7KxGIKBYLAxvUjOQZmVlstnfXOCQF3tkJEuj\n+b6iQiKRGF3CoiJwwpiUZDKZYqD8GwwH6elpWVnfXkDqnx3BKw+dSuVnZPzS1bXP5TqFajW8SsgG\nAz09/doXby3/7EajcWlpKS4uDsG36NqTJ0hz84bNZmIyk2g0Bry24Key4wI6yPycnBw/7PCwgSTc\n3t52j6F47un1R/AL0lgGw+t48GsdXlLQCgsLKy4uDpIlGMAdgtu+sLAAZRLKO5RtnwvgKwAHs7Oz\nA2xQq/8DlBoKERkZFbAAAAAASUVORK5CYII=\n'

# Set Options
sg.SetOptions(
	icon=themera_img,
	font=('Helvetica', 9),
	auto_size_text=True,
	element_padding=(8, 2),
	ttk_theme='alt')

# Random color generator.
def random_color():
	hash_sign = str('#')
	color = ''
	for i in range(6):
		color = color + str(rc([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']))  # Ha ha. Hex.
	color = str(hash_sign + color)
	color = colour.Color(color)
	return color


# Theme-ing for the theme master.
# Custom Themera Theme.
# Generated using Themera. (duh)
LightTheme = {'BACKGROUND': '#ccdeff',
   'TEXT': '#333',
   'INPUT': '#05142e',
   'TEXT_INPUT': '#ffff02',
   'SCROLL': '#667',
   'BUTTON': ('#fdfdce', '#055ffa'),
   'PROGRESS': ('#b2b2b2', '#05142e'),
   'BORDER': 1,
   'SLIDER_DEPTH': 1,
   'PROGRESS_DEPTH': 0}

sg.theme_add_new('Themera_Light', LightTheme)

## Custom Themera - Dark Theme.
## Generated using Themera. (duh)
#import PySimpleGUI as sg  # Please change 'sg' to your liking.
DarkTheme = {'BACKGROUND': '#05142e',
	'TEXT': '#ccdeff',
	'INPUT': '#333',
	'TEXT_INPUT': '#fdfdce',
	'SCROLL': '#990',
	'BUTTON': ('#fdfdce', '#333'),
	'PROGRESS': ('#667', '#333'),
	'BORDER': 1,
	'SLIDER_DEPTH': 1,
	'PROGRESS_DEPTH': 0}

sg.theme_add_new('Themera_Dark', DarkTheme)

def theme_change():
	if theme_switch == 'Themera Dark Mode':
		sg.theme('Themera_Dark')
		
	if theme_switch == 'Themera Light Mode':
		sg.theme('Themera_Light')
		
	elif theme_switch not in ['Themera Light Mode', 'Themera Dark Mode']:
		sg.theme(theme_switch)

theme_change()

# Getting a list of color names supported by the colour module.
raw_list = colour.RGB_TO_COLOR_NAMES
color_names_list = []
lowercase_color_names_list = []
for i in raw_list:
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
tab_layout = [
	# Specifier Tab
	[sg.Tab(title='Specifier',
			layout=[
				[sg.Text('')],
				[sg.Text('Theme Name: '), sg.InputText(key='name', size=(20, 1))],
				[sg.Text('Background Color: ', size=(18, 1)), sg.InputText('...color value', key='bg_c', size=(18, 1)),
				 sg.Button(button_text='', image_data=eraser_icon, size=(22, 1), image_size=(22, 22), image_subsample=0, key='bg_c_erase', tooltip='Erase color selection', pad=(2, 0)),
				 sg.Button(target='bg_c', button_text='Choose Color', key='bg_c_choose')],
				[sg.Text('Text Color: ', size=(18, 1)), sg.InputText('...color value', key='txt_c', size=(18, 1)),
				 sg.Button(button_text='', image_data=eraser_icon, size=(22, 1), image_size=(22, 22), image_subsample=0, key='txt_c_erase', tooltip='Erase color selection', pad=(2, 0)),
				 sg.Button(target='txt_c', button_text='Choose Color', key='txt_c_choose')],
				[sg.Text('Text Input Color: ', size=(18, 1)), sg.InputText('...color value', key='in_c', size=(18, 1)),
				 sg.Button(button_text='', image_data=eraser_icon, size=(22, 1), image_size=(22, 22), image_subsample=0, key='in_c_erase', tooltip='Erase color selection', pad=(2, 0)),
				 sg.Button(target='in_c', button_text='Choose Color', key='in_c_choose')],
				[sg.Text('Input Color: ', size=(18, 1)), sg.InputText('...color value', key='txt_in_c', size=(18, 1)),
				 sg.Button(button_text='', image_data=eraser_icon, size=(22, 1), image_size=(22, 22), image_subsample=0, key='txt_in_c_erase', tooltip='Erase color selection', pad=(2, 0)),
				 sg.Button(target='txt_in_c', button_text='Choose Color', key='txt_in_c_choose')],
				[sg.Text('Scroll Color: ', size=(18, 1)), sg.InputText('...color value', key='scr_c', size=(18, 1)),
				 sg.Button(button_text='', image_data=eraser_icon, size=(22, 1), image_size=(22, 22), image_subsample=0, key='scr_c_erase', tooltip='Erase color selection', pad=(2, 0)),
				 sg.Button(target='scr_c', button_text='Choose Color', key='scr_c_choose')],
				[sg.Text('Button Text Color: ', size=(18, 1)),
				 sg.InputText('...color value', key='bt_txt_c', size=(18, 1)),
				  sg.Button(button_text='', image_data=eraser_icon, size=(22, 1), image_size=(22, 22), image_subsample=0, key='bt_txt_c_erase', tooltip='Erase color selection', pad=(2, 0)),
				 sg.Button(target='bt_txt_c', button_text='Choose Color', key='bt_txt_c_choose')],
				[sg.Text('Button Color: ', size=(18, 1)), sg.InputText('...color value', key='bt_c', size=(18, 1)),
				 sg.Button(button_text='', image_data=eraser_icon, size=(22, 1), image_size=(22, 22), image_subsample=0, key='bt_c_erase', tooltip='Erase color selection', pad=(2, 0)),
				 sg.Button(target='bt_c', button_text='Choose Color', key='bt_c_choose')],
				[sg.Text('Progress Bar Color: ', size=(18, 1)),
				 sg.InputText('...color value', key='pb_c', size=(18, 1)),
				  sg.Button(button_text='', image_data=eraser_icon, size=(22, 1), image_size=(22, 22), image_subsample=0, key='pb_c_erase', tooltip='Erase color selection', pad=(2, 0)),
				 sg.Button(target='pb_c', button_text='Choose Color', key='pb_c_choose')],
				[sg.Text('Progress Bar BG Color: ', size=(18, 1)),
				 sg.InputText('...color value', key='pb_bg_c', size=(18, 1)),
				  sg.Button(button_text='', image_data=eraser_icon, size=(22, 1), image_size=(22, 22), image_subsample=0, key='pb_bg_c_erase', tooltip='Erase color selection', pad=(2, 0)),
				 sg.Button(target='pb_bg_c', button_text='Choose Color', key='pb_bg_c_choose')],
				[sg.Text('Border Width: ', size=(10, 1)),
				 sg.Spin(initial_value='1', values=[x for x in range(0, 10000)], key='bor_w', size=(3, 1)),
				 sg.Text(' || '), sg.Text('Slider Depth: ', size=(10, 1)),
				 sg.Spin(initial_value=1,
						 values=[x for x in range(0, 10000)], key='sl_bor_w', size=(3, 1))],
				[sg.Text('Progress Meter Depth: ', size=(17, 1)),
				 sg.Spin(initial_value=0, values=[x for x in range(0, 10000)], key='pb_w', size=(3, 1))],
				[sg.Button(button_text=' Generate Code ', font=('Helvetica', 13), key='gen', bind_return_key=True)],
			],
			element_justification='center')],
	# Theme Code Reuse Tab
	[sg.Tab(title='Re-Use Theme Code',
			layout=[
				[sg.Text('')],
				[sg.Text('You can re-use existing theme code as Specifier input using this tab.')],
				[sg.Text('Simply paste the code below and click \"Re-Use\".')],
				[sg.Text('Themera\'s Light Mode code is being used as a template here.')],
				[sg.Multiline(
					'import PySimpleGUI as sg\n\n'
				  	'LightTheme = {\n'
   						'\'BACKGROUND\': \'#ccdeff\',\n'
   						'\'TEXT\': \'#333\',\n'
   						'\'INPUT\': \'#05142e\',\n'
   						'\'TEXT_INPUT\': \'#ffff02\',\n'
   						'\'SCROLL\': \'#667\',\n'
   						'\'BUTTON\': (\'#fdfdce\', \'#055ffa\'),\n'
   						'\'PROGRESS\': (\'#b2b2b2\', \'#05142e\'),\n'
   						'\'BORDER\': 1,\n'
   						'\'SLIDER_DEPTH\': 1,\n'
   						'\'PROGRESS_DEPTH\': 0}\n'
						'sg.theme_add_new(\'Themera_Light\', LightTheme)'
				    , key='pasted', size=(50, 8))],
				[sg.Button('Re-Use', key='reuse_main', font=('Helvetica', 13))],
				[sg.Text('Warning: Neither Themera nor its developers shall', text_color=sg.theme_slider_color())],
				[sg.Text('bear responsibility for any repercussion of the code', text_color=sg.theme_slider_color())],
				[sg.Text('you input, so do be careful.', text_color=sg.theme_slider_color())],
				],
			element_justification='center')],
	[sg.Tab(title='Other Options',
			layout=[[sg.Column(layout=[
				[sg.Column([
					[sg.Text(text='', background_color=sg.theme_slider_color(), text_color=sg.theme_background_color())],
				], element_justification='center', background_color=sg.theme_slider_color(), size=(380, 2))],
				[sg.Text(text='Have a feature proposal to add to these options?', background_color=sg.theme_slider_color(), text_color=sg.theme_background_color())],
				[sg.Text(text='Got a complaint?', background_color=sg.theme_slider_color(), text_color=sg.theme_background_color())],
				[sg.Text(text='Open up an issue on the Themera GitHub repository.', background_color=sg.theme_slider_color(), text_color=sg.theme_background_color())],	
				[sg.Frame(title='Dark/Light/Gray Modes',
						  layout=[[sg.Text('Automatically make a...')],
								  [sg.Checkbox('Dark Mode Theme', key='dark')],
								  [sg.Checkbox('Light Mode Theme', key='light')],
								  [sg.Checkbox('Gray Mode Theme', key='grayout')],
								  [sg.Text('...along with the theme currently being made.')]],
						  tooltip='May not always work as expected. Majorly dependent on your color choices.', element_justification='center')],
				[sg.Frame(title='Color Options', layout=[[sg.Button('View valid color names.', key='col_name_view')]], element_justification='center')],
				[sg.Frame(title='\'Unspecified Color\' Actions', layout=[
					[sg.Checkbox('Complementary Mono', key='Inverse')],
					[sg.Checkbox('Haphazard Random', key='H_Random')]
				], element_justification='center')],
				[sg.Frame(title='PySimpleGUI Options', layout=[[sg.Text('Probably unrelated, but useful.')], [
					sg.Button('Preview all PySimpleGUI themes', key='preview', tooltip=(
						'This may take a while to initialize.\nAfter all, there are {0} built-in themes.'.format(
							str(len(sg.ListOfLookAndFeelValues())))))],  # That list sure grows fast.
															   [sg.Button('Update / Install PySimpleGUI', key='update',
																		  tooltip='Requires Python and pip.')]],
						  element_justification='center')],
				[sg.Frame(title='External Links', layout=[[sg.Button('Check out definite_d\'s GitHub page',
																	 key='checkout_me',
																	 tooltip='Come on, don\'t be shy!')], [
															  sg.Button('Check out the Themera GitHub page',
																		key='checkout_themera',
																		tooltip='Whoo! GitHub!')], [
															  sg.Button('Check out the PySimpleGUI GitHub page',
																		key='checkout_psg',
																		tooltip='Whoo! GitHub! Again!')]],
						  element_justification='center')]
			], element_justification='center', scrollable=True, vertical_scroll_only=True, size=(390, 370),
				background_color=sg.theme_slider_color(), pad=(0, 0))]],
			element_justification='center')]
]

default_themes = sg.theme_list()
default_themes.remove('Themera_Dark')
default_themes.remove('Themera_Light')
available_themes = ['Themera Light Mode', 'Themera Dark Mode']+default_themes

window_1_layout = [
	[sg.Column([
		[sg.Button(
			'', 
			key='logo', 
			image_data=themera_img, 
			border_width=0, 
			image_subsample=4, 
			button_color=('#000000', sg.theme_background_color())
			)]
	], pad=(0, 0), element_justification='center'),
		sg.Column([
			[sg.Text('Themera!', font=('Helvetica', 24))],
			[sg.Text('PySimpleGUI Theme Code Generator.')],
			[sg.Text('Developed by definite_d')],
			[sg.Text('Click this text for help.', tooltip='I\'m here to help.', key='Help', enable_events=True)]],
			pad=(0, 0), element_justification='center')
	],
	[sg.TabGroup(layout=tab_layout,)],
	[sg.Text('Current Theme Mode:', tooltip='Changes take effect after a restart.'), sg.DropDown(available_themes, readonly=True, tooltip='Changes take effect after a restart.', default_value=theme_switch, key='theme_switch')]
]
window_1 = sg.Window((f'Themera - {version}'),
					 layout=window_1_layout,
					 element_justification='center',
					 grab_anywhere=False, resizable=False)

def get_colors_of_theme_code(theme_code):
	exec(theme_code)
	r_bg_c = str(sg.theme_background_color())
	r_txt_c = str(sg.theme_text_color())
	r_in_txt_c = str(sg.theme_input_text_color())
	r_in_c = str(sg.theme_input_background_color())
	r_scr_c = str(sg.theme_slider_color())
	r_bt_txt_c = str(sg.theme_button_color()[0])
	r_bt_c = str(sg.theme_button_color()[1])
	r_prog_c = str(sg.theme_progress_bar_color()[0])
	r_prog_bg_c = str(sg.theme_progress_bar_color()[1])
	theme_change()
	return [r_bg_c, r_txt_c, r_in_txt_c, r_in_c, r_scr_c, r_bt_txt_c, r_bt_c, r_prog_c, r_prog_bg_c]

def get_numerical_details_of_theme_code(theme_code):
	exec(theme_code)
	r_bor_w = str(sg.theme_border_width())
	r_sl_w = str(sg.theme_slider_border_width())
	r_prog_w = str(sg.theme_progress_bar_border_width())
	theme_change()
	return [r_bor_w, r_sl_w, r_prog_w]

def get_all_details_of_theme_code(theme_code):
	result = []
	result += get_colors_of_theme_code(theme_code)
	result += get_numerical_details_of_theme_code(theme_code)
	return(result)

# Theme Code Reuser function that gives life to that feature.
def reuse_process(theme_code, window=None, target_key=None):
	window_1.Refresh()
	theme_details = get_all_details_of_theme_code(theme_code)
	key_list = ['bg_c', 'txt_c', 'txt_in_c', 'in_c', 'scr_c', 'bt_txt_c', 'bt_c', 'pb_c', 'pb_bg_c', 'bor_w', 'sl_bor_w', 'pb_w']
	for key in key_list:
		index = key_list.index(key)
		window_1[key](theme_details[index])
	window_1.Refresh()

selected_theme = theme_switch
# Beginning the GUI process.
while True:
	window_1_events, window_1_values = window_1.Read(timeout=10)
	try:selected_theme = window_1_values['theme_switch']
	except TypeError: pass
	
	# Using the Loc8or module.
	loc8or = Locator(window_1)
	popup_height = 120  # Y-Offset value for popup windows.
	subwindow_height = 100  # Y-Offset value for sub windows.
	immediate_window_height = 20  # Y-Offset value for windows that appear immediately below the titlebar of the main window.
	
	try:
		window_1_c = window_1.CurrentLocation()
		window_1_s = window_1.Size
	except:
		break
		pass

	# Configuring the color picker
	if 'choose' in window_1_events:
		color_picker_layout = colorpiq.Colorpiqr(preview_box_height=2, slider_width=50, slider_height=15).colorpiqr_layout
		color_picker = colorpiq.Colorpiqr(title='Colorpiq', icon=themera_img, preview_box_height=2, slider_width=50, slider_height=15,
							   location=loc8or.get_ideal_location(color_picker_layout, 'UC', 'UC', popup_height))
		del color_picker_layout
		window_1[window_1_events.replace('_choose', '')].Update(color_picker.get_color())
	
	# Configuring the erasers
	if 'erase' in window_1_events:
		target = str(window_1_events).replace('_erase', '')
		window_1[target]('...color value')

	# Configuring the theme reuse.
	if window_1_events == 'reuse_main':
		reusable = window_1_values['pasted']
		reuse_process(reusable)
		sg.Popup('Please check the Specifier tab.', title='Code Re-Used')

	if window_1_events == 'gen':
		unsupported_entry = False
		no_name = False
		if window_1_values['name'] == '' or window_1_values['name'].isspace() == True:
			sg.Popup('You didn\'t specify a name for the theme!', title='Warning: No Name!', button_type='Cancel',
					 location=(window_1_c[0] + 80, window_1_c[1] + popup_height))
			no_name = True  # What masterpiece didn't have a name?

		for i in window_1_values:
			# I found that 'Navajo White' (unsupported color) isn't the same as 'NavajoWhite' (supported color).
			if '_c' in str(i) and window_1_values[str(i)] not in ['...color value', 'None'] and str(
					window_1_values[str(i)]).lower() not in lowercase_color_names_list and window_1_values[
				str(i)].startswith('#') == False and window_1_values[str(i)].isspace() == False and window_1_values[
				str(i)] != '':
				given_value = str(window_1_values[str(i)])
				window_1_values[str(i)] = (str(window_1_values[str(i)])).replace(' ', '')
				sg.Popup(
					('The color name \'' + given_value + '\' is not supported.\nYou should use the hex value of the '
														 'intended color instead.'),
					title='Warning: Unsupported Color!', button_type='Cancel',
					location=(window_1_c[0] + 15, window_1_c[1] + popup_height))
				unsupported_entry = True  # To avoid unforeseen error-stances.

		name = str(window_1_values['name'])
		name_safe = name
		if '\'' in name_safe:
			name_safe = str(name_safe).replace('\'', '\\\'')
		if '\\\\\'' in name_safe:
			name_safe = str(name_safe).replace('\\\\\'', '\\\'')
		if ' ' in name_safe:
			name_safe = str(name_safe).replace(' ', '_')
		if '.' in name_safe:
			name_safe = str(name_safe).replace('.', '_')

		bg_c = str(window_1_values['bg_c'])
		txt_c = str(window_1_values['txt_c'])
		txt_in_c = str(window_1_values['txt_in_c'])
		in_c = str(window_1_values['in_c'])
		scr_c = str(window_1_values['scr_c'])
		bt_txt_c = str(window_1_values['bt_txt_c'])
		bt_c = str(window_1_values['bt_c'])
		pb_c = str(window_1_values['pb_c'])
		pb_bg_c = str(window_1_values['pb_bg_c'])
		bor_w = str(window_1_values['bor_w'])
		sl_bor_w = str(window_1_values['sl_bor_w'])
		pb_w = str(window_1_values['pb_w'])
		color_values = [bg_c, txt_c, in_c, txt_in_c, scr_c, bt_txt_c, bt_c, pb_c, pb_bg_c]

		if no_name == False and unsupported_entry == False:
			for o in color_values:
				if (o.isspace() == True) or (o == ''):
					color_values[color_values.index(o)] = 'None'
			# Selected is a list of indexes of all colors selected (NOT their identifiers),
			#  in order of hierarchy on the color_values list.
			selected = []
			for e in color_values:
				if e not in ('...color value', 'None'):
					selected.append(color_values.index(e))
			sel_colors = selected
			sel_colors1 = []
			for s in sel_colors:
				if sel_colors.count(s) > 1:
					for n in range((sel_colors.count(s) - 1)):
						sel_colors.remove(s)
			for i in sel_colors:
				i = color_values[i]
				sel_colors1.append(i)
			sel_colors = sel_colors1

			# Dealing with unspecified color values.
			done = False
			if color_values.count(('...color value' or 'None' or 'none' or '')) > 0:
				unspecified = True
			else:
				unspecified = False
				done = True

			if unspecified == False:
				# These lists are used for sorting colors by brightness.
				luminance_list = []
				for i in color_values:
					i_c = colour.Color(i)
					i_c_l = i_c.get_luminance()
					luminance_list.append(i_c_l)
				sorter_list = list(zip(luminance_list, color_values))
				sorter_list = sorted(sorter_list, key=lambda color: color[0])
				sorted_list = [i[1] for i in sorter_list]
				done = True
			if unspecified == True:
				unspec_no = len(color_values) - len(selected)
				if unspec_no != 1:
					unspec_title = str(unspec_no) + ' color values were not specified!'
				else:
					unspec_title = 'A color value was not specified!'
				if unspec_no == 9:
					unspec_no = 'any'
					unspec_title = 'No color value was specified!'

				if unspec_no == 1:
					message = str('You didn\'t specify a color value.')
				else:
					message = str('You didn\'t specify ' + str(unspec_no) + ' color values.')
				unspec_opts_layout = [
					[sg.Text(text=message)],
					[sg.Text(text='What should be done about that?')],
					[sg.Frame('Your Options', [
						[sg.Radio('Fill in random colors.', key='Randomize', tooltip='Make it crazy random!',
								  group_id='unspec_opts_choices')],
						[sg.Radio('Base other colors off those given.', key='Mono',
								  tooltip='Good for mono-color themes.', group_id='unspec_opts_choices')],
						[sg.Radio('Get colors from an image.', key='Image', tooltip='Introducing... ImagePalette!',
								  group_id='unspec_opts_choices', default=True)]
					])],
					[sg.Button('Confirm', key='Confirm', bind_return_key=True, tooltip='Let\'s begin.'),
					 sg.Button('Cancel', key='Cancel', tooltip='Have it your way.')]
				]
				unspec_opts = sg.Window(title=unspec_title, layout=unspec_opts_layout,
										location = loc8or.get_ideal_location(unspec_opts_layout, 'UC', 'UC', popup_height),
										element_justification='center')
				done = False
				while True:
					def originalize_color_values():
						selections = zip(selected, sel_colors)
						for i in range(len(selected)):
							change = selections.__next__()
							color_values[(change[0])] = change[1]
					try:
						unspec_opts_events, unspec_opts_values = unspec_opts.Read()
						if unspec_opts_events == 'Confirm':
							if unspec_opts_values['Randomize']:  # The most straightforward task for colors.
								for c in color_values:
									if c in ('None', '...color value'):
										if window_1_values['H_Random']:
											color_values[color_values.index(c)] = random_color()
										else:
											random_number = rc([n for n in range(1, 9)])
											the_color = random_color()
											the_color.set_luminance(
												value=((color_values.index(c) + random_number) / (random_number + 8)))
											color_values[color_values.index(c)] = the_color
								if not window_1_values['H_Random']:
									# Sort things out...
									luminance_list = []
									for i in color_values:
										i_c = colour.Color(i)
										i_c_l = i_c.get_luminance()
										luminance_list.append(i_c_l)
									sorter_list = list(zip(luminance_list, color_values))
									sorter_list = sorted(sorter_list, key=lambda color: color[0])
									sorted_list = [i[1] for i in sorter_list]
									color_values = [sorted_list[3], sorted_list[8], sorted_list[1], sorted_list[7], sorted_list[2], sorted_list[0], sorted_list[6], sorted_list[4], sorted_list[5]]
								done = True
								unspec_opts.Close()
								break
							if unspec_opts_values['Mono']:
								# Here comes the mono...
								try:
									if len(sel_colors) == 0:
										sel_colors.append(random_color())
									# Just in case anybody dropped in some Tkinter colors.
									for tk in sel_colors:
										sel_colors[sel_colors.index(tk)] = colour.Color(tk).get_web()
									# I'm gonna expand the list of selected colors to 9, by creating a list of transitioning colors between all selected colors.
									if len(sel_colors) > 1:
										transition = []
										try:
											for n in sel_colors:
												next_color = sel_colors[((sel_colors.index(n)) + 1)]
												n = colour.Color(n)
												next_color = colour.Color(next_color)
												shadegradient = list(n.range_to(next_color, 8))
												transition.extend(shadegradient)
										except:
											pass
										true_transition = []
										for i in range(8):
											true_transition.append(transition[(int((len(transition) * i) / 8))])
										transition = true_transition
										del true_transition
									if len(sel_colors) == 1:  # Mono el mono.
										number = 9
										for i in sel_colors:
											# Who wants a theme where every color is black? Or annoyingly bright?
											if window_1_values['Inverse'] == False:
												if colour.Color(sel_colors[0]).luminance >= 0.6:
													other_shade = colour.Color('black')
													signal = 'black'
												if 0.5 <= colour.Color(sel_colors[0]).luminance < 0.6:
													other_shade = colour.Color(i)
													other_shade.set_luminance((other_shade.get_luminance()) / 4)
												if colour.Color(sel_colors[0]).luminance < 0.5:
													other_shade = colour.Color('white')
													signal = 'white'
											if window_1_values['Inverse'] == True:
												other_shade = colour.Color(
													sg.GetComplimentaryHex(colour.Color(i).hex_l))
												other_shade.set_luminance(colour.Color(i).luminance)
												signal = 'depends'
											i = colour.Color(i)
											# I have to get a list of colors that's sorted from darkest to brightest by
											#   default. So...
											if other_shade.luminance < i.luminance:  # Darker/Blacker to Lighter.
												transition = list(other_shade.range_to(i, number))
											else:  # Darker to Whiter/Lighter.
												transition = list(i.range_to(other_shade, number))

									luminance_list = []
									for i in transition:
										i_c = colour.Color(i)
										i_c_l = i_c.get_luminance()
										luminance_list.append(i_c_l)
									sorter_list = list(zip(luminance_list, transition))
									sorter_list = sorted(sorter_list, key=lambda color: color[0])
									sorted_list = [i[1] for i in sorter_list]
									transition = sorted_list
									transition = [transition[3], transition[8], transition[1], transition[7], transition[2], transition[0], transition[6], transition[4], transition[5]]
									color_values = transition
									originalize_color_values()

									done = True
									unspec_opts.Close()
									break
								except:
									unspec_opts.Close()
									done = False
									break
							if unspec_opts_values['Image']:
								# filetypes = ['.png', '.jpg', '.jpeg', '.gif', '.pdf', '.ico', '.icns', '.bmp', '.tga', '.tiff', '.webp', '.xbm', '.pcx', '.ppm', '.uii', '.j2p', '.j2x', '.spi']
								filetypes = rw_types()
								im_palette_layout = [[sg.Frame(title='Image Palette',
																layout=[
																	[sg.Text(
																		'Creates a theme out of the colors in an image.')],
																	[sg.Text(text=('Theme Name: {0}'.format(name)))],
																	[sg.Frame(title='Select Image', layout=[
																		[sg.Text('Image Filepath:'),
																		sg.InputText(default_text='', key='im_subject',
																						size=(25, 1)),
																		sg.FileBrowse(file_types=(
																			('Image Files', (filetypes)),))],
																		[sg.Checkbox('Don\'t sort the image\'s colors.',
																					key='im_sort')]
																	], element_justification='center')],
																	[sg.Text('\"' * 86, pad=(0, 1))],
																	[sg.Button(button_text=' Obtain Colors ',
																				key='im_color',
																				bind_return_key=True)]
																], element_justification='center')],
														[sg.Button('Cancel')]]
								im_palette = sg.Window(title='ImagePalette', layout=im_palette_layout,
														location=loc8or.get_ideal_location(im_palette_layout, 'UC', 'UC', subwindow_height))
								
								while True:
									im_events, im_values = im_palette.Read()
									if im_events == 'im_color':
										im_subject = im_values['im_subject']
										if isfile(str(im_subject)) and im_events == 'im_color':
											image_factor = int(filesize(im_subject) / 400) + 1
											if not im_values['im_sort']:
												image_factor = image_factor * 1.5
											image_factor = int(image_factor)

											im_colors_true = []
											image = img.open(im_subject)
											image = image.resize((32, 32))
											im_colors = image.getcolors(maxcolors=(image.size[0] * image.size[1]))
											for i in im_colors:
												r = float(i[1][0] / 255)
												g = float(i[1][1] / 255)
												b = float(i[1][2] / 255)
												im_colors_true.append(colour.Color(colour.rgb2hex((r, g, b))))
											im_colors = []
											for i in range(9):
												im_colors.append(im_colors_true[(int((len(im_colors_true) * i) / 9))])

											# Sort things out...
											if not im_values['im_sort']:
												luminance_list = []
												for i in im_colors:
													i_c = colour.Color(i)
													i_c_l = i_c.get_luminance()
													luminance_list.append(i_c_l)
												sorter_list = list(zip(luminance_list, im_colors))
												sorter_list = sorted(sorter_list, key=lambda color: color[0])
												sorted_list = [i[1] for i in sorter_list]
												im_colors = sorted_list
												im_colors = [im_colors[3], im_colors[8], im_colors[1], im_colors[7], im_colors[2], im_colors[0], im_colors[6], im_colors[4], im_colors[5]]

											for color in im_colors:
												im_colors[im_colors.index(color)] = color.get_web()
											color_values = im_colors
											originalize_color_values()

											# Progress bar code.
											prog_c_l = [[sg.Text('Please wait...')],
														[sg.ProgressBar(image_factor, orientation='h', size=(35, 20),
																		key='progbar')]]
											prog_c = sg.Window('Obtaining Colors from Image...', prog_c_l,
																location=loc8or.get_ideal_location(prog_c_l, 'UC', 'UC', popup_height), disable_close=True)
											for i in range(image_factor):
												prog_c_e, prog_c_v = prog_c.Read(timeout=0)
												prog_c['progbar'].UpdateBar(i + 1)

											prog_c.Close()
											im_palette.Close()
											no_image = False
											done = True
											unspec_opts.Close()
											break

									if im_events in (None, 'Cancel'):
										no_image = True
										done = False
										im_palette.Close()
										break
								break

						if unspec_opts_events in [None, 'Cancel']:
							done = False
							unspec_opts.Close()
							break

					except Exception:
						unspec_opts.Close()
						break
						pass


			# This is where the real code generation happens.
			def finisher(color_values):
				try:
					def generate_theme_code(color_values=color_values, purpose=None, commented=False):
						bg_c = str(color_values[0])
						txt_c = str(color_values[1])
						txt_in_c = str(color_values[2])
						in_c = str(color_values[3])
						scr_c = str(color_values[4])
						bt_txt_c = str(color_values[5])
						bt_c = str(color_values[6])
						pb_c = str(color_values[7])
						pb_bg_c = str(color_values[8])
		
						first_line = f'## Generated using Themera.\n'
						if purpose == None:
							first_line = f'# Custom {name} PySimpleGUI Theme.\n'
							themedict_variable = f'{name_safe}_themedict'
							theme_variable = f'\'{name_safe}\''
						if purpose == 'Light':
							first_line = f'# Custom {name} - Light PySimpleGUI Theme.\n'
							themedict_variable = f'{name_safe}_Light_themedict'
							theme_variable = f'\'{name_safe}_Light\''
						if purpose == 'Dark':
							first_line = f'# Custom {name} - Dark PySimpleGUI Theme.\n'
							themedict_variable = f'{name_safe}_Dark_themedict'
							theme_variable = f'\'{name_safe}_Dark\''
						if purpose == 'Gray':
							first_line = f'# Custom {name} - Gray PySimpleGUI Theme.\n'
							themedict_variable = f'{name_safe}_Gray_themedict'
							theme_variable = f'\'{name_safe}_Gray\''
						if purpose == 'Shuffle':
							first_line = f'# Shuffled custom {name} (Shuffle {shuffle_counter}) PySimpleGUI Theme.\n'
							themedict_variable = f'{name_safe}_Shuffled{str(shuffle_counter)}_themedict'
							theme_variable = f'\'{name_safe}_Shuffled{str(shuffle_counter)}\''
							
						code = [first_line,
								f'# Generated using Themera {version}.\n',
								f'import PySimpleGUI as sg  # Please change \'sg\' to your liking.\n',
								f'{themedict_variable} = {{\'BACKGROUND\': \'{bg_c}\',\n    ',
								f'\'TEXT\': \'{txt_c}\',\n    ',
								f'\'INPUT\': \'{in_c}\',\n    ',
								f'\'TEXT_INPUT\': \'{txt_in_c}\',\n    ',
								f'\'SCROLL\': \'{scr_c}\',\n    ',
								f'\'BUTTON\': (\'{bt_txt_c}\', \'{bt_c}\'),\n    ',
								f'\'PROGRESS\': (\'{pb_c}\', \'{pb_bg_c}\'),\n    ',
								f'\'BORDER\': {str(bor_w)},\n    ',
								f'\'SLIDER_DEPTH\': {str(sl_bor_w)},\n    ',
								f'\'PROGRESS_DEPTH\': {str(pb_w)}}}\n\n',
								f'sg.theme_add_new({theme_variable}, {themedict_variable})\n',
								f'sg.theme({theme_variable})\n\n',
								]
						if commented:
							for code_line in code:
								index = code.index(code_line)
								code[index] = '# '+code_line
								
						theme_code = ''
						for code_line in code:
							theme_code += code_line
						
						return theme_code
						
					if done:  # Yep. Real shameless signal system.
						# Set the names of colors just right...
						for i in color_values:
							if not str(i).startswith('#'):
								color_values[(color_values.index(i))] = str(i).lower()  # Lowercase doesn't discriminate.
						global theme
						theme = generate_theme_code()
	
						# Dark and Light modes (and most recently Gray mode) ... I nearly got confused about where to put their code.
						# Sort things out...
						luminance_list = []
						for i in color_values:
							i_c = colour.Color(i)
							i_c_l = i_c.get_luminance()
							luminance_list.append(i_c_l)
						sorter_list = list(zip(luminance_list, color_values))
						sorter_list = sorted(sorter_list, key=lambda color: color[0])
						sorted_list = [i[1] for i in sorter_list]
						# Dark and Light modes implementation.
						if window_1_values['dark'] == True:
							dark_list = [sorted_list[0], sorted_list[6], sorted_list[7],
										 sorted_list[1], sorted_list[2], sorted_list[7],
										 sorted_list[1], sorted_list[8], sorted_list[3]]
							theme += generate_theme_code(dark_list, 'Dark', True)
						if window_1_values['light'] == True:
							light_list = [sorted_list[7], sorted_list[1], sorted_list[0],
										  sorted_list[6], sorted_list[5], sorted_list[0],
										  sorted_list[6], sorted_list[4], sorted_list[8]]
							theme += generate_theme_code(light_list, 'Light', True)
						if window_1_values['grayout'] == True:
							# This is the Gray-Out feature. It gives a black-and-white effect to themes.
							gray_list = []
							for i in sorted_list:
								i = colour.Color(i)
								i.saturation = 0
								gray_list.append(i.get_web())
							theme += generate_theme_code(gray_list, 'Gray', True)
						# I decided to add a progress meter for the code generation because... why not?
						prog_l = [[sg.Text('Please wait...')],
								  [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')]]
						prog = sg.Window('Generating Theme...', prog_l, location=loc8or.get_ideal_location(prog_l, 'UC', 'UC', 20), disable_close=True)
						for i in range(1000):
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
						sg.PopupOK('All done!', 'Your theme code is ready.', location=prog.CurrentLocation(),
								   auto_close=True,
								   auto_close_duration=5)
						prog.Close()
						# Dole out the code for the user's harvest.
						# output_house_size = (618, 180)
						output_window_layout = [
							[sg.Text('Theme Output', font=('Helvetica', 19)), sg.Text((' ' * 124)),
							 sg.Button(' Exit ', key='Exit')],
							[sg.Text(f'Code for {str(name)} Look and Feel theme.')],
							[sg.Text('Please copy and paste the code below into your source code.')],
							[sg.Text('This output is directly modifiable.')],
							[sg.Column([
								[sg.Column([
									[sg.Checkbox('Don\'t Preview automatically upon readibility adjustment.', key='preview_x_adj')],
									[sg.Multiline(default_text=theme, key='output', size=(55, 10))]
								], pad=(0, 0)),
								sg.Column([
									[sg.Button(' Preview Theme ', key='preview')],
									[sg.Button('Shuffle Theme Colors', key='shuffle')],
									[sg.Button('Copy Theme Code to Clipboard', key='copy')],
									[sg.Button('Reuse as Themera Input', key='reuse')],
									[sg.Button('Adjust Readability', key='adjust'),
									 sg.Button('Revert Adjustments', key='revert', visible=False)]
								], pad=(0, 0))
								],
							[sg.Frame('Theme Shuffler', layout=[
								[sg.Column(layout=[
									[sg.Checkbox('Don\'t Preview automatically when Shuffle is clicked.',
												 key='preview_x_shuffle'), sg.Text((' ' * 39)),
									 ],
									[sg.Checkbox('Don\'t Preview automatically upon readibility adjustment.',
												 key='preview_x_adj_shf')],
									[sg.Text('Shuffled Theme:')],
									[sg.Column([[sg.Multiline(default_text='', key='shuffled_theme', size=(50, 10))]],
											   pad=(0, 0)),
									 sg.Column([
										 [sg.Button(' Preview Shuffled Theme ', key='shf_preview')],
										 [sg.Button('Copy Theme Code to Clipboard', key='shf_copy')],
										 [sg.Button('Reuse as Themera Input', key='reuse_shf')],
										 [sg.Button('Adjust Readability', key='adjust_shf'),
										  sg.Button('Revert Adjustments', key='revert_shf', visible=False)]
									 ], pad=(0, 0))],
								])]
							], visible=False, key='shuffle_frame')]
								], key='output_house')]
						]
						output_window = sg.Window(title=('Look and Feel Theme - ' + str(name)),
												  layout=output_window_layout,
												  grab_anywhere=False, element_justification='center',
												  # location=(window_1_c[0] - 50, window_1_c[1] + 50)
												  location = loc8or.get_ideal_location(output_window_layout, 'UC', 'UC', immediate_window_height)
												  )
						# Shuffle Preliminaries and Functions
						shuffle_counter = 0
	
						def generate_shuffled_theme(colors):
							shuffled_theme = generate_theme_code(colors, 'Shuffle')
							return shuffled_theme
	
						def shuffler(colors):
							rs(colors)
							sh_theme = generate_shuffled_theme(colors)
							scrambled_values = colors
							return [sh_theme, scrambled_values]
	
						def adjust_readability(colors):
							for i in colors:
								colors[colors.index(i)] = colour.Color(colors[colors.index(i)])
							if colors[0].luminance < 0.5:
								predisposition = 'dark'
								lum = [round(colors[0].luminance, 1), 1, 0.3, 0.8, 0.4, 0.2, 0.9, 0.8, 0.3]
							else:
								predisposition = 'light'
								lum = [round(colors[0].luminance, 1), 0.2, 0.3, 0.1, 0.4, 0.9, 0.5, 0.4, 0.7]
							for y in range(8):
								colors[y].luminance = lum[y]
							return colors
						
						def smart_executor(cached_theme, compare_to, execute=True):
							if compare_to == cached_theme:  # This guy here and his alternate allow for
								pass  # on-the-fly editing of the theme code even from the
							elif compare_to != cached_theme:  # output panel.
								cached_theme = compare_to  # Tried and tested :).
							if execute:	
								exec(cached_theme)  # Nifty as ever for adjusting the background color in a pinch.
							else:
								pass

						def preview_process(theme):
							output_window_values = output_window.Read(timeout=10)[1]
							user_output = output_window_values['output']
							smart_executor(theme, user_output)
							init_preview(theme_code=theme, theme_name=name)
							
						def sh_preview_process(shuffled_theme):
							output_window_values = output_window.Read(timeout=10)[1]
							user_output = output_window_values['shuffled_theme']
							smart_executor(shuffled_theme, user_output)
							init_preview(theme_code=shuffled_theme, theme_name=name)
							
						def init_preview(theme_code, theme_name):
							# Let's give 'em a feel of their custom theme.
							preview_layout = [[sg.Text(' ' * 40), sg.Text('Theme Preview')],
											  [sg.Text(' ' * 19),
											   sg.Text('This is how your theme will look when used.')],
											  [sg.Text(' ' * 5),
											   sg.Text('This window serves no other purpose than being a mannequin.')],
											  [sg.Text('Only the exit button works.')],
											  [sg.InputText('...just a textbox', size=(60, 8))],
											  [sg.Multiline((f'# This is the code responsible for this window\'s theme.\n\n{theme_code}'),
												  size=(58, 5))],
											  [sg.Frame(title='Progress Bar Preview', layout=[
												  [sg.Text('This bar is static though.')],
												  [sg.ProgressBar(max_value=1000, orientation='h', size=(35, 20),
																  key='p_bar')]
											  ])],
											  [sg.Frame(title='Slider Preview', layout=[
												  [sg.Text('This is a useless slider.')],
	
												  [sg.Slider(range=(0, 1000), size=(35, 10),
															 default_value=rc([0, 500, 1000]), orientation='h')]
											  ])],
											  [sg.Frame(title='Useless Buttons!',
														layout=[[sg.Button(' Button A ', key='btn_a'),
																 sg.Button(' Button B ', key='btn_b'),
																 sg.Button(' Button C ', key='btn_c'),
																 sg.Button(' Another useless button. ',
																		   key='btn_d')]])],
											  [sg.DummyButton(' Exit ', key='Exit')]]
							preview = sg.Window(title=(theme_name + ' Preview Popup'), layout=preview_layout,
												location=loc8or.get_ideal_location(preview_layout, 'UC', 'UC', 20))
	
							preview.read(timeout=0)
							preview['p_bar'].UpdateBar((rc([number for number in range(500, 1001)])))
							# Change back to the previous Themera theme.
							theme_change()
							bar_value = 1
							while False:
								preview_events, preview_values = preview.Read()
								if preview_events in (None, 'Exit') or not output_window_open:
									preview.Close()
									window_1.BringToFront()
									output_window.BringToFront()
									break
							
						revert_cache = None
						shf_revert_cache = None
	
						while True:
							output_window_open = True
							output_window_events, output_window_values = output_window.Read(timeout=10)
	
							if output_window_events in (None, 'Exit'):
								output_window_open = False
								output_window.Close()
								theme_change()
								window_1.BringToFront()
								break
							if output_window_events == 'shuffle':
								shuffle_counter += 1
								global s
								global s_theme
								global s_colors
								if shuffle_counter > 1: color_list = color_values
								else: color_list = get_colors_of_theme_code(output_window_values['output'])
								s = shuffler(color_list)
								s_theme = s[0]
								s_colors = s[1]
								output_window['shuffle_frame'](visible=True)
								output_window['shuffled_theme'](s_theme)
								if not output_window_values['preview_x_shuffle']:
									sh_preview_process(s_theme)
							
							if output_window_events == 'adjust':
								revert_cache = output_window_values['output']
								output_window['adjust'](visible=False)
								output_window['revert'](visible=True)
								adjusted = adjust_readability(get_colors_of_theme_code(output_window_values['output']))
								adjusted_theme = generate_theme_code(adjusted)
								ad_luminance_list = []
								for a_i in adjusted:
									a_i_c = colour.Color(a_i)
									a_i_c_l = a_i_c.get_luminance()
									ad_luminance_list.append(a_i_c_l)
								ad_sorter_list = list(zip(luminance_list, adjusted))
								ad_sorter_list = sorted(ad_sorter_list, key=lambda color: color[0])
								ad_sorted_list = [i[1] for i in ad_sorter_list]
								if window_1_values['dark'] == True:
									ad_dark_list = [ad_sorted_list[0], ad_sorted_list[6], ad_sorted_list[7],
										 ad_sorted_list[1], ad_sorted_list[2], ad_sorted_list[7],
										 ad_sorted_list[1], ad_sorted_list[8], ad_sorted_list[3]]
									adjusted_theme += generate_theme_code(ad_dark_list, 'Dark', True)
								if window_1_values['light'] == True:
									ad_light_list = [ad_sorted_list[7], ad_sorted_list[1], ad_sorted_list[0],
										  ad_sorted_list[6], ad_sorted_list[5], ad_sorted_list[0],
										  ad_sorted_list[6], ad_sorted_list[4], ad_sorted_list[8]]
									adjusted_theme += generate_theme_code(ad_light_list, 'Light', True)
								if window_1_values['grayout'] == True:
									# This is the Gray-Out feature. It gives a black-and-white effect to themes.
									ad_gray_list = []
									for a_i in ad_sorted_list:
										a_i = colour.Color(a_i)
										a_i.saturation = 0
										ad_gray_list.append(a_i.get_web())
									adjusted_theme += generate_theme_code(ad_gray_list, 'Gray', True)
								output_window['output'](adjusted_theme)
								if not output_window_values['preview_x_adj']:
									preview_process(adjusted_theme)
							
							if output_window_events == 'adjust_shf':
								shf_revert_cache = output_window_values['shuffled_theme']
								output_window['adjust_shf'](visible=False)
								output_window['revert_shf'](visible=True)
								shf_adjusted = adjust_readability(colors=get_colors_of_theme_code(output_window_values['shuffled_theme']))
								shf_adjusted_theme = generate_shuffled_theme(shf_adjusted)
								output_window['shuffled_theme'](shf_adjusted_theme)
								if not output_window_values['preview_x_adj_shf']:
									sh_preview_process(shf_adjusted_theme)
	
							if output_window_events == 'revert':
								output_window['revert'](visible=False)
								output_window['adjust'](visible=True)
								output_window['output'](revert_cache)
								revert_cache = None
							
							if output_window_events == 'revert_shf':
								output_window['revert_shf'](visible=False)
								output_window['adjust_shf'](visible=True)
								output_window['shuffled_theme'](shf_revert_cache)
								shf_revert_cache = None
	
							if output_window_events == 'reuse':
								reuse_process(output_window_values['output'])
							
							if output_window_events == 'reuse_shf':
								reuse_process(output_window_values['shuffled_theme'])
								
							if output_window_events == 'copy':
								copy((output_window_values['output']))
								sg.Popup("Your theme code has been copied!", title='Copied!', auto_close=True,
										 auto_close_duration=4,
										 location=(output_window.CurrentLocation()[0], output_window.CurrentLocation()[1]))
							if output_window_events == 'shf_copy':
								copy((output_window_values['shuffled_theme']))
								sg.Popup("Your shuffled theme code has been copied!", title='Copied!', auto_close=True,
										 auto_close_duration=4,
										 location=(output_window.CurrentLocation()[0], output_window.CurrentLocation()[1]))
							if 'preview' in output_window_events:
								if output_window_events == 'preview':
									preview_process(theme)
								if output_window_events == 'shf_preview':
									sh_preview_process(s_theme)
				except:
					theme_change()
					sg.Popup('A fatal error occured! Please check your entries! You may have typed in an '
							 'unsupported character for your theme name or put in a wrong color value.', title='Error!')

			finisher(color_values=color_values)

	if window_1_events == 'preview':
		meta_layout = [[sg.Text(('This is a window of all {0} themes that are built into PySimpleGUI'.format(str(len(sg.ListOfLookAndFeelValues())))), text_color=sg.theme_input_text_color(), background_color=sg.theme_input_background_color())]]

		row = []
		for count, theme in enumerate(sg.theme_list()):
			sg.theme(theme)
			if not count % 10:
				meta_layout += [row]
				row = []
			row += [sg.Frame(theme, layout=[[sg.Text('This is a text element.')],
											[sg.InputText('This is a place to input text.')],
											[sg.Button('OK'), sg.Button('Cancel')]], border_width=4)]
		if row:
			meta_layout += [row]
		theme_change()
		layout = [[sg.Text('Built-In Themes', font=('Helvetica', 18))],
				  [sg.Column(background_color=sg.theme_input_background_color(),
							 layout=meta_layout, size=(600, 300), scrollable=True)],
				  [sg.Button('Close')]]
		theme_preview = sg.Window('Preview All Built-In Themes', layout, location=loc8or.get_ideal_location(layout, 'UC', 'UC', immediate_window_height))
		while True:
			th_e = theme_preview.Read()[0]
			if th_e in (None, 'Close'):
				theme_preview.Close()
				break
	if window_1_events == 'update':
		confirmation_layout = [
			[sg.Text('You chose to update PySimpleGUI.')],
			[sg.Text('Are you sure about this?\nThemera will be unresponsive while this happens.')],
			[sg.Button('I\'m Sure.', key='Sure'), sg.Button('Cancel', key='Cancel')]
		]
		confirmation = sg.Window('Are you sure?', layout=confirmation_layout, element_justification='center', location=loc8or.get_ideal_location(confirmation_layout, 'UC', 'UC', popup_height))
		while True:
			conf_e = confirmation.Read()[0]
			confirmation.NonBlocking = True
			if conf_e in (None, 'Cancel'):
				confirmation.Close()
				break
			if conf_e == 'Sure':
				cmd('python -m pip install --upgrade --no-cache-dir PySimpleGUI')
				confirmation.Close()
				break
	if window_1_events == 'col_name_view':
		color_names = []
		for j in color_names_list:
			color_names.append(([sg.Text(text=(str(j)),
										 size=(20, 1),
										 text_color=sg.theme_input_text_color(),
										 background_color=sg.theme_input_background_color()),
								 sg.DummyButton('', button_color=('#000000', str(colour.Color(str(j)).get_hex_l())),
												size=(10, 1))]))

		viewer_layout = [
			[sg.Text('Valid Color Names', font=('Helvetica', 18))],
			[sg.Text(text=('These are the names of ' + str(len(color_names)) + ' valid color names.'))],
			[sg.Text('Just for reference.')],
			[sg.Text('Ranked from darkest to lightest.')],
			[sg.Column(layout=color_names, size=(250, 200), scrollable=True, vertical_scroll_only=True,
					   background_color=sg.theme_input_background_color())],
			[sg.Button('Exit')]
		]
		viewer = sg.Window('Valid Color Name List', layout=viewer_layout,
						   location=loc8or.get_ideal_location(viewer_layout, 'UC', 'UC', subwindow_height))
		while True:
			viewer_e = viewer.Read()[0]
			viewer.NonBlocking = True
			if viewer_e in (None, 'Exit'):
				viewer.Close()
				break
	if 'checkout' in window_1_events:
		# I don't want to go importing this big dog if I'm not going to use him.
		from webbrowser import open_new_tab as hyp_lnk

		if window_1_events == 'checkout_me':
			hyp_lnk('https://www.github.com/definite-d/')
		if window_1_events == 'checkout_themera':
			hyp_lnk('https://www.github.com/definite-d/Themera/')
		if window_1_events == 'checkout_psg':
			hyp_lnk('https://www.github.com/PySimpleGUI/PySimpleGUI/')

	if window_1_events == 'Help':
		help_text = 'Current Version: {0}\n' \
					'Username: {1}\n\n' \
					'Specifier Tab:\n' \
					'Specifying your theme\'s parameters is done using the Specifier tab. ' \
					'Simply click the buttons or type them in to choose colors manually. ' \
					'Tkinter color names also work.  \n\n' \
					'View Supported Colors:\n' \
					'You can view all supported colors and their names from the \'Other Options\' tab, ' \
					'in the \'Color Options\' panel.\n\n' \
					'Unspecified Colors:\n' \
					'If no color is given, Themera will prompt you to choose what to do about that ' \
					'and present you with the options to fill in the colors not supplied with random colors, ' \
					'base the colors not given off those given, choose colors from an image' \
					' or go back to supply those colors fully.\n\n' \
					'There\'s also some options that affect what happens with whatever option you choose at ' \
					'that point. They can be found in the \'Other Options\' tab under the ' \
					'\'\'Unspecified Color\' Actions\' panel.\n\n' \
					'Choosing \'Haphazard Random\' will leave the colors unordered after random colors' \
					' have been picked, as Themera arranges the random colors by default to give a usable' \
					' theme.\n' \
					'\'Complementary Mono\' is an option that works best when only one color is chosen, as Themera ' \
					'is aware when only one color is chosen and uses a different color picking process for such ' \
					'cases. \nWith \'Complementary Mono\', the complementary color of the single color picked ' \
					'gets involved in the color picking process.\n\n' \
					'Don\'t forget to check out the other options in the Other Options tab.\n' \
					'And yes, the logo is clickable.'.format(__version__, user())
		help_layout = [
			[sg.Text('Help', font=('Helvetica', 18)), sg.Text(' ' * 104), sg.Button('Close', key='exit')],
			[sg.Multiline(default_text=help_text, disabled=True, size=(60, 10))]
		]
		help_window = sg.Window('Help', help_layout,
								location=loc8or.get_ideal_location(help_layout, 'UC', 'UC', subwindow_height))
		while True:
			help_events = help_window.Read()[0]
			if help_events in (None, 'exit'):
				help_window.Close()
				break

	if window_1_events in (None, 'Exit', 'Cancel'):  # The customary exit route.
		try:
			output_window.Close()
			preview.Close()
			window_1.Close()
			break
		except:
			pass
			break

if selected_theme != theme_switch:
	theme_switch_registrar(selected_theme)
	preferences_file.close()

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
