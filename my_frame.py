import cv2

cap = cv2.VideoCapture("Cats.mp4")
count = 0

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow('frame', frame)
        count += 5 # i.e. at 30 fps, this advances one second
        cap.set(cv2.CAP_PROP_POS_FRAMES, count)
        cv2.waitKey(1)
    else:
        cap.release()
        break