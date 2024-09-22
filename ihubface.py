import cv2

# Importing HARR CASCADE XML file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Capture Video from web cam hence (0) or else add your own media file
cap = cv2.VideoCapture(0)
# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (50, 50)

# fontScale
fontScale = 1

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.putText() method

# Creating a loop to capture each frame of the video in the name of Img
while True:
    _, img = cap.read()

    # Converting to grey scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Allowing multiple face detection
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)
    # Creating Rectangle around face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
        a = int(x)
        b = int(y)
        print("x = ", x, " y = ", b)
        if x >= 500:
            img = cv2.putText(img, 'LEFT', (a, b), font,
                              fontScale, color, thickness, cv2.LINE_AA)
        elif x <= 150:
            img = cv2.putText(img, 'RIGHT', (a, b), font,
                              fontScale, color, thickness, cv2.LINE_AA)
        elif y <= 100:
            img = cv2.putText(img, 'TOP', (a, b), font,
                              fontScale, color, thickness, cv2.LINE_AA)
        elif y >= 200:
            img = cv2.putText(img, 'BOTTOM', (a, b), font,
                              fontScale, color, thickness, cv2.LINE_AA)
        else:
            img = cv2.putText(img, 'CENTER', (a, b), font,
                              fontScale, color, thickness, cv2.LINE_AA)


    # Displaying the image
    cv2.imshow('Detected Face Image', img)

    # Waiting for escape key for image to close adding the break statement to end the face detection screen
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Real-time releasing the captired frames
cap.release()