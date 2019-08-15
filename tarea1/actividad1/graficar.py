# subrutina para realizar graficacion de la funcion seleccionada
# dentro de un rango especificado

#librerias requeridas
import matplotlib.pyplot as plt
import numpy as np

# funcion que nos servira como subrutina para graficar
# al usuario se le pide la cota inferior "a" y la cota
# superior "b"

def graficar(a,b,funcion):
    # crear intervalo de graficacion
    x = np.arange(a, b, 0.1)
    # realizar correspondiente evaluacion en el intervalo
    y = funcion(x)
    # graficar
    plt.plot(x, y)
    # mostrar grafica en pantalla
    plt.show()
