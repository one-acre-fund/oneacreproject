import guidefault
import guidata
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, 
                             QPushButton, QFileDialog, QComboBox)

# Input Tab
class InputTab(guidefault.DefaultTab):
    
    # File identifying constants
    DISTANCEFILE = "Distance Matrix"
    WEIGHTFILE = "Site Weights"
    COSTFILE = "Cost Matrix"
    
    # Instance variable widgets needed when "save" is clicked
    combo = None
    district = None
    warehouse = None
    destinations = None
    trucks = None
    distanceLabel = None
    weightLabel = None
    costLabel = None

    def __init__(self):
        """
        Constructor
        """
        super().__init__()
    
        mainBox = QVBoxLayout()
        
        title = QLabel("Input")
        titleFont = title.font()
        titleFont.setPointSize(12)
        titleFont.setBold(True)
        title.setFont(titleFont)
        title.setAlignment(Qt.AlignCenter)

        description = QLabel("Use this to provide input data for calculation in the model. "
                             "You can select inputs from a previously saved warehouse, "
                             "or create new data by selecting \"New\". "
                             "For the spreadsheets, "
                             "use \"Select\" to select a new spreadsheet from file, "
                             "or \"Edit\" to make changes to the previously saved spreadsheet "
                             "associated with the warehouse.")
        description.setWordWrap(True)
        description.setAlignment(Qt.AlignJustify)
        
        (comboBox, self.combo) = self.createComboBox(["New"], 0)
        (districtBox, self.district) = self.createTextBox("District:") 
        (warehouseBox, self.warehouse) = self.createTextBox("Warehouse:")
        (destinationsBox, self.destinations) = self.createTextBox("Destinations/Truck:")
        (trucksBox, self.trucks) = self.createTextBox("Max Trucks/Warehouse/Day:")
 
        (distanceBox, distanceSButton, distanceEButton, self.distanceLabel) \
            = self.createSelectBox("Select Distance Matrix", "None selected.")
        (weightBox, weightSButton, weightEButton, self.weightLabel) \
            = self.createSelectBox("Select Site Weights", "None selected.")
        (costBox, costSButton, costEButton, self.costLabel) \
            = self.createSelectBox("Select Cost Matrix", "None selected.")
        
        botBox = QHBoxLayout()
        saveButton = QPushButton("Save")
        solveButton = QPushButton("Solve")
        deleteButton = QPushButton("Delete")
        botBox.addStretch(1)
        botBox.addWidget(saveButton)
        botBox.addWidget(solveButton)
        botBox.addWidget(deleteButton)
        botBox.addStretch(1)

        mainBox.addWidget(title)
        mainBox.addWidget(description)
        mainBox.addWidget(self.hLine())
        mainBox.addLayout(comboBox)
        mainBox.addWidget(self.hLine())
        mainBox.addLayout(districtBox)
        mainBox.addLayout(warehouseBox)
        mainBox.addLayout(destinationsBox)
        mainBox.addLayout(trucksBox)
        mainBox.addWidget(self.hLine())
        mainBox.addLayout(distanceBox)
        mainBox.addLayout(weightBox)
        mainBox.addLayout(costBox)
        mainBox.addStretch(1)
        mainBox.addLayout(botBox)

        self.setLayout(mainBox)

        distanceSButton.clicked.connect(self.distanceSButtonClicked)
        weightSButton.clicked.connect(self.weightSButtonClicked)
        costSButton.clicked.connect(self.costSButtonClicked)
        saveButton.clicked.connect(self.saveButtonClicked)
    
    def createComboBox(self, options, default):
        """
        Creates a Layout containing a ComboBox Widget 
        It contains a given list of options
        @param options The list of string options
        @param default The integer index of the default option
        @return (Layout, ComboBoxWidget) as a tuple
        """
        combo = QComboBox(self)
        for option in options:
            combo.addItem(option)
        combo.setCurrentIndex(default)
        combo.setMinimumWidth(215)
        combo.setMaximumWidth(215)
        
        box = QHBoxLayout()
        box.addWidget(combo)
        box.addStretch(1)
        
        return (box, combo)
    
    def createTextBox(self, labelText):
        """
        Creates a Layout containing a Label
        Followed by a LineEdit Widget (The "text")
        @param labelText The text of the label
        @return (layout, LineEditWidget) as a tuple
        """
        label = QLabel(labelText)
        text = QLineEdit()
        
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

    def saveButtonClicked(self):
        """
        Handles when save button is clicked
        """
        # TODO
        error = guidata.saveData(self.district.text(), self.warehouse.text(), self.destinations.text(),
                                 self.trucks.text(), "", "", "")
        if error:
            print(error)
        return
    
    def changeUploadedFile(self, fileType):
        """
        Listener that pops up a file dialog to allow user to change uploaded file
        @param fileType Use constants DISTANCEFILE, etc...
        """
        fileName = QFileDialog.getOpenFileName(self, "Open " + fileType,
                                               "", "*.xls *.xlsx")
        if fileName[0] != "":
            if fileType == self.DISTANCEFILE:
                currentDistanceFile = fileName[0]
                self.distanceLabel.setText(fileName[0])
            elif fileType == self.WEIGHTFILE:
                currentWeightFile = fileName[0]
                self.weightLabel.setText(fileName[0])
            elif fileType == self.COSTFILE:
                currentCostFile = fileName[0]
                self.costLabel.setText(fileName[0])
