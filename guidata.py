import os
import sys
import shutil
import json

# guidata module for saving/loading data
dataDir = "data"
indexFile = "index.json"
distanceSuffix = "_dm"
weightSuffix = "_sw"
costSuffix = "_cm"
destinationsSuffix = "_dt"
trucksSuffix = "_tw"

def copyFile(source, destination):
    """
    Copies file from source to destination
    @param source
    @param destination
    @return None if no error, or String error if there is one
    """
    try:
        shutil.copyfile(source, destination)
    except OSError as e:
        return ("Error: Unable to copy from %s to %s" 
                % (source, destination, e.strerror))
    return None

def saveData(districtName, warehouseName, destPerTruck, 
        truckPerW, distanceFile, weightFile, costFile):
    """
    Saves data for a new district-warehouse 
    @return None if successful, or an error string if there is an error
    """
    # Make sure districtName_warehouseName is useable
    districtName = districtName.strip()
    warehouseName = warehouseName.strip()
    name = districtName + "_" + warehouseName
    try:
        open(name, 'w').close()
        os.unlink(name)
    except OSError:
        return ("Make sure %s and %s are legal file names, ie does not contain illegal characters." 
                % (districtName, warehouseName))
    
    # Load json data
    jsonData = None
    with open(indexFile, 'r+') as f:
        jsonData = json.load(f)
    if jsonData is None:
        return "Cannot load json data"
    
    # Save meta data
    if name not in jsonData:
        jsonData[name] = {}
        jsonData[name][distanceSuffix] = None
        jsonData[name][weightSuffix] = None
        jsonData[name][costSuffix] = None
    jsonData[name][destinationsSuffix] = destPerTruck
    jsonData[name][trucksSuffix] = truckPerW
    
    ## Obtain abs paths for all files
    #distanceFileO = jsonData[name][distanceSuffix]
    #weightFileO = jsonData[name][weightSuffix]
    #costFileO = jsonData[name][costSuffix]
    #distanceFileS = os.path.abspath(distanceFile)
    #weightFileS = os.path.abspath(weightFile)
    #costFileS = os.path.abspath(costFile)
    #distanceFileN = os.path.abspath(name+distanceSuffix)
    #weightFileN = os.path.abspath(name+weightSuffix)
    #costFileN = os.path.abspath(name+costSuffix)
    #
    ## Do the copying
    #error = None
    #if distanceFileS != distanceFileO:
    #    if not
    
    # Save json data
    with open(indexFile, 'w') as f:
        json.dump(jsonData, f, indent=4)

    return None
    
def createDataDir():
    """
    Checks whether "data" directory exists
    If it does not, this creates it
    Note that this is used to save application related state
    @return True if success, False if failure
    """
    # TODO: Make this independent of where the program is run
    if os.path.isdir(dataDir):
        return True
    if os.path.exists(dataDir):
        print("Error: Unable to create directory %s since file exists" 
              % dataDir, file=sys.stderr)
        return False
    try:
        os.makedirs(dataDir)
    except OSError as e:
        print("Error: Unable to create directory %s. %s" 
              % (dataDir, e.strerror), file=sys.stderr)
        return False
    return True

def changeToDataDir():
    """
    Changes working directory to "data" directory
    @return True if success, False if failure
    """
    try:
        os.chdir(dataDir)
    except OSError as e:
        print("Error: Unable to change to directory %s. %s" 
              % (dataDir, e.strerror), file=sys.stderr)
        return False
    return True

def createIndexFile():
    """
    Creates the index.json file if it does not exist
    @return True if success, False if failure
    """
    if os.path.isfile(indexFile) and not os.path.isdir(dataDir):
        try:
            with open(indexFile, 'r+') as f:
                jsonData = json.load(f)
        except OSError as e:
            print("Error: Cannot write to %s in directory %s as json file. %s" 
                  % (indexFile, dataDir, e.strerror), file=sys.stderr)
            return False
        return True
    try:
        jsonData = {}
        with open(indexFile, 'w') as f:
            json.dump(jsonData, f)
    except OSError as e:
        print("Error: Cannot write to %s in directory %s as json file. %s" 
              % (indexFile, dataDir, e.strerror), file=sys.stderr)
        return False
    return True


def init():
    """
    Initializes data for the application
    @return True if success, False if failure
    """
    if not createDataDir():
        return False
    if not changeToDataDir():
        return False
    if not createIndexFile():
        return False
    return True
