import cv2 as cv
import numpy as np
import sys



def parseArguments(argumentos):
    global img 
    global distorsion
    if len(argumentos) != 3:
        print("Falta introducir el archivo adjunto y/o grado de distorsion. \n Formato: preprocesamiento.py nombreArchivo GradoDistorsion(int)")
        sys.exit(-1)
    else:
        img = cv.imread(argumentos[1])
        if img is None:
            print("La imagen introducida no existe en " + argumentos[0])
            sys.exit(-1)
        
        distorsion = int(argumentos[2]) if argumentos[2].isnumeric() else None
        if distorsion is None or distorsion < 1:
            print("El grado de distorsion tiene que ser un entero superior a 0")
            sys.exit(-1)
        return


parseArguments(sys.argv)
blur = cv.GaussianBlur(img,(distorsion,distorsion),0)
nuevoNombre = sys.argv[1].split('.')
nombreArchivoBlur = nuevoNombre[0] + "Blur." + nuevoNombre[1]
cv.imwrite(nombreArchivoBlur,blur)
sys.exit(1)
