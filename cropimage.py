import os
from PIL import Image

# 원본 이미지가 있는 경로와 새로 만들 크롭 이미지 저장 경로
original_base_path = "data/newimage"
crop_base_path = "data/newimage_cropped"

# 새로운 폴더 생성
os.makedirs(crop_base_path, exist_ok=True)

# 모든 하위 폴더 탐색 및 크롭 후 저장
for folder_name in os.listdir(original_base_path):
    folder_path = os.path.join(original_base_path, folder_name)
    crop_folder_path = os.path.join(crop_base_path, folder_name)

    # 폴더인 경우 이미지 파일 열기
    if os.path.isdir(folder_path):
        os.makedirs(crop_folder_path, exist_ok=True)  # 크롭 이미지를 저장할 폴더 생성
        
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            # jpg 파일만 처리
            if file_path.endswith(".jpg"):
                try:
                    # 이미지 열기
                    image = Image.open(file_path)
                    
                    # 좌측 상단에서 600*600 크기로 크롭
                    cropped_image = image.crop((0, 0, 600, 600))
                    
                    # 크롭한 이미지를 새 경로에 저장
                    cropped_file_path = os.path.join(crop_folder_path, file_name)
                    cropped_image.save(cropped_file_path, "JPEG")
                    print(f"Cropped and saved: {cropped_file_path}")
                    
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
