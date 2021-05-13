import cv2
path=input('Enter the path of image : ')
img=cv2.imread(path)
img=cv2.resize(img,(600,600))


