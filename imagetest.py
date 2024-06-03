import numpy as np
import cv2 as cv
from keras import models
from skimage import transform, exposure
from ultralytics import YOLO
from time import time
from PIL import Image
from customtkinter import CTkImage

# IMAGE PREPROCESSING FUNCTION
def image_processing(image):
    image = transform.resize(image, (32, 32))  # Resizing images to 32x32 pixels.
    image = exposure.equalize_adapthist(image,
                                        clip_limit=0.1)  # Applying Histogram Equalization to standardize lighting.
    image = image.astype("float32") / 255.0  # Normalizing image values between 0 and 1.
    return image

def get_class_name(class_no):
    classes = ['Speed limit (20km/h)', 'Speed limit (30km/h)', 'Speed limit (50km/h)',
               'Speed limit (60km/h)', 'Speed limit (70km/h)', 'Speed limit (80km/h)',
               'End of speed limit (80km/h)', 'Speed limit (100km/h)', 'Speed limit (120km/h)',
               'No Overtaking', 'No Overtaking for Heavy Vehicles', 'Right-of-Way at next Intersection',
               'Priority Road', 'Yield', 'Stop', 'No Vehicles', 'Heavy Vehicles Prohibited', 'No Entry',
               'General Caution', 'Dangerous Left Curve', 'Dangerous Right Curve', 'Double Curve', 'Bumpy Road',
               'Slippery Road', 'Narrowing Road', 'Road Work', 'Traffic Signals', 'Pedestrian', 'Children',
               'Bike', 'Snow', 'Deer', 'End of Limits', 'Turn Right Ahead', 'Turn Left Ahead', 'Ahead Only',
               'Go Straight or Right', 'Go Straight or Left', 'Keep Right', 'Keep Left', 'Roundabout Mandatory',
               'End of No Overtaking', 'End of No Overtaking for Heavy Vehicles']
    return classes[class_no]

def predict_image(image, model):
    image = image_processing(image)
    image = image.reshape(1, 32, 32, 3)
    prediction = model.predict(image, verbose=0)
    return prediction

def start_image_inference(image_path, yolo_model_path, cnn_model_path):
    brightness = 180
    threshold = 0.5  # PROBABILITY THRESHOLD
    font = cv.FONT_HERSHEY_SIMPLEX
    offset = 40  # Vertical offset for messages

    # IMPORT THE TRAINED MODELS
    print("\nLoading models from disk...")
    t1 = time()
    yolo_model = YOLO(yolo_model_path)
    print(f"Loaded YOLO model. Took {time() - t1} seconds.")
    t1 = time()
    model = models.load_model(cnn_model_path)
    print(f"Loaded CNN model. Took {time() - t1} seconds.")

    print("\nBeginning inference...")

    # READING IMAGE
    img_original = cv.imread(image_path)
    if img_original is None:
        print("Image not found.")
        return
    img_original = cv.resize(img_original, (640, 480))
    img = np.asarray(img_original)

    # DETECTING SIGN AND EXTRACTING ROI
    results = yolo_model.predict(source=img, verbose=True)
    img_plotted = results[0].plot()
    detected_classes = []
    # noinspection PyBroadException
    try:
        boxes = results[0].boxes
        for box in boxes:
            x1 = int(box.xyxy[0][0])
            y1 = int(box.xyxy[0][1])
            x2 = int(box.xyxy[0][2])
            y2 = int(box.xyxy[0][3])
            roi = img[y1:y2, x1:x2]

            # PREDICTING TRAFFIC SIGN CLASS FROM ROI
            predictions = predict_image(roi, model)
            class_index = np.argmax(predictions)
            probability_value = np.amax(predictions)

            # ADD TO DETECTED CLASSES IF ABOVE THRESHOLD
            if probability_value > threshold:
                detected_classes.append((class_index, probability_value, (x1, y1, x2, y2)))
                print(f"Detected Traffic Sign.\tClass: {class_index}\t"
                      f"Probability: {round(probability_value * 100, 2):02.2f}%\t\t"
                      f"Name: {get_class_name(class_index)}")
    except Exception as e:
        print(f"Error processing image: {e}")

    # DRAW RESULTS ON IMAGE
    for i, (class_index, probability_value, (x1, y1, x2, y2)) in enumerate(detected_classes):
        cv.putText(img_plotted, "CLASS: " + str(class_index) + " " + str(get_class_name(class_index)), (8, 24 + i*offset),
                   font, 0.50, (0, 0, 255), 1, cv.LINE_AA)
        cv.putText(img_plotted, "PROBABILITY: " + str(round(probability_value * 100, 2)) + "%", (8, 48 + i*offset),
                   font, 0.50, (0, 0, 255), 1, cv.LINE_AA)

    cv.imshow("Inference", img_plotted)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Example usage
image_path = "C:/Users/KIRA/traffic/traffic/test6.png"
yolo_model_path = "./runs/detect/train/weights/best.pt"
cnn_model_path = './Models/traffic_sign_classifier_v5.0_e10_b32.h5'
start_image_inference(image_path, yolo_model_path, cnn_model_path)
# Enhancement update for 2024-01-11 12:00:00

# Enhancement update for 2024-05-01 12:00:00

# Enhancement update for 2024-09-08 12:00:00

# Enhancement update for 2024-07-16 12:00:00

# Enhancement update for 2024-10-04 12:00:00

# Enhancement update for 2024-03-28 12:00:00

# Enhancement update for 2024-09-07 12:00:00

# Enhancement update for 2024-12-24 12:00:00

# Enhancement update for 2024-10-13 12:00:00

# Enhancement update at 2024-01-04 12:58:31

# Enhancement update at 2024-01-04 16:34:21

# Enhancement update at 2024-01-06 16:14:45

# Enhancement update at 2024-01-11 13:47:03

# Enhancement update at 2024-01-14 17:50:08

# Enhancement update at 2024-03-04 12:12:49

# Enhancement update at 2024-03-13 17:28:54

# Enhancement update at 2024-03-24 22:12:20

# Enhancement update at 2024-03-26 13:07:51

# Enhancement update at 2024-04-05 14:59:17

# Enhancement update at 2024-04-05 18:33:27

# Enhancement update at 2024-04-14 16:36:18

# Enhancement update at 2024-04-27 21:23:56

# Enhancement update at 2024-06-03 13:55:04
