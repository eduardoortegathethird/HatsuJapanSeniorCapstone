import argparse
import os
import sys


def argParser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
                        '--guideX',
                        help='x distance to move through guided mode',
                        type=int)
    parser.add_argument(
                        '--guideY',
                        help='y distance to move through guided mode',
                        type=int)
    parser.add_argument(
                        '--guideZ',
                        help='z distance to move through guided mode',
                        type=int)
    arguments = parser.parse_args()
    return arguments

def fileWriteCommunications(file, guideX, guideY, guideZ):
    file.write('arm safetyoff\n')
    file.write('setspeed 1\n')
    file.write('takeoff ' + str(guideZ) + '\n')
    file.write('mode guided' + '\n')
    file.write('guided ' + str(guideX) + ' ' + str(guideY) + ' ' + str(guideZ) + '\n')

def main():
    print("Adjusting mavinit.scr!\n\n")
    args = argParser()

    guideX = args.guideX
    guideY = args.guideY
    guideZ = args.guideZ
    
    file = open("mavinit.scr", "w")
    fileWriteCommunications(file, guideX, guideY, guideZ)
    file.close()

if __name__=="__main__":
	main()
