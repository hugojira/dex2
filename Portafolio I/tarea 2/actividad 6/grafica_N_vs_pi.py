# autor: Hugo de Jesus Valenzuela Chaparro
# Universidad de Sonora, septiembre 2019
# Curso Desarrollo Experimental 2
# ************** actividad 6 de la tarea 2: ******************
# este programa grafica la relacion entre la estimacion de pi y el
# numero de lanzamientos N. Se recorre N desde 1 a 1000 a pasos de 10

# librerias requeridas para que funcione el programa
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------

np.random.seed(6427937) # semilla para poder hacer los numeros reproducibles
# loop para hacer lanzamientos desde N=  1 a N = 1000, a pasos de 10 en 10
pi_N = np.zeros((101, 2)) # arreglo para guardar la informacion a graficar
for i in range(0, 1010, 10):
    M = 0 # contador (caidas dentro del circulo) inicialmente en cero
    # tirar los numeros aleatorios (distribucion uniforme) entre -1 y 1
    for j in range(1, i + 2):
        x = 2.0*np.random.uniform(low = 0, high = 1, size = 1) - 1
        y = 2.0*np.random.uniform(low = 0, high = 1, size = 1) - 1
        # condicional para ver si cayeron dentro del circulo o no
        dist = x**2.0 + y**2.0 # distancia radial del punto
        if dist < 1:
            M += 1
        else:
            pass
    # estimacion de pi
    pi_hat = (4.0*float(M))/float(i + 1)
    pi_N[int(i/10), 0] = i
    pi_N[int(i/10), 1] = pi_hat

# graficacion
plt.plot(pi_N[:,0], pi_N[:,1])
plt.title("Grafica de N vs estimacion de pi")
plt.xlabel("N")
plt.ylabel("Estimacion de pi")
plt.show()
