'''
Created on Nov 7, 2020

@author: lalop
'''
import cv2
import extract_signal
import time
import matplotlib.pyplot as plt
import multiprocessing as mp

if __name__ == '__main__':
    #videoc = cv2.VideoCapture(0)
    videoc = cv2.VideoCapture("../Helper/matt.mp4")
    
    count = 0
    start_time = time.time()
    extract = extract_signal.Extractor(start_time) # create an instance of the class intialize time
    rppg = []
    x = []
    y = []
    while True:
        success, img = videoc.read() #saves image in first variable and tells us successful or not
        
        if (success == False):
            break
        rppg = extract.process_img(img, count) # process image
        for color,time in rppg:
            x.append(time)
            y.append(color)
        if len(x) > 0 and len(y) > 0:
            plt.plot(x,y)
            plt.pause(.0000001)
            x.clear()
            y.clear()
        cv2.imshow("Video", img) #shows result
        if cv2.waitKey(1) & 0xff ==ord('q'):
            break
        count = count + 1
    videoc.release()
    cv2.destroyAllWindows()
    end_time = time.time()
    time_diff = end_time - start_time
    print('end ' + str(time_diff))
    exit()
