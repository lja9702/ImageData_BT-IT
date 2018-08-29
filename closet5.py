# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'closet3.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sip

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QStandardItem, QDragEnterEvent, QDropEvent
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from colormap import rgb2hex
import os
import shutil
from bs4 import BeautifulSoup
import urllib.request
import os
import random
import csv
import threading
from selenium import webdriver


import Crolling_BrandWeb
import Get_and_Split_path
import Make_dressInfoFile
import rgb2colorname
import retrain_run_inference


#################################################################################################
get_all_path = Get_and_Split_path.GetAllPath()
CROLLING_PATH = get_all_path.CROLLING_PATH
CLOSET_PATH = get_all_path.CLOSET_PATH
#################################################################################################
global new
new = ""

#Crolling_BrandWeb.get_Topten(url="https://www.topten10.co.kr/main/main.asp", brand="Topten")
#Crolling_BrandWeb.get_Mixxo(
#    url="http://mixxo.elandmall.com/main/initMain.action?chnl_no=GAW&chnl_dtl_no=1803401340&_emk_keyword=MIXXO&gclid=CjwKCAjw8O7bBRB0EiwAfbrTh68VSa9JCwk3GQWI-NjCHyojwrkavrow95BQjUkifKMPFftcWZCmzRoC59EQAvD_BwE&utm_referrer=http%3A%2F%2Fwww.elandmall.com%2Fgate%2Fgate.action%3Fchnl_no%3DGAW%26chnl_dtl_no%3D1803401340%26_emk_keyword%3DMIXXO%26gclid%3DCjwKCAjw8O7bBRB0EiwAfbrTh68VSa9JCwk3GQWI-NjCHyojwrkavrow95BQjUkifKMPFftcWZCmzRoC59EQAvD_BwE",
#    brand="Mixxo")
#Crolling_BrandWeb.get_PlasticIsland(url="https://www.theamall.com", brand="PlasticIsland")
#Crolling_BrandWeb.get_LuckyChouette(url="https://www.kolonmall.com/LUCKYCHOUETTE", brand="LuckyChouette")
#Crolling_BrandWeb.get_Tomboy(url="http://fashion.sivillage.com/display/brandTOMBOYMain?temp=www.tomboy.co.kr", brand="Tomboy")
#Crolling_BrandWeb.get_Spao(url="http://spao.elandmall.com/main/initMain.action", brand="Spao")
#Crolling_BrandWeb.get_8seconds(
#    url="http://www.ssfshop.com/8Seconds/main?dspCtgryNo=&brandShopNo=BDMA07A01&brndShopId=8SBSS&leftBrandNM=",
#    brand="8seconds")
#Crolling_BrandWeb.get_ALAND(url="http://www.a-land.co.kr", brand="ALAND")

