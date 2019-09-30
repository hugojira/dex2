# autor: Hugo de Jesus Valenzuela Chaparro
# Universidad de Sonora, septiembre 2019
# Curso Desarrollo Experimental 2
# ************** algoritmo de metropolis: ******************
# SISTEMA: Sistema bidimensional monodisperso de discos duros (HD)
# UNIIDADES REDUCIDAS: sigma-beta

# librerias externas requeridas para que funcione el programa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# ----------------------------------------------------------------
# funciones (o subrutinas) locales
from conf_inic_random_2D_sin_traslapes import conf_inic_random_2D_sin_traslapes
from energia_configuracion import energia_configuracion
# ----------------------------------------------------------------

# ***** Definicion de variables y parametros *****
N = 100 # numero de particulas

# ***** Pedir datos de entrada *****
# numero total de configuraciones (o microestados)
#Nstep = input ("""Escriba el numero total de configuraciones
#""")
# microestados necesarios para que se llegue al equilibrio
#NENER = input ("""Escriba el numero de configuraciones que pasan hasta
#que se da el equilibrio
#""")
# frecuencia de impresion
#iprint = input ("""Escriba la frecuencia de impresion en pantalla deseada
#""")
# frecuencia de muestreo
#isave = input ("""Escriba la frecuencia de muestreo
#""")
# frecuencia de correccion de paso
#iratio = input ("""Escriba la frecuencia de correccion de paso
#""")
# fraccion de area total que cubren las particulas
phit = input ("""Escriba la fraccion de area total que cubren las particulas
""")

# ***** Maximo desplazamiento por coordenada *****
DRMAX = 0.1

# ***** Calculos preliminares *****
# concentracion reducida DENS = phit*4.0/pi
DENS = (float(phit)*4.0)/np.pi
# lado reducido de la celca
boxL = ((1.0*float(N))/float(DENS))**(1.0/2.0)
# el diametro de las particulas
sigma = 1.0
# --- imprimir en pantalla ---
print("El numero de particulas es:", N)
print("La concentracion reducida es:", DENS)
print("La longitud reducida de la celda es:", boxL)

# ***** Escribir datos de entrada en un archivo (dataframe) *****

# ***** Llamar a la configuracion inicial *****
# En este caso es aleatoria sin traslapes y con Maria Luisa
X, Y = conf_inic_random_2D_sin_traslapes(float(N), float(DENS))

# PRUEBA DE GRAFICACION CONF INICIAL
# graficar
plt.plot(X[:], Y[:], "bo")#, markersize = 1)
titulo = str(N) + " particulas (traslape-off) en celda cuadrada de longitud reducida " + str(boxL)
plt.title(titulo)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# ***** Correccion de largo alcance *****
VCLA = 0.0 # en este caso no hay
# ***** Calculo de la energia de la configuracion inicial *****
V_inicial = energia_configuracion(X, Y, float(N), float(DENS))
print("La energia inicial de la configuracion inicial fue:", V_inicial)

# ----------------------------- SEMILLA -----------------------------
# semilla a partir de la cual se generaran los numeros aleatorios
np.random.seed(8729414)
# -------------------------------------------------------------------

# ***** particula trazadora *****
NP = np.around(np.random.uniform(low = 0, high = 1, size = 1)*float(N))
if NP == 0:
    NP = 1
else:
    pass

# ********** MOVIMIENTO DE LAS PARTICULAS **********
# ***** ITERACION SOBRE CONFIGURACIONES Y PARTICULAS *****
