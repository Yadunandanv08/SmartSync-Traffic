import cv2
from ultralytics import YOLO
import cvzone
import numpy as np
import pandas as pd
from collections import Counter
import glob

model = YOLO("yolov8n.pt")
video_path = r"C:\Users\fahad\Downloads\TRAFFIC TESTCASE 3.mp4"

nth_second = 1

cap = cv2.VideoCapture(video_path)
frame_rate = cap.get(cv2.CAP_PROP_FPS)
nth_frame = int(frame_rate * nth_second)

cap.set(cv2.CAP_PROP_POS_FRAMES, nth_frame)
ret, frame = cap.read()

if ret:
    cv2.imwrite(r"C:\DATASET\coco\frame\frame.png", frame)

cap.release()

my_file = open("classes.txt", "r")
class_list = my_file.read().split("\n")

def object(img):
    results = model.predict(img)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
    object_classes = []

    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])

        # Ensure the index is within the range of class_list
        if 0 <= d < len(class_list):
            obj_class = class_list[d]
            object_classes.append(obj_class)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
            cvzone.putTextRect(img, f'{obj_class}', (x2, y2), 1, 1)

    return object_classes

def count_objects_in_image(object_classes):
    counter = Counter(object_classes)
    print("Object Count in Image:")
    for obj, count in counter.items():
        print(f"{obj}: {count}")

path = r'C:\DATASET\coco\frame\frame.png'

for file in glob.glob(path):
    img = cv2.imread(file)
    img = cv2.resize(img, (1020, 500))
    object_classes = object(img)
    count_objects_in_image(object_classes)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
