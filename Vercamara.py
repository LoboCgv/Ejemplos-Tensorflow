import numpy as np
import cv2
 
#cargamos la plantilla e inicializamos la webcam:
face_cascade = cv2.CascadeClassifier('detectors/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
 
while(True):
    #leemos un frame y lo guardamos
    ret, img = cap.read()
 
    #convertimos la imagen a blanco y negro
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    #buscamos las coordenadas de los rostros (si los hay) y
    #guardamos su posicion
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
    #Dibujamos un rectangulo en las coordenadas de cada rostro
    for (x,y,w,h) in faces:
        cv2.rectangle(gray,(x,y),(x+w,y+h),(125,255,0),2)
    #guardar imagenes de caras
    i=0
    for(x,y,w,h) in faces:
        idUsuario=(x+y)*(w+h)
        crop_img = gray[y:y+h, x:x+w]
        i=i+1
        salida="entrenar/"+str(idUsuario)+str(i)+".jpg"
        cv2.imwrite(salida,crop_img)
    #Mostramos la imagen
    cv2.imshow('img',gray)
    

     
    #con la tecla 'q' salimos del programa
    if cv2.waitKey(1) & 0xFF == ord('q'):#apretar q para salir
        break
cap.release()
cv2.destroyAllWindows()
