# autor: Hugo de Jesus Valenzuela Chaparro
# Universidad de Sonora, agosto 2019
# Curso Desarrollo Experimental 2
# ************** actividad 3 de la tarea 1: ******************

# librerias necesarias para que funcione el programa
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------

# ------------------- Descripcion ---------------------------
# programa que distribuye N particulas a lo largo de una
# circunferencia de diametro D. Los parametros N y D son
# pedidos a usuario por pantalla.
# -----------------------------------------------------------


# Informacion a usuario

print("""Este programa distribuye N particulas a lo largo de una cirfuncerencia
de diamedro D""")
# Pedir datos de entrada
D = input ("""Por favor escribe el diametro D de la cirfuncerencia
""")

N = input ("""Da el numero de particulas a distribuir
""")

# para resolver este problema simplemente vamos a dividir el angulo 2*pi
# que forma a la circunferencia, en N partes iguales. Despues a cada pedazo
# de angulo le vamos a calcular las coordenadas x e y, mediante las ecuaciones
# de transformacion
# x = r*cos (theta)
# y = r*cos (theta)

# el radio
radio = float(D)/2.0

# hacemos la division de las N particulas en el angulo 2pi del circulo,
# 2pi no se incluye pues ya esta considerado como 0
angulos = np.linspace(0, 2.0*np.pi ,num = int(N), endpoint = False)

# hacemos las transformaciones  a coordenadas cartesianas
x = radio*np.cos(angulos) # coordenadas x
y = radio*np.sin(angulos) # coordenadas y

# graficar
plt.plot(x,y, "bo")
plt.xlabel("x")
plt.ylabel("y")
plt.title(N + " particulas a lo largo de la circunferencia de diametro " + D)
plt.grid(color='black', linestyle='-', linewidth=0.5, alpha=0.8)
plt.axis("equal")
plt.show()

# dar opcion de guardar tabla en archivo .csv
choice = input ("""Deseas guardar una tabla (csv) con las posiciones? (si/no)
""")

if choice == "si":
    nombre = "diametro_" + D + "_particulas_" + N + ".csv"
    np.savetxt(nombre, np.c_[x,y], delimiter=",") # guardar csv
elif choice == "no":
    pass
else:
    print("Escribe 'si' o 'no', sin comillas ni acento")
# imprimir la tabla en pantalla
print("las posiciones fueron", np.c_[x,y])
