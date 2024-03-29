# autor: Hugo de Jesus Valenzuela Chaparro
# Universidad de Sonora, septiembre-octubre-diciembre 2019
# Curso Desarrollo Experimental 2
# ************** algoritmo de metropolis: ******************
# SISTEMA: Sistema tridimensional monodisperso de esferas duras (HS)
# UNIIDADES REDUCIDAS: sigma-beta

# librerias externas requeridas para que funcione el programa
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
# ----------------------------------------------------------------
# funciones (o subrutinas) locales
from conf_inic_random_3D_sin_traslapes import conf_inic_random_3D_sin_traslapes
from conf_inic_random_3D_con_traslapes import conf_inic_random_3D_con_traslapes
from energia_configuracion import energia_configuracion
from energia_particula_i import energia_particula_i
from GDR import GDR
# ----------------------------------------------------------------

# ***** Definicion de variables y parametros *****
N = 100 # numero de particulas
NN2 = 20000
NN3 = 3500
# matrices de configuraciones
CX = np.zeros((int(N), int(NN2)))
CY = np.zeros((int(N), int(NN2)))
CZ = np.zeros((int(N), int(NN2)))


# ***** Pedir datos de entrada *****
# numero total de configuraciones (o microestados)
nstep = input ("""Escriba el numero total de configuraciones
""")
# microestados necesarios para que se llegue al equilibrio
NENER = input ("""Escriba el numero de configuraciones que pasan hasta
que se da el equilibrio
""")
# frecuencia de impresion
iprint = input ("""Escriba la frecuencia de impresion en pantalla deseada
""")
# frecuencia de muestreo
isave = input ("""Escriba la frecuencia de muestreo
""")
# frecuencia de correccion de paso
iratio = input ("""Escriba la frecuencia de correccion de paso
""")
# razon de aceptacion standard 0.5
razon = input ("""Escriba la razon de aceptacion standard 0.5
""")
# fraccion de area total que cubren las particulas
phit = input ("""Escriba la fraccion de area total que cubren las particulas
""")

# ***** Maximo desplazamiento por coordenada *****
DRMAX = 0.1

# ***** Calculos preliminares *****
# concentracion reducida DENS = phit*4.0/pi
DENS = (float(phit)*6.0)/np.pi
# lado reducido de la celca
boxL = ((1.0*float(N))/float(DENS))**(1.0/3.0)
# el diametro de las particulas
sigma = 1.0
Rcut = boxL/2.0
KI2 = 0
ACATMA = 0.0
ACM = 0.0

# --- imprimir en pantalla ---
print("El numero de particulas es:", N)
print("La concentracion reducida es:", DENS)
print("La fraccion en area total es:", phit)
print("La longitud reducida de la celda es:", boxL)
print("Frecuencia de impresion:", iprint)
print("Frecuencia de muestreo", isave)
print("Frecuencia de correccion de paso", iratio)

# ***** Escribir datos de entrada en un archivo (dataframe) *****

# ********************************************************************
# ******************* arreglos para guardar archivos **********************
terma = np.zeros((int(nstep), 2)) # termalizacion
trazadora = np.zeros((int(nstep), 3)) # particula trazadora
# *************************************************************************

# ***** Llamar a la configuracion inicial *****
# En este caso es aleatoria sin traslapes y con Maria Luisa, o bidimensional
# regular cuadrada con Maria Luisa
choice = input ("""Eliga congifuracion aleatoria sin traslapes (1), 0 con traslapes (2)""")
if int(choice) == 1:
    X, Y, Z = conf_inic_random_3D_sin_traslapes(float(N), float(DENS), float(boxL))
elif int(choice) == 2:
    X, Y, Z = conf_inic_random_3D_con_traslapes(float(N), float(DENS), float(boxL))
else:
    print("Asegurese de escribir bien, se eligio por default la opcion (1)")
    X, Y, Z= conf_inic_random_3D_sin_traslapes(float(N), float(DENS), float(boxL))
# ** GUARDAR configuracion inicial en archivo externo **
nombre_configini = "configini"+ ".csv"
np.savetxt(nombre_configini, np.c_[X,Y,Z], delimiter=",") # guardar csv
# PRUEBA DE GRAFICACION CONF INICIAL
# graficar
ax = plt.axes(projection='3d')
ax.scatter3D(X[:], Y[:], Z[:]) #, cmap = 'Greens')
titulo = str(N) + " particulas en celda cubica de longitud reducida " + str(boxL)
plt.title(titulo)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()

