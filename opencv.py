import cv2
def opencvdemo():
    path="IMG-20.jpg"
    img=cv2.imread(path)
    print(img)
    cv2.imshow("image 1",img)
    cv2.waitkey()
opencvdemo()