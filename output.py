import sys
import xlwt
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QTableWidget,QPushButton,QHBoxLayout,QVBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QTableWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class OutputTab(QtWidgets.QWidget):
    
    def __init__(self,theList,theName):
        """
            Constructor
        """
        super().__init__()
        self.theList = theList
        self.warehouseName=theName
        self.initGraph()

    def initGraph(self):
        """
            Create an output screen containing one table, three line edit widgets and six buttons 
            The first line edit widget will display the name for the warehouse
            The second line edit widget will display the total Optimal Cost
            The third line edit widget will display the total Non-Distance Optimal Cost
            The "show table" button allows the data to be displayed on the table
            The "Show warehouse" button allows the name of the warehouse to be displayed on the first line edit widget 
            The "Calculate optimal cost" button calculates the total optimal cost and displays the value on the second line edit widget
            The "Caulculate non-distance optimal cost" button calculates the total non-distance optimal cost and displays the value on the third edit widget 
            The "Export to excel sheet" button exports the data in the table to a new spreadsheet
            The "quit" button allows the user to terminate the application
        """
        self.resize(800,500)
        self.move(300,200)
        self.setWindowTitle('<output tab>')
        
        self.labelOne=QLabel('Warehouse', self)
        self.line=QLineEdit(self)
        self.labelTwo=QLabel('Total Optimal Cost',self)
        self.lineTwo=QLineEdit(self)
        self.labelThree=QLabel('Total Non-Distance Optimal Cost',self)
        self.lineThree=QLineEdit(self)
        
        hBox=QHBoxLayout()
        hBox.addStretch()
        hBox.addWidget(self.labelOne)
        hBox.addStretch(1)
        hBox.addWidget(self.line)
        hBoxTwo=QHBoxLayout()
        hBoxTwo.addStretch()
        hBoxTwo.addWidget(self.labelTwo)
        hBoxTwo.addStretch(1)
        hBoxTwo.addWidget(self.lineTwo)
        hBoxThree=QHBoxLayout()
        hBoxThree.addStretch()
        hBoxThree.addWidget(self.labelThree)
        hBoxThree.addStretch(1)
        hBoxThree.addWidget(self.lineThree)
        vBox=QVBoxLayout()
        vBox.addStretch()
        vBox.addLayout(hBox)
        vBox.addLayout(hBoxTwo)
        vBox.addLayout(hBoxThree)
        
        self.table=QTableWidget(100,9,self)
        self.table.setHorizontalHeaderLabels(['district','site 1', 'site 2', 'actual distance','optimal distance','weight','truck size','optimal cost', 'Non-Distance optimal cost'])
        self.table.setColumnWidth(0,100)
        self.table.setColumnWidth(1,100)
        self.table.setColumnWidth(2,100)
        self.table.setColumnWidth(3,100)
        self.table.setColumnWidth(4,100)
        self.table.setColumnWidth(5,100)
        self.table.setColumnWidth(6,100)
        self.table.setColumnWidth(7,100)
        self.table.setColumnWidth(8,150)
        
        hBoxFive=QHBoxLayout()
        hBoxFive.addWidget(self.table)
        vBox.addLayout(hBoxFive)
        
        self.buttonOne=QPushButton('Show table',self)
        self.buttonTwo=QPushButton('Show warehouse',self)
        self.buttonThree=QPushButton('Calculate optimal cost',self)
        self.buttonFour=QPushButton('Calculate non-distance optimal cost',self)
        self.buttonFive=QPushButton('Export to excel sheet',self)
        self.buttonSix=QPushButton('Quit', self)
        self.buttonOne.clicked.connect(self.showTable)
        self.buttonTwo.clicked.connect(self.showWarehouse)
        self.buttonThree.clicked.connect(self.getOptimalCost)
        self.buttonFour.clicked.connect(self.getNonDistanceOptimalCost)
        self.buttonFive.clicked.connect(self.createExcelSheet)
        self.buttonSix.clicked.connect(QCoreApplication.instance().quit)

        hBoxSix=QHBoxLayout()
        hBoxSix.addStretch(1)
        hBoxSix.addWidget(self.buttonOne)
        hBoxSix.addWidget(self.buttonTwo)
        hBoxSix.addWidget(self.buttonThree)

        hBoxSeven=QHBoxLayout()
        hBoxSeven.addStretch(1)
        hBoxSeven.addWidget(self.buttonFour)
        hBoxSeven.addWidget(self.buttonFive)
        hBoxSeven.addWidget(self.buttonSix)
        vBox.addStretch(2)
        vBox.addLayout(hBoxSix)
        vBox.addLayout(hBoxSeven)
        
        self.setLayout(vBox)
        self.show()

    def showTable(self):
        """
            Diplays the output on the table
        """
        for i in range(len(self.theList)):
            for j in range(len(self.theList[i])):
                self.table.setItem(i,j,QTableWidgetItem(str(self.theList[i][j])[:11]))
    
    def getOptimalCost(self):
        """
            Calculates the sum of the optimal cost and displays the value in the second line edit widget
        """
        totalCost=0
        for i in range(len(self.theList)):
                totalCost=totalCost+self.theList[i][7]
        self.lineTwo.setText(str(totalCost))
    

    def getNonDistanceOptimalCost(self):
        """
            Calculates the sum of the non-distance optimal cost and displays the value in the third line edit widget
        """
        totalCostOne=0
        for i in range(len(self.theList)):
                totalCostOne=totalCostOne+theList[i][8]
        self.lineThree.setText(str(totalCostOne))

    def showWarehouse(self):
        """
            Displays the name of the warehouse in the first line edit widget
        """
        self.line.setText(self.warehouseName)

    def createExcelSheet(self):
        """
            Exports the data in the table to a new Excel spreasheet
            The new Excel spreasheet is saved as "outputsheet.xls"
        """
        workbook=xlwt.Workbook()
        worksheet=workbook.add_sheet('output')
        
        bold=xlwt.easyxf('font:bold 1')
        worksheet.write(0,0,'Total Optimal Cost',bold)
        worksheet.write(0,2,'Total Non-Distance Optimal Cost',bold)
        worksheet.write(1,0,'District',bold)
        worksheet.write(1,1,'Site 1',bold)
        worksheet.write(1,2,'Site 2',bold)
        worksheet.write(1,3,'Actual Distance',bold)
        worksheet.write(1,4,'Optimal Distance',bold)
        worksheet.write(1,5,'Weight',bold)
        worksheet.write(1,6,'Truck Size',bold)
        worksheet.write(1,7,'Optimal Cost',bold)
        worksheet.write(1,8,'Non-Distance Optimal Cost',bold)
       
        worksheet.col(0).width=256*20
        worksheet.col(1).width=256*10
        worksheet.col(2).width=256*30
        worksheet.col(3).width=256*15
        worksheet.col(4).width=256*15
        worksheet.col(5).width=256*10
        worksheet.col(6).width=256*10
        worksheet.col(7).width=256*15
        worksheet.col(8).width=256*25
        
        # Displays the data in the table in the spreadsheet 
        for i in range(len(self.theList)):
            for j in range(len(self.theList[i])):
                worksheet.write(i+2,j,theList[i][j])
    
        # Calculates the total optimal cost and displays it
        totalOptimalCost=0
        for i in range(len(self.theList)):
            totalOptimalCost=totalOptimalCost+self.theList[i][7]
        worksheet.write(0,1,totalOptimalCost)

        # Calcualtes the total non-distance optimal cost and displays it
        totalNonDistanceOptimalCost=0
        for i in range(len(self.theList)):
            totalNonDistanceOptimalCost=totalNonDistanceOptimalCost+theList[i][8]
        worksheet.write(0,3,totalNonDistanceOptimalCost)

        workbook.save('outputsheet.xls')

if __name__=="__main__":
    theList=[['optimal','site2',3,4.0123123123123,5,6,7,8,9],[11,12,13,14,15,16,17,18,19]]
    theName='New York'
    app=QtWidgets.QApplication(sys.argv)
    outputTab=OutputTab(theList,theName)
    sys.exit(app.exec_())
