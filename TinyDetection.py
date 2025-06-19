import cv2
from ultralytics import YOLO

# model = YOLO("TinyObject Detection/my_model/train5/weights/best.pt")
model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture("/Users/hasib/Code/TinyObject Detection/my_model/road_trafifc.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model.predict(frame, conf=0.4)[0]
    annotated_frame = results.plot()

    cv2.imshow("Real time Detection", annotated_frame)
    cv2.waitKey(25)

cap.release()
cv2.destroyAllWindows()