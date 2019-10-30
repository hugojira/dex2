
# librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import genfromtxt
# lectura de datos
GDR2D = genfromtxt('GDR.csv', delimiter=',')
# graficacion
plt.plot(GDR2D[:, 0], GDR2D[:, 1])#, markersize = 1)
titulo = "GDR 400 particulas, 1200 ciclos"
plt.title(titulo)
plt.xlabel("RT")
plt.ylabel("GDRTA")
plt.show()
