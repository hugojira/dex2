# autor: Hugo de Jesus Valenzuela Chaparro
# Universidad de Sonora, septiembre-octubre 2019
# Curso Desarrollo Experimental 2
# ************** algoritmo de dinamica browneana: ******************
# PROGRAMA BASICO INICIAL DE DINAMICA BROWNIANA. DE UN SISTEMA
# A CONCENTRACION FINITA; REGIMEN DIFUSIVO; SIN HI. EJEMPLO PARA
# UN SISTEMA DE PARTÍCULAS (COLOIDES) CARGADOS (CASO: GAYLOR)
# MODELO DE POTENCIAL: YUKAWA REPULSIVA (Y)
# UNIIDADES REDUCIDAS: sigma-beta

# **** GLOSARIO:
# ISEED (1,2,3): SEMILLAS PARA GENERACION DE NUMEROS ALEATORIOS
# NS: NUMERO TOTAL DE CONFIGURACIONES
# NENER: CONFIGURACION INICIAL DE TERMALIZACION (EQUILIBRIO)
# DT: TIEMPO DE PASO
# PHI: FRACCION EN VOLUMEN
# DENS: DENSIDAD REDUCIDA
# NPC: NUMERO DE PARTICULAS COLOIDALES
# A Y ZK: PARAMETROS DEL POTENCIAL (YUKAWA, u(r)=A*exp[-z*(r-1)]/r)
# NFREC: FRECUENCIA DE ALMACENAMIENTO DE CONFIGURACIONES
# NFREC2: FRECUENCIA PARA EL CALCULO DE PROPIEDADES DINAMICAS
# SIG: DIAMETRO DE LAS PARTICULAS COLOIDALES (ESCALA)
# BOXL: LONGITUD DE LA ARISTA DE LA CELDA DE SIMULACION
# RCUT: RADIO DE CORTE
# VAR: VARIANZA

# **** SUBRUTINAS Y FUNCIONES QUE DEBERA LLAMAR EL PROGRAMA PRINCIPAL:
# FRZAS: SUBRUTINA PARA EL CALCULO DE LA FUERZA DE INTERACCION DE
# LAS PARTICULAS Y LA ENERGIA DE LA CONFIGURACION.
# GR: SUBRUTINA PARA EL CALCULO DE LA FUNCION DE VAN-HOVE
# WDT: SUBRUTINA PARA EL CALCULO DEL DESPLAZAMIENTO CUADRATICO
# MEDIO Y COEFICIENTE DE DIFUSION DEPENDIENTE DEL TIEMPO
# ZRAN: FUNCION GENERADORA DE NUMEROS ALEATORIOS [0,1]
# AZARG: SUBRUTINA PARA EL CALCULO DE NUMEROS ALEATORIOS CON
#
# DISTRIBUCION GAUSSIANA
#
#**** GENERALIDADES:
# EN ESTE EJERCICIO, SE PARTE DE UNA CONFIGURACION INICIAL
# ALEATORIA SIN TRASLAPES.
# SISTEMA 3 DIMENSIONES


# librerias externas requeridas para que funcione el programa
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
# ----------------------------------------------------------------
# funciones (o subrutinas) locales
from conf_inic_random_3D_sin_traslapes import conf_inic_random_3D_sin_traslapes
from GDR import GDR
#from GDR_test import GDR_test
from fuerzas import fuerzas
# ----------------------------------------------------------------

# ***** Definicion de variables y parametros *****
N = 100 # numero de particulas
NN2 = 100
NN3 = 3500

# ----------------------------- SEMILLA -----------------------------
# semilla a partir de la cual se generaran los numeros aleatorios
np.random.seed(8729414)
# -------------------------------------------------------------------

# *****  Datos de entrada y calculos preliminares *****
PI = (4.0e0)*np.arctan(1.0e0)
NS = 5000
NP = 10
NFREC = 50
NFREC2 = 100
NENER = 200

DT = 0.0004

A = 556.0
ZK = 0.149
A = A*np.exp(ZK)
PHI = 4.4e-4
DENS = 6.0*PHI/PI

AA = 1.0/3.0
BOXL =((1.0*NP)/DENS)**AA
RCUT = BOXL/2.0
VAR = np.sqrt(2.0*DT)

KI = 0
KI2 = 0
SIG = 1.0


