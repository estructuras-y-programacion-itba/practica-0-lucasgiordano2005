import random
import csv
def guardado_csv(planilla):
    with open ("Jugadas.csv","w",newline="") as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(["jugada","j1","j2"])
        for jugada in planilla:
            j1=planilla[jugada][0]
            j2=planilla[jugada][1]
            escritor.writerow([jugada,j1,j2])
#juego

def juego ():
    planilla ={
    "E":[None,None],
    "F":[None,None],
    "P":[None,None],
    "G":[None,None],
    "1":[None,None],
    "2":[None,None],
    "3":[None,None],
    "4":[None,None],
    "5":[None,None],
    "6":[None,None]
 }

    for ronda in range(10):
        fin=turno(0,planilla)
        guardado_csv(planilla)
        mostrar_planilla(planilla)
        if fin:
            print("Jugador 1 gana con generala Real")
            return
        fin=turno (1,planilla)
        guardado_csv(planilla)
        mostrar_planilla(planilla)
        if fin:
            print("Jugador 2 gana con Generala Real")
            return
    
    p1=0
    p2=0
    for jugada in planilla:
        if planilla[jugada][0]!=None:
            p1+=planilla[jugada][0]
        if planilla[jugada][1]!=None:
            p2+=planilla[jugada][1]
    
    print("Puntaje jugador 1:", p1)
    print("Puntaje jugador 2:",p2)
    if p1>p2:
        print("Gana el jugador 1")
    elif p2>p1:
        print("Gana el jugador 2")
    else:
        print("Empate")
    

#funcion de la tirada incluidas las elecciones de mantener o volver a tirar dados
def tirada ():
    dados=[]

    for i in range(5):
        dados.append(random.randint(1,6))
    tiradas=1
    
    while tiradas<3:
        print ("dados:", dados)
        rta=input("Qué dados querés volver a tirar? (ej: 1 3 5) o Enter para terminar:")
        if rta=="":
            break
        posiciones=rta.split()
        for p in posiciones:
            if p.isdigit():
                 pos=int(p)
                 if pos>=1 and pos<=5:
                     dados[pos-1]=random.randint(1,6)
        tiradas+=1
    print("Resultado final:", dados)
    return dados ,tiradas

#categorias
def generala(dados):
    if dados.count(dados[0])==5:
        return True
    else:
        return False

def poker (dados):
    for i in dados:
        if dados.count(i)==4:
            return True 
    return False

def full (dados):
    valores=[]
    for i in dados:
        if i not in valores:
            valores.append(i)
    if len(valores)==2:
        if dados.count(valores[0])==3 or dados.count(valores[1])==3:
            return True
    
    return False

def escalera (dados):
    dados_ordenados=sorted(dados)
    if dados_ordenados==[1,2,3,4,5] or dados_ordenados==[2,3,4,5,6] or dados_ordenados==[6,1,2,3,4]:
        return True
    else:
        return False
    
#puntaje

def puntaje(dados,categoria,tiradas):
    if categoria=="G" and generala(dados):
        if tiradas==1:
            print("Generala Real")
            return 80, True 
        return 50,False
    
    if categoria=="P" and poker(dados):
        if tiradas==1:
            return 45,False
        return 40,False
    
    if categoria=="F" and full(dados):
        if tiradas==1:
            return 35,False
        return 30,False
    
    if categoria=="E" and escalera(dados):
        if tiradas==1:
            return 25, False
        return 20,False
    
    if categoria in ["1","2","3","4","5","6"]:
        num=int(categoria)
        puntos=0
        for i in dados:
            if i==num:
                puntos+=i
        return puntos,False
    return 0,False


#funcion de los turnos   
def turno(jugador,planilla):
    print("\nTurno Jugador",jugador+1)
    dados,tiradas=tirada()
    print("Resultado:",dados)
    categoria=input("Elegí una categoría: ")
    while  categoria not in planilla or planilla[categoria] [jugador]!=None:
        print("categoría invalida o ya usada")
        categoria=input("elegí nuevamente la categoría: ")
    puntos,fin=puntaje(dados,categoria,tiradas)
    planilla[categoria][jugador]=puntos
    return fin 

#funcion para ir viendo la planilla
def mostrar_planilla(planilla):
    print("\nPLANILLA")
    print("jugada | j1 | j2")
    for jugada in planilla:
        j1=planilla[jugada][0]
        j2=planilla[jugada][1]
        print (jugada, " | ",j1," | ",j2)

#ejecutar
juego()