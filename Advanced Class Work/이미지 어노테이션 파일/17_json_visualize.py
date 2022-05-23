import os
import json # json 라이브러리 사용
import cv2
import numpy as np

image_root = r'E:\AISchool\DA\ImageAnalize\image_data\17_automotive_engine\automotive_engine\image'
json_root = r'E:\AISchool\DA\ImageAnalize\image_data\17_automotive_engine\automotive_engine\json'

for filename in os.listdir(image_root):
    image_path = os.path.join(image_root, filename)
    image = cv2.imread(image_path)

    filename_json = filename.split('.')[0] + '.json'
    json_path = os.path.join(json_root, filename_json)

    with open(json_path, 'r') as j :
        json_data = json.load(j)

    annos = json_data['shapes']

    for anno in annos:
        points = anno['points']
        points = np.array(points, np.int) # 좌표가 소수점이라 cv2에서 사용할 수 없으므로 int로 바꾼다.
        cv2.polylines(image, [points], True, (255, 255, 0), 3) # 닫힌 그림을 그리고 싶으면 True, 열린 그림은 False

    cv2.imshow('visual', image)

    if cv2.waitKey(0) & 0xff == ord('q'):
        cv2.destroyAllWindows()
        exit()