
# SmartSync-Traffic

SmartSync-Traffic is an intelligent traffic management system designed to optimize traffic flow and reduce congestion in urban areas. Utilizing advanced machine learning algorithms and real-time data, SmartSync-Traffic dynamically adjusts traffic signals to ensure smooth and efficient traffic movement.

The AI model will use machine learning algorithms to predict and anticipate traffic
conditions at every intersection. By continuously learning from incoming data, the system
will optimise and optimise traffic light timing in real time. Specifically, the AI model will
dynamically adjust the duration of the green, yellow, and red lights based on the current
traffic forecast. This proactive approach aims to eliminate complex traffic accidents and
reduce congestion by providing smooth transitions between intersections.
Utilizing Google Cloud, our YOLO-trained model performs real-time vehicle detection, capturing 
images and storing them alongside Green Signal Time (GST) and vehicle counts. This data, stored on Google Cloud,
facilitates thorough analysis, aiding in traffic prediction and enhancing overall traffic management efficiency.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Environment](#environment)
- [Usage](#usage)
- [Website](#Website)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Real-time Traffic Monitoring:** Collects and analyzes real-time traffic data from various sources.
- **Dynamic Signal Control:** Adjusts traffic signal timings based on current traffic conditions.
- **Predictive Analytics:** Uses machine learning to predict traffic patterns and optimize signal timings.
- **User-Friendly Interface:** Provides a graphical user interface for easy monitoring and control.
- **Scalability:** Designed to handle traffic management for both small towns and large cities.

## Installation

To install SmartSync-Traffic, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/Yadunandanv08/SmartSync-Traffic.git
   ```
2. Navigate to the project directory:
  ```sh
  cd SmartSync-Traffic
```
3. Install the required dependencies:
  ```sh
  pip install -r requirements.txt
```
 ### Ultralytics
 
 The code used here is:

 Install YOLOv8:
   ```sh
 pip install ultralytics
   ```
 Train a Model:
   ```sh
 yolo task=detect mode=train model=yolov8n.pt data=coco128.yaml epochs=50 imgsz=640
   ```
 Validate a Model:
   ```sh
 yolo task=detect mode=val model=yolov8n.pt data=coco128.yaml imgsz=640
   ```
 Detect Objects in Images:
   ```sh
 yolo task=detect mode=predict model=yolov8n.pt source=data/images
   ```
 Export a Model:
   ```sh
 yolo export model=yolov8n.pt format=onnx
   ```
Resume Training:
   ```sh
python train.py --resume path/to/last.pt
   ```
## Environment
   SmartSync-Traffic can be run on various environments. Below are the recommended specifications:

Operating System: Windows 10 or above
Python Version: 3.8 or above
Required Packages: Listed in requirements.txt
Hardware Requirements:
Processor: Intel i5 or equivalent
RAM: 8GB or more
Storage: 500MB of free space

## Usage
To run the SmartSync-Traffic system, use the following command:

```sh
python main.py
```
The system will start collecting and processing traffic data.


## Website
The website link is [Smart Sync](http://.com)

## Configuration
You can configure various parameters of the system in the config.yaml file. For example, you can set the data source, update intervals, and other settings.


## Contributing
We welcome contributions from the community! To contribute, follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
Please ensure your code follows our code of conduct and contribution guidelines.


## License
SmartSync-Traffic is licensed under the MIT License.

## Contact
If you have any questions or suggestions, feel free to reach out to the project maintainers:

Email - gmail.com

   
