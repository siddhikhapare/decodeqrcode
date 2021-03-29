#!/usr/bin/env python3
from __future__ import print_function
import cv2
import qrcode
import numpy as np
import glob


def decode(my_list):
    for x in my_list:
        x = np.arange(0,n)
    d = cv2.QRCodeDetector()
    #to detect and decode single qrcode
    #val,points,straight_qrcode = d.detectAndDecode(my_list)
    #to detect and decode multiple qrcodes
    retval,decoded_info,points,straight_qrcode = d.detectAndDecodeMulti(np.hstack(my_list))
    print(decoded_info)
    #print(val)
        
        

if __name__ == '__main__':


    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cv2.waitKey(10)
    filelist = glob.glob('/home/groot/catkin_ws/src/project/src/*.jpg')
    #print(filelist)

    my_list = []
    n = len(my_list)

    path = '/home/groot/catkin_ws/src/project/src/*.jpg'
    
    #glob module used to list multiple images from folder 
    for file in glob.glob(path):
        print(file)
        a = cv2.imread(file)
        my_list.append(a)
       
                                                                       


    decode(my_list)

    
cam.release()

cv2.destroyAllWindows()

