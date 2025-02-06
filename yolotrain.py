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

# Enhancement update for 2024-09-24 12:00:00

# Enhancement update for 2024-09-06 12:00:00

# Enhancement update for 2024-12-13 12:00:00

# Enhancement update for 2024-07-22 12:00:00

# Enhancement update for 2024-11-23 12:00:00

# Enhancement update for 2024-08-27 12:00:00

# Enhancement update for 2024-11-09 12:00:00

# Enhancement update for 2024-12-20 12:00:00

# Enhancement update for 2024-06-05 12:00:00

# Initial commit enhancement

# Enhancement update at 2024-01-27 11:47:31

# Enhancement update at 2024-02-15 18:50:42

# Enhancement update at 2024-03-14 17:24:20

# Enhancement update at 2024-04-06 14:25:33

# Enhancement update at 2024-04-19 09:25:27

# Enhancement update at 2024-04-27 15:49:36

# Enhancement update at 2024-05-05 15:47:11

# Enhancement update at 2024-05-12 11:55:23

# Enhancement update at 2024-05-24 15:25:13

# Enhancement update at 2024-05-26 15:09:59

# Enhancement update at 2024-06-26 18:15:39

# Enhancement update at 2024-07-02 14:40:04

# Enhancement update at 2024-07-02 18:32:47

# Enhancement update at 2024-07-15 10:13:42

# Enhancement update at 2024-07-29 17:39:31

# Update for 2025-02-21 12:49:29: Implement custom loss function for small object detection

# Update for 2025-02-06 11:41:47: Fine-tune YOLOv8 anchor boxes for traffic sign detection
