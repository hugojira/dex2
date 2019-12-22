!DESARROLLO EXPERIMENTAL II
!SIMULACION DE DINAMICA BROWNIANA

PROGRAM DB0
  IMPLICIT NONE

  REAL:: DENS,DT,PI,BOXL,RCUT,VAR,A,ZK
  REAL(KIND=8)::AX,AY,AZ,ENPOT,TIME,WT,DIF
  REAL::A1S,A2S,HSTAR,HCUT,PHIT
  REAL,ALLOCATABLE::X(:),Y(:),Z(:),FX(:),FY(:),FZ(:),XR(:),YR(:),ZR(:)
  REAL,ALLOCATABLE::CX(:,:),CY(:,:),CZ(:,:),CXR(:,:),CYR(:,:),CZR(:,:)
  INTEGER::NP,NN2,N,ISTEP
  REAL:: PT,RAZON,PHI,AA,SIG
  REAL:: SEED,SEED1,SEED2,SEED3,SEED4,SEED5
  INTEGER::NSTEP,NENER,ISAVE1,ISAVE2,IPRINT,TYPE,JCI,NN1
  INTEGER::I,J,K,L
  INTEGER:: KI,KI2,OUT
 
  !Abrir archivos para guardar datos
 !OPEN(10,FILE='1Info.txt',STATUS='unknown')
  OPEN(11,FILE='2conffin.txt',STATUS='unknown')
  OPEN(12,FILE='3termalizacion.txt',STATUS='unknown')
  OPEN(13,FILE='4trazadora.txt',STATUS='unknown')
   OPEN(16,FILE='4GDR.txt',STATUS='unknown')
   OPEN(17,FILE='5PRS.txt',STATUS='unknown')
    OPEN(18,FILE='08WDT.txt',STATUS='unknown')
  
  !LEXTURA DE DATOS DE ENTRADA
 ! WRITE(*,*)'Simulacion de dinamica brownina con 800 particulas con modelo
! de potencial:Yukawa Repulsiva.'
 ! WRITE(*,*)'Introduzca el numero de particulas (N)'
 !READ(*,*)NP
  !WRITE(*,*)'Introduzca el numero total de configuraciones (NSTEP)'
  !READ(*,*)NSTEP
  !WRITE(*,*)'Numero de ciclos de termalizacion (NENER)'
  !READ(*,*) NENER
!  WRITE(*,*)'Frecuencia de impresion (IPRINT)'
 ! READ(*,*)IPRINT
  !WRITE(*,*)'Frecuencia de almacenamiento (ISAVE1)'
  !READ(*,*)ISAVE1
  !WRITE(*,*)'Frecuencia de almacenamiento para el calculo de W(t) (ISAVE2)'
  !READ(*,*)ISAVE2
  !WRITE(*,*)'Tiempo de paso (DT)'
  !READ(*,*)DT
  !WRITE(*,*)'Razon de aceptacion standard 0.5'
  !READ(*,*)RAZON
  !WRITE(*,*)'Fraccion en area'
  !READ(*,*)PHIT
  
  !DATOS DE ENTRADA Y CALCULOS PRELIMINARES
   PI=3.1415927
   !NSTEP=415000
   !NENER=15000
   NSTEP=4000
   NENER=500
  N =400
  NN2=4000
  NN1=810
  IPRINT=100
  ISAVE1=100
  ISAVE2=100
  DT=0.0004 !PARA EL SISTEMA DE GAYLOR
  !VALORES DE GAYLOR
  A=556.D0
  ZK=0.149D0
  A=A*EXP(ZK)
  PHI=4.4D-4
  DENS=6.D0*PHI/PI
  
  NN2=1000 !tamaño del ensemble
 
!Asignando dimensiones
  allocate(X(N))
  allocate(Y(N))
  allocate(Z(N))
  allocate(XR(N))
  allocate(YR(N))
  allocate(ZR(N))
  allocate(FX(N))
  allocate(FY(N))
  allocate(FZ(N))
  allocate(CX(N,NN2))
  allocate(CY(N,NN2))
  allocate(CZ(N,NN2))
  allocate(CXR(N,NN2))
  allocate(CYR(N,NN2))
  allocate(CZR(N,NN2))

!Calculos preliminares
  AA=1.0/3.0
  BOXL=((1.0*N/DENS)**AA)
  RCUT=BOXL/2.0D0
  VAR=SQRT(2.D0*DT)

  KI=0
  KI2=0
  SIG=1.D0 !DIAMETRO

