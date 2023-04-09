""" 두 LAS data의 coord를 표준화"""
import laspy
import numpy as np

def standardize_points(points):
    mean = np.mean(points, axis=0)
    std = np.std(points, axis=0)
    standardized_points = (points - mean) / std
    return standardized_points

def normalize_points(points):
    min_values = np.min(points, axis=0)
    max_values = np.max(points, axis=0)
    normalized_points = (points - min_values) / (max_values - min_values)
    return normalized_points

def find_common_points(points1, points2, tolerence=1e-5):
    common_points = []
    
    for point1 in points1:
        for point2 in points2:
            if np.allclose(point1, point2, atol=tolerence):
                common_points.append(point1)
                break
            
    return np.array(common_points)
    
# 두 LAS 파일 로드
las1 = laspy.read("/Users/taeyeong/job/data/las/배경00_version.las")
las2 = laspy.read("/Users/taeyeong/job/data/las/배경01_version.las")

# 포인트 배열로 변환
points1 = np.stack((las1.x, las1.y, las1.z), axis=-1)
points2 = np.stack((las2.x, las2.y, las2.z), axis=-1)

# 좌표 표준화
standardized_points1 = normalize_points(points1)
standardized_points2 = normalize_points(points2)

# 이후 코드는 표준화된 좌표를 사용하여 두 데이터를 비교하십시오.
common_points = find_common_points(standardized_points1, standardized_points2)

for point in common_points:
    print(point)
# 각 포인트 배열을 튜플 세트로 변환
# points1_set = set(tuple(point) for point in standardized_points1)
# points2_set = set(tuple(point) for point in standardized_points2)

# # 한 데이터에만 있는 좌표를 찾음
# unique_points2 = points2_set - points1_set
# print(len(unique_points2))