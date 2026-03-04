AI Smart Ceiling Fan System

AI-Enabled Occupancy and Temperature Adaptive Smart Ceiling Fan System for Energy Efficient Smart Homes

Developed by Aluvala Ediga Harsha Vardhan Goud (MCA)

Overview

This project presents an AI-powered smart ceiling fan control system that automatically adjusts fan speed based on room occupancy and temperature conditions. The system uses computer vision with YOLOv8 to detect people in a room through a camera and intelligently controls fan speed to improve energy efficiency and comfort.

The prototype demonstrates how Artificial Intelligence, Computer Vision, and Smart Home Automation can be integrated to build intelligent energy-saving devices.

Features

Real-time people detection using YOLOv8

Automatic fan speed adjustment

Temperature adaptive control

Real-time dashboard display

Power consumption estimation

System performance (FPS) monitoring

Data logging for analysis

System Architecture
Camera
   │
   ▼
AI Detection (YOLOv8)
   │
   ▼
People Counting + Temperature Input
   │
   ▼
Decision Logic Engine
   │
   ▼
Smart Fan Control
Practical Implementation Using Prototype

To validate the proposed AI-Enabled Smart Ceiling Fan System, a working prototype was developed and tested in a real-time environment. The prototype uses a webcam connected to a computer running the Python-based AI detection system. The camera captures live video from the room, and the YOLOv8 object detection model processes each frame to identify and count the number of people present.

Based on the detected occupancy and temperature conditions, the system automatically determines the appropriate fan speed (OFF, LOW, MEDIUM, or HIGH). The decision logic is displayed in a real-time dashboard that shows the number of detected persons, estimated power consumption, and system performance.

The prototype demonstrates the practical feasibility of integrating computer vision, artificial intelligence, and smart energy management to develop an intelligent ceiling fan control system. The system successfully adapts airflow based on real-time environmental conditions and occupancy levels, thereby improving comfort and reducing unnecessary energy consumption.

Although the current implementation operates as a software-based prototype, the same control logic can be integrated with embedded hardware such as Raspberry Pi, ESP32, or smart fan controllers to create a fully functional smart home device.

IoT-Based Real-Time Implementation

The system can be extended to a real IoT-based smart fan controller using embedded hardware.

Possible hardware platforms include:

Raspberry Pi

ESP32

Jetson Nano

Smart relay modules

IoT Architecture
Camera
   │
   ▼
AI Detection System
   │
   ▼
Edge Device (Raspberry Pi / ESP32)
   │
   ▼
Relay Controller
   │
   ▼
Smart Ceiling Fan

This allows the system to operate in real time, continuously monitoring occupancy and environmental conditions to automatically regulate airflow.

Technologies Used
Technology	Purpose
Python	Core programming language
OpenCV	Camera access and image processing
YOLOv8	AI-based person detection
NumPy	Numerical operations
Installation

Clone the repository:

git clone https://github.com/yourusername/ai-smart-fan.git
cd ai-smart-fan

Install dependencies:

pip install ultralytics
pip install opencv-python
pip install numpy
Running the Project

Run the program using:

python smart_fan.py

The camera window will open and display:

Number of detected people

Temperature

Fan speed

Power consumption

System FPS

Example Output
People: 2
Temp: 28°C
Fan Speed: MEDIUM
Power: 45W
FPS: 22
Project Structure
AI-Smart-Fan
│
├── smart_fan.py
├── README.md
├── LICENSE
├── documentation.docx
└── fan_log.txt
Future Improvements

IoT cloud integration

Mobile application control

Smart building automation

Energy consumption analytics

License

This project is licensed under the Apache License 2.0

Copyright © 2026
Aluvala Ediga Harsha Vardhan Goud

Author

Aluvala Ediga Harsha Vardhan Goud
Master of Computer Applications (MCA)
