import random
j1=0
j2=0
def tirada_Dados(cant_dados):
    dados=[]
    for i in range(cant_dados) :
        dados.append(random.randint(1,6))
    return dados

def guardar_dados(dados_actuales):
    dados_guardados = []
    print(f"Tus dados actuales son: {dados_actuales}")
    texto_ingresado = input("Ingresá las posiciones a guardar separadas por espacio (o Enter para tirar todos de nuevo): ")
    if texto_ingresado != "":
        posiciones = texto_ingresado.split() 
        for i in posiciones:
            indice = int(i) - 1 
            dado_elegido = dados_actuales[indice]
            dados_guardados.append(dado_elegido)
    return dados_guardados


def turno_jugador(nombre_jugador):
    print(f"\n--- Turno de {nombre_jugador} ---")
    mis_dados = tirada_Dados(5)
    for numero_tirada in range(2, 4): 
        dados_guardados = guardar_dados(mis_dados)
        if len(dados_guardados) == 5:
            print("¡Decidiste plantarte!")
            break 
        dados_a_tirar = 5 - len(dados_guardados)
        nuevos_dados = tirada_Dados(dados_a_tirar)
        mis_dados = dados_guardados + nuevos_dados
    print(f"--> Los dados finales de {nombre_jugador} son: {mis_dados}\n")
    return mis_dados
