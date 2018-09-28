import cv2

img=cv2.imread('P131059.jpg')
detector = cv2.FastFeatureDetector_create()
keypoints = detector.detect(img)
out=cv2.drawKeypoints(img,keypoints,None)
cv2.imshow("keypoints",out)
cv2.waitKey(0)