# matrices de configuraciones
CX = np.zeros((int(NP), int(NN2)))
CY = np.zeros((int(NP), int(NN2)))
CZ = np.zeros((int(NP), int(NN2)))
CXR = np.zeros((int(NP), int(NN2)))
CYR = np.zeros((int(NP), int(NN2)))
CZR = np.zeros((int(NP), int(NN2)))
# arreglos a utilizar
XR = np.zeros((int(NP), 1))
YR = np.zeros((int(NP), 1))
ZR = np.zeros((int(NP), 1))
fx = np.zeros((int(NP), 1))
fy = np.zeros((int(NP), 1))
fz = np.zeros((int(NP), 1))

# --- imprimir en pantalla ---


# ***** Escribir datos de entrada en un archivo (dataframe) *****

# ********************************************************************
# ******************* arreglos para guardar archivos **********************
ep = np.zeros((int(NS), 2)) # termalizacion de energia potencial
trazadora = np.zeros((int(NS), 2)) # particula trazadora
# *************************************************************************

# ***** Llamar a la configuracion inicial *****
# En este caso es aleatoria tridimensional sin traslapes y con Maria Luisa
X, Y, Z = conf_inic_random_3D_sin_traslapes(NP, DENS, BOXL)
L = 1

# SE CALCULA LA FUERZA SOBRE CADA PARTICULA EN LA CONFIGURACION
# INICIAL Y LA ENERGIA DE LA CONFIGURACION
# CALL FRZAS(L)


# ** GUARDAR configuracion inicial en archivo externo **
nombre_configini = "configini"+ ".csv"
np.savetxt(nombre_configini, np.c_[X,Y,Z], delimiter=",") # guardar csv
# PRUEBA DE GRAFICACION CONF INICIAL
# graficar
ax = plt.axes(projection='3d')
ax.scatter3D(X[:], Y[:], Z[:]) #, cmap = 'Greens')
titulo = str(NP) + " particulas en celca cubica de longitud reducida " + str(BOXL)
plt.title(titulo)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()

# ----------------------------- SEMILLA -----------------------------
# semilla a partir de la cual se generaran los numeros aleatorios
#np.random.seed(8729414)
# -------------------------------------------------------------------

# ***** particula trazadora *****
NPtraza = np.around(np.random.uniform(low = 0, high = 1, size = 1)*float(NP))
if NPtraza == 0:
    NPtraza = 1
else:
    pass
NPtraza = int(NPtraza)
print("la particula trazadora sera:", NPtraza)
    # ********** MOVIMIENTO BROWNIANO **********
# ***** ITERACION SOBRE CONFIGURACIONES Y PARTICULAS *****
i_trazadora = 0 # contador para particula trazadora
for L in range(0, int(NS)):
    for I in range(0, int(NP)):
        # GENERACION DE 3 NUMEROS ALEATORIOS CON DISTRIBUCION GAUSSIANA
        AX = np.random.normal(0, VAR, size = 1)
        AY = np.random.normal(0, VAR, size = 1)
        AZ = np.random.normal(0, VAR, size = 1)

        # A MOVER A LAS PARTICULAS EN BASE A LA ECUACION DE LANGEVIN
        # SOBREAMORTIGUADA,O REGIMEN DIFUSIVO
        # ALGORITMO DE ERMAK PARA EL DESPLAZAMIENTO:
        # Ermak y McCammon, J. Chem. Phys,, Vol. 69, 1352 (1978)

        X[I] = X[I] + fx[I]*DT + VAR*AX
        Y[I] = Y[I] + fy[I]*DT + VAR*AY
        Z[I] = Z[I] + fz[I]*DT + VAR*AZ

        XR[I] = XR[I] + fx[I]*DT + VAR*AX
        YR[I] = YR[I] + fy[I]*DT + VAR*AY
        ZR[I] = ZR[I] + fz[I]*DT + VAR*AZ

        # CONDICIONES PERIODICAS
        X[I] = X[I] - BOXL*np.around(X[I]/BOXL)
        Y[I] = Y[I] - BOXL*np.around(Y[I]/BOXL)
        Z[I] = Z[I] - BOXL*np.around(Z[I]/BOXL)


    # ** Trayectoria de la particula trazadora **
        if I == NP:
            #print("la trazadora x", X[i])
            #print("la trazadora y", Y[i])
            trazadora[i_trazadora, 0] = X[I]
            trazadora[i_trazadora, 1] = Y[I]
            i_trazadora = i_trazadora + 1
        else:
            pass
        #print("particula", I)
        # CONCLUYE EL CICLO DE MOVER A TODAS LAS PARTICULAS DE LA CONFIGURACION

    # DECIDIENDO SI ALMACENAMOS LAS CONFIGURACIONES DE EQUILIBRIO EN
    # LAS MATRICES CX, CY Y CZ PARA EL CALCULO DE LA g(r)
    xmod = L % NFREC
    if xmod == 0 and L > NENER:
        KI = KI + 1
    for k in range(0, int(NP)):
        CX[I, KI - 1] = X[I]
        CY[I, KI - 1] = Y[I]
        CZ[I, KI - 1] = Z[I]
    else:
        pass

    # DECIDIENDO SI ALMACENAMOS LAS CONFIGURACIONES DE EQUILIBRIO EN
    # LAS MATRICES CDX, CDY Y CDZ PARA EL CALCULO DE PROPIEDADES DE
    # AUTODIFUSION W(t) Y D(t)
    xmod = L % NFREC
    if xmod == 0 and L > NENER:
        KI2 = KI2 + 1
    for k in range(0, int(NP)):
        CXR[I, KI2 - 1] = X[I]
        CYR[I, KI2 - 1] = Y[I]
        CZR[I, KI2 - 1] = Z[I]
    else:
        pass

    # AL CALCULO DE LA FUERZA SOBRE CADA PARTICULA EN LA CONFIGURACION GENERADA
    fx, fy, fz, ENPOT = fuerzas(NP, BOXL, RCUT, ZK, A, X, Y, Z)
    ep[L, 0] = L + 1
    ep[L, 1] = ENPOT

    print("congifuracion", L)
    print("la enpot es", ENPOT)
    # CONCLUYE EL CICLO DE LAS CONFIGURACIONES

