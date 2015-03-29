import guidefault
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton

# Import Tab
class ImportTab(guidefault.DefaultTab):
    DISTANCEFILE = 'd'
    SITEFILE = 's'
    COSTFILE = 'c'
    currentDistanceFile = ""
    currentSiteFile = ""
    currentCostFile = ""
    
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
        distanceButton = QPushButton("Upload Distance Matrix")
        distanceButton.setMinimumWidth(220)
        distanceButton.setMaximumWidth(220)
        distanceLabel = QLabel("None uploaded.")
        distanceBox.addWidget(distanceButton)
        distanceBox.addStretch(1)
        distanceBox.addWidget(distanceLabel)
 
        weightBox = QHBoxLayout()
        weightButton = QPushButton("Upload Site Weights")
        weightButton.setMinimumWidth(220)
        weightButton.setMaximumWidth(220)
        weightLabel = QLabel("None uploaded.")
        weightBox.addWidget(weightButton)
        weightBox.addStretch(1)
        weightBox.addWidget(weightLabel)
        
        costBox = QHBoxLayout()
        costButton = QPushButton("Upload Cost Matrix")
        costButton.setMinimumWidth(220)
        costButton.setMaximumWidth(220)
        costLabel = QLabel("None uploaded.")
        costBox.addWidget(costButton)
        costBox.addStretch(1)
        costBox.addWidget(costLabel)
        
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

    def changeUploadedFile(self):
        """
        Listener that pops up a file dialog to allow user to change uploaded file
        """
        return
        
