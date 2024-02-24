from ultralytics import YOLO

# Define absolute paths for the configuration file and the model file
config_path = r"C:\DATASET\coco\config.yaml"

# Initialize the YOLO model with the absolute path to the model file
model = YOLO("yolov8n.yaml")

# Train the model using the absolute path to the configuration file
results = model.train(data=config_path, epochs=5)
