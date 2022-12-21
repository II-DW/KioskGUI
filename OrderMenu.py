from PyQt5.QtWidgets import *
from PyQt5 import uic
from datetime import datetime

New = uic.loadUiType(r"orderUi.ui")[0] #두 번째창 ui


class window_1(QDialog,QWidget,New):
    def __init__(self, MenuList, MenuNameList):
        super().__init__()
        self.setupUi(self)

        # 버튼 정의
        self.Confirm.clicked.connect(self.ok)
        self.Cancel .clicked.connect(self.cancel_a)

        # 메뉴 리스트 정의 
        self.MenuList = MenuList
        self.MenuNameList = MenuNameList

        self.prt_msg()
        self.show() # 두번째창 실행
    

    # 텍스트 추가 
    def prt_msg (self) :
        e = 0
        msg = ''
        day = datetime.today().strftime('%Y년 %m월 %d일 |') #오늘 날짜
        msg += day + '\n' + '----------------' + '\n' + '\n'
        for a in range (3) :
            for b in range (2) :
                if self.MenuList[a][b] != 0 :
                    msg += self.MenuNameList[a][b] + ':' + str(self.MenuList[a][b]) + '개' +'\n'
        self.text.setText(msg)
        self.show()
    

    # 확인
    def ok (self) :
        self.close() #창 닫기

    # 취소
    def cancel_a (self) :
        self.close() #창 닫기
