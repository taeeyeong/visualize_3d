import open3d as o3d
import numpy as np
import laspy

# 두 LAS 파일 로드
las1 = laspy.read("/Users/taeyeong/job/data/las/배경00_cloud.las")
las2 = laspy.read("/Users/taeyeong/job/data/las/배경01_cloud.las")

# 포인트 배열로 변환
points1 = np.stack((las1.x, las1.y, las1.z), axis=-1)
points2 = np.stack((las2.x, las2.y, las2.z), axis=-1)

# 각 포인트 배열을 튜플 세트로 변환
points1_set = set(tuple(point) for point in points1)
points2_set = set(tuple(point) for point in points2)

# 한 데이터에만 있는 좌표를 찾음
unique_points2 = points2_set - points1_set

# 결과 출력


print("\nPoints in input2.las not in input1.las:")
print(len(unique_points2))
