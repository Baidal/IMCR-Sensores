import cv2 as cv
import num as np
import requests
import sys
import os.path
import socket


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class exit_codes:
    EX_OK = 0
    EX_USAGE = 64
    EX_NOINPUT = 66


class server_addresses:
    DEFAULT = "http://wewewew.com/apirest"


def checkArguments(argumentos):
    if len(argumentos) != 3:
        print(bcolors.FAIL,
              "Falta introducir el archivo adjunto y/o grado de distorsion. \n",
              bcolors.OKBLUE,
              "python3 preprocesamiento.py [archivo: string] [grado_distorsion: int]",
              bcolors.ENDC)
        sys.exit(exit_codes.EX_USAGE)


def checkFile(file):

    if not os.path.isfile(file):
        print(bcolors.FAIL,
              "La imagen introducida no existe:\n",
              bcolors.OKBLUE,
              file,
              bcolors.ENDC)

        sys.exit(exit_codes.EX_NOINPUT)


def checkDistortion(distorsion):

    distorsion = int(distorsion) if distorsion.isnumeric() else None

    if distorsion is None or distorsion < 1 or (distorsion % 2) == 0:
        print(bcolors.FAIL,
              "El grado de distorsion tiene que ser:",
              bcolors.OKBLUE,
              "un entero, impar y superior a 0",
              bcolors.ENDC)
        sys.exit(exit_codes.EX_USAGE)


def returnGaussianBlurred(image):
    return cv.GaussianBlur(
        image, (distortion, distortion), cv.BORDER_DEFAULT)


def sendBinaryData(path_data, camNumber):

    timeoutTime = 30
    
    file = {
        'media': open(path_data, 'rb'),
    }
    
    values = {        
        'camname': socket.gethostname()
    }

    response = requests.post(server_addresses.DEFAULT, files=file, data=values, timeout=timeoutTime)


def main():
    checkArguments(sys.argv)
    checkFile(sys.argv[1])
    checkDistortion(sys.argv[2])

    image = cv.imread(sys.argv[1])
    imgBlurred = returnGaussianBlurred(image)

    cv.imwrite(sys.argv[1], imgBlurred)

    # sendBinaryData(sys.argv[1])

    sys.exit(EX_OK)


main()
