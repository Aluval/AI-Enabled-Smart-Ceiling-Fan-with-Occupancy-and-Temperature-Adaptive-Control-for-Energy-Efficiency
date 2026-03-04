from ultralytics import YOLO
import cv2
import time

# Load YOLO model
model = YOLO("yolov8n.pt")
model.to("cpu")

# Open webcam
cap = cv2.VideoCapture(0)

temperature = 28
prev_time = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # AI detection
    results = model(frame, device="cpu")

    people = 0

    for r in results:
        for box in r.boxes:

            cls = int(box.cls[0])

            if cls == 0:   # person class
                people += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

                cv2.putText(frame,"Person",(x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    # -----------------------
    # Smart Fan Logic
    # -----------------------

    if people == 0:
        fan_speed = "OFF"
    else:
        if temperature < 25:
            fan_speed = "LOW"
        elif temperature < 30:
            fan_speed = "MEDIUM"
        else:
            fan_speed = "HIGH"

        if people >= 3:
            fan_speed = "HIGH"

    # -----------------------
    # Power Consumption
    # -----------------------

    if fan_speed == "OFF":
        power = 0
    elif fan_speed == "LOW":
        power = 25
    elif fan_speed == "MEDIUM":
        power = 45
    else:
        power = 70

    # -----------------------
    # FPS Calculation
    # -----------------------

    current_time = time.time()
    fps = 1/(current_time-prev_time) if prev_time != 0 else 0
    prev_time = current_time

    # -----------------------
    # Dashboard Panel
    # -----------------------

    cv2.rectangle(frame,(10,10),(380,220),(255,255,255),-1)

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame,f"People: {people}",(20,50),
                font,1.1,(0,0,0),3)

    cv2.putText(frame,f"Temp: {temperature} C",(20,90),
                font,1.1,(0,0,0),3)

    cv2.putText(frame,f"Fan Speed: {fan_speed}",(20,130),
                font,1.1,(0,0,0),3)

    cv2.putText(frame,f"Power: {power} W",(20,170),
                font,1,(0,0,0),2)

    cv2.putText(frame,f"FPS: {int(fps)}",(20,200),
                font,0.8,(0,0,0),2)

    cv2.putText(frame,
    "Developed By Aluvala Ediga Harsha Vardhan Goud, MCA",
    (10, frame.shape[0] - 10),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5,
    (255,255,255),
    1)

    # -----------------------
    # Log Data
    # -----------------------

    with open("fan_log.txt","a") as log:
        log.write(f"People:{people}, Temp:{temperature}, Fan:{fan_speed}, Power:{power}\n")

    # -----------------------
    # Show window
    # -----------------------

    cv2.imshow("AI Smart Fan Camera",frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

    if key == ord('u'):
        temperature += 1

    if key == ord('d'):
        temperature -= 1

cap.release()
cv2.destroyAllWindows()