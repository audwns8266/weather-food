from pyowm import OWM
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

API_key = "10d4923cb75c31bfa0a786005f4803db"
owm = OWM(API_key)



class MyWindow(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        self.setupUI()

       
    def setupUI(self):
        
        self.setGeometry(800, 400, 300, 300)
        
        textLabel = QLabel("지역 : ",self)
        textLabel.move(40, 20)

        self.lineEdit = QLineEdit("",self)
        self.lineEdit.move(100,20)
        self.lineEdit.returnPressed.connect(self.lineEditPressed)

        self.label = QLabel("", self)
        self.label.move(90, 10)
        self.label.resize(150, 200)

        self.image = QLabel(self)
        self.image.resize(100,100)
        self.image.move(100, 160)

    def lineEditPressed(self):
        city = str(self.lineEdit.text())
        obs = owm.weather_at_place(city)
        w = obs.get_weather()
        l = obs.get_location()
        self.label.setText(l.get_name()+'\n최고 기온 : ' + str(w.get_temperature(unit='celsius')['temp_max']) +
                           '˚C' + '\n최저 기온 : '+ str(w.get_temperature(unit='celsius')['temp_min']) + '˚C'
                           + '\n현재 기온 : ' + str(w.get_temperature(unit='celsius')['temp']) + '˚C' +
                            '\n현재 날씨 : ' + w.get_status())

        if w.get_status() == 'Snow':
            pixmap = QPixmap('Snow.png')
            self.image.setPixmap(pixmap)
            
        if w.get_status() == 'Rain':
            pixmap = QPixmap('Rain.png')
            self.image.setPixmap(pixmap)
            
        if w.get_status() == 'Clear':
            pixmap = QPixmap('Clear.png')
            self.image.setPixmap(pixmap)
            
        if w.get_status() == 'Clouds':
            pixmap = QPixmap('Clouds.png')
            self.image.setPixmap(pixmap)
            
        if w.get_status() == 'Mist':
            pixmap = QPixmap('Mist.png')
            self.image.setPixmap(pixmap)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