!Escribir datos de entrada en formato de salida
  WRITE(*,*)"NUMERO DE PARTICULAS",N
  WRITE(*,*)"NUMERO DE CONFIGURACIONES TOTALES",NSTEP
  WRITE(*,*)"FRECUENCIA DE IMPRESION",IPRINT
  WRITE(*,*)"RECUENCIA DE MUESTREO",ISAVE1
  WRITE(*,*)"TIEMPO DE PASO",DT
  WRITE(*,*)"FRACCION EN EL AREA TOTAL",PHIT
  WRITE(*,*)"LONGITUD DE LA CELDA",BOXL
 ! WRITE(*,*)'CONFIGURACION INICIAL: ALEATORIA (0) O REGULAR CUADRADA (1)'
 ! READ(*,*)JCI

 ! IF(JCI==0)THEN
     
!CONFIGURACION INICIAL ALEATORIA SIN TRASLAPES
     CALL CONFIGINI(N,BOXL,X,Y,Z)
  !END IF
  L=1
 CALL FUERZAS(L, N, BOXL, X, Y, Z, FX, FY, FZ, A, ZK, ENPOT)
!Mover a las particulas

 Call random_number(SEED3)
  
  PT=NINT((SEED3)*N)
  IF(PT==0)THEN
     PT=1
  END IF
  WRITE(*,*)'La particula trazadra sera:',PT

!CONSTRUCCION DE CONFIGURACIONES
  DO 20  L=1,NSTEP
     DO 25 I=1,N
  Call random_number(SEED)
  Call random_number(SEED1)
  Call random_number(SEED2)
  Call random_number(SEED4)

Call AZARG(SEED1,AX)
Call AZARG(SEED2,AY)
Call AZARG(SEED4,AZ)

  

  !ALGORITMO DE ERMAK
  X(I)=X(I)+FX(I)*DT+VAR*AX
  Y(I)=Y(I)+FY(I)*DT+VAR*AY
  Z(I)=Z(I)+FZ(I)*DT+VAR*AZ

  XR(I)=XR(I)+FX(I)*DT+VAR*AX
  YR(I)=YR(I)+FY(I)*DT+VAR*AY
  ZR(I)=ZR(I)+FZ(I)*DT+VAR*AZ

  !CONDICIONES PERIODICAS
  X(I)=X(I)-BOXL*ANINT(X(I)/BOXL)
  Y(I)=Y(I)-BOXL*ANINT(Y(I)/BOXL)
  Z(I)=Z(I)-BOXL*ANINT(Z(I)/BOXL)
  !CONCLUYE EL CICLO DE MOVER A TODAS LAS PARTICULAS DE LA CONFIGURACION
  !SEGUIR A LA PARTICULA TRAZADORA
  IF(I==PT) THEN
     WRITE(13,*)X(I),Y(I),Z(I)
  END IF
  
  
25 CONTINUE
   !VERIFICAR SI ESCRIBIMOS INFO DE EJECUCION EN PANTALLA
  IF(MOD(L,IPRINT)==0)THEN
     WRITE(*,*)L
  END IF

!************************************************************************
  !DECIDIENDO SI ALMACENAMOS LAS CONF DE EQUILIBRIO EN LAS MATRICES CX,CY,CZ
  !PARA EL CALCULO DE LA G(R)
  IF(MOD(L,ISAVE1)==0.AND.L>NENER) THEN !OJO LYR: CAMBIAR "L" POR "ISTEP"
     KI=KI+1
     DO I=1,N
        CX(I,KI)=X(I)
        CY(I,KI)=Y(I)
        CZ(I,KI)=Z(I)
     END DO
  END IF
!**************************************************************************
  ! DECIDIENDO SI ALMACENAMOS LA CONFIGURACION CONF DE EQUILIBRIO CXR,CYR,CZR
  !PARA EL CALCULO DE W(T) Y D(T)
  IF(MOD(L,ISAVE2)==0.AND.L>NENER) THEN !OJO LYR: CAMBIAR "L" POR "ISTEP"
     KI2=KI2+1
     DO I=1,N
        CXR(I,KI2)=XR(I)
        CYR(I,KI2)=YR(I)
        CZR(I,KI2)=ZR(I)
     END DO
  END IF
 !**************************************************************       
  !CALCULO DE LA FUERZA Y ENERGIA POR PARTICULA DE LA CONF
  CALL FUERZAS(L, N, BOXL, X, Y, Z, FX, FY, FZ, A, ZK, ENPOT) !OJO LYR: TU NO USAS "L" USAS "ISTEP" CAMBIAR
  
