@echo
cd C:\Users\Definite\Temporary\Documents\Code Scripts\Python\LookyFeely
pyinstaller ^
--windowed ^
--onefile ^
--clean ^
--icon="icon\lf_ico.ico" ^
--add-data="icon\lf_ico.ico;\icon" ^
--name="PSGLookyFeely" ^
PSGLookyFeely.py