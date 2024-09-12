
from random import randrange

def MostrarTablero(tablero):
   
    print("+-------" * 3,"+", sep="")
    for fila in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(tablero[fila][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

def SiguienteMovimiento(tablero):

    ok = False    
    while not ok:
        movimiento = input('Ingresa tu movimiento: ') 
        ok = len(movimiento) == 1 and movimiento >= '1' and movimiento <= '9' 
        if not ok:
            print('Movimiento erroneo, ingresalo nuevamente') 
            continue
        movimiento = int(movimiento) - 1     
        fila = movimiento // 3     
        col = movimiento % 3        
        eleccion = tablero[fila][col]    
        ok = eleccion not in ['O','X'] 
        if not ok:   
            print('Cuadro ocupado, ingresalo nuevamente!')
            continue
    tablero[fila][col] = 'O'    

def LugaresVacios(tablero):

    libre = []    
    for fila in range(3): 
        for col in range(3):
            if tablero[fila][col] not in ['O','X']: 
                libre.append((fila,col)) 
    return libre

def Ganador(tablero, simbolo):

    if simbolo == 'X':    
        quien = 'yo'    
    elif simbolo == "O": 
        quien = 'tu'    
    else:
        quien = None    
    diagonal1 = diagonal2 = True 
    for k in range(3):
        if tablero[k][0] == simbolo and tablero[k][1] == simbolo and tablero[k][2] == simbolo:    
            return quien
        if tablero[0][k] == simbolo and tablero[1][k] == simbolo and tablero[2][k] == simbolo: 
            return quien
        if tablero[k][k] != simbolo: 
            diagonal1 = False
        if tablero[2 - k][2 - k] != simbolo: 
            diagonal2 = False
    if diagonal1 or diagonal2:
        return quien
    return None

def MovimientoMaquina(tablero):

  libres = LugaresVacios(tablero) 
  cuenta = len(libres)
  if cuenta > 0: 
    lugar_maquina = randrange(cuenta)
    fila, col = libres[lugar_maquina]
    tablero[fila][col] = 'X'


tablero = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
tablero[1][1] = 'X' 
libre = LugaresVacios(tablero)
turno_humano = True 
while len(libre):
    MostrarTablero(tablero)
    if turno_humano:
        SiguienteMovimiento(tablero)
        ganador = Ganador(tablero,'O')
    else:    
        MovimientoMaquina(tablero)
        ganador = Ganador(tablero,'X')
    if ganador != None:
        break
    turno_humano = not turno_humano        
    libre = LugaresVacios(tablero)

MostrarTablero(tablero)
if ganador == 'tu':
    print('Ganaste!')
elif ganador == 'yo':
    print('Perdiste!')
else:
    print('Empate!')