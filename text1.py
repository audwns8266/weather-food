from pyowm import OWM
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

API_key = "10d4923cb75c31bfa0a786005f4803db" #openweathermap API
owm = OWM(API_key)

class MyWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
      
        self.setupUI()
        
       
    def setupUI(self):
        palette = QtGui.QPalette() # 배경색 지정
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        self.setPalette(palette)

        
        font = QtGui.QFont() # 폰트 지정
        font.setFamily("휴먼옛체")
        font.setPointSize(10)
        self.setFont(font)
        
        self.setGeometry(800, 400, 300, 350) # 창 크기 설정
        self.setWindowTitle('W-F') # 창 이름 설정
        self.setWindowIcon(QIcon('아이콘.png')) # 아이콘 설정
        
        textLabel = QLabel("지역 : ",self) # 텍스트 출력
        
        textLabel.move(40, 30) # 텍스트 위치 설정

        self.lineEdit = QLineEdit("",self) #lineEdit 생성
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter) #텍스트 가운데 정렬
        self.lineEdit.move(100,30) #lineEdit 위치 설정
        self.lineEdit.returnPressed.connect(self.lineEditPressed) #엔터를 누르면 lineEditPressed 실행

        self.label = QLabel("", self) # QLabel 생성
        self.label.setAlignment(QtCore.Qt.AlignCenter) #텍스트 가운데 정렬
        
        self.image = QLabel(self) # QLabel 생성
        self.image.setAlignment(QtCore.Qt.AlignCenter) #텍스트 가운데 정렬

        btn1 = QPushButton("추천 메뉴", self) # 버튼 생성
        btn1.setStyleSheet('QPushButton {background-color: white}')
        btn1.move(105, 280)
        btn1.clicked.connect(self.btn1_clicked)
        

    def btn1_clicked(self):
        self.image.move(55, 200) # QLabel 위치 설정
        self.image.resize(210, 100) # QLabel 크기 설정
        
        self.label.move(75, 70) # QLabel 위치 설정
        self.label.resize(150, 150) # QLabel 크기 설정

        try :
            city = str(self.lineEdit.text()) # city에 lineEdit에 써진 텍스트 입력 
            obs = owm.weather_at_place(city) #날씨를 검색할 장소를 city로 설정
            w = obs.get_weather() # 날씨 정보 가져오기
            l = obs.get_location() # 위치 정보 가져오기
            
            if w.get_status() == 'Snow':
                self.image.setText("눈 오는 날 ")
                pixmap = QPixmap('우동.png')
                self.label.setPixmap(pixmap)
            
            if w.get_status() == 'Rain': 
                self.image.setText("비 오는 날 ")
                pixmap = QPixmap('파전.png')
                self.label.setPixmap(pixmap)
        
            if w.get_status() == 'Clear': 
                self.image.setText("맑은 날 ")
                pixmap = QPixmap('치맥.png')
                self.label.setPixmap(pixmap)
            
            if w.get_status() == 'Clouds': 
                self.image.setText("흐린 날 ")
                pixmap = QPixmap('수육.png')
                self.label.setPixmap(pixmap)
            
            if w.get_status() == 'Mist': 
                self.image.setText("안개 낀 날 ")
                pixmap = QPixmap('라멘.png')
                self.label.setPixmap(pixmap)

        except: # 오류 발생시 처리 
            print('순서 오류')
            self.image.setText("지역을 입력해 주세요.")
            pixmap = QPixmap('물음표.png')
            self.label.setPixmap(pixmap)
        
        
    def lineEditPressed(self): #lineEditPressed 선언
        
        self.label.move(75, 20) # QLabel 위치 설정
        self.label.resize(150, 200) # QLabel 크기 설정
        
        self.image.resize(100,100) # QLabel 크기 설정
        self.image.move(105, 170) # QLabel 위치 설정

        try :
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

            
            
        except: #오류 발생시 처리
            print('지역명 오류')
            self.image.move(45, 200) # QLabel 위치 설정
            self.image.resize(220, 100) # QLabel 크기 설정
        
            self.label.move(75, 70) # QLabel 위치 설정
            self.label.resize(150, 150) # QLabel 크기 설정

            self.image.setText('지역을 정확하게 입력해주세요.')
            pixmap = QPixmap('물음표.png')
            self.label.setPixmap(pixmap)
            
            
if __name__ == "__main__": # 창 출력
   
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
