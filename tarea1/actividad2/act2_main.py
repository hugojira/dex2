# autor: Hugo de Jesus Valenzuela Chaparro
# Universidad de Sonora, agosto 2019
# Curso Desarrollo Experimental 2
# ************** actividad 2 de la tarea 1: ******************
# Este programa crea N puntos (particulas) a lo largo de una recta de
# longitud L y los distribuye equidistantemente, luego, las particulas
# etiquetadas con numero par las coloca a la derecha del origen, y las de
# numero impar a la izquierda.
# el origen se considera en el centro de la recta, (N, L) son datos que
# se piden al usuario por medio de pantalla.

# librerias necesarias para que funcione el programa
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------

# dar informacion sobre el programa

print ("""Este programa distribuye equitativamente N particulas puntuales
en una recta de longitud L, con el origen en el centro de la recta,
ademas pondrá los puntos con etiquetas par a la derecha del origen
y los etiquetados con impar a la izquierda
""")

# leer datos de entrada

L = input ("""Da la longitud L de la recta
""") # longitud de la recta
N = input ("""Escribe el numero de particulas puntuales a distribuir
sobre la recta
""") # numero de particulas a distribuir

print("la longitud es", L)
print("el numero de particulas es", N)

# cada vez que se distribuyen equitativamente N puntos sobre la recta,
# se hacen N-1 divisiones iguales, entonces dividimos la recta en N-1
# partes iguales lo que nos servira para ir separando las particulas.
# Excepto para N=1, en ese caso la particula solo quedara en el origen
step = float(L)/(float(N)-1.0)

# si el numero de particulas es 1, N=1, simplemente es una particula
# en el origen
if int(N) == 1:
    pass
# para N mayor o igual a 2:
# hacemos un loop sobre las N particulas para asignarle sus respectivas
# posiciones. Se iran  recorriendo hacia L/2 o -L/2
# dependiendo de la paridad, despues se iran seguiran distribuyendo
# acercandose al origen a pasos de L/(N-1), (step), hasta terminar
 # el loop sobre N. Para numero de particulas impares la particula 1 siempre
 # estara en 0 (el origen) por acuerdo.




posiciones = np.zeros((int(N), 2), dtype = object) # crear arreglo (N,2)

# variables auxuliares que serviran para empezar a las particulas en los
# extremos de la cuerda y luego irlas recorriendo al origen con "step"
aux_par = float(L)/2.0
aux_impar = -float(L)/2.0


if int(N)%2==0:# *** acomodo para el caso de numero de particulas N par ***
    for i in range(int(N)):
        if (i+1)%2==0: # particula con etiqueta par
            posiciones[i, 0] = int(i + 1) # etiqueta de la particula
            posiciones[i, 1] = aux_par # posicion de la particula
            #restar step para recorrer al origen
            aux_par = aux_par - step
        else: # particula con etiqueta impar
            posiciones[i, 0] = int(i + 1) # etiqueta de la particula
            posiciones[i, 1] = aux_impar # posicion de la particula
            #sumar step para recorrer al origen
            aux_impar = aux_impar + step

else: # *** acomodo para el caso de numero de particulas N impar ***
    for i in range(int(N)):
        print(i)
        if (i+1)==1: # particula con etiqueta 1 va al origen
            posiciones[i, 0] = int(i + 1) # etiqueta de la particula
            posiciones[i, 1] = 0.0 # posicion de la particula
        elif (i+1)%2==0:  # particula con etiqueta par
            posiciones[i, 0] = int(i + 1) # etiqueta de la particula
            posiciones[i, 1] = aux_par # posicion de la particula
            #restar step para recorrer al origen
            aux_par = aux_par - step
        else: # particula con etiqueta impar
            posiciones[i, 0] = int(i + 1) # etiqueta de la particula
            posiciones[i, 1] = aux_impar # posicion de la particula
            #sumar step para recorrer al origen
            aux_impar = aux_impar + step

# imprimir en pantalla las posiciones
print(posiciones)
print(type(posiciones))
print(type(step))

# ***** graficacion de los resultados *****
# coordenada x
x = posiciones[:,1]
# coordenada y (todas en cero pues estan sobre la recta en eje x)
y = np.zeros(int(N), dtype = float)
# etiquetas de paridad, declaramos arreglo y luego lo llenamos
etiquetas = np.full(int(N), "vacio" ,dtype = np.dtype('U100')) # arreglo
for j in range(int(N)):
    if (j+1)%2==0:
        etiquetas[j] = "par"
    else:
        etiquetas[j] = "impar"
    print(etiquetas[j])



# colores asignados, pares seran azules e impares rojos
cdict = {"impar": "red", "par": "blue"}
# realizar la grafica
fig, ax = plt.subplots()
for g in np.unique(etiquetas):
    ix = np.where(etiquetas == g)
    ax.scatter(x[ix], y[ix], c = cdict[g], label = g, s = 100)
ax.legend()
ax.set_title("{} particulas a lo largo de la recta de longitud {}".format(N,L))
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(color='black', linestyle='-', linewidth=0.5, alpha=0.8)
plt.show() # dar grafica en pantalla

print(np.where(etiquetas=="par"))


print(x)
print(y)
print(etiquetas)
print(type(etiquetas))
