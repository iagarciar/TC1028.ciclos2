import random

def generarMazo():
    mazo = []
    for i in range(1,14):
        mazo.extend([i]*4)
    return mazo

def main():
    #Generando semilla para poder reproducir el mismo resultado
    semilla = int(input())
    random.seed(semilla)
    #Contador de eventos de dos pares
    cont = 0
    for e in range(1000):#Corriendo el experimento 1000 veces
    #Iniciando experimento    
        #Generando el mazo
        mazo = generarMazo()
        #Iniciando la mano vacia
        mano = []
    
        for i in range(5): #Obteniendo las 5 cartas del mazo de forma aleatoria
            pos = random.randint(0,len(mazo)-1) #Posicion de la carta para tomarla aleatoriamente
            carta = mazo.pop(pos) #Tomo 1 carta y la retiro del mazo
            mano.append(carta) #La agrego en la mano
        #Condicional para verificar si tiene 2 pares y lo cuente como evento exitoso
        #¡COMPLETAR CODIGO!

    #Mostrar el resultado
    print(cont/1000)

if __name__=='__main__':
    main()
