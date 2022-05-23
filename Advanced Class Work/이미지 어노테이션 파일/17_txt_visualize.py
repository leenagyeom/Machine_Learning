import os
import cv2

image_root = r'E:\AISchool\DA\ImageAnalize\image_data\17_automotive_engine\automotive_engine\image'
txt_root = r'E:\AISchool\DA\ImageAnalize\image_data\17_automotive_engine\automotive_engine\txt'

for filename in os.listdir(image_root):
    image_path = os.path.join(image_root, filename)
    image = cv2.imread(image_path)
    height, width, channel = image.shape
    # print(height, width, channel)

    filename_txt = filename.split('.')[0] + '.txt'
    txt_path = os.path.join(txt_root, filename_txt)

    # print(image_path)
    # print(txt_path)
    # exit()

    with open(txt_path, 'r') as f:
        while True:
            line = f.readline()[:-2] # -2는 \n(개행) 때문에 해준다
            if not line:
                break
            line = line.split(' ')
            x_center, y_center, w, h = line[1:]
            x_center = float(x_center)
            y_center = float(y_center)
            w = float(w)
            h = float(h)

            # 역으로 YOLO 숫자 돌려주기

            x_center = x_center * width
            y_center = y_center * height
            w = w * width
            h = h * height

            xmin = int(x_center - w/2)
            ymin = int(y_center - h/2)
            xmax = int(x_center + w/2)
            ymax = int(y_center + h/2)

            image = cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 255, 0), 3)

    cv2.imshow('visualize', image)
    if cv2.waitKey(0) & 0xff == ord('q'):
        cv2.destroyAllWindows()
        exit()