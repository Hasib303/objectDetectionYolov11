import cv2
import time
if __name__ == '__main__':
    cap = cv2.VideoCapture('TinyObject Detection/car-detection.mp4')

    if not cap.isOpened():
        print("Error")
    else:
        print("successfully")

    print('video dimention:', cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print('video FPS:', cap.get(cv2.CAP_PROP_FPS))

    while(cap.isOpened()):
        ret, img = cap.read()
        if ret:
            imgin = img[:, :, (0, 1, 2)]
        else:
            break
        
        cv2.imshow("first frame:", img)
        cv2.waitKey(10)
        time.sleep(1/(12.5-1))

    cap.release()