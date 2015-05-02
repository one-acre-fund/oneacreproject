import guidefault, guidata
import oneAcreLP
import os, sys, subprocess
from PyQt4.QtCore import Qt, QSize, QMargins
from PyQt4.QtGui import (QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QInputDialog, 
                         QPushButton, QFileDialog, QComboBox, QSizePolicy, QMessageBox)

# Input Tab
class InputTab(guidefault.DefaultTab):
    # Parent
    parent = None

    # File identifying constants
    DISTANCEFILE = "Distance Matrix"
    WEIGHTFILE = "Site Weights"
    COSTFILE = "Cost Matrix"
    
    # Save file locations
    distanceFile = guidata.FILENONE
    weightFile = guidata.FILENONE
    costFile = guidata.FILENONE
    lastFile = "../"

    # Instance variable widgets needed when "save" is clicked
    warehouseCombo = None
    destinations = None
    trucks = None
    costLabel = None
    districtCombo = None
    distanceLabel = None
    weightLabel = None

    # Widgets related to warehouses and districts, for disabling purposes
    warehouseWidgets = []
    districtWidgets = []

    def __init__(self, parent):
        """
        Constructor
        """
        super().__init__()
        self.parent = parent

        mainBox = QVBoxLayout()
        
        title = QLabel("Input")
        titleFont = title.font()
        if sys.platform == "win32":
            titleFont.setPointSize(12)
        elif sys.platform == "darwin":
            titleFont.setPointSize(17)
        titleFont.setBold(True)
        title.setFont(titleFont)
        title.setAlignment(Qt.AlignCenter)

        description = QLabel("Use this to provide input data for calculation in the model. "
                             "You can select inputs from a previously saved warehouse through the dropdown. "
                             "Afterwards, you can select from the multiple districts associated with the warehouse. "
                             "Use the \"Add\" buttons to add new districts or warehouses. "
                             "Use the \"Select\" buttons to select new spreadsheets from file. "
                             "Use the \"Edit\" buttons to make changes to previously saved spreadsheets. "
                             "Don't forget to click \"Save\" to save your changes.")
        descriptionFont = description.font()
        if sys.platform == "win32":
            descriptionFont.setPointSize(10)
        elif sys.platform == "darwin":
            descriptionFont.setPointSize(15)
        description.setFont(descriptionFont)
        description.setWordWrap(True)
        description.setAlignment(Qt.AlignJustify)
        
        (warehouseBox, self.warehouseCombo) = self.createComboBox("Warehouse:", [], 0)
        (destinationsBox, self.destinations) = self.createTextBox("Destinations/Truck:")
        (trucksBox, self.trucks) = self.createTextBox("Max Trucks/Warehouse/Day:")
        (costBox, costSButton, costEButton, self.costLabel) \
            = self.createSelectBox("Select Cost Matrix", "")
        warehouseButton = self.createWButton("Add New Warehouse")
        warehouseDButton = self.createWButton("Delete Warehouse")
        
        (districtBox, self.districtCombo) = self.createComboBox("District:", [], 0)
        (distanceBox, distanceSButton, distanceEButton, self.distanceLabel) \
            = self.createSelectBox("Select Distance Matrix", "")
        (weightBox, weightSButton, weightEButton, self.weightLabel) \
            = self.createSelectBox("Select Site Weights", "")
        districtButton = self.createWButton("Add New District")
        districtDButton = self.createWButton("Delete District")
        
        botBox = QHBoxLayout()
        saveButton = QPushButton("Save")
        solveButton = QPushButton("Solve")
        botBox.addStretch(1)
        botBox.addWidget(saveButton)
        botBox.addWidget(solveButton)
        botBox.addStretch(1)

        mainBox.addWidget(title)
        mainBox.addWidget(description)
        mainBox.addWidget(self.hLine())
        mainBox.addLayout(warehouseBox)
        mainBox.addLayout(destinationsBox)
        mainBox.addLayout(trucksBox)
        mainBox.addLayout(costBox)
        mainBox.addWidget(warehouseButton)
        mainBox.addWidget(warehouseDButton)
        mainBox.addWidget(self.hLine())
        mainBox.addLayout(districtBox)
        mainBox.addLayout(distanceBox)
        mainBox.addLayout(weightBox)
        mainBox.addWidget(districtButton)
        mainBox.addWidget(districtDButton)
        mainBox.addWidget(self.hLine())
        mainBox.addStretch(1)
        mainBox.addLayout(botBox)

        self.setLayout(mainBox)
        
        self.warehouseCombo.currentIndexChanged.connect(self.warehouseChanged)
        self.districtCombo.currentIndexChanged.connect(self.districtChanged)
        warehouseButton.clicked.connect(self.warehouseButtonClicked)
        warehouseDButton.clicked.connect(self.warehouseDButtonClicked)
        districtButton.clicked.connect(self.districtButtonClicked)
        districtDButton.clicked.connect(self.districtDButtonClicked)
        distanceSButton.clicked.connect(self.distanceSButtonClicked)
        weightSButton.clicked.connect(self.weightSButtonClicked)
        costSButton.clicked.connect(self.costSButtonClicked)
        distanceEButton.clicked.connect(self.distanceEButtonClicked)
        weightEButton.clicked.connect(self.weightEButtonClicked)
        costEButton.clicked.connect(self.costEButtonClicked)
        saveButton.clicked.connect(self.saveButtonClicked)
        solveButton.clicked.connect(self.solveButtonClicked)
        
        self.warehouseWidgets.append(self.destinations)
        self.warehouseWidgets.append(self.trucks)
        self.warehouseWidgets.append(costSButton)
        self.warehouseWidgets.append(costEButton)
        self.warehouseWidgets.append(warehouseDButton)
        self.warehouseWidgets.append(saveButton)
        self.warehouseWidgets.append(districtButton)
        self.districtWidgets.append(distanceSButton)
        self.districtWidgets.append(distanceEButton)
        self.districtWidgets.append(weightSButton)
        self.districtWidgets.append(weightEButton)
        self.districtWidgets.append(districtDButton)
        self.districtWidgets.append(solveButton)

        self.loadAllData(None, None)
    
    def createComboBox(self, labelText, options, default):
        """
        Creates a Layout containing a Label and a ComboBox Widget
        The ComboBox contains a given list of options
        @param labelText The text on the label 
        @param options The list of string options
        @param default The integer index of the default option
        @return (Layout, ComboBoxWidget) as a tuple
        """
        label = QLabel(labelText)
        combo = QComboBox(self)
        for option in options:
            combo.addItem(option)
        combo.setCurrentIndex(default)
        combo.setMinimumWidth(200)

        box = QHBoxLayout()
        box.addWidget(label)
        box.addStretch(1)
        box.addWidget(combo)
        
        return (box, combo)
    
    def createWButton(self, buttonText):
        """
        Creates a Button that takes up the whole width
        @param buttonText The text on the button
        @return The button
        """
        button = QPushButton(buttonText)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        return button

    def createTextBox(self, labelText):
        """
        Creates a Layout containing a Label
        Followed by a LineEdit Widget (The "text")
        @param labelText The text of the label
        @return (layout, LineEditWidget) as a tuple
        """
        label = QLabel(labelText)
        text = QLineEdit()
        text.setMinimumWidth(200)
        
        box = QHBoxLayout()
        box.addWidget(label)
        box.addStretch(1)
        box.addWidget(text)

        return (box, text)
    
    def createSelectBox(self, buttonText, labelText):
        """
        Creates a Layout containing 2 buttons and a Label
        The first button allows the user to "Select" from file
        The second button allows the user to "Edit" currently selected file
        @param buttonText The text on the first button
        @param labelText The text on the label
        @return (layout, button1, button2, label) as a tuple
        """
        button1 = QPushButton(buttonText)
        button1.setMinimumWidth(220)
        button1.setMaximumWidth(220)
        button2 = QPushButton("Edit")
        button2.setMinimumWidth(100)
        button2.setMaximumWidth(100)
        label = QLabel(labelText)
        
        box = QHBoxLayout()
        box.addWidget(button1)
        box.addWidget(button2)
        box.addStretch(1)
        box.addWidget(label)

        return (box, button1, button2, label)

    def loadDistrictData(self):
        """
        Loads all data associated with the currently selected district onto the GUI
        """
        warehouse = self.warehouseCombo.currentText()
        district = self.districtCombo.currentText()
        if not district:
            self.enableDistrictWidgets(False)
            return
        self.enableDistrictWidgets(True)
        (d, w) = guidata.getDistrictInfo(warehouse, district)
        if d != guidata.FILENONE:
            self.distanceLabel.setText("Saved in data directory.")
            self.distanceFile = d
        else:
            self.distanceLabel.setText(guidata.FILENONE)
            self.distanceFile = guidata.FILENONE
        if w != guidata.FILENONE:
            self.weightLabel.setText("Saved in data directory.")
            self.weightFile = w
        else:
            self.weightLabel.setText(guidata.FILENONE)
            self.weightFile = guidata.FILENONE
        return
   
    def loadDistricts(self, districtName):
        """
        Loads the district list and its associated data onto the GUI
        If districtName is empty, the first district is picked
        @param districtName
        """
        warehouse = self.warehouseCombo.currentText()
        self.districtCombo.clear()
        districts = guidata.getDistricts(warehouse)
        for district in districts:
            self.districtCombo.addItem(district)
        if districtName:
            districtIndex = self.districtCombo.findText(districtName)
            if districtName != -1:
                self.districtCombo.setCurrentIndex(districtIndex)
        self.loadDistrictData()

    def loadWarehouseData(self, districtName):
        """
        Loads all data associated with the currently selected warehouse onto the GUI
        If districtName is empty, the first district is picked
        @param districtName
        """
        self.loadDistricts(districtName)
        warehouse = self.warehouseCombo.currentText()
        if not warehouse:
            self.enableWarehouseWidgets(False)
            return
        self.enableWarehouseWidgets(True)
        (d, t, c) = guidata.getWarehouseInfo(warehouse)
        if not d:
            self.destinations.setText("2")
        else:
            self.destinations.setText(d)
        if not t:
            self.trucks.setText("1000")
        else:
            self.trucks.setText(t)
        if c != guidata.FILENONE:
            self.costLabel.setText("Saved in data directory.")
            self.costFile = c
        else:    
            self.costLabel.setText(guidata.FILENONE)
            self.costFile = guidata.FILENONE
        return
 
    def loadAllData(self, warehouseName, districtName):
        """
        Loads all data, including the lists, onto the GUI
        Clears any previous data loaded to the GUI
        If warehouseName is empty, the first warehouse is picked
        If districtName is empty, the first district is picked
        @param warehouseName
        @param districtName
        """
        self.warehouseCombo.clear()
        warehouses = guidata.getWarehouses()
        for warehouse in warehouses:
            self.warehouseCombo.addItem(warehouse)
        if warehouseName:
            warehouseIndex = self.warehouseCombo.findText(warehouseName)
            if warehouseIndex != -1:
                self.warehouseCombo.setCurrentIndex(warehouseIndex)
        self.loadWarehouseData(districtName)
    
    def enableWarehouseWidgets(self, enable):
        """
        Call this to enable/disable all widgets that require a warehouse to be selected
        Does not include the district widgets
        @param enable True or False
        """
        for widget in self.warehouseWidgets:
            widget.setEnabled(enable)
        if not enable:
            self.costLabel.setText("")

    def enableDistrictWidgets(self, enable):
        """
        Call this to enable/disable all widgets that require a district to be selected
        @param enable True or False
        """
        for widget in self.districtWidgets:
            widget.setEnabled(enable)
        if not enable:
            self.distanceLabel.setText("")
            self.weightLabel.setText("")
    
    def warehouseChanged(self, name):
        """
        Handles when a new warehouse is selected
        """
        self.loadWarehouseData(None)
        
    def districtChanged(self, name):
        """
        Handles when a new warehouse is selected
        """
        self.loadDistrictData()

    def warehouseButtonClicked(self):
        """
        Handles when "Add Warehouse" is clicked
        """
        name, ok = QInputDialog.getText(self, "Add New Warehouse", "Warehouse Name:")
        if ok:
            success, errorString = guidata.addWarehouse(name)
            if not success:
                QMessageBox.critical(self, "Error", errorString)
                return
            if errorString:
                QMessageBox.warning(self, "Warning", errorString)
            self.loadAllData(name, None)
    
    def districtButtonClicked(self):
        """
        Handles when "Add Warehouse" is clicked
        """
        warehouseName = self.warehouseCombo.currentText()
        name, ok = QInputDialog.getText(self, "Add New District", "District Name:")
        if ok:
            success, errorString = guidata.addDistrict(warehouseName, name)
            if not success:
                QMessageBox.critical(self, "Error", errorString)
                return
            if errorString:
                QMessageBox.warning(self, "Warning", errorString)
            self.loadDistricts(name)
 
    def distanceSButtonClicked(self):
        """
        Handles when distance button is clicked
        """
        self.changeUploadedFile(self.DISTANCEFILE)

    def weightSButtonClicked(self):
        """
        Handles when weight button is clicked
        """
        self.changeUploadedFile(self.WEIGHTFILE)
    
    def costSButtonClicked(self):
        """
        Handles when cost button is clicked
        """
        self.changeUploadedFile(self.COSTFILE)

    def distanceEButtonClicked(self):
        """
        Handles when distance edit button is clicked
        """
        self.editUploadedFile(self.DISTANCEFILE)

    def weightEButtonClicked(self):
        """
        Handles when weight edit button is clicked
        """
        self.editUploadedFile(self.WEIGHTFILE)
    
    def costEButtonClicked(self):
        """
        Handles when cost edit button is clicked
        """
        self.editUploadedFile(self.COSTFILE)
    
    def warehouseDButtonClicked(self):
        """
        Handles when the delete warehouse button is clicked
        """
        name = self.warehouseCombo.currentText()
        reply = QMessageBox.question(self, "Delete Warehouse", 
                "Are you you want to delete warehouse %s?" % name,
                QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            success, errorString = guidata.deleteWarehouse(name)
            if not success:
                QMessageBox.critical(self, "Error", errorString)
                return
            if errorString:
                QMessageBox.warning(self, "Warning", errorString)
            self.loadAllData(None, None)

    def districtDButtonClicked(self):
        """
        Handles when the delete district button is clicked
        """
        warehouseName = self.warehouseCombo.currentText()
        name = self.districtCombo.currentText()
        reply = QMessageBox.question(self, "Delete District", 
                "Are you you want to delete district %s from warehouse %s?" 
                % (name, warehouseName), QMessageBox.Yes|QMessageBox.No, 
                QMessageBox.No)
        if reply == QMessageBox.Yes:
            success, errorString = guidata.deleteDistrict(warehouseName, name)
            if not success:
                QMessageBox.critical(self, "Error", errorString)
                return
            if errorString:
                QMessageBox.warning(self, "Warning", errorString)
            self.loadDistricts(None)
    
    def saveInfo(self):
        """
        Saves info
        @return (success, errorString) as a tuple, success is True/False
        """
        warehouseName = self.warehouseCombo.currentText()
        districtName = self.districtCombo.currentText()
        success, errorString = guidata.saveInfo(warehouseName, districtName, 
                                                self.destinations.text(), self.trucks.text(), 
                                                self.distanceFile, 
                                                self.weightFile, 
                                                self.costFile)
        return (success, errorString)

    def saveButtonClicked(self):
        """
        Handles when save button is clicked
        """
        warehouseName = self.warehouseCombo.currentText()
        districtName = self.districtCombo.currentText()
        success, errorString = self.saveInfo()
        if not success:
            QMessageBox.critical(self, "Error", errorString)
            return
        if errorString:
            QMessageBox.warning(self, "Warning", errorString)
        else:
            QMessageBox.information(self, "Success", "Saved successfully")
        self.loadAllData(warehouseName, districtName)
    
    def solveButtonClicked(self):
        """
        Handles when solve button is clicked
        """
        warehouseName = self.warehouseCombo.currentText()
        districtName = self.districtCombo.currentText()
        success, errorString = self.saveInfo()
        if success:
            self.loadAllData(warehouseName, districtName)
        
        (d, t, c, districtList) = guidata.getAllWarehouseInfo(warehouseName)
        if not d:
            QMessageBox.critical(self, "Error", "Please enter a valid Destinations/Truck value.")
            return
        if not t:
            QMessageBox.critical(self, "Error", "Please enter a valid Trucks/Warehouse/Day value.")
            return
        if c == guidata.FILENONE:
            QMessageBox.critical(self, "Error", "Please upload a Cost Matrix first.")
            return
        
        goodDistricts = []
        badDistricts = []
        for district in districtList:
            if district[1] == guidata.FILENONE or district[2] == guidata.FILENONE:
                badDistricts.append(district)
            else:
                goodDistricts.append(district)
        if len(goodDistricts) == 0:
            QMessageBox.critical(self, "Error", "Upload all spreadsheets for at least one district first.")
            return
        if len(badDistricts) > 0:
            text = ("District data for the following districts will not be included "
                    "because one or more associated spreadsheets are missing: \n") 
            for district in badDistricts:
                text += "* " + district[0] + "\n"
            text += "Do you still want to continue?"
            reply = QMessageBox.question(self, "Run Solver", text,
                    QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
            if reply != QMessageBox.Yes:
                return
        
        # TODO: Note that Back End doesn't use d and t currently
        # TODO: Temporary test code
        if not success:
            QMessageBox.warning(self, "Warning", "Solver will still run. " + errorString)
        error = oneAcreLP.solve(self.parent, warehouseName, c, goodDistricts)
        if not error:
            self.parent.setCurrentIndex(self.parent.OUTPUTTABINDEX)
        else:
            QMessageBox.critical(self, "Error", error)
    
    def changeUploadedFile(self, fileType):
        """
        Listener that pops up a file dialog to allow user to change uploaded file
        @param fileType Use constants DISTANCEFILE, etc...
        """
        fileName = QFileDialog.getOpenFileName(self, "Open " + fileType,
                                               self.lastFile, "*.xls *.xlsx")
        if fileName != "":
            self.lastFile = fileName
            if fileType == self.DISTANCEFILE:
                self.distanceFile = fileName
                self.distanceLabel.setText(fileName)
            elif fileType == self.WEIGHTFILE:
                self.weightFile = fileName
                self.weightLabel.setText(fileName)
            elif fileType == self.COSTFILE:
                self.costFile = fileName
                self.costLabel.setText(fileName)

    def editUploadedFile(self, fileType):
        """
        Opens up a file using Excel for editing
        @param fileType Use constants DISTANCEFILE, etc...
        """
        theFile = ""
        if fileType == self.DISTANCEFILE:
            theFile = self.distanceFile
        elif fileType == self.WEIGHTFILE:
            theFile = self.weightFile
        elif fileType == self.COSTFILE:
            theFile = self.costFile
        else:
            return
        if theFile == guidata.FILENONE:
            return
        if sys.platform == "win32":
            os.startfile(theFile)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, theFile])
