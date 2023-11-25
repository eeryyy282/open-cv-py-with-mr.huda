import cv2 as cv

img = cv.imread("eka-ai.jpg")
cv.imshow("eka", img)
cv.waitKey(0)
cv.destroyAllWindows()
 