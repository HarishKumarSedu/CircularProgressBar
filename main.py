import sys 
import os 
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

#IMPORT THE CIRCULAR PROGRESS BAR FROM THE CIRCULAR_PROGRESSBAR 
from circular_progress.circular_progress import CircularProgress

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        #RESIZE THE MAIN WINDOW 
        self.resize(500,500)

        # #REMOVE THE TITLE BAR 
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #CREATE THE QFRAME THAT CONTAIN OUR CIRCULAR BAR 
        self.container = QFrame()
        self.container.setStyleSheet(
            # "background-color: transparent"
            "background-color: #222222"
        )
        self.container_layout = QVBoxLayout()

        #CREATE THE CIRCULAR PROGRESS 
        self.progress = CircularProgress()
        self.progress.value = 50
        self.progress.setMinimumSize(self.progress.pwidth,self.progress.pheight)
        self.progress.font_size = 30
        # self.progress.text_color = 0xFFFFFF
        # self.progress.progress_color = 0xFFFFFF
        self.progress.add_shadow(True)

        #ADD THE SLIDER
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,100)
        self.slider.valueChanged.connect(self.change_value)

        #ADD THE WIDGETS 
        self.container_layout.addWidget(self.progress,Qt.AlignCenter,Qt.AlignCenter)
        self.container_layout.addWidget(self.slider,Qt.AlignCenter,Qt.AlignCenter)

        #SET THE CENTRAL WIDEGET 
        self.container.setLayout(self.container_layout)
        
        #SET THE CENTRAL WIDGET 
        self.setCentralWidget(self.container)

        # SHOW THE WINDOW 
        self.show()


    def change_value(self,value):
        self.progress.set_value(value)
        self.repaint()

if __name__ =='__main__':

    app = QApplication()
    win = MainWindow()
    sys.exit(app.exec_())
