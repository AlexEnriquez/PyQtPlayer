__author__ = 'Alex Enriquez'
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.phonon import Phonon

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.UIGenerator()
        self.Bindings()
        
    def UIGenerator(self):
        self.mainLayout=QGridLayout()
        self.videoPlayer=Phonon.VideoPlayer()
        self.btnPlay=QPushButton("Play")
        self.btnStop=QPushButton("Stop")
        self.btnPuase=QPushButton("Pause")
        self.duration=QProgressBar()
        self.mainLayout.addWidget(self.videoPlayer,0,0,2,3)
        self.mainLayout.addWidget(self.duration,3,0,1,3)
        self.mainLayout.addWidget(self.btnPlay,4,0)
        self.mainLayout.addWidget(self.btnStop,4,1)
        self.mainLayout.addWidget(self.btnPuase ,4,2)
        self.setLayout(self.mainLayout)
        self.setMinimumSize(500,500)

    def Bindings(self):
        self.duration.setValue(0)
        self.btnPlay.clicked.connect(self.Play)
        self.btnStop.clicked.connect(self.Stop)
        self.btnPuase.clicked.connect(self.Pause)

    def Play(self):

        self.videoPlayer.load(Phonon.MediaSource("Here Put the name of your video.*"))
        self.videoPlayer.play()

    def Stop(self):
        self.videoPlayer.stop()

    def Pause(self):

        if self.videoPlayer.isPaused():
            self.videoPlayer.play()
        else:
            self.videoPlayer.pause()

if __name__=="__main__":

    try:
        app=QApplication(sys.argv)
        app.setStyle("Plastique")
        ventana=Window()
        ventana.show()
        sys.exit(app.exec_())
    except SystemExit:
        print "Thanks for use it"
