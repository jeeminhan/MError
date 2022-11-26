# this is just a look at python forking & such
''' ========================= SOURCES =========================
https://www.studytonight.com/python/python-threading-event-object#:~:text=The%20Event%20class%20object%20provides,the%20waiting%20thread%20gets%20activated.
https://superfastpython.com/threading-in-python/

'''
import threading as thr
import cv2

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
ret,frame = cap.read() # return a single frame in variable `frame`

while(True):
    cv2.imshow('img1',frame) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite('images/c1.png',frame)
        cv2.destroyAllWindows()
        break

def capture_face(event, saveFaces=False):
    print("Looking for faces...")
    # capture one frame from camera feed
    camera = cv2.VideoCapture(0)
    while not event.is_set():
        # return frame as facial image
        ret,face = camera.read()
        if saveFaces:
            imgName = 'images/c' + i + '.png'
            
            cv2.imwrite(imgName,face)
            cv2.imwrite('images/mostRecent.png',face)
            # cv2.destroyAllWindows()
            i += 1
        event.set()  # flag that a face has been captured

def process_face(event):
    print("Started thread but waiting for event...")
    # make the thread wait for event with timeout set
    while event.is_set():  # once a face is captured
        facePic= cv2.imread('images/mostRecent.png')  # read the most recent image
        # do the facial recognition
        
    
if __name__ == '__main__':
    faceCaptured = thr.Event()  # initializing the event
    saveFaces = True
    i = 0
    # define each thread
    thread1 = thr.Thread(name='Face-Processing', target=process_face, args=(faceCaptured))
    # thread2 = thr.Thread(name='Face-Capturing', target=capture_face, args=(e2))
    thread1.start()
    capture_face(faceCaptured, saveFaces)
