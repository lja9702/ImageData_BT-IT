import Get_and_Split_path
from colormap import rgb2hex
import rgb2colorname
import re
import csv
import os
import retrain_run_inference
#from os import listdir
#from os.path import isfile, join

#파일명에서 _기준으로 파일명 분리 앞은 옷의 번호, 뒤는 옷의 가격
filename = Get_and_Split_path.filename_includeExt
split_filename = Get_and_Split_path.filename_noExt.partition('_')
split_dirpath = Get_and_Split_path.dir_path.split('s/')
closet_path = Get_and_Split_path.CLOSET_PATH
#폴더내 파일 가져오기
#files = [f for f in listdir(closet_path) if isfile(join(closet_path, f))]
#폴더내의 .csv이외의 파일 모두 가져오기
#files = [x for x in files if x.find(".csv") == -1]

#TODO:러닝된 옷의 가장 높은 확률 가져오기
temp = retrain_run_inference.run_inference_on_image()
type = temp[2:-3]
print("type:", type)

#TODO:옷의 가격 입력한 값 가져오기
    #price =
#TODO:옷의 브랜드 입력한 값 가져오기
    #brand =

#옷의 색깔 (hex)
color = rgb2colorname.color
print("color:", color)
print("hexcolor:", rgb2hex(color[0], color[1], color[2]))
#옷의 색깔 (name)
nearestcolor = rgb2colorname.ColorName
#r = re.compile("([a-zA-Z]+)([0-9]+)")   #색이 tan4일경우 tan만 추출하는 코드
#items = r.match(nearestcolor)
#simplecolor = items.group(1)
print("simplecolor:" + nearestcolor)


file = open(closet_path + "/closetInfo.csv", 'a', encoding='utf-8', newline='')
wr = csv.writer(file)

wr.writerow([filename, type, "옷의 브랜드", "가격", rgb2hex(color[0], color[1], color[2]), nearestcolor])

file.close()
