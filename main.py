from loading import load_dataset
from visualizing import visualize, show_accuracy_loss_graphs
from training import train
from testing import start_webcam_inference

# PARAMETERS
classes_csv_path = './Datasets/GTSRB/Classes.csv'
sample_images_path = './Datasets/GTSRB/Samples'

train_images_path = './Datasets/GTSRB/Train'
train_csv_path = './Datasets/GTSRB/Train.csv'
validation_images_path = './Datasets/GTSRB/Test'
validation_csv_path = './Datasets/GTSRB/Test.csv'

ver = "103.0"
epochs = 10
batch_size = 32
image_dimensions = (32, 32, 3)

model_name = f'traffic_sign_classifier_v{ver}_e{epochs}_b{batch_size}.model'

# BOOLEAN PARAMETERS
condition_load = True
condition_preload = True
condition_visualize = False
condition_train = True
condition_inference = False
condition_prerecorded = False


if __name__ == "__main__":
    # LOADING DATASET
    if condition_load:
        X_train, Y_train, X_validation, Y_validation = load_dataset(train_images_path,
                                                                    validation_images_path,
                                                                    validation_csv_path,
                                                                    image_dimensions,
                                                                    preloaded=condition_preload)

    # VISUALIZING DATASET
    if condition_visualize:
        visualize(classes_csv_path, sample_images_path, train_csv_path, validation_csv_path, image_dimensions)

    # TRAINING THE MODEL
    if condition_train:
        # noinspection PyUnboundLocalVariable
        history = train(dimensions=image_dimensions,
                        X_train=X_train, Y_train=Y_train,
                        X_validation=X_validation, Y_validation=Y_validation,
                        epochs=epochs, batch_size=batch_size,
                        model_name=model_name)

        # SHOWING GRAPHS
        show_accuracy_loss_graphs(history, model_name)

    # INFERENCE
    if condition_inference:
        start_webcam_inference(model_name, condition_prerecorded)
# Initial commit enhancement

# Enhancement update for 2024-12-14 12:00:00

# Enhancement update for 2024-03-04 12:00:00

# Enhancement update for 2024-08-09 12:00:00

# Enhancement update for 2024-09-20 12:00:00

# Enhancement update for 2024-11-28 12:00:00

# Enhancement update for 2024-02-10 12:00:00

# Enhancement update for 2024-01-28 12:00:00

# Enhancement update for 2024-07-05 12:00:00

# Enhancement update for 2024-08-12 12:00:00

# Enhancement update for 2024-06-21 12:00:00

# Enhancement update for 2024-11-27 12:00:00

# Enhancement update for 2024-12-15 12:00:00

# Enhancement update for 2024-03-08 12:00:00

# Enhancement update for 2024-08-13 12:00:00

# Enhancement update for 2024-08-21 12:00:00

# Enhancement update for 2024-01-03 12:00:00

# Enhancement update for 2024-04-03 12:00:00

# Enhancement update at 2024-02-18 14:37:02

# Enhancement update at 2024-02-21 19:37:35

# Enhancement update at 2024-03-25 16:10:30

# Enhancement update at 2024-04-19 16:04:28

# Enhancement update at 2024-06-02 21:00:07

# Enhancement update at 2024-06-10 14:38:13

# Enhancement update at 2024-06-11 13:39:54

# Enhancement update at 2024-06-13 15:19:44

# Enhancement update at 2024-07-02 13:30:25

# Enhancement update at 2024-07-21 15:46:11
