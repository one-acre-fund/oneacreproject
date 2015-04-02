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

# guidata global jsonData dictionary
jsonData = None

def saveJsonData():
    """
    Saves the jsonData in RAM to file
    @return None if no error, or String error if there is one
    """
    global jsonData
    try:
        with open(indexFile, 'w') as f:
            json.dump(jsonData, f, indent=4)
    except OSError as e:
        return ("unable to save to %s in directory %s. %s" 
                % (indexFile, dataDir, e.strerror))
    return None

def addWarehouse(warehouseName):
    """
    Adds a new warehouse
    @param warehouseName
    @return (success, errorString) as a tuple, success is True/False
    """
    global jsonData
    if warehouseName in jsonData:
        return (False, "There is already a warehouse named %s added"
                % warehouseName)
    jsonData[warehouseName] = {}
    error = saveJsonData()
    if error:
        return (True, "Warehouse was added, but " + error)
    return (True, "")

def getWarehouses():
    """
    Returns a list of warehouse names, sorted alphabetically
    @return the list
    """
    global jsonData
    wList = list(jsonData.keys())
    wList.sort()
    return wList

def addDistrict(warehouseName, districtName):
    """
    Adds a new district to be associated with a warehouse
    @param districtName
    @param warehouseName
    @return (success, errorString) as a tuple, success is True/False
    """
    global jsonData
    if districtName in jsonData[warehouseName]:
        return (False, "There is already a district named %s added to warehouse %s"
                % (districtName, warehouseName))
    jsonData[warehouseName][districtName] = {}
    error = saveJsonData()
    if error:
        return (True, "District was added, but " + error)
    return (True, "")

def getDistricts(warehouseName):
    """
    Returns a list of district names, sorted alphabetically
    @param warehouseName Name of warehouse, or None
    @return the list, [] returned if no warehouse provided
    """
    global jsonData
    if not warehouseName:
        return []
    dList = list(jsonData[warehouseName].keys())
    dList.sort()
    return dList

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

def saveInfo(warehouseName, districtName, destPerTruck, 
        truckPerW, distanceFile, weightFile, costFile):
    """
    Saves data for a new district-warehouse 
    @return None if successful, or an error string if there is an error
    """
    global jsonData
    
    # Make sure districtName_warehouseName is useable
    warehouseName = warehouseName.strip()
    districtName = districtName.strip()
    name = warehouseName + "_" + districtName
    try:
        open(name, 'w').close()
        os.unlink(name)
    except OSError:
        return ("Make sure %s and %s are legal file names, ie does not contain illegal characters." 
                % (districtName, warehouseName))
    
    # Save meta data
    if districtName not in jsonData:
        jsonData[districtName] = {}
        jsonData[districtname][distanceSuffix] = None
        jsonData[name][weightSuffix] = None
    jsonData[districtName][costSuffix] = None
    jsonData[districtName][destinationsSuffix] = destPerTruck
    jsonData[districtName][trucksSuffix] = truckPerW
    
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
    

    return None

def getInfo(warehouseName, districtName):
    """
    Returns the associated info with the given warehouse and district
    Returns a tuple
    @return (destPerTruck, truckPerW, distanceFile, weightFile, costFile)
    """
    # TODO: Finish
    return

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

def loadJsonData():
    """
    Loads the json data from index.json file
    Creates the index.json file if it does not exist
    @return True if success, False if failure
    """
    global jsonData
    if os.path.isfile(indexFile) and not os.path.isdir(dataDir):
        try:
            with open(indexFile, 'r+') as f:
                jsonData = json.load(f)
        except OSError as e:
            print("Error: Cannot read from/write to %s in directory %s as json file. %s" 
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
    if not loadJsonData():
        return False
    return True