20 CONTINUE  
  !ALMACENAMOS FUERZA Y ENERGIA POR PARTICULA
  !WRITE(12,*)L,ENPOT/REAL(N)
  
 
!Calculo de la funcion de distribucion radial GDR
  WRITE(*,*)'Se calculará la funcion de distribucion radial'
  CALL GDR(N,BOXL,DENS,NN2,CX,CY,CZ,KI) !OJO LYR: AQUI NO MANDAS KI2 SINO EL VALOR DE KI 
  CALL WDT(N,NN2,BOXL,DENS,CXR,CYR,CZR,KI2,DT,ISAVE2)
  
  !ALMACENAMOS LA CONFIGURACION FINAL
  DO L=1,N
     WRITE(11,*)X(L),Y(L),Z(L)
  END DO
  
END PROGRAM DB0


!***********************************SUBRUTINAS***************************
!INCLUYENDO LAS SUBRUTINAS NECESARIAS

!****************************************


!SUBRUTINA PARA CONSTRUIR CONFIG INICIAL ALEATORIA 3D
!SIN TRASLAPES
!******************************************************
SUBROUTINE CONFIGINI(N,BOXL,X,Y,Z)
  
  IMPLICIT NONE
 
  INTEGER::I,J
  REAL,INTENT(IN) ::BOXL
  INTEGER,INTENT(IN)::N
  INTEGER ::IML
  REAL, DIMENSION(N),INTENT(OUT)::X,Y,Z
  REAL:: ISEED1,ISEED2,R,S,T,ISEED3
  REAL::SIGMA,xij,yij,zij,RO
    
  !Almacenando el archivo para guardar la configuración inicial que se genere
  !En ésta subrutina
  !OPEN(10,FILE='confini.txt', STATUS='UNKNOWN')

!ASIGNAR DIMENSION AL VECTOR 
 ! allocate(X(N))
 ! allocate(Y(N))
  
  !SEMILLAS
  SIGMA=1.0  
  !*****************************************
 !PARA DECIDIR CON O SIN MARIA LUISA
   WRITE(*,*)'Con (1) o Sin (0) Maria Luisa'
   READ(*,*)IML

  
DO 10 I=1,N
     
2  Call random_number(ISEED1)
   Call random_number(ISEED2)
   Call random_number(ISEED3)
   
   R=(ISEED1)-0.5
   S=(ISEED2)-0.5
   T=(ISEED3)-0.5
  !WRITE(*,*)R,S,T
   IF (IML==1)THEN
      !COLOCAMOS MARIA LUISA DE SIGMA/2
   X(I)=R*(BOXL-1.0)
   Y(I)=S*(BOXL-1.0)
   Z(I)=T*(BOXL-1.0)
ELSE
   !COLOCAMOS SIN MARIA LUISA
   X(I)=R*(BOXL)
   Y(I)=S*(BOXL)
   Z(I)=T*(BOXL)
   END IF

     DO 9 J=1,I-1
        
     xij=X(I)-X(J)
     yij=Y(I)-Y(J)
     zij=Z(I)-Z(J)
     
     RO=(xij**2)+(yij**2)+(zij**2)
  ! WRITE(*,*)RO     
        IF (RO<=SIGMA) THEN
           WRITE(*,*) 'traslape',I,J
        GO TO 2
     END IF
9 CONTINUE
 
  WRITE(12,*)I,SNGL(X(I)),SNGL(Y(I)),SNGL(Z(I))
  
10 CONTINUE
  
RETURN
END SUBROUTINE CONFIGINI

!***************************************
!Subrutina calculo de la G(r)
SUBROUTINE GDR(N,BOXL,DENS,NN2,CX,CY,CZ,KI)
  IMPLICIT NONE
  REAL,INTENT(IN)::BOXL,DENS
  REAL,DIMENSION(N,NN2),INTENT(IN)::CX,CY,CZ
  REAL,ALLOCATABLE::gX(:),gY(:),gZ(:)
  REAL::DELTAR,PI,XL0,XLT,XL0T,YL0,ZL0,ZL0T,ZLT
  REAL::YLT,YL0T,R0T,C1,RL,RU,RT,C2
  REAL::GDRTA,PRS
  INTEGER,INTENT(IN)::N,NN2,KI
  INTEGER,ALLOCATABLE::NHIST(:)
  INTEGER::I,L,M,J,NBIN,NN3,MAXBIN
  PARAMETER(NN3=3500)

 
