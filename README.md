# IMCR-Sensores
Parte de tratamiento de imágenes  por parte del grupo de sensores.

## Funcionamiento

El código principal se encuentra en el archivo preprocesamiento.py, el cual debe ser llamado de la siguiente forma:
```
python preprocesamiento.py nombrearchivo distorsion
```
Donde "nombrearchivo" es el nombre de la imagen a procesar, y "distorsión" un entero que representa el grado de distorsión de la imagen.
En caso de no pasar los argumentos, la imagen no sea encontrada, o se pase una distorsión que no sea un entero, o este sea menor que 0, el programa se abortará con estado -1. En caso contrario se creará una nueva imagen, que será guardada con el nombre original de la imagen más el sufijo "Blur". 

Así, si la imagen original es
```
Kante.png
```
La imagen resultante será:
```
KanteBlur.png
```

## Instalación
Para ejecutar el script es necesario que esté instalada la librería python3-opencv en el sistema, además de python.

