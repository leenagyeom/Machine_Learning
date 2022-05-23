import pandas as pd
import os
import shutil

image_root = r'E:\AISchool\DA\ImageAnalize\image_data\16_pocketmon\pocketmon\image'
csv_path = r'E:\AISchool\DA\ImageAnalize\image_data\16_pocketmon\pocketmon\pokemon.csv'

save_root = r'E:\AISchool\DA\ImageAnalize\image_data\16_pocketmon\pocketmon\sorted'
os.makedirs(save_root, exist_ok=True)

pokemon_df = pd.read_csv(csv_path)

# print(pokemon_df['Type1'].unique())

# 속성 18개의 폴더만들기

type_list = pokemon_df['Type1'].unique()

for t in type_list:
    dir_path = os.path.join(save_root, t)
    os.makedirs(dir_path, exist_ok=True)
    # print(t)
    # print(dir_path)

# 이미지 폴더 안에서 포켓몬 파일 / 이름 읽기
filenames = os.listdir(image_root)
# print(filenames)

i = 0
for filename in filenames:
    # 읽은 포켓몬 이름을 csv 파일이랑 매칭해서 type1 값 찾기
    # print(filename[:-4])
    name = filename.split('.')[0]

    type_ = pokemon_df[pokemon_df['Name'] == name]['Type1'].values[0]
    print(type_)
    # print(name, type_)
    # i += 1
    # if i > 5:
    #     exit()

    # 만들어 놓은 하위 폴더에 이미지 파일을 옮기기
    current_path = os.path.join(image_root, filename)
    # print(current_path)
    move_path = os.path.join(save_root, type_, filename)
    # print(move_path)

    shutil.move(current_path, move_path) # 현재 파일 위치, 옮길 파일 위치