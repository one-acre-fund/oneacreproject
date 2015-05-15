# oneacreproject


Description
------------------------
This project is a Dynamic Schedule Optimizer program for One Acre Fund. It includes a GUI interface that requires PyQt4

Requirements
------------------------
1. Python 3.4
2. PyQt4 4.11.3
3. 

Organization
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

