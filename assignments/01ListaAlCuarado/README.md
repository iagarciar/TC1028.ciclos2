![Tec de Monterrey](../../images/logotecmty.png)
# Lista al cuadrado

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

#### Descripción
Escribe un programa que reciba del usuario un número entero que representa la cantidad de números que va a ingresar al programa. 
El programa deberá recibir (a través de la función input) esa cantidad de números enteros, los colocará en una lista y la desplegará a pantalla. 
Posteriormente deberá construir una nueva lista, con el cuadrado de cada uno de los elementos y desplegarla de igual manera.
En caso de que el primer número de entra sea menor o igual a 0, este solo deberá mostrar 2 listas vacías. 

#### Entrada
El primer número ***n*** entero representa la cantidad de números enteros que se debe leer.
Los ***n*** números enteros, uno en cada línea y de acuerdo a la cantidad anterior.

#### Salida
Se imprime la lista con los números ingresados por el usuario.
Se imprime la lista creada con los números del usuario al cuadrado


***Ejemplo 1:***

Entrada:
```
5
2
4
6
8
10
```

Salida:
```
[2, 4, 6, 8, 10]
[4, 16, 36, 64, 100]
```

***Ejemplo 2:***

Entrada:
```
0
```

Salida:
```
[]
[]
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