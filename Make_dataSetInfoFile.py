import Get_and_Split_path
from colormap import rgb2hex
import rgb2colorname
import re
import csv
import os, random
from os import listdir
from os.path import isfile, join

dataset_path = "/home/lja97/dataSets/"

brandList = ['Topten', '8seconds', 'ALAND', 'ClubCambridge', 'LuckyChouette',
             'Mixxo', 'PlasticIsland', 'Spao', 'Tomboy']

fileList = [f for f in listdir(dataset_path + 'T-shirt(Short)') if isfile(join(dataset_path + 'T-shirt(Short)', f))]

infoFile = open(dataset_path + "T-shirt(Short)/dataSetInfo.csv", 'a', encoding='utf-8', newline='')
wr = csv.writer(infoFile)

print(fileList)
get_all_path = Get_and_Split_path.GetAllPath()
for f in fileList:
    fileName = f
    #이미지 파일이 아니라면 넘어가기
    if (not'.jpg' in fileName) and (not '.jpeg' in fileName) and (not '.png' in fileName):
        continue
    no_extFileName = (fileName.split('.'))[0]
    type = 't shirt short '
    price = (no_extFileName.split('_'))[1]
    brand = random.choice(brandList)
    print(dataset_path + 'T-shirt(Short)/' + fileName)
    get_all_path.set_Filepath(filepath = dataset_path + 'T-shirt(Short)/' + fileName)
    color, nearestcolor = rgb2colorname.rgb2colorname(get_all_path)
    wr.writerow([fileName, type, brand, price, rgb2hex(color[0], color[1], color[2]), nearestcolor])

#random.choice(os.listdir("C:\\"))