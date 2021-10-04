![Tec de Monterrey](../../images/logotecmty.png)
# Suma de listas

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

#### Descripción
Desarrolla el programa que permita realizar la suma elemento a elemento de dos listas (con la misma cantidad de elementos). Ambas compuestas por números naturales. 
La salida deberá ser una lista que contenga la suma de cada elemento en las listas.

#### Entrada
La primera lista está dada por n valores enteros, donde n es mayor o igual a 2, uno en cada renglón. 
La primera lista finaliza con un /
La segunda lista está dada por n valores enteros, donde n es mayor o igual a 2, uno en cada renglón. 
La segunda lista finaliza con un /
La captura Finaliza con un *.

#### Salida
Se muestra la salida que deberá mostrar tu programa (tal como se ilustra). 
Para los dos ejemplos anteriores, la salida debería ser:


***Ejemplo 1:***

Entrada:
```
3
2
/
2
3
/
*
```

Salida:
```
[5, 5]
```

***Ejemplo 2:***

Entrada:
```
5
4
3
/
3
2
4
/
*
```

Salida:
```
[8, 6, 7]
```

***Ejemplo 3:***

Entrada:
```
1
1
1
1
1
1
1
/
0
0
0
0
0
0
0
/
*
```

Salida:
```
[1, 1, 1, 1, 1, 1, 1]
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