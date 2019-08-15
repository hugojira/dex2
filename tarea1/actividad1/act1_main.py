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
# y exportar los datos a un archivo .dat

# librerias requeridas para que funcione el programa
import numpy as np
# llamar a las funciones
from funciones import func_a,func_b,func_c,func_d,func_e,func_f

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
    print("La evaluacion resultante es:", func_a(float(eval)))
elif choice == "b":
    eval = input ("""Elige el valor x0 que deseas evaluar, usando
    valores mayores o iguales 0
    """)
    print("La evaluacion resultante es:", func_b(float(eval)))
elif choice == "c":
    eval = input ("""Elige el valor x0 que deseas evaluar, usando
    valores mayores a -0.5
    """)
    print("La evaluacion resultante es:", func_c(float(eval)))
elif choice == "d":
    eval = input ("""Elige el valor x0 que deseas evaluar
    """)
    print("La evaluacion resultante es:", func_d(float(eval)))
elif choice == "e":
    eval = input ("""Elige el valor x0 que deseas evaluar
    """)
    print("La evaluacion resultante es:", func_e(float(eval)))
elif choice == "f":
    eval = input ("""Elige el valor x0 que deseas evaluar
    """)
    print("La evaluacion resultante es:", func_f(float(eval)))
elif choice == "i love you":
    print("i love you too!")
else:
    print("Por favor, ingresa un dato numerico valido")

# dar opcion para graficar
plot_choice = input ("""Deseas especifizar un intervalo para graficar
la funcion que seleccionaste? (si/no)
""")

if plot_choice == "si":
    pass
elif plot_choice == "no":
    pass
else:
    print("teclea 'si' o 'no', sin las comillas")
