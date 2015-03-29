from PyQt5.QtWidgets import QWidget

# Default Tab - all other tabs should inherit this
class DefaultTab(QWidget):
    def __init__(self):
        """
        Constructor
        """
        QWidget.__init__(self)
