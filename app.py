__author__ = 'Alex'
from PyQt4.QtGui import *
from  PyQt4.phonon import Phonon
import sys
from PyQt4 import uic

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        #SE CARGA LA VISTA O INTERFAZ GRAFICA
        uic.loadUi("window.ui",self)

        #LLAMA  a los binding para conectar con la ui
        self.mediaSource=Phonon.MediaSource("aqui se pone el video")#los videos soportados por el momento son wvm
        self.videoPlayer.load(self.mediaSource)
        #auto reproduce el video
        self.videoPlayer.play()

        #BINDINGS DE BOTONES
        self.btnPlay.clicked.connect(self.Play)
        self.btnStop.clicked.connect(self.Stop)
        self.btnPause.clicked.connect(self.Pause)
        self.volumen.valueChanged.connect(self.Volumen)

    def Play(self):
        if self.videoPlayer.isPlaying():
            pass
        else:
            self.videoPlayer.play()

    def Stop(self):
        self.videoPlayer.stop()

    def Pause(self):
        if self.videoPlayer.isPaused():
            self.videoPlayer.play()
        else:
            self.videoPlayer.pause()

    def Volumen(self):
        volum=(float(self.volumen.value())*float(self.volumen.maximum()))/10000
        self.videoPlayer.setVolume(float(volum))

    def Salir(self):
        app.exit()

if __name__=="__main__":
    try:
        app=QApplication(sys.argv)
        ventana=Window()
        ventana.show()
        sys.exit(app.exec_())
    except SystemExit:
        ventana.Salir()
