import sys
import os
import guiinput
import guioutput
import guidata
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget
from PyQt5.QtGui import QFont

# The Main Window
class MainWindow(QTabWidget):
    
    # Tabs
    INPUTTABINDEX = 0
    OUTPUTTABINDEX = 1
    outputTab = None
    inputTab = None

    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        
        self.outputTab = guioutput.OutputTab()
        self.inputTab = guiinput.InputTab(self)
        
        self.resize(860, 645)
        self.addTab(self.inputTab, "Input")
        self.addTab(self.outputTab, "Output")
        self.setWindowTitle("One Acre Fund DSO")
        self.show()

# Main 
if __name__ == "__main__":
    if not guidata.init():
        sys.exit()
    app = QApplication(sys.argv)
    if sys.platform == "win32":
        font = QFont("Arial", 11)
    elif sys.platform == "darwin":
        font = QFont("Arial", 16)
    app.setFont(font)
    window = MainWindow()
    sys.exit(app.exec_())
