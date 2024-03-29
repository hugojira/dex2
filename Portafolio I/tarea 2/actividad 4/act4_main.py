# autor: Hugo de Jesus Valenzuela Chaparro
# Universidad de Sonora, septiembre 2019
# Curso Desarrollo Experimental 2
# ************** actividad 4 de la tarea 2: ******************
# Este programa crea un arreglo cubico de N^3 particulas en una
# celca cubica de longitud reducida boxL. Los datos DENS (concentracion reducida)
# y N son dados por usuario en pantalla. Cabe destacar que el numero de particulas
# siempre sera N^3, esto para que quede un arreglo cubico perfecto.

# librerias necesarias para que funcione el programa
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
# --------------------------------------------------

# dar informacion sobre el programa
print("""Este programa crea un arreglo cubico de N^3 particulas en una
celca cubica de lado L.
""")

# pedir datos de entrada
N = input("""Da el numero N a distribuir. Recuerda que el numero total de
particulas que habra distribuidas equidistantemente sera N^3, para tener un
acomodo cubico perfecto.
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

# imprimir los parametros de corrida
print("la concentracion reducida es", DENS)
print("el numero de particulas es", N)
print("el lado reducido de la celca es", boxL)
print("la fraccion en area es", phit)


# ------- caso de una sola particula, se pone en el origen -------
if int(N) == 1:
    pos = np.zeros((1, 3))
    ax = plt.axes(projection='3d')
    ax.scatter3D(pos[0,0], pos[0,1], pos[0,2]) #, cmap = 'Greens')
    titulo = "1" + " particula en celca cubica de longitud reducida " + str(boxL)
    plt.title(titulo)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()
    print(pos)
    exit()
else:
    pass
# -----------------------------------------------------------


# separacion de las particulas, es L/(n-1)
dL = float(boxL)/(float(N) - 1.0)
# total de particulas que llenaran la celda cubica
total_particulas = (int(N))**3

# arreglo dimension Ntotal x 2 que servira para almacenar posiciones x, y
# de todas las particulas
pos = np.zeros((total_particulas, 3))

# ciclos anidados para llenar el cubo
for i in range(0, int(N)):
    x_temp = float(boxL) - float(i)*dL # coordenada x
    contador_aux1 = (i)*(int(N))*(int(N))
    for j in range(0, int(N)):
        contador_aux2 = (j)*int(N) + contador_aux1
        y_temp = float(boxL) - float(j)*dL # coordenada y
        for k in range(0, int(N)):
            contador_final = contador_aux2 + k
            z_temp = float(boxL) - float(k)*dL # coordenada z
            pos[contador_final, 0] = x_temp # almacenar coord x en arreglo
            pos[contador_final, 1] = y_temp # almacenar coord y en arreglo
            pos[contador_final, 2] = z_temp # almacenar coord z en arreglo
            #ax = plt.axes(projection='3d')
            #ax.scatter3D(pos[:,0], pos[:,1], pos[:,2]) #, cmap = 'Greens')
            #titulo = str(contador_final+1) + " particulas en celca cubica de longitud " + str(L)
            #plt.title(titulo)
            #ax.set_xlabel("X")
            #ax.set_ylabel("Y")
            #ax.set_zlabel("Z")
            #plt.show()

# trasladar el centro de la celda al origen (0,0)
pos[:,0] = pos[:,0] - float(boxL)/2.0 # coordenadas x
pos[:,1] = pos[:,1] - float(boxL)/2.0 # coordenadas y
pos[:,2] = pos[:,2] - float(boxL)/2.0 # coordenadas z

# realizar la grafica de la celda centrada en el origen
ax = plt.axes(projection='3d')
ax.scatter3D(pos[:,0], pos[:,1], pos[:,2]) #, cmap = 'Greens')
titulo = str(total_particulas) + " particulas en celca cubica de longitud reducida " + str(boxL)
plt.title(titulo)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()

# dar opcion de guardar tabla en archivo .csv
choice = input ("""Deseas guardar una tabla (csv) con las posiciones? (si/no)
""")

if choice == "si":
    nombre = "ConcRed_" + DENS + "_particulas_" + str(total_particulas) + ".csv"
    np.savetxt(nombre, pos, delimiter=",") # guardar csv
elif choice == "no":
    pass
else:
    print("Escribe 'si' o 'no', sin comillas ni acento")

# imprimir la tabla en pantalla
print("las posiciones fueron", pos)
