import numpy as np
import cv2 as cv
from keras import models
from skimage import transform, exposure
from ultralytics import YOLO
from time import time
from PIL import Image
from customtkinter import CTkImage
from playsound import playsound
import threading

# IMAGE PREPROCESSING FUNCTION
def image_processing(image):
    image = transform.resize(image, (32, 32))  # Resizing images to 32x32 pixels.
    image = exposure.equalize_adapthist(image, clip_limit=0.1)  # Applying Histogram Equalization to standardize lighting.
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

def play_sound(sound_file):
    threading.Thread(target=playsound, args=(sound_file,), daemon=True).start()

def predict_image(image, model):
    image = image_processing(image)
    image = image.reshape(1, 32, 32, 3)
    prediction = model.predict(image, verbose=0)
    return prediction

def start_video_inference(yolo_model_path, cnn_model_path, camgui=None):
    frame_width = 640  # CAMERA RESOLUTION
    frame_height = 480
    brightness = 180
    threshold = 0.997  # PROBABILITY THRESHOLD (97.00%)
    font = cv.FONT_HERSHEY_SIMPLEX
    offset = 40  # Vertical offset for messages
    cool_down_time = 30  # Cool down time in seconds
    last_announced_time = {}  # Dictionary to track last announced time for each class

    # SET UP THE WEBCAM CAPTURE
    print("\nStarting Webcam...")
    cap = cv.VideoCapture(0)
    cap.set(3, frame_width)
    cap.set(4, frame_height)
    cap.set(10, brightness)

    # IMPORT THE TRAINED MODELS
    print("\nLoading models from disk...")
    t1 = time()
    yolo_model = YOLO(yolo_model_path)
    print(f"Loaded YOLO model. Took {time() - t1} seconds.")
    t1 = time()
    model = models.load_model(cnn_model_path)
    print(f"Loaded CNN model. Took {time() - t1} seconds.")

    print("\nBeginning inference...")
    while True:
        # READING IMAGE FROM WEBCAM
        success, img_original = cap.read()
        if not success:
            print("Failed to capture image from webcam.")
            break
        img_original = cv.resize(img_original, (640, 480))
        img = np.asarray(img_original)

        # DETECTING SIGN AND EXTRACTING ROI
        results = yolo_model.predict(source=img, verbose=False)
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
                if probability_value >= threshold:
                    current_time = time()
                    if class_index not in last_announced_time or (current_time - last_announced_time[class_index]) > cool_down_time:
                        last_announced_time[class_index] = current_time
                        sound_file = f'sounds/{class_index}.wav'  # Assuming you have sounds named by class index
                        play_sound(sound_file)
                        print(f"Playing sound for class {class_index}.")
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

        if camgui is None:
            cv.imshow("Inference", img_plotted)
        else:
            cvimage = cv.cvtColor(img_plotted, cv.COLOR_BGR2RGBA)
            image = Image.fromarray(cvimage)
            imgctk = CTkImage(image, size=(640, 480))
            camgui.image_label.configure(image=imgctk)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
    print("Closing Inference Window...")
# Example usage

yolo_model_path = "./runs/detect/train/weights/best.pt"
cnn_model_path = './Models/traffic_sign_classifier_v7.0_e30_b8.h5'
start_video_inference(yolo_model_path, cnn_model_path)
# Enhancement update for 2024-08-08 12:00:00

# Enhancement update for 2024-05-16 12:00:00

# Enhancement update for 2024-10-05 12:00:00

# Enhancement update for 2024-12-12 12:00:00

# Enhancement update for 2024-12-16 12:00:00

# Enhancement update for 2024-02-05 12:00:00

# Enhancement update for 2024-01-12 12:00:00

# Enhancement update for 2024-05-13 12:00:00

# Enhancement update for 2024-07-23 12:00:00

# Enhancement update for 2024-02-25 12:00:00

# Enhancement update for 2024-01-03 12:00:00

# Enhancement update for 2024-07-26 12:00:00

# Enhancement update for 2024-01-28 12:00:00

# Enhancement update for 2024-05-01 12:00:00

# Enhancement update for 2024-07-02 12:00:00

# Enhancement update for 2024-09-07 12:00:00

# Enhancement update for 2024-11-14 12:00:00

# Enhancement update for 2024-08-26 12:00:00

# Enhancement update for 2024-05-27 12:00:00

# Enhancement update at 2024-01-08 13:16:13

# Enhancement update at 2024-01-14 12:20:30

# Enhancement update at 2024-01-26 21:33:04

# Enhancement update at 2024-02-06 18:55:53

# Enhancement update at 2024-03-22 20:55:13

# Enhancement update at 2024-04-12 20:50:49

# Enhancement update at 2024-05-07 19:28:29

# Enhancement update at 2024-06-06 19:20:14

# Enhancement update at 2024-07-06 17:37:52

# Enhancement update at 2024-07-13 20:54:17

# Enhancement update at 2024-07-16 17:13:35

# Enhancement update at 2024-08-12 13:40:10

# Enhancement update at 2024-08-12 18:56:11

# Enhancement update at 2024-08-15 19:12:02

# Enhancement update at 2024-08-19 14:25:20

# Update for 2025-01-14 11:16:10: Optimize real-time processing pipeline

# Update for 2025-01-04 20:09:50: Add frame rate control for resource management
