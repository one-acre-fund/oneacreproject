import sys
import os
import guiinput
import guioutput
import guidata
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget
from PyQt5.QtGui import QFont

# The Main Window
class MainWindow(QTabWidget):
    
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        
        inputTab = guiinput.InputTab()
        outputTab = guioutput.OutputTab()
        
        self.resize(800, 600)
        self.addTab(inputTab, "Input")
        self.addTab(outputTab, "Output")
        self.setWindowTitle('<Application Name>')
        self.show()

# Main 
if __name__ == "__main__":
    if not guidata.init():
        sys.exit()
    app = QApplication(sys.argv)
    font = QFont("Arial", 11)
    app.setFont(font)
    window = MainWindow()
    sys.exit(app.exec_())
