# Analisis de datos

repo: data (https://github.com/AltamarMx/explorador/blob/main/notebooks/data_MOOC_Usuario_a_Explorador.zip)

## Python de usuario a explorador de datos (Coursera)

Una función simplifica y organiza tu código de manera eficiente desde el inicio. Imagina cada función como una pequeña máquina diseñada para tareas específicas, lista para ser reutilizada en diferentes partes de tu proyecto. Desde aceptar argumentos hasta devolver resultados, las funciones promueven la modularidad y la reutilización del código.
Series temporales

1. Momentos en el tiempo
2. Valores correspondientes

Cada punto de datos como un evento en la historia, con su sello de tiempo y su medida, que puede ser numérica o de otro tipo.
En pandas la parte temporal suele definirse como índice, aunque no necesariamente es así. Los valores por otro lado son la esencia de nuestra serie.
Se recomienda en Pandas tratar las fechas como objetos datetime, lo que permite realizar muchas operaciones de manera fácil.
Instalar pandas: pip install pandas o pip install –upgrade pandaspd
Importar la librería panda para el manejo de datos.
import pandas as pd

```
# Formato año-mes-día
# 2025-01-01

# Formato año-mes-día hora:minuto
# en forma 24 horas
# 2025-01-01 14:30

# Formato año-mes-día hora:minuto:segundo
# en forma 24 horas
# 2025-01-01 14:30:00

# Formato año-mes-día hora:minuto
# en forma AM PM
# 2025-01-01 2:30:00 PM
```

## Lectura de archivos Pandas

DataFrames, parametros útiles de la función pd.read_csv de Pandas.

- **Sep y delimeter**: Nos permite especificar el carácter que separa los valores de nuestro archivo CSV, asegurando que los datos se dividen correctamente.
- **Header**: nos indica que fila del archivo CSV debe usarse para los nombres de las columnas del DataFrame.
- **Names**: podemos definir o reemplazar los nombres de las columnas del DataFrame, ofreciendo control sobre la identificación de cada columna de datos.
- **Skip_rows**: se puede definir el numero de renglones a saltarse. Con los renglones eespecíficos en forma de lista.
- **Index_col**: establece una o más columnas como índice del DataFrame, proporcionando un método directo para referenciar y acceder a los datos.
- **parse_dates**: nos ayuda a convertir el índice en formato de tiempo o datetime.
- **Usecols**: nos ayuda a seleccionar solo las columnas específicas que queremos cargar en el DataFrame,
  lo cual es útil para enfocarnos en segmentos particulares de datos y optimizar la memoria y el tiempo.

## Ejemplo:

![alt text](https://github.com/hnaranjog/analisis_de_datos/blob/main/img/example01.jpg "Read CSV")
