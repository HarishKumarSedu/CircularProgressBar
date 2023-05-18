from PySide6.QtCore import  *
from PySide6.QtGui import  *
import PySide6.QtGui
from PySide6.QtWidgets import  *

class CircularProgress(QWidget):
    

    def __init__(self):
        QWidget.__init__(self)


        self.value = 0
        self.pwidth = 200
        self.pheight = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0x498BD1
        self.max_value = 100
        self.font_family= 'Segoe UI'
        self.font_size = 12 
        self.suffix = "%"
        self.text_color = 0x498BD1
        # self.enable_shadow = True

        #self resize parametes 

        self.resize(self.pwidth,self.pheight)

    def add_shadow(self,enable):
        if enable :
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0,0,0,120))
            self.setGraphicsEffect(self.shadow)
            
    def set_value(self,value):
        self.value = value
    
    # SET THE PAINT ENVE WHICH IS SHOULD BE THE EXACT NAME OF THE QT EVEN FUNCTION 
    def paintEvent(self, e):
        #set the progress parameters 
        width = self.pwidth - self.progress_width
        height = self.pheight - self.progress_width
        margin = self.progress_width / 2 
        value  = self.value * 360 / self.max_value


        #QPAINTER 
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) # remove the pixlated edges 
        paint.setFont(QFont(self.font_family,self.font_size))
        #CREAT THE RECTANGLE 
        rect = QRect(0,0,self.pwidth,self.pheight)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        #PEN 
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        
        if self.progress_rounded_cap :
            pen.setCapStyle(Qt.RoundCap)


        paint.setPen(pen)
        paint.drawArc(margin,margin,width,height,-90*16,-value*16)  

        #CREATE THE TEST 
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect,Qt.AlignCenter,f"{self.value}{self.suffix}")

        #END 
        paint.end()
    
