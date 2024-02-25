import cv2
from ultralytics import YOLO
import numpy as np
import pandas as pd
from collections import Counter

model = YOLO("yolov8s.pt")
coco_txt_path = "D:\developer\SmartsyncTraffic\SmartSync-Traffic\classes.txt"
with open(coco_txt_path, "r") as my_file:
    data = my_file.read()
    class_list = data.split("\n")
def detect_objects(img):
    results = model.predict(img)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
    object_classes = []

    for index, row in px.iterrows():
        d = int(row[5])
        if 0 <= d < len(class_list):
            obj_class = class_list[d]
            object_classes.append(obj_class)
    return object_classes

def count_objects_in_video_frame(video_path):
    global total,density
    cap = cv2.VideoCapture(video_path)
    success, frame = cap.read()
    if success:
        object_classes = detect_objects(frame)
        counter = Counter(object_classes)
        print("Total Object Count:")
        total=0
        for obj, count in counter.items():
            print(f"{obj}: {count}")
            if(f"{obj}"!="person"):
                total+=count
        print("total vehicles : ",total)
        density=total/40
        return density,total
    else:
        print("Error: Failed to read the first frame from the video.")
    cap.release()