class Banner(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, flags=Qt.Widget)

        bannerLayout = QBoxLayout(QBoxLayout.TopToBottom, self)

        self.Banner_img = QLabel("Banner_img")
        self.Banner_name = QLabel("Banner_name")

        #path_dir = "C:\\Users/jykatharGram/Desktop/contest2/Brand_img"
        dir_list = os.listdir(CROLLING_PATH)
        #print(dir_list)
        random_brand = random.choice(dir_list)

        brand_file_list = os.listdir(CROLLING_PATH + random_brand)
        #print(brand_file_list)
        random_img_in_brand = random.choice(brand_file_list)
        print(random_img_in_brand)

        bannerPixelMap = QPixmap(CROLLING_PATH + random_brand + '/' + random_img_in_brand)
        smallerBannerPixmap = bannerPixelMap.scaled(300, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.Banner_img.setPixmap(smallerBannerPixmap)
        self.Banner_name.setText(random_brand)

        bannerLayout.addWidget(self.Banner_img)
        bannerLayout.addWidget(self.Banner_name)



class closetLabel(QLabel):
    def __init__(self, title):
        QLabel.__init__(self, title)
        self.setText("<옷을 추가해주세요>")
        self.setAcceptDrops(True)
        self.check = 0


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
            self.check = 0
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            self.check = 0
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                self.path = str(url.toLocalFile())
                closetPixelMap = QPixmap(self.path)
                smaller_pixmap = closetPixelMap.scaled(431, 431, Qt.KeepAspectRatio, Qt.FastTransformation)
                self.setPixmap(smaller_pixmap)
                self.check = 1




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

        self.treeview.setRootIndex(self.dirModel.index(get_all_path.ROOT_PATH))
        self.listview.setRootIndex(self.fileModel.index(get_all_path.ROOT_PATH))

        self.listview.setViewMode(QListView.IconMode)
        self.listview.setDragEnabled(True)
        self.treeview.clicked.connect(self.on_clicked)

    def on_clicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.listview.setRootIndex(self.fileModel.setRootPath(path))

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
        #self.label_3.setObjectName("label_3")
        #self.label_3.setAcceptDrops(True)
        #self.verticalLayout_3.addWidget(self.label_3)

        self.cl = closetLabel("closetLabel")
        self.cl.acceptDrops()
        self.verticalLayout_3.addWidget(self.cl)
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
        #self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        #self.pushButton_6.setObjectName("pushButton_6")
        #self.verticalLayout_5.addWidget(self.pushButton_6)
        #self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        #self.pushButton_7.setObjectName("pushButton_7")
        #self.verticalLayout_5.addWidget(self.pushButton_7)
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

        self.info_layout = QGridLayout()
        self.info_button = QPushButton("옷 정보보기")
        self.info_button.clicked.connect(self.infoButtonClicked)
        self.info_layout.addWidget(self.info_button)
        self.verticalLayout_5.addLayout(self.info_layout)


    def infoButtonClicked(self):
        if self.cl.check == 0:
            for i in reversed(range(self.info_layout.count())):
                self.info_layout.itemAt(i).widget().deleteLater()
            self.label1 = QLabel("Type: ")
            self.label2 = QLabel("Cost: ")
            self.label3 = QLabel("Brand: ")
            self.label4 = QLabel("Color: ")
            self.fn = os.path.split(self.new_cloth_name) #파일 경로

            get_all_path.set_Filepath(self.new_cloth_name)  #파일 경로 저장
            # TODO:러닝된 옷의 가장 높은 확률 가져오기
            retrain = retrain_run_inference.retrain_run_inference(get_all_path) #옷의 타입 판단
            temp_type = retrain.run_inference_on_image()
            self.type = temp_type[2:-3]

            self.label5 = QLabel(self.type)

            self.lineEdit1 = QLineEdit()
            self.lineEdit2 = QLineEdit()
            self.styleChoice = QtWidgets.QLabel()

            # TODO:새로운 옷의 컬러 추출
            self.color, self.nearestcolor = rgb2colorname.rgb2colorname(get_all_path)
            self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % (rgb2hex(self.color[0], self.color[1], self.color[2])))
            #self.fontColor = QtWidgets.QPushButton('Changing Color')
            #self.fontColor.clicked.connect(self.color_picker)

            self.pushButton1 = QPushButton("내 옷장에 추가하기")
            self.pushButton1.clicked.connect(self.OKButtonClicked)

            self.pushButton2 = QPushButton("뒤로가기")
            self.pushButton2.clicked.connect(self.backButtonClicked)

            self.info_layout.addWidget(self.label1, 0, 0)
            self.info_layout.addWidget(self.label2, 1, 0)
            self.info_layout.addWidget(self.label3, 2, 0)
            self.info_layout.addWidget(self.label4, 3, 0)
            self.info_layout.addWidget(self.label5, 0, 1)
            self.info_layout.addWidget(self.lineEdit1, 1, 1)
            self.info_layout.addWidget(self.lineEdit2, 2, 1)
            self.info_layout.addWidget(self.styleChoice, 3, 1)
            #self.info_layout.addWidget(self.fontColor, 3, 2)
            self.info_layout.addWidget(self.pushButton1, 4, 1)
            self.info_layout.addWidget(self.pushButton2, 4, 2)
        else:
            for i in reversed(range(self.info_layout.count())):
                self.info_layout.itemAt(i).widget().deleteLater()
            self.label1 = QLabel("Type: ")
            self.label2 = QLabel("Cost: ")
            self.label3 = QLabel("Brand: ")
            self.label4 = QLabel("Color: ")
            fn = os.path.split(self.cl.path)

            get_all_path.set_Filepath(self.cl.path)  #옷의 파일 경로 받기

            ################################# TODO: 옷정보 CSV파일에서 읽기
            #csv파일 읽기
            read_csv = Get_and_Split_path.read_csvFile(FILE_NAME = fn[1], CLOSET_PATH= CLOSET_PATH)
            read_csv.get_specificRow_useFilePath()
            self.label5 = QLabel(str(read_csv.type))
            self.label6 = QLabel(str(read_csv.price))
            self.label7 = QLabel(str(read_csv.brand))
            self.styleChoice = QtWidgets.QLabel()

            self.styleChoice.setStyleSheet(
                "QWidget { background-color: %s}" % (read_csv.hexcolor))

            #self.fontColor = QtWidgets.QPushButton('Changing Color')
            #self.fontColor.clicked.connect(self.color_picker)
            self.pushButton2 = QPushButton("뒤로가기")
            self.pushButton2.clicked.connect(self.backButtonClicked)

            self.info_layout.addWidget(self.label1, 0, 0)
            self.info_layout.addWidget(self.label2, 1, 0)
            self.info_layout.addWidget(self.label3, 2, 0)
            self.info_layout.addWidget(self.label4, 3, 0)
            self.info_layout.addWidget(self.label5, 0, 1)
            self.info_layout.addWidget(self.label6, 1, 1)
            self.info_layout.addWidget(self.label7, 2, 1)
            self.info_layout.addWidget(self.styleChoice, 3, 1)
            #self.info_layout.addWidget(self.fontColor, 3, 2)
            self.info_layout.addWidget(self.pushButton2, 4, 2)
            self.cl.check = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "옷장 관리"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "<옷 추천>"))
        self.pushButton_2.setText(_translate("MainWindow", "매칭"))
        self.pushButton_3.setText(_translate("MainWindow", "옷 불러오기"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        #self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        #self.pushButton_7.setText(_translate("MainWindow", "PushButton"))

    def openFile(self):

        fname = QtWidgets.QFileDialog.getOpenFileName(None, "Open Movie", QDir.homePath())
        self.new_cloth_name = fname[0]
        PixelMap = QPixmap(self.new_cloth_name)
        smaller_pixmap = PixelMap.scaled(431, 431, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.cl.setPixmap(smaller_pixmap)

        for i in reversed(range(self.info_layout.count())):
            self.info_layout.itemAt(i).widget().deleteLater()

        self.info_button = QPushButton("옷 정보보기")
        self.info_button.clicked.connect(self.infoButtonClicked)
        self.info_layout.addWidget(self.info_button)



    def OKButtonClicked(self):
        self.cost = self.lineEdit1.text()
        self.brand = self.lineEdit2.text()

        #TODO: 새로운 옷 MyCloset에 저장
        shutil.copy2(self.new_cloth_name, CLOSET_PATH + self.fn[1])
        Make_dressInfoFile.make_DressInfoFile(file_path = self.new_cloth_name, type = self.type, brand = self.brand, price = self.cost, color = self.color,
                                              nearestcolor = self.nearestcolor)

    def backButtonClicked(self):
        for i in reversed(range(self.info_layout.count())):
            self.info_layout.itemAt(i).widget().deleteLater()
        self.info_button = QPushButton("옷 정보보기")
        self.info_button.clicked.connect(self.infoButtonClicked)
        self.info_layout.addWidget(self.info_button)

    def color_picker(self):
        color = QtWidgets.QColorDialog.getColor()
        print(color.name())
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    #def style_choice(self, text):
     #   self.styleChoice.setText(text)
     #   QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

