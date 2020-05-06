import argparse
import os
import sys


def argParser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
                        '--pixelX',
                        help='x distance to move through guided mode',
                        type=int)
    parser.add_argument(
                        '--pixelY',
                        help='y distance to move through guided mode',
                        type=int)
    parser.add_argument(
                        '--pixelZ',
                        help='z distance to move through guided mode',
                        type=int)
    arguments = parser.parse_args()
    return arguments

def main():
    print("Adjusting mavinit.scr!\n\n")
    args = argParser()

    pixX = args.pixelX
    pixY = args.pixelY
    pixZ = args.pixelZ
    
    #the constant is needed for height adjustment
    #assumed that the dront charging sttion is facing north
    #conversion hashtable implementation ~ all assumed drone will fly at 2m hieght
    guideX = -1.0 * (float(((pixX - 1640) / 1640)) * 3.79)
    guideY = -1.0 * (float(((pixY - 1232) / 1232)) * 2.28)
    #for current progress of project - assume z is at 2 meters
    guideZ = 2.0

    os.popen('cd /home/pi/MyCopter')
    os.popen('rm mavinit.scr')
    os.popen('touch mavinit.scr')
    os.popen('python mavinit.py --guideX ' + str(guideX) + ' --guideY ' + str(guideY) + ' --guideZ '+ str(guideZ))
    os.popen('cd /home/pi')
    os.popen('mavproxy.py --master=/dev/serial0 --baudrate 921600 --aircraft MyCopter')

if __name__=="__main__":
	main()
