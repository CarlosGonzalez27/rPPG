'''
Created on Nov 7, 2020

@author: lalop
'''
import numpy as np
import cv2
import face_detection
import time


lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")

class Extractor():
   
    def __init__(self, time):
        self.prev_face = [0,0,0,0]
        self.skin_prev = []
        self.rPPG = []
        self.cropped_img = []
        self.start_time = time
        self.last_time_check = 0
        self.running_time = 0
        self.detect_face = face_detection.FaceDetector()
        
    def RGB_avg_signal (self,num_pixels,img):
        return (np.sum(img[:,:,0])/num_pixels
               + np.sum(img[:,:,1])/num_pixels
               + np.sum(img[:,:,2])/num_pixels)/3
    
    def process_img(self, img, count):
        if count == 0:
            self.start_time = time.time()
        
        self.running_time = time.time() - self.start_time
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.detect_face.face(img, img_gray)
        
        if len(faces) != 0 and count % 2:
            # create a mask
            converted = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            skinMask = cv2.inRange(converted, lower, upper)
            num_pixels = np.sum(np.max(skinMask,1))
            skin = cv2.bitwise_and(img,img, mask = skinMask)
            # retrieve RGB_mean
            self.rPPG.append((self.RGB_avg_signal(num_pixels, skin),self.running_time))
            if self.running_time - self.last_time_check >= 3:
                self.last_time_check = self.running_time
                return self.rPPG
        return []        
            
        
            
        
