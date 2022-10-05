#Creamos tablero 10x10, en blanco.
from random import choice, randint, random
from xml.dom.expatbuilder import ElementInfo
import numpy as np
def crear_tablerosj1():
    global tablero_disparoj1, tableroj1

    tablero_disparoj1=np.full((10,10)," ")
    tableroj1=np.full((10,10)," ")
    return tablero_disparoj1,tableroj1
def crear_tablerosj2():
    global tablero_disparoj2, tableroj2

    tablero_disparoj2=np.full((10,10)," ")

    tableroj2=np.full((10,10)," ")
    return tablero_disparoj2,tableroj2

#Verificamos y colocamos barcos aleatoriamente sin superponerse.(Codigo de Alberto)
def imprimir_tablero_barcoj1(tamaño):     
    while True:
        # Orientacion aleatoria
        orientacion= choice(["N","S","E","O"])
        # Posicion inicial del barco
        current_pos = np.random.randint(10, size=2)
        fila = current_pos[0]
        col = current_pos[1]
   
        #Recogemos las 4 posiciones candidatas
        coors_posiN = tableroj1[fila:fila-tamaño:-1, col]
        coors_posiE = tableroj1[fila, col:col+tamaño]
        coors_posiS = tableroj1[fila:fila + tamaño, col]
        coors_posiO = tableroj1[fila, col:col - tamaño:-1]
        if (orientacion=='N') and len(coors_posiN) == tamaño and ('O' not in coors_posiN):
            tableroj1[fila:fila-tamaño:-1, col]='O'
            break    
        # Compruebo E
        elif (orientacion == 'E') and len(coors_posiE) == tamaño and ('O' not in coors_posiE):
            tableroj1[fila, col:col+tamaño] = 'O'
            break    
        # Compruebo S
        elif (orientacion=='S') and len(coors_posiS) == tamaño and ('O' not in coors_posiS):
            tableroj1[fila:fila + tamaño, col] = 'O'
            break    
        # Compruebo O
        elif (orientacion=='O') and len(coors_posiO) == tamaño and ('O' not in coors_posiO):
            tableroj1[fila, col: col - tamaño:-1] ='O'
            break

def imprimir_tablero_barcoj2(tamaño):     
    while True:
        # Orientacion aleatoria
        orientacion= choice(["N","S","E","O"])
        # Posicion inicial del barco
        current_pos = np.random.randint(10, size=2)
        fila = current_pos[0]
        col = current_pos[1]
   
        # Recogemos las 4 posiciones candidatas
        coors_posiN = tableroj2[fila:fila-tamaño:-1, col]
        coors_posiE = tableroj2[fila, col:col+tamaño]
        coors_posiS = tableroj2[fila:fila + tamaño, col]
        coors_posiO = tableroj2[fila, col:col - tamaño:-1]
        if (orientacion=='N') and len(coors_posiN) == tamaño and ('O' not in coors_posiN):
            tableroj2[fila:fila-tamaño:-1, col]='O'
            break    
        # Compruebo E
        elif (orientacion == 'E') and len(coors_posiE) == tamaño and ('O' not in coors_posiE):
            tableroj2[fila, col:col+tamaño] = 'O'
            break    
        # Compruebo S
        elif (orientacion=='S') and len(coors_posiS) == tamaño and ('O' not in coors_posiS):
            tableroj2[fila:fila + tamaño, col] = 'O'
            break    
        # Compruebo O
        elif (orientacion=='O') and len(coors_posiO) == tamaño and ('O' not in coors_posiO):
            tableroj2[fila, col: col - tamaño:-1] ='O'
            break
#Colocando Barcos aleatorios
def ubicar_barcosj1():
    qty_barco1=4
    qty_barco2=3
    qty_barco3=2
    qty_barco4=1

    for i in range(qty_barco1):
        imprimir_tablero_barcoj1(1)
        2
    for i in range(qty_barco2):
        imprimir_tablero_barcoj1(2)

    for i in range(qty_barco3):
        imprimir_tablero_barcoj1(3)

    for i in range(qty_barco4):
        imprimir_tablero_barcoj1(4)

def ubicar_barcosj2():
    qty_barco1=4
    qty_barco2=3
    qty_barco3=2
    qty_barco4=1

    for i in range(qty_barco1):
        imprimir_tablero_barcoj2(1)
        2
    for i in range(qty_barco2):
        imprimir_tablero_barcoj2(2)

    for i in range(qty_barco3):
        imprimir_tablero_barcoj2(3)

    for i in range(qty_barco4):
        imprimir_tablero_barcoj2(4)


#Disparando a los barcos
def dispararj1():
    Fila=int(input("Ingresar coordenas 0 al 9 Horizontal"))
    Columna=int(input("Ingresar coordenadas 0 al 9 Vertical"))
    if tableroj2[Fila,Columna]=="O":
        tablero_disparoj1[Fila,Columna]="*"
        tableroj2[Fila,Columna]="*"
        print(tablero_disparoj1) 
        print("OUCH,ACERTASTE.TU TURNO")
        return dispararj1()
    else:
        tablero_disparoj1[Fila,Columna]="#"
        tableroj2[Fila,Columna]="#"
        print("FALLASTE JAJA, MI TURNO")
        return False

def dispararj2():
    Fila=randint(0,9)
    Columna=randint(0,9)
    if tableroj1[Fila,Columna]=="O":
        tableroj1[Fila,Columna]="*"             
        print("TE ENCONTRE, MI TURNO NUEVAMENTE")
        return dispararj2()
    elif tableroj1[Fila,Columna]==" ":
        tableroj1[Fila,Columna]="#"
        print("OH NO FALLE, TU TURNO")
        return False
    else:
        return dispararj2()      

while True:
        ingreso = input("Bienvenid@s a HUNDIR LA FLOTA. Marca 1 para comenzar a jugar")
        if ingreso!="":
                crear_tablerosj1()
                ubicar_barcosj1()
                print("Estos son tus tableros \n")
                crear_tablerosj2()
                ubicar_barcosj2()          
        break

while True:
    print(tablero_disparoj1)
    print()
    print(tableroj1)
    ingresar=input("Marcar 2 para comenzar disparar=") 
    if ingresar=="2":
        if "O" in tableroj1 and "O" in tableroj2:
            dispararj1()
            dispararj2()
        else:
            break

    

    