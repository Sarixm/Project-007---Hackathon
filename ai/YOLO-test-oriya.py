import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolov8n-face.pt")

# To test on a static image insert the path to the imgae in iamge_path variable and uncomment the next 3 lines
#image_path = ""
#image_results = model(image_path)
#image_results[0].show()

# Start webcam capture
cap = cv2.VideoCapture(0) # To detect faces on video change the value "0" to the path to the video 
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Frame not captured.")
        break

    # Perform inference on the frame
    results = model(frame)

    # Render the results on the frame
    annotated_frame = results[0].plot()  # Draw bounding boxes and labels

    # Display the frame
    cv2.imshow('YOLO Detection', annotated_frame)

    # Break loop on 'q' key press
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
exit()
