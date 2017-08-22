import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_alt_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
profile_face_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
left_eye_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
right_eye_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')


# Press q to quit
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    face_detected = False
    for (x,y,w,h) in faces:
        face_detected = True
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        # search region of interest (face) for eyes
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # eyes = eye_cascade.detectMultiScale(roi_gray)

        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
        #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        left_eye = left_eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in left_eye:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(51,153,255),2)

        right_eye = right_eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in right_eye:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(51,255,255),2)

        # smiles = smile_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in smiles:
        #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

    if not face_detected:
        # search complete frame for eyes
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # search complete frame for profile
    # profile = profile_face_cascade.detectMultiScale(gray, 1.3, 5)
    # for (ex,ey,ew,eh) in profile:
    #     cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,0,0),2)
   

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



        # search region of interest (face) for eyes
        # roi_gray = gray[y:y+h, x:x+w]
        # roi_color = frame[y:y+h, x:x+w]
        # eyes = eye_cascade.detectMultiScale(roi_gray)

  