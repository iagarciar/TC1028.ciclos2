![Tec de Monterrey](../../images/logotecmty.png)
# Lista al cuadrado

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y ***completa el codigo donde se indica para terminar la simulación***:

```python
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
```

#### Descripción
Calcular la probabilidad de que al repartirte 5 cartas (sin repetir cartas) de póker tengas dos pares. Complete el código que se plantea en la parte de arriba para conseguir este objetivo. 

```
Por ejemplo si tu mano es:
1,1,2,3,3  (existe un par de 1 y un par de 3) [Se cumple el evento]
Por ejemplo si tu mano es:
4,7,4,9,9  (existe un par de 4 y un par de 9) [Se cumple el evento]
Por ejemplo si tu mano es:
4,4,4,9,9  (existe una tercia de 4 y un par de 9) [No se cumple el evento, ya que esto es un full]
Por ejemplo si tu mano es:
K,Q,1,2,1  (existe una tercia de 1) [No se cumple el evento, ya que solo hay un par]
Por ejemplo si tu mano es:
3,Q,3,3,3  (existe una póker) [A pesar de existir dos pares de 3, como son cuatro del mismo número se considera póker y no dos pares]
```

Importante 1: La simulación deberá correr 1000 veces [no modificar este valor]
Importante 2: No hay que modificar el mazo, ni como se obtienen las cartas

#### Entrada
Número entero positivo, este número deberá ser la semilla que se empleara para generar números aleatorios y seleccionar correctamente la posición de la carta del mazo (garantizando que el resultado sea el mismo)

#### Salida
La probabilidad calculada

***Ejemplo 1:***

Entrada:
```
0
```

Salida:
```
0.055
```

***Ejemplo 2:***

Entrada:
```
11
```

Salida:
```
0.047
```

***Ejemplo 3:***

Entrada:
```
42
```

Salida:
```
0.046
```

#### NOTA IMPORTANTE:
Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

La salida del programa debe de ser exactamente de la siguiente forma:

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento.
No la vamos a necesitar para este programa, pero es una buena práctica
incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con
`pytest [nombre de la carpeta] -vv`, subela a tu repositorio en GitHub,
con el proceso de commit + push.