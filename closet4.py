# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'closet3.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QStandardItem
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
import os
from bs4 import BeautifulSoup
import urllib.request
import os
import random
from PyQt5.QtGui import QDragEnterEvent
from PyQt5.QtGui import QDropEvent



class Banner(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, flags=Qt.Widget)

        bannerLayout = QBoxLayout(QBoxLayout.TopToBottom, self)

        self.Banner_img = QLabel("Banner_img")
        self.Banner_name = QLabel("Banner_name")

        path_dir = "C:\\Users/jykatharGram/Desktop/contest2/Brand_img"
        dir_list = os.listdir(path_dir)
        #print(dir_list)
        random_brand = random.choice(dir_list)

        brand_file_list = os.listdir(path_dir + '/' + random_brand)
        #print(brand_file_list)
        random_img_in_brand = random.choice(brand_file_list)
        print(random_img_in_brand)

        bannerPixelMap = QPixmap(path_dir + '/' + random_brand + '/' + random_img_in_brand)
        smallerBannerPixmap = bannerPixelMap.scaled(300, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.Banner_img.setPixmap(smallerBannerPixmap)
        self.Banner_name.setText(random_brand)

        bannerLayout.addWidget(self.Banner_img)
        bannerLayout.addWidget(self.Banner_name)

    # base_url: 이미지를 따올 서버의 주소
    # url: 접속할 URL
    def get_Topten(url):
        count = 1  # 웹사이트에 있는 이미지를 크롤링 한 순서번호로 파일 저장
        html = urllib.request.urlopen(url)  # url에 접속하여
        source = html.read()  # html소스코드를 source변수에 저장
        # 불러온 HTML소스를 기반으로 하여 BeautifulSoup 객체 생성 -> 파싱
        soup = BeautifulSoup(source, "html.parser")
        for div_tag in soup.find_all('div'):  # 불러온 HTML에서 모든 div태그에서
            if div_tag.has_attr('data-slick-index'):
                print("bb")
                # a태그찾기
                for a_tag in soup.find_all('a'):
                    st = a_tag['style']  # style속성을 받아오고
                    start_idx = st.index("url(") + len("url(")  # url 뒤부터 인덱스 받아오기
                    end_idx = st.index(");")  # 괄호가 닫히기 전 인덱스 받기
                    print(st[start_idx:end_idx])  # url string받아오기
                    img_url = "http:" + st[start_idx:end_idx]  # url 풀네임 저장
                    img_name = str(count) + ".jpg"  # 이미지 명은 count
                    urllib.request.urlretrieve(img_url,
                                               "C:\\Users/jykatharGram/Desktop/contest2/Brand_img/Topten/" + img_name)
                    print("이미지 url: ", img_url)
                    print("이미지 명: ", img_name)
                    print("\n")
                    count += 1

    def get_Mixxo(url):
        count = 1
        html = urllib.request.urlopen(url)
        source = html.read()
        soup = BeautifulSoup(source, "html.parser")
        for li_tag in soup.find_all("li"):
            if li_tag.has_attr('style') and "background-image" in li_tag['style']:
                st = li_tag['style']
                start_idx = st.index("url(") + len("url(")
                end_idx = st.index(");")
                img_url = "http:" + st[start_idx + 1:end_idx - 1]
                print(img_url)
                filepath, fileext = os.path.splitext(img_url)
                if fileext != '.jpg': continue
                img_name = str(count) + ".jpg"
                urllib.request.urlretrieve(img_url,
                                           "C:\\Users/jykatharGram/Desktop/contest2/Brand_img/Mixxo/" + img_name)
                print("이미지 url: ", img_url)
                print("이미지 명: ", img_name)
                print("\n")
                count += 1

    def get_PlasticIsland(url):
        count = 1
        html = urllib.request.urlopen(url + '/plastic')
        source = html.read()
        soup = BeautifulSoup(source, "html.parser")
        for img_tag in soup.find_all("img"):
            if not img_tag.has_attr('usemap'):
                continue
            if img_tag.has_attr('src'):
                use_map = img_tag['usemap']
                if (not "brand-top-plastic" in use_map):
                    continue
                st = img_tag['src']
                if "http://" in st:
                    img_url = st
                else:
                    img_url = url + st
                filepath, fileext = os.path.splitext(img_url)
                if fileext == '.jpg' or fileext == '.jpeg':
                    img_name = str(count) + str(fileext)
                else:
                    continue
                urllib.request.urlretrieve(img_url,
                                           "C:\\Users/jykatharGram/Desktop/contest2/Brand_img/PlasticIsland/" + img_name)
                print("이미지 url: ", img_url)
                print("이미지 명: ", img_name)
                print("\n")
                count += 1

    def get_LuckyChouette(url):
        count = 1
        html = urllib.request.urlopen(url)
        source = html.read()
        soup = BeautifulSoup(source, "html.parser")
        div = soup.find_all('div', {'class': 'fix-ratio-106 bg-image'})
        for d_tag in div:
            if d_tag.has_attr('style'):
                st = d_tag['style']
                start_idx = st.index("url(") + len("url(")
                end_idx = st.index(")")
                img_url = st[start_idx + 1:end_idx - 1]
                print(img_url)
                filepath, fileext = os.path.splitext(img_url)
                if fileext == '.jpg' or fileext == '.jpeg':
                    img_name = str(count) + str(fileext)
                else:
                    continue
                urllib.request.urlretrieve(img_url,
                                           "C:\\Users/jykatharGram/Desktop/contest2/Brand_img/LuckyChouette/" + img_name)
                print("이미지 url: ", img_url)
                print("이미지 명: ", img_name)
                print("\n")
                count += 1

    def get_Tomboy(url):
        count = 1
        html = urllib.request.urlopen(url)
        source = html.read()
        soup = BeautifulSoup(source, "html.parser")
        div = soup.find_all('div', {'class': 'gridItem'})
        for d_tag in div:
            for img_tag in soup.find_all('img'):
                if img_tag.has_attr('src') and "http://" in img_tag['src']:
                    st = img_tag['src']
                    start_idx = st.index("http://") + len("http://")
                    end_idx = len(st)
                    img_url = "http://" + urllib.parse.quote(st[start_idx:end_idx])
                    print(img_url)
                    filepath, fileext = os.path.splitext(img_url)
                    if fileext == '.jpg' or fileext == '.jpeg':
                        img_name = str(count) + str(fileext)
                        urllib.request.urlretrieve(img_url,
                                                   "C:\\Users/jykatharGram/Desktop/contest2/Brand_img/Tomboy/" + img_name)
                        print("이미지 url: ", img_url)
                        print("이미지 명: ", img_name)
                        print("\n")
                        count += 1

    def get_Spao(url):
        count = 1
        html = urllib.request.urlopen(url)
        source = html.read()
        soup = BeautifulSoup(source, "html.parser")
        div = soup.find_all('div', {'class': 'bnr_sub'})
        for d_tag in div:
            for img_tag in soup.find_all('img'):
                st = img_tag['src']
                if "http" in st:
                    img_url = st
                else:
                    img_url = "http:" + st
                print(img_url)
                filepath, fileext = os.path.splitext(img_url)
                if fileext == '.jpg' or fileext == '.jpeg':
                    img_name = str(count) + str(fileext)
                urllib.request.urlretrieve(img_url,
                                           "C:\\Users/jykatharGram/Desktop/contest2/Brand_img/Spao/" + img_name)
                print("이미지 url: ", img_url)
                print("이미지 명: ", img_name)
                print("\n")
                count += 1

    # CLUB CAMBRIDGE
    # https://www.kolonmall.com/CLUB-CAMBRIDGE -> 데이터 개별저장
    #get_Topten(url="https://www.topten10.co.kr/main/main.asp")
    #get_Mixxo(
     #   url="http://mixxo.elandmall.com/main/initMain.action?chnl_no=GAW&chnl_dtl_no=1803401340&_emk_keyword=MIXXO&gclid=CjwKCAjw8O7bBRB0EiwAfbrTh68VSa9JCwk3GQWI-NjCHyojwrkavrow95BQjUkifKMPFftcWZCmzRoC59EQAvD_BwE&utm_referrer=http%3A%2F%2Fwww.elandmall.com%2Fgate%2Fgate.action%3Fchnl_no%3DGAW%26chnl_dtl_no%3D1803401340%26_emk_keyword%3DMIXXO%26gclid%3DCjwKCAjw8O7bBRB0EiwAfbrTh68VSa9JCwk3GQWI-NjCHyojwrkavrow95BQjUkifKMPFftcWZCmzRoC59EQAvD_BwE")
    #get_PlasticIsland(url="https://www.theamall.com")
    #get_LuckyChouette(url="https://www.kolonmall.com/LUCKYCHOUETTE")
    #get_Tomboy(url="http://fashion.sivillage.com/display/brandTOMBOYMain?temp=www.tomboy.co.kr")
    #get_Spao(url="http://spao.elandmall.com/main/initMain.action")



class closetLabel(QLabel):
    def __init__(self, title):
        QLabel.__init__(self, title)
        self.setText("<옷장에서 옷을 드래그 해주세요>")
        self.setAcceptDrops(True)


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
     if event.mimeData().hasUrls:
         event.setDropAction(QtCore.Qt.CopyAction)
         event.accept()
     else:
         event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                path = str(url.toLocalFile())
                closetPixelMap = QPixmap(path)
                smaller_pixmap = closetPixelMap.scaled(431, 431, Qt.KeepAspectRatio, Qt.FastTransformation)
                self.setPixmap(smaller_pixmap)


        else:
            event.ignore()


class myCloset(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        hlay = QHBoxLayout(self)
        self.treeview = QTreeView()
        self.listview = QListView()
        hlay.addWidget(self.treeview)
        hlay.addWidget(self.listview)

        path = QDir.rootPath()

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)

        self.fileModel = QFileSystemModel()
        self.fileModel.setFilter(QDir.NoDotAndDotDot |  QDir.Files)

        self.treeview.setModel(self.dirModel)
        self.listview.setModel(self.fileModel)

        self.treeview.setRootIndex(self.dirModel.index("C:\\Users/jykatharGram/Documents/GitHub/ImageData_BT-IT/dataSets"))
        self.listview.setRootIndex(self.fileModel.index("C:\\Users/jykatharGram/Documents/GitHub/ImageData_BT-IT/dataSets"))

        self.listview.setViewMode(QListView.IconMode)
        self.listview.setDragEnabled(True)
        self.treeview.clicked.connect(self.on_clicked)

    def on_clicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.listview.setRootIndex(self.fileModel.setRootPath(path))


class valueDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.cost = None
        self.brand = None

    def setupUI(self):
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("Cost & Brand")
        self.setWindowIcon(QIcon('icon.png'))

        label1 = QLabel("Cost: ")
        label2 = QLabel("Brand: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.pushButton1= QPushButton("OK")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.cost = self.lineEdit1.text()
        self.brand = self.lineEdit2.text()
        self.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("옷장 관리")
        MainWindow.resize(1291, 848)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(430, 0, 431, 431))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        #self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        #self.label_2.setObjectName("label_2")
        #self.verticalLayout_2.addWidget(self.label_2)
        cl = closetLabel("closetLabel")
        self.verticalLayout_2.addWidget(cl)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(860, 0, 431, 431))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(430, 430, 431, 181))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_4.addWidget(self.pushButton_5)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(860, 430, 431, 181))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_5.addWidget(self.pushButton_7)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 610, 431, 181))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        bn1 = Banner("EventBanner")
        bn2 = Banner("EventBanner")
        self.horizontalLayout.addWidget(bn1)
        self.horizontalLayout.addWidget(bn2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(430, 610, 861, 181))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.addWidget(myCloset())
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1291, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_3.clicked.connect(self.openFile)
        self.pushButton_6.clicked.connect(self.inputValue)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "옷장 관리"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "<옷을 추가해주세요>"))
        self.pushButton_2.setText(_translate("MainWindow", "내 옷장에서 불러오기"))
        #self.label_2.setText(_translate("MainWindow", "<옷을 추가해주세요>"))
        self.pushButton_3.setText(_translate("MainWindow", "옷 불러오기"))
        self.label_3.setText(_translate("MainWindow", "<옷을 추가해주세요>"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))

    def openFile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None, "Open Movie", QDir.homePath())
        PixelMap = QPixmap(fname[0])
        smaller_pixmap = PixelMap.scaled(431, 431, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label_3.setPixmap(smaller_pixmap)

    def inputValue(self):
        dlg = valueDialog()
        dlg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

