import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (100,125),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(210,250,250))
cv2.putText(img, "Mercury", (110,185),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(210,250,250))
cv2.putText(img, "Venus", (190,170),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(210,250,250))
cv2.putText(img, "Earth", (285,165),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(210,250,250))
cv2.putText(img, "Mars", (380,175),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(210,250,250))
cv2.putText(img, "Jupiter", (565,50),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(210,250,250))
cv2.putText(img, "Saturn", (800,140),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(210,250,250))
cv2.putText(img, "Uranus", (965,140),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(210,250,250))
cv2.putText(img, "Neptune", (1110,145),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(210,250,250))

cv2.imshow("output", img)
cv2.waitKey(0)