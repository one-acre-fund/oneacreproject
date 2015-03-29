from PyQt5.QtWidgets import QWidget, QFrame

# Default Tab - all other tabs should inherit this
class DefaultTab(QWidget):
    def __init__(self):
        """
        Constructor
        """
        QWidget.__init__(self)
    
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
