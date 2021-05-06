import cv2

# Taking the path for input image
path=input("Enter the path of the image: ")
img = cv2.imread(path)
#Resizing the image
img=cv2.resize(img,(600,600))
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the cascade
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')

# Detecting the faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

i=0
# Draw rectangle around the faces and crop the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    faces = img[y:y + h, x:x + w]
    cv2.imshow('face',faces)
    #Naming the file
    desti='face'+str(i)+'.jpg'
    cv2.imwrite(desti, faces)
    i+=1

	
# Display the output
cv2.imwrite('detcted.jpg', img)
cv2.imshow('Output',img)
cv2.waitkey(0)
cv2.destroyAllWindows()
