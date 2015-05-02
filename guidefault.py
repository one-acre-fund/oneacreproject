from PyQt4.QtGui import QWidget, QFrame

# Default Tab - all other tabs should inherit this
class DefaultTab(QWidget):
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
    
    def hLine(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        return line
    
    def vLine(self):
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        return line
