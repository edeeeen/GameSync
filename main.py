import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from server import *

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("looks.ui",self)
        #on button pushes run functions
        self.pushButton_3.clicked.connect(self.browsefiles)
        self.pushButton_2.clicked.connect(self.send)
        self.pushButton.clicked.connect(self.receive)
    #Browse button
    def browsefiles(self):
        fname=QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.lineEdit.setText(fname)

    #Send Button
    def send(self):
        import requests
        import shutil 
        #ip + : + port
        url = 'http://' + self.lineEdit_2.text() + ":" + self.lineEdit_3.text()
        saveMinus = ""
        #only way i could think of to find ../
        split = self.lineEdit.text().split("/")
        for x in range(len(split)-1):
            saveMinus += split[x]+"/"
        #archive the selected folder
        shutil.make_archive(saveMinus+"/save", 'zip', self.lineEdit.text())
        #open the file
        zipFile = open(saveMinus+"save.zip", 'rb')
        try:
            #try to send it
            files = {'media': zipFile}
            requests.post(url, files=files)
        except:
            #if it cant send then throw an error
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Error sending. Is there a computer recieving?")
            x = msg.exec_()
        try:
            #kill the server
            requests.get(url+"/stopServer")
        except:
            #if it doesnt work debug message in console
            print("no server")
        #close the zip so it can be deleted
        zipFile.close()
        #delete zip
        os.remove(saveMinus+"/save.zip")
    #recieve button
    def receive(self):
        #run server
        run(self.lineEdit_3.text(), self.lineEdit.text())

if __name__ == "__main__":
    #start the app
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(400)
    widget.setFixedHeight(300)
    widget.setWindowTitle("GameSync")
    widget.setWindowIcon(QtGui.QIcon('logo.png'))
    widget.show()
    sys.exit(app.exec_())