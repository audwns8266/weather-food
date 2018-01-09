from pyowm import OWM
import sys
from PyQt5.QtWidgets import *

API_key = "10d4923cb75c31bfa0a786005f4803db"
owm = OWM(API_key)


    
class MyWindow(QMainWindow):
    
    
        
        
    def __init__(self):
        super().__init__()
        self.setupUI()

       
    def setupUI(self):
        
        self.setGeometry(800, 400, 300, 300)

        textLabel = QLabel("지역 : ",self)
        textLabel.move(20, 20)

        self.lineEdit = QLineEdit("",self)
        self.lineEdit.move(70,20)
        self.lineEdit.returnPressed.connect(self.lineEditPressed)

        self.label = QLabel("", self)
        self.label.move(90, 10)
        self.label.resize(150, 200)

        
        btn2 = QPushButton("추천 메뉴", self)
        btn2.move(100,180)

    def lineEditPressed(self):
        city = str(self.lineEdit.text())
        obs = owm.weather_at_place(city)
        w = obs.get_weather()
        l = obs.get_location()
        self.label.setText(l.get_name()+'\n최고 기온 : ' + str(w.get_temperature(unit='celsius')['temp_max']) + '˚C' + '\n최저 기온 : '+ str(w.get_temperature(unit='celsius')['temp_min']) + '˚C'
                           + '\n현재 기온 : ' + str(w.get_temperature(unit='celsius')['temp']) + '˚C' + '\n현재 날씨 : ' + w.get_status())
        
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