!*************************************************
!Calculos pre
  DELTAR=0.01E0
  MAXBIN=INT(BOXL/2.E0/DELTAR)
  ALLOCATE(NHIST(MAXBIN))
!************************************************
  DO I=1,MAXBIN
     NHIST(I)=0
  END DO
!************************************************ 
!CALCULO DE G(R) asignando dimension
 ALLOCATE(gX(MAXBIN))
  ALLOCATE(gY(MAXBIN))
 ALLOCATE(gZ(MAXBIN))
  !Calculo de pi
  PI=4.E0*ATAN(1.E0)
  !Constante para modelo de potencial HD
  C1=(4.0/3.0)*PI*DENS
  
!******************************************
  DO 20 L=1,N
     DO 25 M=1,N
        IF(M==L)GO TO 25
        DO 40 J=1,KI
           XL0=CX(L,J)
           XLT=CX(M,J)
           XL0T=XL0-XLT

           YL0=CY(L,J)
           YLT=CY(M,J)
           YL0T=YL0-YLT

           ZL0=CZ(L,J)
           ZLT=CZ(M,J)
           ZL0T=ZL0-ZLT
!****************************************
           XL0T=XL0T-BOXL*ANINT(XL0T/BOXL)
           YL0T=YL0T-BOXL*ANINT(YL0T/BOXL)
           ZL0T=ZL0T-BOXL*ANINT(ZL0T/BOXL)
           
!*****************************************

           R0T=SQRT(XL0T**2+YL0T**2+ZL0T**2)
           NBIN=INT(R0T/DELTAR)+1
           
           IF(NBIN<=MAXBIN)THEN
              NHIST(NBIN)=NHIST(NBIN)+1
           END IF

40         CONTINUE
25         CONTINUE
20         CONTINUE

           DO 30 NBIN=1,MAXBIN

              RL=REAL(NBIN-1)*DELTAR
              RU=RL+DELTAR
              RT=RL+DELTAR/2.E0
              C2=C1*(RU**3-RL**3)
              GDRTA=REAL(NHIST(NBIN))/REAL(KI)/REAL(N)/C2
              WRITE(16,*)SNGL(RT),SNGL(GDRTA)

30            CONTINUE
             
!Identificar g(1+) de contacto para el cálculo de la presión
             !DO I=1,MAXBIN
             !   READ(16,*)gX(i),gY(i)
             !   IF (gY(i)/=0.0)THEN
             !      PRS=1.0+(1.0/2.0)*PI*DENS*gY(i)
             !      WRITE(17,*)DENS,gY(i),PRS
             !   END IF
            ! END DO
              
         END SUBROUTINE GDR
         !**********************************************************
