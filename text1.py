from pyowm import OWM
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

API_key = "10d4923cb75c31bfa0a786005f4803db" #openweathermap API
owm = OWM(API_key)



class MyWindow(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        self.setupUI()

       
    def setupUI(self):
        
        self.setGeometry(800, 400, 300, 300) # 창 크기 설정
        
        textLabel = QLabel("지역 : ",self) # 텍스트 출력
        textLabel.move(40, 20) # 텍스트 위치 설정

        self.lineEdit = QLineEdit("",self) #lineEdit 생성
        self.lineEdit.move(100,20) #lineEdit 위치 설정
        self.lineEdit.returnPressed.connect(self.lineEditPressed) #엔터를 누르면 lineEditPressed 실행

        self.label = QLabel("", self) # QLabel 생성
        self.label.move(90, 10) # QLabel 위치 설정
        self.label.resize(150, 200) # QLabel 상자 크기 설정

        self.image = QLabel(self) # QLabel 생성
        self.image.resize(100,100) # QLabel 크기 설정
        self.image.move(100, 160) # QLabel 위치 설정

    def lineEditPressed(self): #lineEditPressed 선언
        city = str(self.lineEdit.text()) # city에 lineEdit에 써진 텍스트 입력 
        obs = owm.weather_at_place(city) #날씨를 검색할 장소를 city로 설정
        w = obs.get_weather() # 날씨 정보 가져오기
        l = obs.get_location() # 위치 정보 가져오기
        self.label.setText(l.get_name()+'\n최고 기온 : ' + str(w.get_temperature(unit='celsius')['temp_max']) +
                           '˚C' + '\n최저 기온 : '+ str(w.get_temperature(unit='celsius')['temp_min']) + '˚C'
                           + '\n현재 기온 : ' + str(w.get_temperature(unit='celsius')['temp']) + '˚C' +
                            '\n현재 날씨 : ' + w.get_status()) # QLabel에 날씨정보 출력
                                                        
        if w.get_status() == 'Snow': # 눈오는 날씨면 눈 그림 출력
            pixmap = QPixmap('Snow.png')
            self.image.setPixmap(pixmap)
            
        if w.get_status() == 'Rain': # 비오는 날씨면 비 그림 출력
            pixmap = QPixmap('Rain.png')
            self.image.setPixmap(pixmap)
            
        if w.get_status() == 'Clear': # 화창한 날씨면 해 그림 출력
            pixmap = QPixmap('Clear.png')
            self.image.setPixmap(pixmap)
            
        if w.get_status() == 'Clouds': # 구름낀 날씨면 구름 그림 출력
            pixmap = QPixmap('Clouds.png')
            self.image.setPixmap(pixmap)
            
        if w.get_status() == 'Mist': # 안개낀 날씨면 안개 그림 출력
            pixmap = QPixmap('Mist.png')
            self.image.setPixmap(pixmap)
            
if __name__ == "__main__": # 창 출력
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
