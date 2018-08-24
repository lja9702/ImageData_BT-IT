import getColor
import os
import Get_and_Split_path
from colormap import rgb2hex

#파일명에서 _기준으로 파일명 분리 앞은 옷의 번호, 뒤는 옷의 가격
split_filename = Get_and_Split_path.filename_noExt.partition('_')

split_dirpath = Get_and_Split_path.dir_path.split('/')
#옷의 타입을 디렉토리 명에서 가져옴
type = split_dirpath[len(split_dirpath) - 1]
print("type:" + type)
#옷의 번호
number = split_filename[0]
print("number: " + number)
#옷의 가격
price = split_filename[2]
print("price: " + price)
#옷의 색깔
color = getColor.mostColor.RGBvalue
print("color:", color)

file = open(Get_and_Split_path.filename2[0] + ".txt", 'w')

file.write("type:" + type + "\n")
file.write("number:" + number + "\n")
file.write("price:" + price + "\n")
file.write("color:" + rgb2hex(color[0], color[1], color[2]) + "\n") #16진수 꼴로 바꿈

file.close()
