import os
import csv
import numpy as np
import pandas as pd
class GetAllPath:
    # ======================================================================================================
    # 가져온 path에서 디렉토리와 파일명 분리 추출

    # WINDOW는 이것도 해줘야 됌
    # 드라이브명까지 포함된 Windows 전용 패스를 취급
    # split_path = os.path.splitdrive(FILE_PATH)

    # 드라이브 이름 (MS윈도우의 경우)
    # drive_name = split_path[0]  # D:
    # ------------------------------------------------------------------------------------------------------
    def __init__(self):
        ##retrain_run_inference.py 실행시킬 때의 graph와 label의 위치 경로
        self.RETRAIN_PATH = '/home/lja97/PycharmProjects/IT_BTProject_aboutFasion'
        ##옷장의 경로
        self.CLOSET_PATH = '/home/lja97/MyCloset/'
        #크롤링 할때의 브랜드별 크롤링 데이터 저장 경로
        self.CROLLING_PATH = "/home/lja97/Crolling/"
        #루트 경로
        self.ROOT_PATH = "/home/lja97/"
        self.DATASET_PATH = "/home/lja97/dataSets/"
    def set_Filepath(self, filepath):
        self.FILE_PATH = filepath
        return self.FILE_PATH  ##옷 자체의 경로 <- 옷 새로 저장할 때 디렉토리 정보 받이오기

    def path_split(self):
        split_path = os.path.split(self.FILE_PATH)  ##윈도우는 FILE_PATH대신 split_path[1]를 사용
        #split_path[0]는 디렉토리명 , [1]은 확장자를 포홤한 파일명
        return split_path

    def get_extention(self):
        return (os.path.splitext(self.FILE_PATH))[1]

    def get_noExt_filename(self):
        return (os.path.split(os.path.splitext(self.FILE_PATH)[0]))[1]


class read_csvFile:
    def __init__(self, FILE_NAME, CLOSET_PATH):
        # csv파일불러서 지역변수에 저장하기
        self.filename = FILE_NAME
        self.closetpath = CLOSET_PATH
        self.csv_file = pd.read_csv(self.closetpath + 'closetInfo.csv',
                                    names = ["name","type","brand","price","hexcolor","simplecolor"])

    def get_specificRow_useFilePath(self):
        # 파일 명이 해당 파일 명인 얘를 받아오기

        specRow = self.csv_file[self.csv_file.name == self.filename]
        specRow = specRow.iloc[0]
        self.type = specRow['type']
        self.brand = specRow['brand']
        self.price = specRow['price']
        self.hexcolor = specRow['hexcolor']

        #print(self.type, self.brand, self.price, self.hexcolor)
#read_csvFile = read_csvFile(FILE_NAME = "4.jpg", CLOSET_PATH = '/home/lja97/MyCloset/')
#read_csvFile.get_specificRow_useFilePath()
