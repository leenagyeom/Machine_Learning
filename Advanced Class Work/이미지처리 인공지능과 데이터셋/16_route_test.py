import os
from PIL import Image
import cv2

path = r'E:\AISchool\DA\ImageAnalize\image_data\16_pocketmon\pocketmon\image'
#print(os.listdir(path))
#print(os.path.abspath(path))

# for (path, dir, files) in os.walk(path):
#     # 파일이 여러개일 때는 os.walk가 좋다
#     for file in files:
#         print(path, dir, file)

filename = 'abra.png'

img_path = os.path.join(path, filename)
# img = Image.open(img_path)
img = cv2.imread(img_path)
img = cv2.resize(img, (500, 500))
cv2.imshow('test', img)
cv2.waitKey(0)

# img = img.resize((500, 500))
# img = img.crop((0, 0, 100, 50))