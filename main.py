import cv2
import mtcnn
#import tensorflow as tf
import matplotlib.pyplot as plt


print("Welcome :")
print("Do you want to recognize new face or an old face (O,N)")
oldNewCh=input()
while True:
    if(oldNewCh=='N'):
        print("LET's take a pic of new face")
        print("Enter anything to continue")
        input()
        print("press c to capture")
        img=0
        vedioSource = cv2.VideoCapture(0)
        while(True):

            conformation, frame = vedioSource.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('c'):
                img=frame
                break
        vedioSource.release()
        cv2.destroyAllWindows()
    
        ##Show Image
        plt.imshow(img)
        plt.show()
        #############################################
        #  EXTRACT FACES 
        #############################################
        # draw an image with detected objects
        detector = mtcnn.MTCNN()
        faces = detector.detect_faces(img)
        for result in faces:
            x, y, width, height = result['box']
            img=img[y:y+height,x:x+width]
        plt.imshow(img)
        plt.show()
        break

