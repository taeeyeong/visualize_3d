# visualize_3d
- LAS 데이터 처리, 분석 및 시각화 scripts

## Set up
'''c
pip install -r requirements.txt
'''
## Code
- data_loader.py: las 데이터의 (latitude, longitude, altitude)좌표를 지구 표준 형상 좌표계로 변환
- dbscan.py: dbscan 클러스터링 구현 코드 
- detect_object_from_las.py: 두 las데이터의 좌표를 뽑고, 두 데이터의 좌표 중 중복되지 않는 좌표만 출력 
- kmeans.py: kmeans 클러스터링 구현 알고리즘 
- main.py: 디스플레이 좌표에 해당하는 후면의 좌표를 받아와 디스플레이에 표시하여 시각화하는 코드 
- transform_coord.py: las 데이터의 좌표를 표준화 또는 정규화 시켜 변환하는 코드 