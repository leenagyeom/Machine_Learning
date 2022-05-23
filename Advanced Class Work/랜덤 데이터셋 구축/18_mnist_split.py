import shutil
import os
import random
from tqdm import tqdm

def main():
    image_root = r'E:\AISchool\DA\ImageAnalize\image_data\18_mnist\label'
    save_root = r'E:\AISchool\DA\ImageAnalize\image_data\18_mnist\dataset'

    # airport split 코드와 동일

    image_paths = {}
    for (path, dir, files) in os.walk(image_root):
        for file in files:
            image_path = os.path.join(path, file)
            label = os.path.basename(path)
            if label not in image_paths.keys():
                image_paths[label] = []
            image_paths[label].append(image_path)

    use_type = ['train','valid', 'test']
    for label in image_paths.keys():
        for use in use_type:
            path = os.path.join(save_root, use, label)
            os.makedirs(path, exist_ok=True)

    for label in image_paths.keys():
        path_list = image_paths[label]
        random.shuffle(path_list)

        idx_train = int(len(path_list) * 0.8)
        idx_valid = int(len(path_list) * 0.9)

        for path in tqdm(path_list[:idx_train], desc=f'{label}-train: '): # 1600장
            filename = os.path.basename(path)
            save_path = os.path.join(save_root, 'train', label, filename)
            shutil.copy(path, save_path) # 현재 위치, 옮길 저장할 파일 위치

        for path in tqdm(path_list[idx_train:idx_valid], desc=f'{label}-valid: '): # 200장
            filename = os.path.basename(path)
            save_path = os.path.join(save_root, 'valid', label, filename)
            shutil.copy(path, save_path)

        for path in tqdm(path_list[idx_valid:], desc=f'{label}-test: '): # 200장
            filename = os.path.basename(path)
            save_path = os.path.join(save_root, 'test', label, filename)
            shutil.copy(path, save_path)

if __name__ == '__main__':
    main()