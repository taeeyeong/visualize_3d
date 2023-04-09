import open3d as o3d
import numpy as np

# 포인트 클라우드 데이터 로드
input = '/Users/taeyeong/job/data/las/배경00_cloud.las'
pcd = o3d.io.read_point_cloud("input.las", format="las")

# 디스플레이 위치를 정의 (예: x, y, z 범위)
display_position = {
    "x_range": (0, 10),
    "y_range": (0, 10),
    "z_range": (0, 10),
}

# 디스플레이 위치에 해당하는 포인트를 필터링
points = np.asarray(pcd.points)
mask = (
    (points[:, 0] >= display_position["x_range"][0])
    & (points[:, 0] <= display_position["x_range"][1])
    & (points[:, 1] >= display_position["y_range"][0])
    & (points[:, 1] <= display_position["y_range"][1])
    & (points[:, 2] >= display_position["z_range"][0])
    & (points[:, 2] <= display_position["z_range"][1])
)
display_points = points[mask]

# 필터링된 포인트로 새로운 포인트 클라우드 생성
display_pcd = o3d.geometry.PointCloud()
display_pcd.points = o3d.utility.Vector3dVector(display_points)

# 포인트 클라우드 시각화
o3d.visualization.draw_geometries([display_pcd])
