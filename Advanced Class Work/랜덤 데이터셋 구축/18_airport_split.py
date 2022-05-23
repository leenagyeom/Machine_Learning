import shutil
import os
import random

def main():
    image_root = r'E:\AISchool\DA\ImageAnalize\image_data\18_airport\cropped'
    save_root = r'E:\AISchool\DA\ImageAnalize\image_data\18_airport\datatset'
    image_paths = {}
    # {
    #   'label1' : [path1, path2, ...],
    #   'label2' : [path0, ...]
    # }
    for (path, dir, files) in os.walk(image_root):
        for file in files:
            image_path = os.path.join(path, file)
            label = os.path.basename(path)
            if label not in image_paths.keys():
                image_paths[label] = []
            image_paths[label].append(image_path)

    use_type = ['train', 'test']
    for label in image_paths.keys():
        for use in use_type:
            path = os.path.join(save_root, use, label)
            os.makedirs(path, exist_ok=True)

    for label in image_paths.keys():
        path_list = image_paths[label]
        random.shuffle(path_list)

        idx_train = int(len(path_list) * 0.9) # 90% 사용
        for path in path_list[:idx_train]:
            filename = os.path.basename(path)
            save_path = os.path.join(save_root, 'train', label, filename)
            shutil.copy(path, save_path) # 현재 위치, 옮길 저장할 파일 위치

        for path in path_list[idx_train:]:
            filename = os.path.basename(path)
            save_path = os.path.join(save_root, 'test', label, filename)
            shutil.copy(path, save_path)

if __name__ == '__main__':
    main()