from crypt import methods
from ctypes import resize
from sre_constants import SUCCESS
import cv2
import face_recognition
import numpy as npy
import os
float_value = npy.float64(3.14)
    # Path to the main directory containing subfolders
main_dir = '/Users/shivansh685/Desktop/attendance system/dataset'
stuImg=[]
stuName=[]
# Loop through each subfolder
for subdir in os.listdir(main_dir):
    subdir_path = os.path.join(main_dir, subdir)
    
    # Check if the item in the main directory is a directory
    if os.path.isdir(subdir_path):
        print(f"Reading images from folder: {subdir}")
        
        # Loop through each file in the subfolder
        for file_name in os.listdir(subdir_path):
            file_path = os.path.join(subdir_path, file_name)
            
            # Check if the file is an image file (you can add more image formats if needed)
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                # Read the image using OpenCV
                curImage = cv2.imread(file_path)
                stuImg.append(curImage)
                stuName.append(os.path.splitext(file_name)[0])

def findEncoding(images):
    imgEncoding= []
    for img in images:
        img=cv2.resize(img,(0,0),None,0.50,0.50)
        img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encodeimg= face_recognition.face_encodings(img)
        # Check if any face encodings are found
        if len(encodeimg) > 0:
        # Return the first face encoding
            imgEncoding.append(encodeimg[0])
        else:
        # If no face encodings are found, return None or handle the error as needed
            imgEncoding.append(None)
    return imgEncoding

EncodeList= findEncoding(stuImg)

vid= cv2.VideoCapture(0)
while True:
    success, frame=vid.read()
    Smaller_frames=cv2.resize(frame, (0,0), None, 0.25, 0.25)
    facesInFrame= face_recognition.face_locations(Smaller_frames)
    encodeFacesInFrame= face_recognition.face_encodings(Smaller_frames,facesInFrame)
    for encodeFace, faceloc in zip(encodeFacesInFrame, facesInFrame):
        matches=face_recognition.compare_faces(EncodeList,encodeFace)
        facedis=face_recognition.face_distance(EncodeList,encodeFace)
        print(facedis)
        matchIndex=npy.argmin(facedis)

        if matches[matchIndex]:
            name= stuName[matchIndex].upper()
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(frame,(x1,y2-25),(x2,y2-25),(0,255,0),cv2.FILLED)
            cv2.putText(frame,name, (x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()