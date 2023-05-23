import laspy
import numpy as np
from sklearn.cluster import DBSCAN

# LAS 파일 로드
las = laspy.read("/Users/taeyeong/job/data/las/배경01_cloud.las")

# 포인트 배열로 변환
points = np.stack((las.x, las.y, las.z), axis=-1)

# DBSCAN 클러스터링 알고리즘 설정 및 실행
eps = 5  # 클러스터링 시 사용할 입실론 값 설정 (이웃 포인트를 결정하는 데 사용되는 거리)
min_samples = 5  # 클러스터를 형성하기 위한 최소 포인트 개수

dbscan = DBSCAN(eps=eps, min_samples=min_samples)
labels = dbscan.fit_predict(points)
# print(labels)

# 클러스터별로 포인트를 분리
clusters = {}
for idx, label in enumerate(labels):
    if label == -1:
        continue

    if label not in clusters:
        clusters[label] = []

    clusters[label].append(points[idx])

# 결과 출력
for label, cluster_points in clusters.items():
    print(f"Cluster {label}:")
    for point in cluster_points:
        print(point)
    print("\n")
print(clusters.keys())