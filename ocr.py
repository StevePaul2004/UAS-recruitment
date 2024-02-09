import cv2
import numpy as np
img=cv2.imread("/Users/stevepaul/Desktop/Test_images/7.jpeg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#thresholding

_,tresh=cv2.threshold(gray,145,255,cv2.THRESH_BINARY)

#adaptive thresholding
adaptive=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,201,25)


cv2.imshow("original image",img)
cv2.imshow("threshold",tresh)
cv2.imshow("adaptively",adaptive)
cv2.waitKey(0)
cv2.destroyAllWindows()
