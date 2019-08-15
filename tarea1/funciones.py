# subrutina para las funciones a evaluar

# librerias requeridas
import numpy as np

# declaracion de las funciones

def func_a(x):
    y = 4.0 - x*x
    return y

def func_b(x):
    y = np.sqrt(x)
    return y

def func_c(x):
    y = np.log(1.0 + 2.0*x)
    return y

def func_d(x):
    y = np.sin(x)
    return y

def func_e(x):
    y = np.exp(((-1.0)*x*x)/2.0)
    return y

def func_f(x):
    y = 1.0/(1.0 + x*x)
    return y
