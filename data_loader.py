import numpy as np
import math

def geodetic2ecef(lat, lon, alt):
    """_summary_
        구면좌표(lat, lon, alt)를 xyz 좌표(x, y, z)로 변환
    
    Notes:
        지구 위의 지오디트릭 좌표 (latitude, longitude, altitude)를 지구 표준 형상 좌표계 (ECEF: Earth-Centered, Earth-Fixed)로 변환하는 기능을 가진 함수
        
    Args:
        lat (_type_): _description_
        lon (_type_): _description_
        alt (_type_): _description_

    Returns:
        _type_: _description_
    """
    a = 6378137.0
    e = 8.1819190842622e-2
    N = a / math.sqrt(1 - e**2 * math.sin(lat)**2)
    x = (N + alt) * math.cos(lat) * math.cos(lon)
    y = (N + alt) * math.cos(lat) * math.sin(lon)
    z = (N * (1 - e**2) + alt) * math.sin(lat)
    return x, y, z

def lidar_data_to_xyz(lidar_data):
    """_summary_
        LiDAR 데이터를 xyz 좌표계로 변환하는 함수
        intensity 데이터도 변환된 xyz 좌표와 같이 저장

    Args:
        lidar_data (_type_): _description_

    Returns:
        _type_: _description_
    """
    xyz_data = []
    for i in range(len(lidar_data)):
        lat, lon, alt = lidar_data[i][:3]
        intensity = lidar_data[i][3]
        x, y, z = geodetic2ecef(lat, lon, alt)
        xyz_data.append([x, y, z, intensity])
    return xyz_data

if __name__ == '__main__':
    geo_array = np.array([[125058.2, 423021.5, 345.6, 42]])
    print(lidar_data_to_xyz(geo_array))  
    