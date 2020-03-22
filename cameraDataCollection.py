#!/usr/bin/python

from picamera import PiCamera
from time import sleep
import os
from datetime import datetime

def main():
    #creates camera object and the gets the current working directory
    camera = PiCamera()
    currWorkingPath = os.getcwd()
    
    #loop for camera-input data collection
    for picNum in range(0, 10):
        #previews the image
        camera.start_preview();
        sleep(1)
        
        #adjust the path to the test_pic we need for a data point to be annotated later
        picCapture = currWorkingPath + "/testPic_" + str(picNum) + ".jpg"
        print(picCapture)
        camera.capture(picCapture)
        
        #stops preview to be updated in next iteration of the loop or if at the end, just exit
        camera.stop_preview()

    #pulls the current time stamp for folder name creation
    timeStamp = datetime.now()
    timeStamp_split = str(timeStamp).split(" ")
    timeStampAdjust = timeStamp_split[0] + "_" + timeStamp_split[1]

    #creates the name of the folder
    folder = "dataSet_" + timeStampAdjust
    
    #creates the folder and moves the data points into folder
    os.popen("mkdir " + folder)
    os.popen("mv testPic_*.jpg " + folder)

if __name__ == "__main__":
        main()
