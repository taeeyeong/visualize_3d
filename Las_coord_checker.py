import open3d as o3d
import laspy
import numpy as np

# LAS 파일 읽기
las_file_path = "/Users/taeyeong/job/data/las/배경01_version.las"
las_data = laspy.read(las_file_path)

# X, Y, Z 좌표 추출
xyz_points = np.vstack((las_data.X, las_data.Y, las_data.Z)).T

# 포인트 클라우드 생성
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz_points)

# VoxelGrid 다운샘플링
voxel_size = 0.5  # 높은 값일수록 더 많이 다운샘플링
downsampled_pcd = pcd.voxel_down_sample(voxel_size)

# 시각화
o3d.visualization.draw_geometries([downsampled_pcd])

# if __name__ == '__main__':
#     las_input0 = "/Users/taeyeong/job/data/las/배경00_version.las"
#     las_input1 = "/Users/taeyeong/job/data/las/배경01_version.las"
    
#     las_data0 = laspy.read(las_input0)
#     las_data1 = laspy.read(las_input1)
    
#     points0 = np.vstack((las_data0.X, las_data0.Y, las_data0.Z)).T
#     points1 = np.vstack((las_data1.X, las_data1.Y, las_data1.Z)).T
    
#     print(points0)
#     # print(f'len of points 0 : {len(points0)}')
#     # print(f'len of points 1 : {len(points1)}')
    
#     # points0_set = set(tuple(point for point in points0))
#     # points1_set = set(tuple(point for point in points1))
    
#     uniq_points = points0 - points1
#     for point in uniq_points:
#         print(point)