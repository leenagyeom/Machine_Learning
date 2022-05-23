import os
import json
import cv2

json_data = {}
mask_root = r'E:\AISchool\DA\ImageAnalize\image_data\16_steel_masking\steel_masking\mask'
for filename in os.listdir(mask_root):
    mask_path = os.path.join(mask_root, filename)
    mask = cv2.imread(mask_path)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY) # gray로 3차원을 1차원 이미지로 바꿔준다.

    # json annotation file
    # {
    #     filename : {
    #         'filename' : filename,
    #         'width' : 이미지 가로 길이,
    #         'height' : 이미지 세로 길이,
    #         'anno' : [
    #             {
    #             'label' : 라벨,
    #             'bbox' : [xmin, ymin, xmax, ymax]
    #             }
    #         ]
    #     }
    # }

    height, width = mask.shape

    annos = []
    coutours, h = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 복잡하지 않아서 SIMPLE 사용
    # print(len(contours))
    # print(contours)

    for coutour in coutours:
        xs, ys = [], []

        for coord in coutour:
            x, y = coord[0]
            xs.append(x)
            ys.append(y)

        xmin, xmax = min(xs), max(xs)
        ymin, ymax = min(ys), max(ys)

        anno = [int(xmin), int(ymin), int(xmax), int(ymax)]
        annos.append(anno)

    json_image = {
        'filename': filename,
        'width': width,
        'height': height,
        'anno': annos
    }
    json_data[filename] = json_image

# print(json_data)
# 저장

save_path = r'E:\AISchool\DA\ImageAnalize\image_data\annotation\annotation.json'
with open(save_path, 'w') as j:
    json.dump(json_data, j, indent='\t')