# autor: Hugo de Jesus Valenzuela Chaparro
# Universidad de Sonora,  2019
# Curso Desarrollo Experimental 2
# ************** configuracion inicial: ******************
# Este codigo es una funcion que sirve como subrutina  para crear
# una configuracion inicial aleatoria sin traslapes y con Maria Luisa
# SISTEMA: tridimensional de particulas esféricas
# UNIDADES REDUCIDAS: sigma-beta

# librerias requeridas para que funcione el programa
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------

# N numero de particulas
# DENS concentracion reducida

def conf_inic_random_3D_con_traslapes(N, DENS, boxL):

# ------------------- calculos preliminares ------------------------
# fraccion en area phit = pi*DENS/4
    phit = (float(DENS)*np.pi)/6.0
# el diametro de las particulas
    sigma = 1.0
# --------------------------------------------------------------------

# arreglos que almacenaran las posiciones
    X = np.zeros((int(N), 1))
    Y = np.zeros((int(N), 1))
    Z = np.zeros((int(N), 1))

    np.random.seed(4958202) # semilla para poder hacer los numeros reproducibles

# generar posiciones
    for i in range(0, int(N)):
    # numeros aleatorios para generar las posiciones
        deltax = np.random.uniform(low = 0, high = 1, size = 1) - 0.5
        deltay = np.random.uniform(low = 0, high = 1, size = 1) - 0.5
        deltaz = np.random.uniform(low = 0, high = 1, size = 1) - 0.5

    # posiciones (con Maria Luisa)
        X[i] = deltax*(boxL - 1.0)
        Y[i] = deltay*(boxL - 1.0)
        Z[i] = deltaz*(boxL - 1.0)


# dar resultados (posiciones)
    return X, Y, Z
