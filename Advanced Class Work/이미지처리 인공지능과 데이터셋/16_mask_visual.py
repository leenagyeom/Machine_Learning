import os
import cv2
import shutil

image_root = r'E:\AISchool\DA\ImageAnalize\image_data\16_steel_masking\steel_masking\image'
mask_root = r'E:\AISchool\DA\ImageAnalize\image_data\16_steel_masking\steel_masking\mask'
# print(os.listdir(image_root))

for filename in os.listdir(image_root):
    # 파일명이 매칭되는 이미지 / 마스킹 가져오기
    image_path = os.path.join(image_root, filename)
    mask_path = os.path.join(mask_root, filename)
    # print(image_path)
    # print(mask_path)

    img = cv2.imread(image_path)
    mask = cv2.imread(mask_path)

    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    # print(img.shape, mask.shape)
    image_masked = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('test', image_masked)
    cv2.waitKey(0)
    exit()

    cv2.imshow('image', img)
    cv2.imshow('mask', mask)

    if cv2.waitKey(0) & 0xff == ord('q'):
        cv2.destroyAllWindows()
        exit()