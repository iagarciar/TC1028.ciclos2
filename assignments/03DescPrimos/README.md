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
Este ejercicio poder descomponer un número n en sus factores primos, dicho número es un entero positivo en el rango de 2 hasta 9999999.  
El programa deberá mostrar los factores primos uno por linea.

#### Entrada
Número entero positivo


#### Salida
Todos los factores primos, cada uno de ellos en una linea. En caso de tener mas de un factor primo, estos se deberán mostrar en orden ascendiente (es importante notar que si el factor primo se repite, cada uno de ellos deberá ser mostrado).



***Ejemplo 1:***

Entrada:
```
7
```

Salida:
```
7
```

***Ejemplo 2:***

Entrada:
```
20
```

Salida:
```
2
2
5
```

***Ejemplo 3:***

Entrada:
```
101
```

Salida:
```
101
```

***Ejemplo 4:***

Entrada:
```
4000
```

Salida:
```
2
2
2
2
2
5
5
5
```

***Ejemplo 5:***

Entrada:
```
9999999
```

Salida:
```
3
3
239
4649
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