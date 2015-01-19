#!/usr/bin/env python
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMainWindow, QWidget, QApplication
import sys, os
from collections import OrderedDict
from datetime import datetime

class Capture():
    def __init__(self):
        self.commande = ""


    def commandCapture(self, duree, photoSec):
        
        self.photoSec = 1/float(photoSec)
	self.nbPhoto = duree // photoSec
        self.commande = 'streamer -t bbb -r aaa -o image00000.jpeg -s 640x480'
        self.commande = self.commande.replace('aaa', str(self.photoSec))
        self.commande = self.commande.replace('bbb', str(self.nbPhoto))

	print(self.commande)
        
        os.system(self.commande)
        
        os.system("timeLapse.sh")

class QTWindow(QtGui.QWidget):
    def __init__(self):
        super(QTWindow, self).__init__()
        # self.setCentralWidget(self.container)

        self.setWindowTitle("TimeLapse QT")
        self.showMaximized()
        
        self.newFolder()
        self.timelapse = Capture()
        
        self.initUI()
        self.show()

    def initUI(self):
        pix = QtGui.QPixmap(self.capture())
        self.labelPix = QtGui.QLabel(self)
        self.labelPix.setPixmap(pix)
        
        
        buttonStart = QtGui.QPushButton("Start TimeLapse")
        #buttonStart.setAutoDefault(self, True)
        buttonStart.setDefault(True)
        buttonCapt = QtGui.QPushButton("Capture apercu")
        #buttonCapt.setAutoDefault(self,True)
        buttonCapt.setDefault(True)
        
        labelDuree = QtGui.QLabel("Durree : ")
        labelPhotoSec = QtGui.QLabel("Intervale : ")

        self.comboBoxDuree = QtGui.QComboBox()
        self.comboBoxPhotoSec = QtGui.QComboBox();
        self.comboBoxDelay = QtGui.QComboBox();

        self.dictBoxDuree = OrderedDict([
                        ("20 secondes", 20),
                        ("1 jour", 86400),
                        ("2 jour", 172800),
                        ("1 heure", 3600),
                        ("2 heures", 7200),
                        ("3 heures", 10800),
                        ("4 heures", 14400),
                        ("5 heures", 5 * 3600),
                        ("6 heures", 6 * 3600),
                        ("7 heures", 7 * 3600),
                        ("8 heures", 8 * 3600),
                        ("9 heures", 9 * 3600),
                        ("10 heures", 10 * 3600)])
        self.dictBoxPhotoSec = OrderedDict([("1", 1),
                        ("2", 2),
                        ("3", 3),
                        ("4", 4),
                        ("5", 5),
                        ("6", 6),
                        ("7", 7),
                        ("8", 8),
                        ("9", 9),
                        ("10", 10)])
        self.dicttBoxDelay = OrderedDict([("5 secondes", 5),
                        ("10 secondes", 10),
                        ("30 secondes", 30),
                        ("1 minutes", 60),
                        ("5 minutes", 300)])

        self.comboBoxDuree.addItems(list(self.dictBoxDuree.keys()))
        self.comboBoxPhotoSec.addItems(list(self.dictBoxPhotoSec.keys()))
        self.comboBoxDelay.addItems(list(self.dicttBoxDelay.keys()))


        buttonCapt.clicked.connect(self.captureClicked)
        buttonStart.clicked.connect(self.startTimeLapse)

        self.grid = QtGui.QGridLayout()
        
        self.grid.addWidget(buttonCapt, 1, 4, 1, 5)

        self.grid.addWidget(self.labelPix, 1, 0, 4, 4, QtCore.Qt.AlignHCenter)

        self.grid.addWidget(labelDuree, 2, 4, QtCore.Qt.AlignHCenter)
        self.grid.addWidget(self.comboBoxDuree, 2, 5)

        self.grid.addWidget(labelPhotoSec, 3, 4, QtCore.Qt.AlignHCenter)
        self.grid.addWidget(self.comboBoxPhotoSec, 3, 5)

        self.grid.addWidget(buttonStart, 4, 4, 4, 5)


        self.setLayout(self.grid)

    def startTimeLapse(self):
        photoSec = self.dictBoxPhotoSec[str(self.comboBoxPhotoSec.currentText())]
        dure = self.dictBoxDuree[str(self.comboBoxDuree.currentText())]
        self.timelapse.commandCapture(dure, photoSec)


    def captureClicked(self):
        pix = QtGui.QPixmap(self.capture())
        self.labelPix.setPixmap(pix)
        self.show()
    
    def capture(self):
        os.system("streamer -f jpeg -o image.jpeg -s 426x320")
        return "image.jpeg"
        
    def newFolder(self):
        folderName = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        os.system("mkdir ~/Desktop/" + folderName)
        os.chdir("~/Desktop")
        
def main():
    app = QtGui.QApplication(sys.argv)
    window = QTWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
	main()
