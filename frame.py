import cv2
cap = cv2.VideoCapture(f"E://bikeing videos/1.mp4")
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
