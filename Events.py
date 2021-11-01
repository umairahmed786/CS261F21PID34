from numpy import array
import Algorithms
import sys
from GUI import Ui_Dialog
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
import scrapData
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from threading import Thread
import csv
import Sort
import datetime
import search


class ThreadScrapping(Thread):
    def run(self):
        #self.changeValue.emit(0)
        QtWidgets.QApplication.processEvents()

        scrapData.scrapPermission=True
        scrapData.StartScraping(self.progressbar,self.time)
        #self.changeValue.emit(scrapData.mainIndex)
    def setProgressbar(self, progressbar,time):
        self.progressbar = progressbar
        self.time=time
        
class LoadData(Thread):
    data=[]
    def run(self):
        self.df=pd.read_csv("university3.csv")
        self.data=self.df.to_dict('records')





class UI_Dialog(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.startScrapping.clicked.connect(self.start)
        self.ui.pauseScrapping.clicked.connect(self.pause)
        self.ui.loadData.clicked.connect(self.LoadData)
        self.ui.applySorting.clicked.connect(self.sortData)
        self.ui.searchButton.clicked.connect(self.searchData)
    def searchData(self):
        self.attribute=self.ui.sortColumn.currentText()
        self.key=self.ui.searchText.text()
        search.linearSearch(self.attribute,self.key)
        self.loadSearchData()
    def loadSearchData(self):
        searchData=[]
        self.df=pd.read_csv("searchedData.csv")
        searchData=self.df.to_dict('records')
        self.scrappedData=searchData
        th=Thread(target=self.showData)
        th.start()
        th.join()
        msg="Your Search is Here.."
        self.showMsg(msg)


    def sortData(self):
        self.sortAlgorithm=self.ui.sortingAlgorithm.currentText()
        self.sortOrder=self.ui.sortingOrder.currentText()
        self.sortcolumn=self.ui.sortColumn.currentText()
        beforeTime=datetime.datetime.now().replace(microsecond=0)
        Sort.SortData(self.sortcolumn,self.sortAlgorithm,self.sortOrder)
        self.LoadData()
        currentTime=datetime.datetime.now().replace(microsecond=0)
        self.ui.time.setText(str(currentTime-beforeTime))
        msg="Data is sorted successfully"
        self.showMsg(msg)

    def LoadData(self):
        csv=LoadData()
        csv.start()
        csv.join()
        self.scrappedData=csv.data
#        th=Thread(target=self.showData)
        th=Thread(target=self.showData)

        th.start()
        th.join()
    def start(self):
        self.worker=ThreadScrapping()
        #self.worker.changeValue.connect(self.ValueofProgress)
        self.worker.setProgressbar(self.ui.progressBarOfScrapping,self.ui.time)
        #self.worker.setTime(self.ui.time)
        self.worker.start()
    def pause(self,Dialog):
        scrapData.scrapPermission=False 
    def showData(self):
        rowNumber=0
        self.ui.tableWidget.setRowCount(len(self.scrappedData))
        for line in self.scrappedData:
            self.ui.tableWidget.setItem(rowNumber,0,QtWidgets.QTableWidgetItem(str(line['Name'])))
            self.ui.tableWidget.setItem(rowNumber,1,QtWidgets.QTableWidgetItem(str(line['Acronym'])))
            self.ui.tableWidget.setItem(rowNumber,2,QtWidgets.QTableWidgetItem(str(line['Address'])))
            self.ui.tableWidget.setItem(rowNumber,3,QtWidgets.QTableWidgetItem(str(line['Founded'])))
            self.ui.tableWidget.setItem(rowNumber,4,QtWidgets.QTableWidgetItem(str(line['Motto'])))
            self.ui.tableWidget.setItem(rowNumber,5,QtWidgets.QTableWidgetItem(str(line['WorldRank'])))
            self.ui.tableWidget.setItem(rowNumber,6,QtWidgets.QTableWidgetItem(str(line['CountryRank'])))
            self.ui.tableWidget.setItem(rowNumber,7,QtWidgets.QTableWidgetItem(str(line['Phone'])))
            self.ui.tableWidget.setItem(rowNumber,8,QtWidgets.QTableWidgetItem(str(line['Fax'])))
            rowNumber+=1
        #self.showMsg()
       
    def showMsg(self,mg):
        msg=QtWidgets.QMessageBox()
        msg.setWindowTitle("msg")
        msg.setText(mg)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x=msg.exec_()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UI_Dialog()
    win.show()
    sys.exit(app.exec_())