!SUBRUTINA FUERZAS 
        SUBROUTINE FUERZAS(L, N, BOXL, X, Y, Z, FX, FY, FZ, A, ZK, ENPOT)
           IMPLICIT NONE
           REAL,INTENT(IN)::BOXL,A,ZK
           REAL(KIND=8),INTENT(OUT)::ENPOT
           REAL,DIMENSION(N),INTENT(IN)::X,Y,Z
           REAL,DIMENSION(N),INTENT(OUT)::FX,FY,FZ
           INTEGER,INTENT(IN)::N,L
           REAL::RCUT,XIJ,YIJ,RIJ,ZIJ
           REAL::FXI,FYI,FZI,U,U2,FXIJ,FYIJ,FZIJ
           REAL::FP
           INTEGER::I,J
           RCUT=BOXL/2.0
           ENPOT=0.0 !ENERGIA POTENCIAL DE LA CONF CON LA QUE TRABAJAMOS

           !INICIAMOS CON EL VALOR DE LA FUERZA EN CEROS
           DO I=1,N
              FX(I)=0.0
              FY(I)=0.0
              FZ(I)=0.0
           END DO

           ! CALCULO DE FUERZAS
           DO 3 I=1,N-1
              FXI=FX(I)
              FYI=FY(I)
              FZI=FZ(I)

              DO 2 J=I+1,N

                 XIJ=X(I)-X(J)
                 YIJ=Y(I)-Y(J)
                 ZIJ=Z(I)-Z(J)

                 !CONDICION DE IMAGEN MINIMA
                 XIJ=XIJ-BOXL*ANINT(XIJ/BOXL)
                 YIJ=YIJ-BOXL*ANINT(YIJ/BOXL)
                 ZIJ=ZIJ-BOXL*ANINT(ZIJ/BOXL)

                 !DISTANCIA ENTRE ELLAS
                 RIJ=SQRT(XIJ**2+YIJ**2+ZIJ**2)

                 !VERIFICANDO TRASLAPES
                 IF(RIJ.LE.1.D0)THEN
                   WRITE(*,*)'traslape',I,J
                 !  STOP
                 END IF

                 !INICIA LA ESPECIFICACION DEL MODELO DE POTENCIAL DEL CUAL
                 !SE DERIVA LA FUERZA DE NTERACION ENTRE LAS PARTICULAS
                 IF(RIJ.LT.RCUT)THEN
                    U=EXP(-ZK*RIJ)
                    U2=A*U*(ZK*RIJ+1.D0)/RIJ**3
                    ENPOT=(A*U)/RIJ+ENPOT

                    !FUERZA POR COMPONENTES
                    FXIJ=XIJ*U2
                    FYIJ=YIJ*U2
                    FZIJ=(ZIJ)*U2

                    FXI=FXI+FXIJ
                    FYI=FYI+FYIJ
                    FZI=FZI+FZIJ

                    FX(J)=FX(J)-FXIJ
                    FY(J)=FY(J)-FYIJ
                    FZ(J)=FZ(J)-FZIJ

                 END IF
2                CONTINUE
                 FX(I)=FXI
                 FY(I)=FYI
                 FZ(I)=FZI
              
3                CONTINUE
                 
              
               END SUBROUTINE FUERZAS

SUBROUTINE AZARG(SEED5, X)
      IMPLICIT NONE
        REAL(KIND=8), INTENT(OUT)   :: X
        REAL(KIND=8)                :: PI, A, B, C, D
        REAL        :: SEED5

!   Cálculos preeliminares
    PI = 4.0*ATAN(1.0)
    !   Dos números aleatorios con distribución uniforme
 CALL RANDOM_NUMBER(SEED5)
    A=REAL(SEED5)
   
    C = SQRT(-2.0*LOG(A))

CALL RANDOM_NUMBER(SEED5)
    B=REAL(SEED5)
   
    D = COS(2.0*PI*B)
!   Número aleatorio con distribución gaussiana (o normal)    
    X =C*D

END SUBROUTINE

!************subrutina wdt desplazamiendo cuadratico medio
!Y COEFICIENTE DE DIFUSION DEPENDIENTE DEL TIEMPO
!*******************************************************************
SUBROUTINE WDT(N,NN2,BOXL,DENS,CXR,CYR,CZR,KI2,DT,ISAVE2)
  IMPLICIT NONE
  INTEGER::I,J,K,NTMAX
  REAL,INTENT(IN)::BOXL,DENS,DT
  INTEGER,INTENT(IN)::N,ISAVE2,KI2,NN2
  REAL,DIMENSION(N,NN2),INTENT(IN)::CXR,CYR,CZR
  REAL::TIM,WTX,WTY,WTZ,WT,TIME,DIF

 !ABRIMOS ARCHIVO EN 18
 

  TIM=REAL(ISAVE2)*DT

  DO I=1,KI2-1
     NTMAX=KI2-I
     WTX=0.d0
     WTY=0.d0
     WTZ=0.d0
     WT=0.d0

     DO J=1,N
!CICLO DE AVACE TEMPORAL
        DO K=1,NTMAX
           WTX=WTX+(CXR(J,I+K)-CXR(J,K))**2
           WTY=WTY+(CYR(J,I+K)-CYR(J,K))**2
           WTZ=WTZ+(CZR(J,I+K)-CZR(J,K))**2

        END DO
     END DO

     TIME=TIM*REAL(I)
     WT=(WTX+WTY+WTZ)/REAL(NTMAX)/REAL(N)/6.0D0
     DIF=WT/TIME

     WRITE(18,*)TIME,WT,DIF
     IF(MOD(I,500)==0) THEN
        WRITE(*,*) I
     END IF
  END DO
END SUBROUTINE WDT 
     

           
