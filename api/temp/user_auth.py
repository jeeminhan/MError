# This file has all the associated helper functions for authentication purposes
from .models import UserAccount
import cv2

import threading
import face_recognition as fr
import numpy as np
import os

# Accessing User Information
def all_users():
     users=UserAccount.objects.all()
     print(users)
     return users


def get_picture():  
    # define a video capture object
    vid = cv2.VideoCapture(0)
    counter=0

    while(counter<400):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
    
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        counter+=1
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


def get_face_encodings():
    faces_path = r"D:\Projects Collection\Personal Website\MError\user_profile_images"
    face_names = os.listdir(faces_path)
    face_encodings = []

    # For loop to retrieve all face encodings and store them in a list.
    # Below loop also gets the names of people and removes ".jpg", and stores
    # the names in a list
    for i, name in enumerate(face_names):
        face = fr.load_image_file(f"{faces_path}\\{name}")
        face_encodings.append(fr.face_encodings(face)[0])

        face_names[i] = name.split(".")[0] # To remove ".jpg" or any other image extension
    
    return face_encodings, face_names


def examine_user(auth):
    global AUTH_USER
    AUTH_USER=""

    # Retrieving face encodings and storing them in the face_encodings variable, along with the names
    face_encodings, face_names = get_face_encodings()

    # Reference to webcam
    video = cv2.VideoCapture(0)

    # Setting variable which will be used to scale size of image
    scl = 2

    # Continuously capturing webcam footage
    # while True:
    while not auth.is_set():
        success, image = video.read()

        # Making current frame smaller so program runs faster
        resized_image = cv2.resize(image, (int(image.shape[1]/scl), int(image.shape[0]/scl)))

        # Converting current frame to RGB, since that's what the face recognition module uses
        rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

        # Retrieving face location coordinates and unknown encodings
        face_locations = fr.face_locations(rgb_image)
        unknown_encodings = fr.face_encodings(rgb_image, face_locations)

        # Iterating through each encoding, as well as the face's location
        for face_encoding, face_location in zip(unknown_encodings, face_locations):
            # Comparing known faces with unknown faces
            result = fr.compare_faces(face_encodings, face_encoding, 0.4)
            print(result)
            # Getting correct name if a match was found
            if True in result:
                # print(result, face_names[result.index(True)])
                name = face_names[result.index(True)]

                # # Setting coordinates for face location
                top, right, bottom, left = face_location

                # # Drawing rectangle around face
                cv2.rectangle(image, (left*scl, top*scl), (right*scl, bottom*scl), (0, 0, 255), 2)

                # # Setting font, as well as displaying text of name
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(image, name, (left*scl, bottom*scl + 20), font, 0.8, (255, 255, 255), 1)

        # Displaying final image on the screen
        cv2.imshow("frame", image)
        cv2.waitKey(1)