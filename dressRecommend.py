import os, random
from os import listdir
from os.path import isfile, join
import pandas as pd
import dressMatching

class recommend_area1:
    # dress_path: 불러온 옷의 경로, closet_path: 옷장의 경로
    def __init__(self, dataset_path, type, simplecolor):
        self.type = type
        self.simplecolor = simplecolor
        self.dataSet_path = dataset_path

    def type_to_dirName(self, type):
        # 타입에 맞게 디렉토리 명 변경
        if (type == 'coat'):   dirName = 'Coat/'
        elif (type == 'dress'):    dirName = 'Dress/'
        elif (type == 'headwear'):    dirName = 'Headwear/'
        elif (type == 'jacket'):    dirName = 'Jacket/'
        elif (type == 'padded'):    dirName = 'Padded/'
        elif (type == 'pants long '):    dirName = 'Pants(Long)/'
        elif (type == 'pants shorts '):    dirName = 'Pants(Shorts)/'
        elif (type == 'shirt'):   dirName = 'Shirt/'
        elif (type == 'skirt'):    dirName = 'Skirt/'
        elif (type == 't shirt long '):    dirName = 'T-shirt(Long)/'
        elif (type == 't shirt short '):    dirName = 'T-shirt(Short)/'

        print(type)

        return dirName

    def recommand_cloth(self):
        #어울리는 색과 타입 리스트 받기
        colorList = dressMatching.color_matching[self.simplecolor]
        typeList = dressMatching.type_matching[self.type]

        recomList = []
        for cnt in range(0,2):
        #어울리는 타입 랜덤으로 선택
            type = random.choice(typeList)
            dirName = self.type_to_dirName(type)

            info = pd.read_csv(self.dataSet_path + dirName + 'dataSetInfo.csv',
                               names=["name", "type", "brand", "price", "hexcolor", "simplecolor"])
            #랜덤 추출
            df = info.sample(frac=0.3, replace=False)

            flag = False

            while not flag:
                for index, row in df.iterrows():
                    if(row['type'] == type) and (row['simplecolor'] in colorList): #만약 어울리는 옷이 있으면 True반환
                        recomList.append(self.dataSet_path + dirName + row['name'])
                        flag = True
                        break

        return recomList