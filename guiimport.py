import guidefault
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog

# Import Tab
class ImportTab(guidefault.DefaultTab):
    DISTANCEFILE = "Distance Matrix"
    WEIGHTFILE = "Site Weights"
    COSTFILE = "Cost Matrix"
    
    currentDistanceFile = ""
    currentWeightFile = ""
    currentCostFile = ""
    
    distanceLabel = None
    weightLabel = None
    costLabel = None

    def __init__(self):
        super().__init__()
    
        mainBox = QVBoxLayout()
        
        title = QLabel("Import")
        titleFont = title.font()
        titleFont.setPointSize(12)
        titleFont.setBold(True)
        title.setFont(titleFont)
        title.setAlignment(Qt.AlignCenter)

        description = QLabel("Use this to import input data not already saved into the application.")
        description.setWordWrap(True)

        districtBox = QHBoxLayout()
        districtLabel = QLabel("District:")
        districtText = QLineEdit()
        districtBox.addWidget(districtLabel)
        districtBox.addStretch(1)
        districtBox.addWidget(districtText)

        warehouseBox = QHBoxLayout()
        warehouseLabel = QLabel("Warehouse:")
        warehouseText = QLineEdit()
        warehouseBox.addWidget(warehouseLabel)
        warehouseBox.addStretch(1)
        warehouseBox.addWidget(warehouseText)

        destinationBox = QHBoxLayout()
        destinationLabel = QLabel("Destinations/Truck:")
        destinationText = QLineEdit()
        destinationBox.addWidget(destinationLabel)
        destinationBox.addStretch(1)
        destinationBox.addWidget(destinationText)
        
        maxBox = QHBoxLayout()
        maxLabel = QLabel("Max Trucks/Warehouse/Day:")
        maxText = QLineEdit()
        maxBox.addWidget(maxLabel)
        maxBox.addStretch(1)
        maxBox.addWidget(maxText)
 
        distanceBox = QHBoxLayout()
        distanceButton = QPushButton("Select Distance Matrix")
        distanceButton.setMinimumWidth(220)
        distanceButton.setMaximumWidth(220)
        distanceButton.clicked.connect(self.distanceButtonClicked)
        self.distanceLabel = QLabel("None selected.")
        distanceBox.addWidget(distanceButton)
        distanceBox.addStretch(1)
        distanceBox.addWidget(self.distanceLabel)

        weightBox = QHBoxLayout()
        weightButton = QPushButton("Select Site Weights")
        weightButton.setMinimumWidth(220)
        weightButton.setMaximumWidth(220)
        weightButton.clicked.connect(self.weightButtonClicked)
        self.weightLabel = QLabel("None selected.")
        weightBox.addWidget(weightButton)
        weightBox.addStretch(1)
        weightBox.addWidget(self.weightLabel)
        
        costBox = QHBoxLayout()
        costButton = QPushButton("Select Cost Matrix")
        costButton.setMinimumWidth(220)
        costButton.setMaximumWidth(220)
        costButton.clicked.connect(self.costButtonClicked)
        self.costLabel = QLabel("None selected.")
        costBox.addWidget(costButton)
        costBox.addStretch(1)
        costBox.addWidget(self.costLabel)
        
        saveBox = QHBoxLayout()
        saveButton = QPushButton("Save")
        saveBox.addStretch(1)
        saveBox.addWidget(saveButton)
        saveBox.addStretch(1)

        mainBox.addWidget(title)
        mainBox.addWidget(description)
        mainBox.addWidget(self.hLine())
        mainBox.addLayout(districtBox)
        mainBox.addLayout(warehouseBox)
        mainBox.addLayout(destinationBox)
        mainBox.addLayout(maxBox)
        mainBox.addWidget(self.hLine())
        mainBox.addLayout(distanceBox)
        mainBox.addLayout(weightBox)
        mainBox.addLayout(costBox)
        mainBox.addStretch(1)
        mainBox.addLayout(saveBox)

        self.setLayout(mainBox)

    def distanceButtonClicked(self):
        """
        Handles when distance button is clicked
        """
        self.changeUploadedFile(self.DISTANCEFILE)

    def weightButtonClicked(self):
        """
        Handles when weight button is clicked
        """
        self.changeUploadedFile(self.WEIGHTFILE)
    
    def costButtonClicked(self):
        """
        Handles when cost button is clicked
        """
        self.changeUploadedFile(self.COSTFILE)
    
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
