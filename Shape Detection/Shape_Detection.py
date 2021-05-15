import cv2
path=input('Enter the path of image : ')
img=cv2.imread(path)
img=cv2.resize(img,(600,600))
gray=cv2.cvtColor(img,cv2.COLORBGR2GRAY)
blur=cv2.Gaussianblur(gray,(5,5),0)
_,thresh=cv2.threshold(gray)

