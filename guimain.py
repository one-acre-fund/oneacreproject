import sys
import guiinput
import guioutput
import guiimport
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget
from PyQt5.QtGui import QFont

# The Main Window
class MainWindow(QTabWidget):
    
    def __init__(self):
        """
        Constructor
        """
        QTabWidget.__init__(self)
        
        inputTab = guiinput.InputTab()
        outputTab = guioutput.OutputTab()
        importTab = guiimport.ImportTab()
        
        self.resize(800, 600)
        self.addTab(inputTab, "Input")
        self.addTab(outputTab, "Output")
        self.addTab(importTab, "Import")
        self.setWindowTitle('<Application Name>')
        self.show()

# Main 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = QFont("Arial", 11)
    app.setFont(font)
    window = MainWindow()
    sys.exit(app.exec_())