# AL CALCULO DE PROPIEDADES

# AL CALCULO DE PROPIEDADES
#CALL GDR(CX,CY,CZ,KI)
print("la KI es", KI)
GDR2D = GDR(CX, CY, CZ, DENS, BOXL, KI, NP, NN2, NN3)

plt.plot(GDR2D[:, 0], GDR2D[:, 1], "bo")#, markersize = 1)
tituloGDR = str(int(NP)) + " particulas,celda cuadrada de longitud reducida " + str(BOXL) + " GDR2D"
plt.title(tituloGDR)
plt.xlabel("RT")
plt.ylabel("GDRTA")
plt.show()

#print("las pos son", np.c_[X,Y,Z])
#print("las fuercitas son", np.c_[fx,fy,fz])

#CALL WDT(CXR,CYR,CZR,KI2,DT,NFREC2)


    # ** Verificando si requiere escribir informacion de ejecucion **
    #if int(istep) % int(iprint) == 0:
    #    print("istep, ratio, DRMAX, VN", istep, ratio, DRMAX, VN)
    #else:
    #    pass
    # ** Verificando si debe almacenar configuraciones de equilibrio **
    #if int(istep) % int(isave) == 0 and int(istep) > int(NENER):
    #    KI2 = KI2 + 1
    #    for k in range(0, int(N)):
    #        CX[k, KI2 - 1] = X[k]
    #        CY[k, KI2 - 1] = Y[k]
    #else:
    #    pass

# ** CALCULO de la funcion de distribucion radial **
#GDR2D = GDR_test(CX, CY, DENS, boxL, KI2, N, NN2, NN3)

#plt.plot(GDR2D[:, 0], GDR2D[:, 1], "bo")#, markersize = 1)
#tituloGDR = str(int(N)) + " particulas,celda cuadrada de longitud reducida " + str(boxL) + " GDR2D"
#plt.title(tituloGDR)
#plt.xlabel("RT")
#plt.ylabel("GDRTA")
#plt.show()
# --------------------------------------------------

# ----------------------------------------------------------------------
# ------------------ Escritura archivos externos -----------------------
# ** termalizacion **
#nombre_terma = "termalizacion" + ".csv"
#np.savetxt(nombre_terma, terma, delimiter=",") # guardar csv
# ** particula trazadora **
#nombre_traza = "trazadora" + ".csv"
#np.savetxt(nombre_traza, trazadora, delimiter=",") # guardar csv
# ** configuracion final **
#nombre_confinal = "confinal" + ".csv"
#np.savetxt(nombre_confinal, np.c_[X,Y], delimiter=",") # guardar csv
# ** GDR **
#nombre_confinal = "GDR" + ".csv"
#np.savetxt(nombre_confinal, GDR2D, delimiter=",") # guardar csv
# -----------------------------------------------------------------------

# PRUEBA DE GRAFICACION CONF FINAL
# graficar
#plt.plot(X[:], Y[:], "bo")#, markersize = 1)
#plt.title(titulo)
#plt.xlabel("X")
#plt.ylabel("Y")
#plt.show()
