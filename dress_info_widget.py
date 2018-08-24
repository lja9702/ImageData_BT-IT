
#일단 컬러 수정 및 선택할 수 있게 하는 위젯

###추가해야될 사항 : 브랜드명, 가격 <- 인풋으로 받게 , 옷을 러닝시켜서 분류시킨거 보내서 자동으로 띄우기

import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from colormap import rgb2hex
import Get_and_Split_path

dir_path = Get_and_Split_path.dir_path
file = open('test.txt', mode='r', encoding='utf-8')

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        extractAction = QtWidgets.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):

        extractAction = QtWidgets.QAction(QtGui.QIcon('todachoppa.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar("Extraction")
        #self.toolBar.addAction(extractAction)

        self.styleChoice = QtWidgets.QLabel(self)
        #여기에 텍스파일에서 넘어간 컬러값 넣기
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % (rgb2hex(0, 128, 64)))

        fontColor = QtWidgets.QAction('Changing Color', self)
        fontColor.triggered.connect(self.color_picker)

        self.toolBar.addAction(fontColor)

        #print(self.style().objectName())
        #self.styleChoice = QtWidgets.QLabel(self)
        self.styleChoice.move(50, 150)

        self.show()

    def color_picker(self):
        color = QtWidgets.QColorDialog.getColor()
        print(color.name())
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Extract!',
                                            "Get into the chopper?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