# ***** Correccion de largo alcance *****
Vlrc = 0.0 # en este caso no hay
# ***** Calculo de la energia de la configuracion inicial *****
V = energia_configuracion(X, Y, Z, int(N), boxL, Rcut)
V_inicial = V + Vlrc
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
NP = int(NP)
print("la particula trazadora sera:", NP)
# ********** MOVIMIENTO DE LAS PARTICULAS **********
# ***** ITERACION SOBRE CONFIGURACIONES Y PARTICULAS *****
i_trazadora = 0 # contador para particula trazadora
for istep in range(0, int(nstep)):
    for i in range(0, int(N)):
        # posiciones viejas
        rxiOLD = X[i]
        ryiOLD = Y[i]
        rziOLD = Z[i]
        # *** ENERGIA DE LA i-ESIMA PARTICULA EN CONFIGURACION vieja ***
        VOLD = energia_particula_i(rxiOLD, ryiOLD, rziOLD, i, X, Y, Z, int(N), boxL, Rcut)
        # ************************************************************
        # *******     Movimiento arbitrario aleatorio      *******
        # ************************************************************
        rxiNEW = rxiOLD + (2.0*np.random.uniform(low = 0, high = 1, size = 1) - 1.0)*DRMAX
        ryiNEW = ryiOLD + (2.0*np.random.uniform(low = 0, high = 1, size = 1) - 1.0)*DRMAX
        rziNEW = rziOLD + (2.0*np.random.uniform(low = 0, high = 1, size = 1) - 1.0)*DRMAX
        # *************************************************************
        # ** Incluyendo condiciones periodicas **
        rxiNEW = rxiNEW - boxL*np.around(rxiNEW/boxL)
        ryiNEW = ryiNEW - boxL*np.around(ryiNEW/boxL)
        rziNEW = rziNEW - boxL*np.around(rziNEW/boxL)
        # *** ENERGIA DE LA i-ESIMA PARTICULA EN CONFIGURACION nueva ***
        VNEW = energia_particula_i(rxiNEW, ryiNEW, rziNEW, i, X, Y, Z, int(N), boxL, Rcut)
        # ***************************************************************
        # ******** ALGORITMO: Criterios de aceptacion o rechazo ********
        deltaV = VNEW - VOLD
        #print("deltaV", deltaV)
        if deltaV < 75.0:
            if deltaV < 0.0:
                V = V + deltaV
                #print("potencial menor a cero", V)
                X[i] = rxiNEW
                Y[i] = ryiNEW
                ACATMA = ACATMA + 1.0
            elif np.exp((-1.0)*deltaV) > np.random.uniform(low = 0, high = 1, size = 1):
                V = V + deltaV
                #print("potencial mayor a bolztman", V)
                X[i] = rxiNEW
                Y[i] = ryiNEW
                Z[i] = rziNEW
                ACATMA = ACATMA + 1.0
            else:
                pass
        else:
            ACM = ACM + 1.0
        # ***************************************************************

    # ** Trayectoria de la particula trazadora **
        if i == NP:
            #print("la trazadora x", X[i])
            #print("la trazadora y", Y[i])
            trazadora[i_trazadora, 0] = X[i]
            trazadora[i_trazadora, 1] = Y[i]
            trazadora[i_trazadora, 2] = Z[i]
            i_trazadora = i_trazadora + 1
        else:
            pass
    # ** Guardando energia/particula de la configuracion (termalizacion) *
    VN = (V + Vlrc)/float(N)
    terma[istep, 0] = istep + 1
    terma[istep, 1] = VN

    # ** Verificando si ajusta el desplazamiento DRMAX **
    if int(istep) % int(iratio) == 0:
        ratio = ACATMA/float(float(N)*float(iratio))

        if ratio > float(razon):
            DRMAX = DRMAX*1.05
        else:
            DRMAX = DRMAX*0.95
        ACATMA = 0.0
    else:
        pass
    # ** Verificando si requiere escribir informacion de ejecucion **
    if int(istep) % int(iprint) == 0:
        print("istep, ratio, DRMAX, VN", istep, ratio, DRMAX, VN)
    else:
        pass
    # ** Verificando si debe almacenar configuraciones de equilibrio **
    if int(istep) % int(isave) == 0 and int(istep) > int(NENER):
        KI2 = KI2 + 1
        for k in range(0, int(N)):
            CX[k, KI2 - 1] = X[k]
            CY[k, KI2 - 1] = Y[k]
            CZ[k, KI2 - 1] = Z[k]
    else:
        pass

# ** CALCULO de la funcion de distribucion radial **
GDR3D = GDR(CX, CY, CZ, DENS, boxL, KI2, N, NN2, NN3)

plt.plot(GDR3D[:, 0], GDR3D[:, 1], "bo")#, markersize = 1)
tituloGDR = str(int(N)) + " particulas,celda cubica de longitud reducida " + str(boxL) + " GDR2D"
plt.title(tituloGDR)
plt.xlabel("RT")
plt.ylabel("GDRTA")
plt.show()
# --------------------------------------------------

# ----------------------------------------------------------------------
# ------------------ Escritura archivos externos -----------------------
# ** termalizacion **
nombre_terma = "termalizacion" + ".csv"
np.savetxt(nombre_terma, terma, delimiter=",") # guardar csv
# ** particula trazadora **
nombre_traza = "trazadora" + ".csv"
np.savetxt(nombre_traza, trazadora, delimiter=",") # guardar csv
# ** configuracion final **
nombre_confinal = "confinal" + ".csv"
np.savetxt(nombre_confinal, np.c_[X,Y,Z], delimiter=",") # guardar csv
# ** GDR **
nombre_confinal = "GDR" + ".csv"
np.savetxt(nombre_confinal, GDR3D, delimiter=",") # guardar csv
# -----------------------------------------------------------------------

# PRUEBA DE GRAFICACION CONF FINAL
# graficar
ax = plt.axes(projection='3d')
ax.scatter3D(X[:], Y[:], Z[:]) #, cmap = 'Greens')
titulo = str(N) + " particulas en celda cubica de longitud reducida " + str(boxL)
plt.title(titulo)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
