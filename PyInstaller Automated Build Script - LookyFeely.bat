echo Testing Command Prompt... Testing...
echo Automated Build Commencing...

cd C:\Users\Definite\Temporary\Documents\Code Scripts\Python\LookyFeely
python ^
-m ^
PyInstaller ^
--windowed ^
--onefile ^
--clean ^
--icon="icon\lf_ico.ico" ^
--name="PSGLookyFeely" ^
PSGLookyFeely.py
