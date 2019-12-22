# autor: Hugo de Jesus Valenzuela Chaparro
# curso desarrollo experimental 2
# Universidad de Sonora, agosto 2019

# este programa sirve para evaluar funciones, preguntando al usuario
# el valor de x a evaluar, las funciones son
# --------------------------------------------------------
# a) 4 - x^2
# b) x^(1/2)
# c) ln(1 +2x)
# d) Sen(x)
# e) exp((-x^2)/2)
# f) 1/(1+x^2)
# --------------------------------------------------------
# posteriormente se da la opcion de graficar en un intervalo dado
# y exportar los datos a un archivo .csv con la etiqueta de la funcion
# seleccionada

# librerias requeridas para que funcione el programa
import numpy as np
# llamar a las funciones (subrutinas)
from funciones import func_a,func_b,func_c,func_d,func_e,func_f
from graficar import graficar
# mensaje a usuario
print("""
Este programa te sirve para evaluar una de las siguientes funciones:

a) 4 - x^2
b) x^(1/2)
c) ln(1 +2x)
d) Sen(x)
e) exp((-x^2)/2)
f) 1/(1+x^2)
""")

#test = func_f(2)
#print("la prueba es", test)

# leer entrada de eleccion
choice = input ("""
Por favor elige una tecleando la letra (minuscula) que le corresponda:

""")


# condicionales para evaluar las funciones
if choice == "a":
    eval = input ("""Elige el valor x0 que deseas evaluar
    """)
    func_aux = func_a
    print("La evaluacion resultante es:", func_aux(float(eval)))
elif choice == "b":
    eval = input ("""Elige el valor x0 que deseas evaluar, usando
    valores mayores o iguales 0
    """)
    func_aux = func_b
    print("La evaluacion resultante es:", func_aux(float(eval)))
elif choice == "c":
    eval = input ("""Elige el valor x0 que deseas evaluar, usando
    valores mayores a -0.5
    """)
    func_aux = func_c
    print("La evaluacion resultante es:", func_aux(float(eval)))
elif choice == "d":
    eval = input ("""Elige el valor x0 que deseas evaluar
    """)
    func_aux = func_d
    print("La evaluacion resultante es:", func_aux(float(eval)))
elif choice == "e":
    eval = input ("""Elige el valor x0 que deseas evaluar
    """)
    func_aux = func_e
    print("La evaluacion resultante es:", func_aux(float(eval)))
elif choice == "f":
    eval = input ("""Elige el valor x0 que deseas evaluar
    """)
    func_aux = func_f
    print("La evaluacion resultante es:", func_aux(float(eval)))
elif choice == "i love you":
    print("i love you too!")
    exit()
else:
    print("Por favor, ingresa una opcion valida")
    exit()

# dar opcion para graficar y guardar los datos en csv
plot_choice = input ("""Deseas especificar un intervalo para graficar
la funcion que seleccionaste (adicionalmente se exportaran las evaluaciones
en un archivo csv)? (si/no)
""")

if plot_choice == "si":
    cota_inf = input ("Ingresa la cota inferior del intervalo")
    cota_sup = input ("Ingresa la cota superior del intervalo")
    a, b = float(cota_inf), float(cota_sup)
    graficar(a, b, func_aux, choice) #llamar funcion graficadora/exportadora
elif plot_choice == "no":
        pass
else:
    print("teclea 'si' o 'no', sin las comillas")
