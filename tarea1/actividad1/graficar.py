# subrutina para realizar graficacion de la funcion seleccionada
# dentro de un rango especificado, ademas exporta los datos
# en un archivo csv con el nombre de la funcion evaluada

#librerias requeridas
import matplotlib.pyplot as plt
import numpy as np

# funcion que nos servira como subrutina para graficar,
# al usuario se le pide la cota inferior "a" y la cota
# superior "b". Ademas se tiene como argumentos "funcion" a
# la funcion misma que se va a evaluar y la "etiqueta"
# para exportar los datos

def graficar(a,b,funcion,etiqueta):
    # crear intervalo de graficacion
    x = np.arange(a, b, 0.05)
    # realizar correspondiente evaluacion en el intervalo
    y = funcion(x)
    # escribir nombre de archivo y exportar .csv
    nombre = "funcion_" + etiqueta + ".csv"
    np.savetxt(nombre, np.c_[x,y], delimiter=",")
    # graficar
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    # mostrar grafica en pantalla
    plt.show()
