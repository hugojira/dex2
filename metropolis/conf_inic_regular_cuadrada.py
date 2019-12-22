# autor: Hugo de Jesus Valenzuela Chaparro
# Universidad de Sonora, agosto 2019
# Curso Desarrollo Experimental 2
# ************** actividad 4 de la tarea 1: ******************
# Este programa crea un arreglo cuadrado de N^2 particulas en una
# celca cuadrada de lado L. Los datos N y L son dados por usuario
# en pantalla. Cabe destacar que el numero de particulas siempre
# sera N^2, esto para que quede un arreglo cuadrado perfecto.

# librerias necesarias para que funcione el programa
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------

def conf_inic_regular_cuadrada(N, DENS):

# ------- caso de una sola particula, se pone en el origen -------
    if int(N) == 1:
        pos = np.zeros((1, 2))
        plt.plot(pos[0,0], pos[0,1], "bo")
        plt.title("una sola particula en el origen")
        plt.show()
        print(pos)
        exit()
    else:
        pass
# -----------------------------------------------------------

# ------------------- calculos preliminares ------------------------
# lado reducido de la celda
    boxL = ((1.0*float(N))/float(DENS))**(1.0/2.0)
# fraccion en area phit = pi*DENS/4
    phit = (float(DENS)*np.pi)/4.0
# el diametro de las particulas
    sigma = 1.0
# --------------------------------------------------------------------


# separacion de las particulas, es L/(n-1)
    dL = float(boxL)/(float(N) - 1.0)
# total de particulas que llenaran la celda cuadrada
    total_particulas = (int(N))**2

# arreglo dimension Ntotal x 2 que servira para almacenar posiciones x, y
# de todas las particulas
    pos = np.zeros((total_particulas, 2))

# ciclos anidados para llenar la cuadricula
    for i in range(0, int(N)):
        x_temp = float(boxL) - float(i)*dL # coordenada x
        contador_auxiliar = (i)*int(N)
        for j in range(0, int(N)):
            contador_final = contador_auxiliar + j
            y_temp = float(boxL) - float(j)*dL # coordenada y
            pos[contador_final, 0] = x_temp # almacenar coord x en arreglo
            pos[contador_final, 1] = y_temp # almacenar coord y en arreglo


# trasladar el centro de la celda al origen (0,0)
    pos[:,0] = pos[:,0] - float(boxL)/2.0
    pos[:,1] = pos[:,1] - float(boxL)/2.0
    X = pos[:, 0]
    Y = pos[:, 1]


    return X, Y
