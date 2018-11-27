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

**Additional notes on deployment**
------------------------

From Toby Krause, global logistics

As the software takes drop weights as one input, and then determines which truck of which size should go to which drop(s) - the only thing we have to manually add afterwards is the dates basically - it would somehow contradict with the R script proposal. As both the R script and the Optimizer determine which truck size should be used. For the optimizer to work, we would ideally only take the drop weights after the split and upload it. So the Optimizer would still work but would completely ignore the R script recommendation for the truck size. (For context, the R script in question is a proposal by Kenya to do some simple grouping in R to make the site splitting process more time efficient but not necessarily optimal.)

One issue why we can't use the Optimizer currently is because we upload available truck sizes and costs as well, but if one drop has more MT than the biggest available truck, it breaks and can't solve. 
* This means we want to test various splits in creating the drop weights and a) make sure that they don’t exceed the weight of the largest possible trucks and b) iterate through those splits to find the best possible option.
When we add bigger trucks to the Optimizer, the Optimizer of course utilizes those bigger trucks as much as possible to save costs - but as we don't have those bigger trucks, the schedule would not make sense anymore. 

As this student software is also far away from being perfect, I think we should discuss the way forward in general - while it would be nice to be able to use the software I would not say it as a must. 

I think it would be great to have a call and discuss the way forward in more detail. 

Thanks,
Toby
 
How does the Optimizer work in more detail?
As a very short description: we upload three files as input into the software: 
* site weights (which is actually drop weights and is the weight of all inputs we need to deliver to that drop)
* truck costs (how much transport costs us per truck size - based on the pricing structure we use in Kenya)
* distance matrix (the distances between all the different drops and the warehouse - we get this from Roster based on google maps). 
The output of the software is then a truck schedule, showing which truck of which size should go to which drop(s).  

The optimizer is an on-premise software, using Python and PuLP. 
I am also sharing the [Kenya Pilot Folder](https://drive.google.com/drive/u/1/folders/1GYvcMZhCkYjNaraRfUbVkkN5Mdh_w_Xl) for this with you, this is where we saved all the information about the trial we did this year. 
Within this folder, the sub-folder related to the actual software are "[OafOptimizer](https://drive.google.com/drive/u/1/folders/12NT9huy6nEN42cAfsGdAOg-tPkrmsq1M)" and "[Fleet Efficiency](https://drive.google.com/drive/u/1/folders/1kK8VfvzIE6fOklh3hEHWPBZlO-Pp4obP)" .

Within those folders the most helpful documents to get a general understanding are probably:
* [Software User Guide](https://drive.google.com/file/d/1-CQshnRhJJXw2CBBltpJNkyxYRq8YCex/view)
* [Final Presentation](https://drive.google.com/file/d/1DimD2bGH5ah9YoTe679QgJv-Eu0ttDjo/view)  (this is not the final presentation of the trial we did this year but from the students who developed the tool) 
* [Optimized Truck Schedule Example](https://drive.google.com/file/d/1lyH3sA9geV8Tqq1K_LliiFALKbaQneJq/view) (that's the tool output) 
* [Test files folder](https://drive.google.com/drive/u/1/folders/1vcNILDKfUlxdxqndf1XzszlAHesOhROA) (those three files are the input for the tool)


