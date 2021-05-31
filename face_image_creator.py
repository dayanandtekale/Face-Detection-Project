# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:47:35 2021

@author: dayanand
"""
# data collection
# create and train a model
# predection
#pre-requites -- TF, opencv, haar cascade file

import cv2
import numpy as np
#load HAAR face classifier
face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_extractor(img):
    faces=face_classifier.detectMultiScale(img,1.3,5)
    
    if faces is ():
        return None
        
    for (x,y,w,h) in faces:
        x=x-10
        y=y-10
        cropped_face=img[y:y+h+50,x:x+w+50]
        
    return cropped_face


#Init webcam
caputer_video=cv2.VideoCapture(0)
count=0

while True:
    ret,frame=caputer_video.read()
    if face_extractor(frame) is not None:
        count+=1
        face=cv2.resize(face_extractor(frame),(400,400))
        file_name='./dayanand_tekale/dayanand-'+str(count)+'.jpg'
        cv2.imwrite(file_name,face)
        cv2.putText(face, str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(250,20,23),2 )
        cv2.imshow('Face cropper', face)
    else:
        pass
   
    if cv2.waitKey(1)==13 or count==100:
        break
    
caputer_video.release()
cv2.destroyAllWindows()























































