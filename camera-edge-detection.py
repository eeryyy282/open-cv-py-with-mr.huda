import cv2 as cv
kamera = cv.VideoCapture(0)
while True:
    cond, frame = kamera.read()
    edge = cv.Canny(frame, 70, 70)
    cv.imshow("Deteksi Edge", edge)
    exit = cv.waitKey(1) & 0xff
    if exit == ord('q'):
        break

kamera.release()
cv.destroyAllWindows()
        
    