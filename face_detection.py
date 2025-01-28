import cv2
import face_recognition
Adriana_Lima = face_recognition.load_image_file('dataset/pins_Adriana Lima/Adriana_Lima.jpg')
Adriana_Lima= cv2.cvtColor(Adriana_Lima, cv2.COLOR_BGR2RGB)
faceLocation_Adriana_Lima=face_recognition.face_locations(Adriana_Lima)[0]
Adriana_Lima_encode=face_recognition.face_encodings(Adriana_Lima)[0]
cv2.rectangle(Adriana_Lima,(faceLocation_Adriana_Lima[3],faceLocation_Adriana_Lima[0]),(faceLocation_Adriana_Lima[1],faceLocation_Adriana_Lima[2]),(255,0,0),2)

Adriana_Lima2=face_recognition.load_image_file('dataset/pins_Adriana Lima/Adriana_Lima2.jpg')
Adriana_Lima2= cv2.cvtColor(Adriana_Lima2, cv2.COLOR_BGR2RGB)
faceLocation_Adriana_Lima2=face_recognition.face_locations(Adriana_Lima2)[0]
Adriana_Lima2_encode=face_recognition.face_encodings(Adriana_Lima2)[0]
cv2.rectangle(Adriana_Lima2,(faceLocation_Adriana_Lima2[3],faceLocation_Adriana_Lima2[0]),(faceLocation_Adriana_Lima2[1],faceLocation_Adriana_Lima2[2]),(255,0,0),2)

results=face_recognition.compare_faces([Adriana_Lima_encode],Adriana_Lima2_encode)
print(results)

Alex_Lawther=face_recognition.load_image_file('dataset/pins_Alex Lawther/Alex_Lawther.jpg')
Alex_Lawther= cv2.cvtColor(Alex_Lawther, cv2.COLOR_BGR2RGB)
faceLocation_Alex_Lawther=face_recognition.face_locations(Alex_Lawther)[0]
Alex_Lawther_encode=face_recognition.face_encodings(Alex_Lawther)[0]
cv2.rectangle(Alex_Lawther,(faceLocation_Alex_Lawther[3],faceLocation_Alex_Lawther[0]),(faceLocation_Alex_Lawther[1],faceLocation_Alex_Lawther[2]),(255,0,0),2)

Alex_Lawther1=face_recognition.load_image_file('dataset/pins_Alex Lawther/Alex_Lawther1.jpg')
Alex_Lawther1= cv2.cvtColor(Alex_Lawther1, cv2.COLOR_BGR2RGB)
faceLocation_Alex_Lawther1=face_recognition.face_locations(Alex_Lawther1)[0]
Alex_Lawther1_encode=face_recognition.face_encodings(Alex_Lawther1)[0]
cv2.rectangle(Alex_Lawther1,(faceLocation_Alex_Lawther1[3],faceLocation_Alex_Lawther1[0]),(faceLocation_Alex_Lawther1[1],faceLocation_Alex_Lawther1[2]),(255,0,0),2)

Alexandra_Daddario =face_recognition.load_image_file('dataset/pins_Alexandra Daddario/Alexandra_Daddario.jpg')
Alexandra_Daddario= cv2.cvtColor(Alexandra_Daddario, cv2.COLOR_BGR2RGB)
faceLocation_Alexandra_Daddario=face_recognition.face_locations(Alexandra_Daddario)[0]
Alexandra_Daddario_encode=face_recognition.face_encodings(Alexandra_Daddario)[0]
cv2.rectangle(Alexandra_Daddario,(faceLocation_Alexandra_Daddario[3],faceLocation_Alexandra_Daddario[0]),(faceLocation_Alexandra_Daddario[1],faceLocation_Alexandra_Daddario[2]),(255,0,0),2)

Alexandra_Daddario1 =face_recognition.load_image_file('dataset/pins_Alexandra Daddario/Alexandra_Daddario1.jpg')
Alexandra_Daddario1= cv2.cvtColor(Alexandra_Daddario1, cv2.COLOR_BGR2RGB)
faceLocation_Alexandra_Daddario1=face_recognition.face_locations(Alexandra_Daddario1)[0]
Alexandra_Daddario1_encode=face_recognition.face_encodings(Alexandra_Daddario1)[0]
cv2.rectangle(Alexandra_Daddario1,(faceLocation_Alexandra_Daddario1[3],faceLocation_Alexandra_Daddario1[0]),(faceLocation_Alexandra_Daddario1[1],faceLocation_Alexandra_Daddario1[2]),(255,0,0),2)


cv2.imshow('main_image',Adriana_Lima)
cv2.imshow('image2',Adriana_Lima2)
cv2.waitKey(0)
cv2.destroyAllWindows()