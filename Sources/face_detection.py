'''
Created on Nov 7, 2020

@author: lalop
'''
import cv2
import numpy as np



class FaceDetector():

    def __init__(self):
        self.rect = []
        self.intitial = True
        self.faceCascade = cv2.CascadeClassifier("../../sources/haarcascade_frontalface_default.xml")
    
    def skin(self, img):
        return None
    
    def crop_img(self, img, rect):
        x = rect[0]
        y = rect[1]
        w = rect[2]
        h = rect[3]
        return img[y:y+h,x:x+w]
    
    def face(self,img, img_gray):
        self.rect = self.faceCascade.detectMultiScale(img_gray,1.1,2, minSize = (130,130))
        for (x,y,w,h) in self.rect:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        return self.rect;
        #faces = faceCascade.detectMultiScale(img_gray,1.1,2, minSize = (130,130))
        #if len(faces) == 0:
        #    return img, img_gray
        #else:
        #    return self.crop_img(img,faces),self.crop_img(img_gray, faces)
        #for(x,y,w,h) in faces:
        #    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)