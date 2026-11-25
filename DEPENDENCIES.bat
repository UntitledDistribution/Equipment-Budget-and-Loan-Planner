@echo off

:: Try calling PIP directly directly.

echo This script WILL call the PIP and Python process in order to install packages.
echo Do you want to continue? (close the window if you do not)
pause

:: Clear the CLI
cls

pip install pandas
pip install matplotlib
pip install termcolor
pip install clear
pip install readchar

:: if that fails, call PIP through Python as pip might not be in PATH.

python -m pip install pandas
python -m pip install matplotlib
python -m pip install termcolor
python -m pip install clear
python -m pip install readchar

:: Tell user the script has finished
echo.
echo ======================================
echo The script had finished. there is a chance you might see errors though this is probably normal as either Python OR Pip isn't registered in path.
echo If errors were produced all the way and you didn't see the CLI install anything. Try installing Python from https://python.org or manually view the content of this batch file and install it that way.
echo ======================================
echo The script has finished.
color 17
pause


