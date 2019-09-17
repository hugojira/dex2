# autor: Hugo de Jesus Valenzuela Chaparro
# Universidad de Sonora, septiembre 2019
# Curso Desarrollo Experimental 2
# ************** actividad 1 de la tarea 2: ******************
# Este codigo genera una configuracion inicial aleatoria SIN IMPEDIR traslapes
# SISTEMA: bidimensional de particulas discos
# UNIDADES REDUCIDAS: sigma

# librerias requeridas para que funcione el programa
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------

# dar informacion del programa
print("""Este programa genera una configuracion inicial bidimensional
aleatoria, a partir del numero de particulas y la concentracion reducida
crea la celda en unidades reducidas""")

# pedir datos de entrada
N = input("""Escriba el numero de particulas
""") # numero de particulas
DENS = input("""De la concentracion reducida
""") # concentracion reducida

# ------------------- calculos preliminares ------------------------
# lado reducido de la celca
boxL = ((1.0*float(N))/float(DENS))**(1.0/2.0)
# fraccion en area phit = pi*DENS/4
phit = (float(DENS)*np.pi)/4.0
# el diametro de las particulas
sigma = 1.0
# --------------------------------------------------------------------

# escribir los parametros de corrida en un archivo
print("la concentracion reducida es", DENS)
print("el numero de particulas es", N)
print("el lado reducido de la celca es", boxL)
print("la fraccion en area es", phit)


# arreglos que almacenaran las posiciones
X = np.zeros((int(N), 1))
Y = np.zeros((int(N), 1))


np.random.seed(4958202) # semilla para poder hacer los numeros reproducibles
# generar posiciones
for i in range(0, int(N)):
    #print("la iesima es", i)
    # numeros aleatorios para generar las posiciones
    deltax = np.random.uniform(low = 0, high = 1, size = 1) - 0.5
    deltay = np.random.uniform(low = 0, high = 1, size = 1) - 0.5
    # posiciones
    X[i] = deltax*boxL
    Y[i] = deltay*boxL

#print("las posiciones fueron", np.c_[X,Y])

# graficar
plt.plot(X[:], Y[:], "bo")#, markersize = 1)
titulo = N + " particulas (traslape-on) en celda cuadrada de longitud reducida " + str(boxL)
plt.title(titulo)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# dar opcion de guardar tabla en archivo .csv
choice = input ("""Deseas guardar una tabla (csv) con las posiciones? (si/no)
""")

if choice == "si":
    nombre = "ConcRed_" + DENS + "_particulas_" + N + "_2D" ".csv"
    np.savetxt(nombre, np.c_[X, Y], delimiter=",") # guardar csv
elif choice == "no":
    pass
else:
    print("Escribe 'si' o 'no', sin comillas ni acento")
