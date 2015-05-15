# oneacreproject


Description
------------------------
This project is a Dynamic Schedule Optimizer program for One Acre Fund. It includes a GUI interface that requires PyQt4, linked to a backend linear program solver. Tested on WINDOWS and MACINTOSH systems.

Requirements
------------------------
1. Python 3.4
2. PyQt4 4.11.3
3. PuLP 1.5.6
4. xlrd 0.9.3
5. xlwt 1.0.0

Installation
------------------------
For PyQt4 on Windows:
- Install Python 3.4 as usual
- There's a very nice PyQt4 installer on the PyQt website, please use it :)

For PyQt4 on Mac:
- Go to Mac App store and install XCode
- Install XCode Command Line tools 
```
xcode-select --install
```
-  

For the rest of the packages:
1. Download the Package
2. Unzip and type "python setup.py install"

Running
------------------------
python guimain.py

Organization
------------------------
1. guimain.py - sets up the PyQt application
2. guidata.py - loading/saving data (in JSON format)
3. guiinput.py - Input tab
4. guioutput.py - Output tab
5. oneAcreLP.py - PuLP linear program code
6. Some other files included

Deployment
------------------------

2. wxPython - http://www.wxpython.org/

Mac Instructions for installing PyQt5:

Following instructions mostly from:
http://www.pythonschool.net/pyqt/distributing-your-application-on-mac-os-x/

Install XCode (From Mac App store)
Install XCode Command Line Tools
==> xcode-select --install
Download the pkg installer for MacPorts for your version of OS X
Follow the installer to install MacPorts
Use MacPorts to install PyQT5
==> sudo port selfupdate
==> sudo port install py34-pyqt5

1. List the available pythons to select from:
==> sudo port select --list python

run version python3.4 through terminal
==> sudo port select python python34

The error message pops up while installing pulp 1.5.8

ImportError: No module named 'pkg_resources'

1) Download ez_setup.py module from

https://pypi.python.org/pypi/setuptools

2) Open a Terminal

3) cd to the directory where you put the 'ez_setup.py'

4) type 'python ez_setup.py' and run it.

5) You should have it then.

