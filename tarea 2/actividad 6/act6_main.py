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
