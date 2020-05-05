import argparse
import os
import sys


def argParser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
                        '-s',
                        help='Variable to be parse wither SITL or communications MAVINIT',
                        action='store_true')
    parser.add_argument(
                        '--startCoord',
                        help='starting coordinates',
                        type=tuple)
    arguments = parser.parse_args()
    return arguments


def fileRead(file):
    listToBeReturned = []
    aliasFirstCheck = 0
    aliasExtra = 0
    for line in file.readlines():
        listToBeReturned.apppend(line)

def main():
    print("editing mavinit right now!\n\n")
    args = argParser()
    checkSITL = args.s
    startingCoordinates = args.startCoord
    startingX = startingCoordinates[0]
    startingY = startingCoordinates[1]
    if checkSITL:
        file = open("Mavinit.scr", "r")
        savingLines = fileRead(file)
            
    else:
        print("in the raspberry pi to run communication commands, do something else")
    
if __name__=="__main__":
	main()