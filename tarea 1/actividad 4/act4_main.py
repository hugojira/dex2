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

# dar informacion sobre el programa
print("""Este programa crea un arreglo cuadrado de N^2 particulas en una
celca cuadrada de lado L.
""")

# pedir datos de entrada
L = input("""Introduce la longitud L de lado de la celca cuadrada
a crearse
""")

N = input("""Da el numero N a distribuir. Recuerda que el numero total de
particulas que habra distribuidas equitativamente sera N^2, para tener un
acomodo cuadrado perfecto.
""")

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


# separacion de las particulas, es L/(n-1)
dL = float(L)/(float(N) - 1.0)
# total de particulas que llenaran la celda cuadrada
total_particulas = (int(N))**2

# arreglo dimension Ntotal x 2 que servira para almacenar posiciones x, y
# de todas las particulas
pos = np.zeros((total_particulas, 2))

# ciclos anidados para llenar la cuadricula
for i in range(0, int(N)):
    x_temp = float(L) - float(i)*dL # coordenada x
    contador_auxiliar = (i)*int(N)
    for j in range(0, int(N)):
        contador_final = contador_auxiliar + j
        y_temp = float(L) - float(j)*dL # coordenada y
        pos[contador_final, 0] = x_temp # almacenar coord x en arreglo
        pos[contador_final, 1] = y_temp # almacenar coord y en arreglo


# trasladar el centro de la celda al origen (0,0)
pos[:,0] = pos[:,0] - float(L)/2.0
pos[:,1] = pos[:,1] - float(L)/2.0

# realizar la grafica de la celda centrada en el origen
plt.plot(pos[:,0], pos[:,1], "bo")
titulo = str(total_particulas) + " particulas en una celda de lado " + L + " centrada en el origen"
plt.title(titulo)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# dar opcion de guardar tabla en archivo .csv
choice = input ("""Deseas guardar una tabla (csv) con las posiciones? (si/no)
""")

if choice == "si":
    nombre = "lado_" + L + "_particulas_" + str(total_particulas) + ".csv"
    np.savetxt(nombre, pos, delimiter=",") # guardar csv
elif choice == "no":
    pass
else:
    print("Escribe 'si' o 'no', sin comillas ni acento")

# imprimir la tabla en pantalla
print("las posiciones fueron", pos)
