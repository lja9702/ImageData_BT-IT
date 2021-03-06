import numpy as np
import cv2
from os import listdir
from os.path import isfile, join
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

class colorRGB_and_per_matching:
    def __init__(self):
        self.RGBvalue = []
        self.percent = 0.0
    def set_RGBfvalue(self, RGBvalue):
        self.RGBvalue = RGBvalue
    def set_percent(self, percent):
        self.percent = percent

def centroid_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist

def get_Color(get_all_path):
    #가져올 파일의 디렉토리와 파일 명 풀네임 받기
#    dir_path = (get_all_path.path_split())[0]
    file_path = get_all_path.FILE_PATH

    image = cv2.imread(file_path)
    print(image.shape)

    # 채널을 BGR -> RGB로 변경
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = image.reshape((image.shape[0] * image.shape[1], 3)) # height, width 통합
    print(image.shape)

    k = 5 # KMeans clustering 실행
    clt = KMeans(n_clusters = k)
    clt.fit(image)


    matchingList = []
    #클러스터링 된 컬러값들
    #컬러값들과 그 컬러값이 차지하는 퍼센트 묶어서 리스트에 저장
    #먼저 클러스터링 된 컬러값들 저장
    for center in clt.cluster_centers_:
        centerColor = colorRGB_and_per_matching()
        centerColor.set_RGBfvalue(center)
        matchingList.append(centerColor)


    hist = centroid_histogram(clt)
    #클러스터링 된 컬러값들이 차지하는 퍼센테이지 저장
    for idx in range(0, len(hist)):
        matchingList[idx].set_percent(hist[idx])

    #매칭한 칼러와 퍼센트 리스트셋 정렬
    sortingList = sorted(matchingList, key = lambda c: c.percent, reverse = True)

    #두번째로 높은 컬러 추출 (첫번쨰 컬러는 배경색이라고 가정)
    mostColor = sortingList[1]
    mostColor.RGBvalue = [int (i) for i in mostColor.RGBvalue]

    print(mostColor.RGBvalue)
    return mostColor
    #def plot_colors(hist, centroids):
    #    bar = np.zeros((50, 300, 3), dtype="uint8")
    #    startX = 0
    #    for (percent, color) in zip(hist, centroids):
    #        endX = startX + (percent * 300)
    #        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
    #        startX = endX
    #    return bar

    #bar = plot_colors(hist, clt.cluster_centers_)
    #plt.figure()
    #plt.axis("off")
    #plt.imshow(bar)
    #plt.show()
