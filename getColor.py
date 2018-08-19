import numpy as np
import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


image = cv2.imread("/home/lja97/5_329000.jpg")
print(image.shape)

# 채널을 BGR -> RGB로 변경
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image = image.reshape((image.shape[0] * image.shape[1], 3)) # height, width 통합
print(image.shape)

k = 5 # KMeans clustering 실행
clt = KMeans(n_clusters = k)
clt.fit(image)
#클러스터링 된 컬러값들
for center in clt.cluster_centers_:
    print(center)

def centroid_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist

hist = centroid_histogram(clt)
print(hist)

def plot_colors(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0
    for (percent, color) in zip(hist, centroids):
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
        startX = endX
    return bar

bar = plot_colors(hist, clt.cluster_centers_)
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()
