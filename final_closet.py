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
import pandas as pd

import dressMatching
import Crolling_BrandWeb
import Get_and_Split_path
import Make_dressInfoFile
import rgb2colorname
import retrain_run_inference
import dressRecommend


#################################################################################################
get_all_path = Get_and_Split_path.GetAllPath()
CROLLING_PATH = get_all_path.CROLLING_PATH
CLOSET_PATH = get_all_path.CLOSET_PATH
DATASET_PATH = get_all_path.DATASET_PATH
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 612))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(430, 0, 431, 612))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(860, 0, 431, 431))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.cl = closetLabel("closetLabel")
        self.cl.acceptDrops()
        self.verticalLayout_3.addWidget(self.cl)

        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(860, 430, 431, 181))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

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

        #옷 불러오기 버튼 클릭시 이벤트 동작
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_3.clicked.connect(self.openFile)

        #옷 정보를 볼 수 있는 레이아웃
        self.info_layout = QGridLayout()
        self.info_button = QPushButton("옷 정보보기")
        self.info_button.clicked.connect(self.infoButtonClicked)
        self.info_layout.addWidget(self.info_button)
        self.verticalLayout_5.addLayout(self.info_layout)

        #옷 매칭을 할 수 있는 레이아웃
        self.matchingLayout = QGridLayout()
        #'매칭' -> '옷 매칭하기'로 텍스트 바꿈
        self.matching_button = QPushButton("옷 매칭하기")
        self.matching_button.clicked.connect(self.matchingButtonClicked)
        self.matchingLayout.addWidget(self.matching_button)
        self.verticalLayout_2.addLayout(self.matchingLayout)

        #옷 추천을 할 수 있는 레이아웃
        self.recommendLayout = QGridLayout()
        #self.recommend_button = QPushButton("옷 추천하기")
        #self.recommend_button.clicked.connect(self.recommendButtonClicked)
        #self.recommendLayout.addWidget(self.recommend_button)
        #self.verticalLayout.addLayout(self.recommendLayout)
        #TODO: 여기에 영역1 추천받은 옷들 함수 넣기
        self.recommend_cloth()


    def recommend_cloth(self):

        for i in reversed(range(self.recommendLayout.count())):
            self.recommendLayout.itemAt(i).widget().deleteLater()

        #카테고리 라벨
        self.cat_label_1 = QLabel("   옷장속의 옷")
        self.cat_label_2 = QLabel("   추천하는 옷 1")
        self.cat_label_3 = QLabel("   추천하는 옷 2")

        #1열에 출력하는 옷장 속의 옷들
        self.closet_img_1 = QLabel()
        self.closet_img_2 = QLabel()
        self.closet_img_3 = QLabel()

        #2,3열에 출력하는 추천받은 옷들
        self.recommend_img_1 = QLabel()
        self.recommend_img_2 = QLabel()
        self.recommend_img_3 = QLabel()
        self.recommend_img_4 = QLabel()
        self.recommend_img_5 = QLabel()
        self.recommend_img_6 = QLabel()

        # 2,3열에 출력하는 추천받은 옷 브랜드 이름
        self.recommend_bname_1 = QLabel()
        self.recommend_bname_2 = QLabel()
        self.recommend_bname_3 = QLabel()
        self.recommend_bname_4 = QLabel()
        self.recommend_bname_5 = QLabel()
        self.recommend_bname_6 = QLabel()


        # 랜덤한 스타일로 랜덤한 옷 1열에 이미지 출력
        filelist = os.listdir(CLOSET_PATH)
        filelist.remove('closetInfo.csv')
        #첫번째 랜덤 옷
        closet_info = pd.read_csv(CLOSET_PATH + 'closetInfo.csv',
                           names=["name", "type", "brand", "price", "hexcolor", "simplecolor"])

        random_closet = closet_info.sample(frac=1)
        print(random_closet.iloc[0]['name'])
        random_cloth_1 = random_closet.iloc[0]['name']
        random_cloth_2 = random_closet.iloc[1]['name']
        random_cloth_3 = random_closet.iloc[2]['name']

        bannerPixelMap_1 = QPixmap(CLOSET_PATH + random_cloth_1)
        smallerBannerPixmap_1 = bannerPixelMap_1.scaled(143, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.closet_img_1.setPixmap(smallerBannerPixmap_1)

        print(CLOSET_PATH + random_cloth_1)

        type = random_closet.iloc[0]['type']  # 옷1의 타입
        color = random_closet.iloc[0]['simplecolor']  # 옷1의 rgb값, 가까운 영문 색

        # 첫번째 옷장 옷에 대한 추천
        cloth1_recommend = dressRecommend.recommend_area1(dataset_path=DATASET_PATH, type=type,
                                                          simplecolor=color)
        cloth1_recomList, cloth1_brandList = cloth1_recommend.recommand_cloth()

        cloth1_recom1_brand = cloth1_brandList[0]
        cloth1_recom2_brand = cloth1_brandList[1]

        bannerPixelMap_cloth1_recommend1 = QPixmap(cloth1_recomList[0])
        bannerPixelMap_cloth1_recommend2 = QPixmap(cloth1_recomList[1])

        smallerBannerPixmap_cloth1_recommend1 = bannerPixelMap_cloth1_recommend1.scaled(143, 200, Qt.KeepAspectRatio,
                                                                                        Qt.FastTransformation)
        self.recommend_img_1.setPixmap(smallerBannerPixmap_cloth1_recommend1)
        self.recommend_bname_1.setText(cloth1_recom1_brand)

        smallerBannerPixmap_cloth1_recommend2 = bannerPixelMap_cloth1_recommend2.scaled(143, 200, Qt.KeepAspectRatio,
                                                                                        Qt.FastTransformation)
        self.recommend_img_2.setPixmap(smallerBannerPixmap_cloth1_recommend2)
        self.recommend_bname_2.setText(cloth1_recom2_brand)

        # 두번째 랜덤옷
        bannerPixelMap_2 = QPixmap(CLOSET_PATH + random_cloth_2)
        smallerBannerPixmap_2 = bannerPixelMap_2.scaled(143, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.closet_img_2.setPixmap(smallerBannerPixmap_2)

        type = random_closet.iloc[1]['type']  # 옷1의 타입
        color = random_closet.iloc[1]['simplecolor']  # 옷1의 rgb값, 가까운 영문 색

        # 두번째 옷장 옷에 대한 추천
        cloth2_recommend = dressRecommend.recommend_area1(dataset_path=DATASET_PATH, type=type,
                                                          simplecolor=color)
        cloth2_recomList, cloth2_brandList = cloth2_recommend.recommand_cloth()

        cloth2_recom1_brand = cloth2_brandList[0]
        cloth2_recom2_brand = cloth2_brandList[1]

        bannerPixelMap_cloth2_recommend1 = QPixmap(cloth2_recomList[0])
        bannerPixelMap_cloth2_recommend2 = QPixmap(cloth2_recomList[1])

        smallerBannerPixmap_cloth2_recommend1 = bannerPixelMap_cloth2_recommend1.scaled(143, 200, Qt.KeepAspectRatio,
                                                                                        Qt.FastTransformation)
        self.recommend_img_3.setPixmap(smallerBannerPixmap_cloth2_recommend1)
        self.recommend_bname_3.setText(cloth2_recom1_brand)

        smallerBannerPixmap_cloth2_recommend2 = bannerPixelMap_cloth2_recommend2.scaled(143, 200, Qt.KeepAspectRatio,
                                                                                        Qt.FastTransformation)
        self.recommend_img_4.setPixmap(smallerBannerPixmap_cloth2_recommend2)
        self.recommend_bname_4.setText(cloth2_recom2_brand)

        # 세번째 랜덤 옷
        bannerPixelMap_3 = QPixmap(CLOSET_PATH + random_cloth_3)
        smallerBannerPixmap_3 = bannerPixelMap_3.scaled(143, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.closet_img_3.setPixmap(smallerBannerPixmap_3)

        type = random_closet.iloc[2]['type']  # 옷3의 타입
        color = random_closet.iloc[2]['simplecolor']  # 옷3의 rgb값, 가까운 영문 색

        # 세번째 옷장 옷에 대한 추천
        cloth3_recommend = dressRecommend.recommend_area1(dataset_path=DATASET_PATH, type=type,
                                                          simplecolor=color)

        cloth3_recomList, cloth3_brandList = cloth3_recommend.recommand_cloth()
        cloth3_recom1_brand = cloth3_brandList[0]
        cloth3_recom2_brand = cloth3_brandList[1]

        bannerPixelMap_cloth3_recommend1 = QPixmap(cloth3_recomList[0])
        bannerPixelMap_cloth3_recommend2 = QPixmap(cloth3_recomList[1])

        smallerBannerPixmap_cloth3_recommend1 = bannerPixelMap_cloth3_recommend1.scaled(143, 200, Qt.KeepAspectRatio,
                                                                                        Qt.FastTransformation)
        self.recommend_img_5.setPixmap(smallerBannerPixmap_cloth3_recommend1)
        self.recommend_bname_5.setText(cloth3_recom1_brand)

        smallerBannerPixmap_cloth3_recommend2 = bannerPixelMap_cloth3_recommend2.scaled(143, 200, Qt.KeepAspectRatio,
                                                                                        Qt.FastTransformation)
        self.recommend_img_6.setPixmap(smallerBannerPixmap_cloth3_recommend2)
        self.recommend_bname_6.setText(cloth3_recom2_brand)

        #새로고침 버튼
        self.update_button = QPushButton("새로고침")
        self.update_button.clicked.connect(self.recommendButtonClicked)

        # 카테고리 라벨
        self.recommendLayout.addWidget(self.cat_label_1, 0, 0)
        self.recommendLayout.addWidget(self.cat_label_2, 0, 1)
        self.recommendLayout.addWidget(self.cat_label_3, 0, 2)

        # 옷장속의 옷 라벨
        self.recommendLayout.addWidget(self.closet_img_1, 1, 0)
        self.recommendLayout.addWidget(self.closet_img_2, 3, 0)
        self.recommendLayout.addWidget(self.closet_img_3, 5, 0)

        # 추천하는 옷 라벨
        self.recommendLayout.addWidget(self.recommend_img_1, 1, 1)
        self.recommendLayout.addWidget(self.recommend_img_2, 1, 2)
        self.recommendLayout.addWidget(self.recommend_img_3, 3, 1)
        self.recommendLayout.addWidget(self.recommend_img_4, 3, 2)
        self.recommendLayout.addWidget(self.recommend_img_5, 5, 1)
        self.recommendLayout.addWidget(self.recommend_img_6, 5, 2)
        self.recommendLayout.addWidget(self.update_button, 7, 2)

        # 추천하는 옷 브랜드 이름
        self.recommendLayout.addWidget(self.recommend_bname_1, 2, 1)
        self.recommendLayout.addWidget(self.recommend_bname_2, 2, 2)
        self.recommendLayout.addWidget(self.recommend_bname_3, 4, 1)
        self.recommendLayout.addWidget(self.recommend_bname_4, 4, 2)
        self.recommendLayout.addWidget(self.recommend_bname_5, 6, 1)
        self.recommendLayout.addWidget(self.recommend_bname_6, 6, 2)
        self.verticalLayout.addLayout(self.recommendLayout)

    def learning_cloth_type(self, CLOTH_PATH):
        get_all_path.set_Filepath(CLOTH_PATH)  # 파일 경로 저장
        # TODO:러닝된 옷의 가장 높은 확률 가져오기
        retrain = retrain_run_inference.retrain_run_inference(get_all_path)  # 옷의 타입 판단
        temp_type = retrain.run_inference_on_image()
        self.newCloth_type = temp_type[2:-3]  # 옷의 타입

    def learning_cloth_color(self, CLOTH_PATH):
        get_all_path.set_Filepath(CLOTH_PATH)
        self.newCloth_color, self.newCloth_nearestcolor = rgb2colorname.rgb2colorname(get_all_path)  # 옷의 rgb값, 가까운 영문 색

    # 영역3의 '옷 정보보기' 버튼에 대한 이벤트 리스너
    def infoButtonClicked(self):
        if self.cl.check == 0:
            for i in reversed(range(self.info_layout.count())):
                self.info_layout.itemAt(i).widget().deleteLater()
            self.label1 = QLabel("Type: ")
            self.label2 = QLabel("Cost: ")
            self.label3 = QLabel("Brand: ")
            self.label4 = QLabel("Color: ")
            self.fn = os.path.split(self.new_cloth_name) #파일 경로

            self.label5 = QLabel(self.newCloth_type)

            self.lineEdit1 = QLineEdit()
            self.lineEdit2 = QLineEdit()
            self.styleChoice = QtWidgets.QLabel()

            # TODO:새로운 옷의 컬러 추출
            self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % (rgb2hex(self.newCloth_color[0], self.newCloth_color[1], self.newCloth_color[2])))
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

            #csv파일 읽기
            read_csv = Get_and_Split_path.read_csvFile(FILE_NAME = fn[1], CLOSET_PATH= CLOSET_PATH)
            read_csv.get_specificRow_useFilePath()

            self.label5 = QLabel(str(read_csv.type))
            self.label6 = QLabel(str(read_csv.price))
            self.label7 = QLabel(str(read_csv.brand))
            self.styleChoice = QtWidgets.QLabel()

            self.styleChoice.setStyleSheet(
                "QWidget { background-color: %s}" % (read_csv.hexcolor))

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
        self.pushButton_3.setText(_translate("MainWindow", "옷 불러오기"))


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

        self.cl.repaint()

        self.learning_cloth_type(CLOTH_PATH = self.new_cloth_name)  # 옷의 타입
        self.learning_cloth_color(CLOTH_PATH = self.new_cloth_name)  # 옷의 rgb값, 가까운 영문 색

    # 영역2의 '매칭' 버튼에 대한 이벤트 리스너
    def matchingButtonClicked(self):

        for i in reversed(range(self.matchingLayout.count())):
            self.matchingLayout.itemAt(i).widget().deleteLater()

        self.matching_img_1 = QLabel()
        self.matching_img_2 = QLabel()
        self.matching_img_3 = QLabel()
        self.matching_img_4 = QLabel()

        # 옷장 경로
        dir_list = os.listdir(CLOSET_PATH)

        #TODO: 색상과 옷의 타입 고려해서 옷장 속의 옷 추천하기

        matching = dressMatching.matching_area2(dress_path = self.new_cloth_name, closet_path = CLOSET_PATH,
                                                type = self.newCloth_type, simplecolor = self.newCloth_nearestcolor)

        #옷장 리스트 받아오기
        info = pd.read_csv(CLOSET_PATH + 'closetInfo.csv',
                               names=["name", "type", "brand", "price", "hexcolor", "simplecolor"])

        #옷장 리스트 한줄씩 검색하면서 보여줄 옷 뽑기
        matchingList = []   #매칭된 옷들의 경로
        cnt = 0     #최대 4개의 옷만 추출
        for index, row in info.iterrows():
            if cnt == 4:    break
            if(matching.matching_cloth(rowtype = row['type'], rowcolor = row['simplecolor'])): #만약 어울리는 옷이 있으면 True반환
                matchingList.append(CLOSET_PATH + row['name'])
                cnt += 1

        ########TODO: 재영오빠한테 질문 if문 작성

        #만약 옷장속의 매칭된 옷이 없다면 어울리는 옷이 없다고 출력
        if len(matchingList) == 0 :
            self.setText("<어울리는 옷이 없습니다.>")
        #옷장속의 매칭된 옷의 개수에 따라 출력 결과 달라짐
        else:
            if len(matchingList) >= 1:
                bannerPixelMap_1 = QPixmap(matchingList[0])
                smallerBannerPixmap_1 = bannerPixelMap_1.scaled(300, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
                self.matching_img_1.setPixmap(smallerBannerPixmap_1)

            if len(matchingList) >= 2:
                bannerPixelMap_2 = QPixmap(matchingList[1])
                smallerBannerPixmap_2 = bannerPixelMap_2.scaled(300, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
                self.matching_img_2.setPixmap(smallerBannerPixmap_2)

            if len(matchingList) >= 3:
                bannerPixelMap_3 = QPixmap(matchingList[2])
                smallerBannerPixmap_3 = bannerPixelMap_3.scaled(300, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
                self.matching_img_3.setPixmap(smallerBannerPixmap_3)

            if len(matchingList) >= 4:
                bannerPixelMap_4 = QPixmap(matchingList[3])
                smallerBannerPixmap_4 = bannerPixelMap_4.scaled(300, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
                self.matching_img_4.setPixmap(smallerBannerPixmap_4)

        self.back_button_2 = QPushButton("뒤로 가기")
        self.back_button_2.clicked.connect(self.backButtonClicked_2)

        self.matchingLayout.addWidget(self.matching_img_1, 0, 0)
        self.matchingLayout.addWidget(self.matching_img_2, 0, 1)
        self.matchingLayout.addWidget(self.matching_img_3, 1, 0)
        self.matchingLayout.addWidget(self.matching_img_4, 1, 1)
        self.matchingLayout.addWidget(self.back_button_2, 5, 1)

    # 영역1의 '옷 추천하기' 버튼에 대한 이벤트 리스너
    def recommendButtonClicked(self):

        self.recommend_cloth()

        #self.update_button = QPushButton("새로고침")
        #self.update_button.clicked.connect(self.recommendButtonClicked)


    # 영역3의 '내 옷장에 추가하기' 버튼에 대한 이벤트 리스너
    def OKButtonClicked(self):
        self.cost = self.lineEdit1.text()
        self.brand = self.lineEdit2.text()

        #TODO: 새로운 옷 MyCloset에 저장
        shutil.copy2(self.new_cloth_name, CLOSET_PATH + self.fn[1])
        Make_dressInfoFile.make_DressInfoFile(file_path = self.new_cloth_name, type = self.newCloth_type,
                                              brand = self.brand, price = self.cost, color = self.newCloth_color,
                                              nearestcolor = self.newCloth_nearestcolor)

    # 영역3의 '뒤로가기' 버튼에 대한 이벤트 리스너
    def backButtonClicked(self):
        for i in reversed(range(self.info_layout.count())):
            self.info_layout.itemAt(i).widget().deleteLater()
        self.info_button = QPushButton("옷 정보보기")
        self.info_button.clicked.connect(self.infoButtonClicked)
        self.info_layout.addWidget(self.info_button)



    #영역2의 '뒤로가기' 버튼에 대한 이벤트 리스너
    def backButtonClicked_2(self):
        for i in reversed(range(self.matchingLayout.count())):
            self.matchingLayout.itemAt(i).widget().deleteLater()
        #'매칭' -> '옷 매칭하기' 로 텍스트 바꿈
        self.matching_button = QPushButton("옷 매칭하기")
        self.matching_button.clicked.connect(self.matchingButtonClicked)
        self.matchingLayout.addWidget(self.matching_button)


    def color_picker(self):
        color = QtWidgets.QColorDialog.getColor()
        print(color.name())
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

