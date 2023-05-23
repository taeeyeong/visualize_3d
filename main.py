import open3d as o3d
import laspy
import numpy as np

# las 파일 읽기
las_file_path = 'path/to/배경01_cloud.las'
las_data = laspy.read(las_file_path)


# xyz 좌표 추출
xyz_points = np.vstack((las_data.X, las_data.Y, las_data.Z)).T

# 포인트 클라우드 생성
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz_points)

# 디스플레이 설정 (디스플레이 x,y 좌표 범위 및 z 좌표)
display_x_range = (20000000, 22537186)
display_y_range = (40000071, 46011203)
display_z = -239972192

# 디스플레이 뒷면의 점들 찾기
behind_display_indices = np.where((xyz_points[:, 0] > display_x_range[0]) & (xyz_points[:, 0] < display_x_range[1]) &
                                  (xyz_points[:, 1] > display_y_range[0]) & (xyz_points[:, 1] < display_y_range[1]) &
                                  (xyz_points[:, 2] < display_z))[0]

# 디스플레이 뒷면의 점들을 디스플레이에 표시
xyz_points[behind_display_indices, 2] = display_z

# 시각화
o3d.visualization.draw_geometries([pcd])
