from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMainWindow, QWidget, QApplication
import sys, os
from collections import OrderedDict
from datetime import datetime

class Capture():
    def __init__(self):
        self.commande = ""


    def commandCapture(self, duree, photoSec):
        self.nbPhoto = duree // photoSec
        self.photoSec = photoSec
        self.commande = 'streamer -s 1280x720 -t bbb -r aaa -o image0000.jpeg -c /dev/video0'
        self.commande = self.commande.replace('aaa', str(self.photoSec))
        self.commande = self.commande.replace('bbb', str(self.nbPhoto))
        
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
        
        labelDuree = QtGui.QLabel("Duree : ")
        labelPhotoSec = QtGui.QLabel("Seconde par photo : ")
        labelDelay = QtGui.QLabel("Debuter dans : ")

        self.comboBoxDuree = QtGui.QComboBox()
        self.comboBoxPhotoSec = QtGui.QComboBox();
        self.comboBoxDelay = QtGui.QComboBox();

        self.dictBoxDuree = OrderedDict([
                        ("20 secondes", 20),
                        ("1 jour", 24),
                        ("2 jour", 172800),
                        ("1 heure", 86400),
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
        
        self.grid.addWidget(buttonCapt, 1, 1, 1, 3)

        self.grid.addWidget(self.labelPix, 2, 0, 4, 5, QtCore.Qt.AlignHCenter)

        self.grid.addWidget(labelDuree, 7, 1, QtCore.Qt.AlignHCenter)
        self.grid.addWidget(self.comboBoxDuree, 8, 1)

        self.grid.addWidget(labelPhotoSec, 7, 3, QtCore.Qt.AlignHCenter)
        self.grid.addWidget(self.comboBoxPhotoSec, 8, 3)

        #self.grid.addWidget(labelDelay, 6, 2, QtCore.Qt.AlignHCenter)
        #self.grid.addWidget(self.comboBoxDelay, 7, 2)

        self.grid.addWidget(buttonStart, 9, 1, 9, 3)


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
        os.system("streamer -f jpeg -o image.jpeg -s 1280x720")
        return "image.jpeg"
        
    def newFolder(self):
        folderName = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        os.system("mkdir ~/Bureau/" + folderName)
        os.chdir("/home/bhacaz/Bureau/" + folderName)
        
def main():
    app = QtGui.QApplication(sys.argv)
    window = QTWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
	main()
