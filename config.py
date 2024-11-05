# Configuration settings

import torch
# Paths
IMAGE_DIR = "data/cropdata/"  # Update this to the correct path
CSV_FILE_PATH = 'data/undersampled_images_data.csv'

# DataLoader settings
BATCH_SIZE = 32

# Model settings
# MODEL_NAME = 'resnet18'  # You can change to other models like 'resnet34', 'resnet50' if needed

# Training settings
NUM_EPOCHS = 10
LEARNING_RATE = 0.005

# Normalization parameters for pretrained models
NORMALIZE_MEAN = [0.485, 0.456, 0.406]
NORMALIZE_STD = [0.229, 0.224, 0.225]

DEVICE = 'cpu'
