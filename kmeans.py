import laspy
import numpy as np
from sklearn.cluster import KMeans
import open3d as o3d

def is_floor_cluster(cluster_points, z_threshold=0.1):
    """
    클러스터가 바닥을 나타내는지 확인
    """
    z_values = cluster_points[:, 2]
    z_range = np.max(z_values) - np.min(z_values)
    return z_range < z_threshold

# LAS 파일 로드
las = laspy.read("path/to/배경01_cloud.las")

# 포인트 배열로 변환
points = np.stack((las.x, las.y, las.z), axis=-1)

# 객체 개수를 미리 알고 있을 때
num_objects = 4  # 객체의 총 개수

# K-means 클러스터링 알고리즘 실행
kmeans = KMeans(n_clusters=num_objects)
labels = kmeans.fit_predict(points)

# 클러스터별로 포인트를 분리
clusters = {}
for idx, label in enumerate(labels):
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

# 클러스터별로 포인트를 시각화
pcd_list = []
for label, cluster_points in clusters.items():
    cluster_points = np.array(cluster_points)

    # 바닥 클러스터 제외
    if is_floor_cluster(cluster_points):
        continue

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(cluster_points)
    pcd.paint_uniform_color([np.random.rand(), np.random.rand(), np.random.rand()])
    pcd_list.append(pcd)

# 시각화 결과 출력
o3d.visualization.draw_geometries(pcd_list)