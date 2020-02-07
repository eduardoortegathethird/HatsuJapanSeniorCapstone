#!/usr/bin/python

from picamera import PiCamera
from time import sleep

def main():
    camera = PiCamera()
    camera.start_preview()
    sleep(10)
    camera.capture('/tmp/picture.jpg')
    camera.stop_preview()

if __name__ == "__main__":
        main()
