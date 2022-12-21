import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from OrderMenu import window_1


form_class = uic.loadUiType("MenuUi.ui")[0]

  
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # plus 버튼 정의
        self.kor1_plus.clicked.connect(self.kor_plus_1)
        self.kor2_plus.clicked.connect(self.kor_plus_2)
        self.chi1_plus.clicked.connect(self.chi_plus_1)
        self.chi2_plus.clicked.connect(self.chi_plus_2)
        self.wes1_plus.clicked.connect(self.wes_plus_1)
        self.wes2_plus.clicked.connect(self.wes_plus_2)

        # minus 버튼 정의
        self.kor1_minus.clicked.connect(self.kor_minus_1)
        self.kor2_minus.clicked.connect(self.kor_minus_2)
        self.chi1_minus.clicked.connect(self.chi_minus_1)
        self.chi2_minus.clicked.connect(self.chi_minus_2)
        self.wes1_minus.clicked.connect(self.wes_minus_1)
        self.wes2_minus.clicked.connect(self.wes_minus_2)

        # 메뉴 별 개수 정의 
        self.MenuList = [[0, 0], [0, 0], [0, 0]]

        # 메뉴 이름 정의
        self.MenuNameList = [['비빔밥', '된장찌개'], ['짜장면', '짬뽕'], ['파스타', '스테이크']]
        self.set_menu_mane()

        # 주문 버튼 정의
        self.order.clicked.connect(self.orderMenu)

        # 기본 텍스트 상자 설정
        self.set_label()
    
    # 갯수 더하기 함수 
    def kor_plus_1 (self) :
        self.MenuList[0][0] += 1
        self.set_label()
        self.show()
    def kor_plus_2 (self) :
        self.MenuList[0][1] += 1
        self.set_label()
        self.show()
    def chi_plus_1 (self) :
        self.MenuList[1][0] += 1
        self.set_label()
        self.show()
    def chi_plus_2 (self) :
        self.MenuList[1][1]+= 1
        self.set_label()
        self.show()
    def wes_plus_1 (self) :
        self.MenuList[2][0] += 1
        self.set_label()
        self.show()
    def wes_plus_2 (self) :
        self.MenuList[2][1] += 1
        self.set_label()
        self.show()


    # 갯수 빼기 함수
    def kor_minus_1 (self) : 
        if self.MenuList[0][0] >= 1 :
            self.MenuList[0][0] -= 1
        self.set_label()
        self.show()
    def kor_minus_2 (self) : 
        if self.MenuList[0][1] >= 1 :
            self.MenuList[0][1] -= 1
        self.set_label()
        self.show()
    def chi_minus_1 (self) : 
        if self.MenuList[1][0] >= 1 :
            self.MenuList[1][0] -= 1
        self.set_label()
        self.show()
    def chi_minus_2 (self) : 
        if self.MenuList[1][1] >= 1 :
            self.MenuList[1][1] -= 1
        self.set_label()
        self.show()
    def wes_minus_1(self) : 
        if self.MenuList[2][0] >= 1 :
            self.MenuList[2][0] -= 1
        self.set_label()
        self.show()
    def wes_minus_2 (self) : 
        if self.MenuList[2][1] >= 1 :
            self.MenuList[2][1] -= 1
        self.set_label()
        self.show()

    
    # 항목 별 갯수 정의
    def set_label (self) :
        self.kor1_info.setText(str(self.MenuList[0][0]))
        self.kor2_info.setText(str(self.MenuList[0][1]))
        self.chi1_info.setText(str(self.MenuList[1][0]))
        self.chi2_info.setText(str(self.MenuList[1][1]))
        self.wes1_info.setText(str(self.MenuList[2][0]))
        self.wes2_info.setText(str(self.MenuList[2][1]))

    # 메뉴 이름 정의
    def set_menu_mane(self) :
        self.kor1_text.setText(self.MenuNameList[0][0])
        self.kor2_text.setText(self.MenuNameList[0][1])
        self.chi1_text.setText(self.MenuNameList[1][0])
        self.chi2_text.setText(self.MenuNameList[1][1])
        self.wes1_text.setText(self.MenuNameList[2][0])
        self.wes2_text.setText(self.MenuNameList[2][1])
    

    # 주문 완료 화면 실행
    def orderMenu(self):
        self.hide() #메인 윈도우 숨김
        self.second = window_1(self.MenuList, self.MenuNameList)
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.MenuList = [[0, 0], [0, 0], [0, 0]]
        self.set_label()
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐int(self.MenuList)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()