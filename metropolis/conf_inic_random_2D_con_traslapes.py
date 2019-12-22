# autor: Hugo de Jesus Valenzuela Chaparro
# Universidad de Sonora, septiembre 2019
# Curso Desarrollo Experimental 2
# ************** configuracion inicial: ******************
# Este codigo es una funcion que sirve como subrutina  para crear
# una configuracion inicial aleatoria sin traslapes y con Maria Luisa
# SISTEMA: bidimensional de particulas discos
# UNIDADES REDUCIDAS: sigma-beta

# librerias requeridas para que funcione el programa
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------

# N numero de particulas
# DENS concentracion reducida

def conf_inic_random_2D_con_traslapes(N, DENS):

# ------------------- calculos preliminares ------------------------
# lado reducido de la celda
    boxL = ((1.0*float(N))/float(DENS))**(1.0/2.0)
# fraccion en area phit = pi*DENS/4
    phit = (float(DENS)*np.pi)/4.0
# el diametro de las particulas
    sigma = 1.0
# --------------------------------------------------------------------

# arreglos que almacenaran las posiciones
    X = np.zeros((int(N), 1))
    Y = np.zeros((int(N), 1))

    np.random.seed(4958202) # semilla para poder hacer los numeros reproducibles

# generar posiciones
    for i in range(0, int(N)):
    # numeros aleatorios para generar las posiciones
        deltax = np.random.uniform(low = 0, high = 1, size = 1) - 0.5
        deltay = np.random.uniform(low = 0, high = 1, size = 1) - 0.5
    # posiciones (con Maria Luisa)
        X[i] = deltax*(boxL - 1.0)
        Y[i] = deltay*(boxL - 1.0)


# dar resultados (posiciones)
    return X, Y
