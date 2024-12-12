import os
from PIL import Image

# Paths for the original images and the folder to save cropped images
original_base_path = "data/newimage"
crop_base_path = "data/newimage_cropped"

# Create a new folder for cropped images
os.makedirs(crop_base_path, exist_ok=True)

# Traverse all subfolders, crop images, and save them
for folder_name in os.listdir(original_base_path):
    folder_path = os.path.join(original_base_path, folder_name)
    crop_folder_path = os.path.join(crop_base_path, folder_name)

    # If it's a folder, open image files
    if os.path.isdir(folder_path):
        os.makedirs(crop_folder_path, exist_ok=True)  # Create a folder to save cropped images
        
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            # Process only jpg files
            if file_path.endswith(".jpg"):
                try:
                    # Open the image
                    image = Image.open(file_path)
                    
                    # Crop the image to 600x600 from the top-left corner
                    cropped_image = image.crop((0, 0, 600, 600))
                    
                    # Save the cropped image to the new path
                    cropped_file_path = os.path.join(crop_folder_path, file_name)
                    cropped_image.save(cropped_file_path, "JPEG")
                    print(f"Cropped and saved: {cropped_file_path}")
                    
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

