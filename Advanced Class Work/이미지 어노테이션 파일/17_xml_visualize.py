import os
import xml.etree.ElementTree as ET
import cv2

image_root = r'E:\AISchool\DA\ImageAnalize\image_data\17_automotive_engine\automotive_engine\image'
xml_root = r'E:\AISchool\DA\ImageAnalize\image_data\17_automotive_engine\automotive_engine\xml'

for filename in os.listdir(image_root):
    image_path = os.path.join(image_root, filename)
    image = cv2.imread(image_path)

    filename_xml = filename.split('.')[0] + '.xml'
    xml_path = os.path.join(xml_root, filename_xml)

    annotation = ET.parse(xml_path)

    # print(annotation.find('size').text)
    # exit()
    object_nodes = annotation.findall('object')
    for object_node in object_nodes:
        bnd_node = object_node.find('bnd_box')
        xmin = int(bnd_node.find('xmin'))
        xmax = int(bnd_node.find('xmax').text)
        ymin = int(bnd_node.find('ymin').text)
        ymax = int(bnd_node.find('ymax').text)
        
        image = cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 255, 0), 3) # 255, 255, 0 은 색상, 3은 선의 굵기

    cv2.imshow('visual', image)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        exit()