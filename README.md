# Convertidor de Palabras a Binario

Este programa en Python permite a los usuarios convertir palabras y caracteres a su representación binaria, mostrando también el valor ASCII de cada letra.

## Contenido

1. [Estructura del Repositorio](#estructura-del-repositorio)
2. [Cómo Usar el Programa](#cómo-usar-el-programa)
3. [Funciones Principales](#funciones-principales)
4. [Explicación de `ord()`](#explicación-de-ord)

## Estructura del Repositorio

- `evaluacionfinal.py`: Contiene el código fuente en Python.
- `README.md`: Documentación del proyecto.

## Cómo Usar el Programa

1. Ejecuta el script `evaluacionfinal.py`.
2. Selecciona la opción de "CARACTER" o "PALABRA" según tu preferencia.
3. Ingresa el carácter o palabra cuando se solicite.
4. Observa la salida, que incluirá la palabra original, el valor ASCII y la representación binaria de cada letra, así como el binario de la palabra completa.

### EJEMPLO VISUAL:
![EJEMPLODEUSO](https://github.com/Nicolle2702/HERRAMIENTAS-FINAL/blob/main/imagen_2023-11-14_231137259.png)

## Funciones Principales

### `menu()`

Esta función muestra un menú al usuario para seleccionar si desea convertir un carácter o una palabra. Devuelve la entrada del usuario.

### `letra_a_binario(letra)`

Convierte un carácter dado a su representación binaria de 8 bits utilizando el valor ASCII de la letra.

### `palabra_a_binario(palabra)`

Convierte una palabra dada a una lista de tuplas, donde cada tupla contiene la letra, su representación binaria y su valor ASCII. Además, devuelve la representación binaria completa de la palabra.

## Uso de ord
La función `ord()` en Python se utiliza para obtener el valor ASCII  de un carácter

`letra = 'A' 
valor_ascii = ord(letra) print(f"El valor ASCII de '{letra}' es: {valor_ascii}")`

