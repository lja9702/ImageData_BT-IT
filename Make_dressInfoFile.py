import Get_and_Split_path
from colormap import rgb2hex
import rgb2colorname
import re
import csv
import os
import retrain_run_inference


def make_DressInfoFile(file_path, brand, price):
    get_all_path = Get_and_Split_path.GetAllPath()
    #파일 경로 넘겨주기
    get_all_path.set_Filepath(file_path)
    #확장자를 포함한 파일명
    filename = (get_all_path.path_split())[1]

    # 파일명에서 _기준으로 파일명 분리 앞은 옷의 번호, 뒤는 옷의 가격
    split_filename = get_all_path.get_noExt_filename().partition('_')

    #디렉토리명 추출
    split_dirpath = (get_all_path.path_split())[0].split('s/')
    #옷장 경로
    closet_path = get_all_path.CLOSET_PATH

    #폴더내 파일 가져오기
    #files = [f for f in listdir(closet_path) if isfile(join(closet_path, f))]
    #폴더내의 .csv이외의 파일 모두 가져오기
    #files = [x for x in files if x.find(".csv") == -1]

    #TODO:러닝된 옷의 가장 높은 확률 가져오기
    retrain = retrain_run_inference.retrain_run_inference(get_all_path)
    temp = retrain.run_inference_on_image()
    type = temp[2:-3]
    print("type:", type)

    #TODO:옷의 가격, 브랜드 입력한 값 가져오기

    #옷의 색깔 (hex), (nearest_color)
    color, nearestcolor = rgb2colorname.rgb2colorname(get_all_path)
    #color = rgb2colorname.rgb2colorname(get_all_path).color
    print("color:", color)
    print("hexcolor:", rgb2hex(color[0], color[1], color[2]))
    #옷의 색깔 (name)
    #nearestcolor = rgb2colorname.rgb2colorname(get_all_path)
    #r = re.compile("([a-zA-Z]+)([0-9]+)")   #색이 tan4일경우 tan만 추출하는 코드
    #items = r.match(nearestcolor)
    #simplecolor = items.group(1)
    print("simplecolor:" + nearestcolor)


    file = open(closet_path + "/closetInfo.csv", 'a', encoding='utf-8', newline='')
    wr = csv.writer(file)

    wr.writerow([filename, type, brand, price, rgb2hex(color[0], color[1], color[2]), nearestcolor])

    file.close()

make_DressInfoFile(file_path = '/home/lja97/MyCloset/383.jpg', brand = "Topten", price = 13400)