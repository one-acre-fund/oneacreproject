# oneacreproject

Description
------------------------
This project is a Dynamic Schedule Optimizer program for One Acre Fund. It includes a GUI interface that requires PyQt4, linked to a backend linear program solver. Tested on WINDOWS and MACINTOSH systems.

NOTES ON USAGE: Pressing "Edit" (After you've saved a spreadsheet) will open up that spreadsheet in your local Excel Editor. Make sure you save the spreadsheet in the editor for any changes you make to be permanent.

FEATURES NOT COMPLETELY ADDED YET: "Destinations/Truck" and "Max Trucks/Warehouse/Day" are currently editable on the front end, but are not supported by the linear program solver.

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
- Download the pkg installer for MacPorts for your version of OS X
- Follow the installer to install MacPorts
- Use MacPorts to install Python 3.4, PyQt4, and py2app (needed for deployment)
```
sudo port install python34
port select python python34
sudo port install py34-macholib 
sudo port install py34-sip
sudo port install py34-pyqt4
sudo port install py34-py2app
```

For the rest of the packages:
- Download the Package
- Unzip and install 
```
python setup.py install
```

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
We've only deployed on MACINTOSH so far, and it requires py2app. Please follow the instructions in "Installation" above to install it. Follow instructions on this page:
- https://pythonhosted.org/py2app/tutorial.html
- Make sure that the includes contain "sip" and other modules listed above
