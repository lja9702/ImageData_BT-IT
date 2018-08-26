import os
import Get_and_Split_path
from colormap import rgb2hex
import rgb2colorname
import re
import csv
import retrain_run_inference

#파일명에서 _기준으로 파일명 분리 앞은 옷의 번호, 뒤는 옷의 가격
filename = Get_and_Split_path.filename_includeExt
split_filename = Get_and_Split_path.filename_noExt.partition('_')
split_dirpath = Get_and_Split_path.dir_path.split('s/')
closet_path = Get_and_Split_path.CLOSET_PATH
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
r = re.compile("([a-zA-Z]+)([0-9]+)")   #색이 tan4일경우 tan만 추출하는 코드
items = r.match(nearestcolor)
simplecolor = items.group(1)
print("simplecolor:" + simplecolor)


file = open(closet_path + "/closetInfo.csv", 'a', encoding='utf-8', newline='')
wr = csv.writer(file)

wr.writerow([filename, type, "옷의 브랜드", rgb2hex(color[0], color[1], color[2]), simplecolor])

file.close()
