from ultralytics import YOLO
import torch
import os
import multiprocessing
# Correct CUDA_VISIBLE_DEVICES usage:

os.environ["CUDA_VISIBLE_DEVICES"] = "1"  # Use GPU for training

def main():
    # Load the model
    model = YOLO("yolov8n.pt")  # Pre-trained model

    # Train the model with valid batch size:
    model.train(data="data.yaml", epochs=100,batch=32 )  #

if __name__ == '__main__':
    multiprocessing.freeze_support()  # For Windows
    main()


pip install ultralytics
# Enhancement update for 2024-07-03 12:00:00

# Enhancement update for 2024-03-06 12:00:00

# Enhancement update for 2024-12-12 12:00:00

# Enhancement update for 2024-01-03 12:00:00

# Enhancement update for 2024-09-15 12:00:00

# Enhancement update for 2024-12-25 12:00:00

# Enhancement update for 2024-02-23 12:00:00

# Enhancement update for 2024-07-25 12:00:00
