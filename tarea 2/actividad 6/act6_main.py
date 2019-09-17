# autor: Hugo de Jesus Valenzuela Chaparro
# Universidad de Sonora, septiembre 2019
# Curso Desarrollo Experimental 2
# ************** actividad 6 de la tarea 2: ******************
# este programa aproxima el numero pi haciendo uso del metodo
# de Monte Carlo, para esto nos ayudamos de un circulo unitario
# inscrito a un cuadrado de lado 2, ambos con centros en el origen.
# lanzamos N numeros aleatorios y contamos las M veces que se cae
# dentro del circulo, posteriormente relacionamos la proporcion M/N
# con la propabilidad de caer dentro del circulo y calculamos pi como
# pi = (4*M)/N

# librerias requeridas para que funcione el programa
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------

# dar informacion del programa
print("""Este programa aproxima pi con el metodo de Monte Carlo, esto haciendo
N lanzamientos aleatorios dentro de un cuadrado con un circulo inscrito, y
contando las M veces que se cae dentro del circulo""")

N = input("""De el numero de N lanzamientos aleatorios que desee hacer
""")

np.random.seed(6427937) # semilla para poder hacer los numeros reproducibles
M = 0 # contador (caidas dentro del circulo) inicialmente en cero
# tirar los numeros aleatorios (distribucion uniforme) entre -1 y 1
for i in range(0, int(N)):
    x = 2.0*np.random.uniform(low = 0, high = 1, size = 1) - 1
    y = 2.0*np.random.uniform(low = 0, high = 1, size = 1) - 1
    # condicional para ver si cayeron dentro del circulo o no
    dist = x**2.0 + y**2.0 # distancia radial del punto
    if dist < 1:
        M += 1
    else:
        pass

# estimacion de pi
pi_hat = (4.0*float(M))/float(N)
# el error relativo, comparando con pi = 3.1415
epsilon = (np.absolute(pi_hat - 3.1415))/3.1415
# dar resultados
print("La estimacion de pi fue", pi_hat)
print("El error relativo (comparado con 3.1415) fue", epsilon)
