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