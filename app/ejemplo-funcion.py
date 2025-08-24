import pandas as pd

def ejemplo_funcion():
    c = a + b
    return c

a = 1
b = 2
c = ejemplo_funcion()
print(c)

def ejemplo_funcion2(a, b):
    d = a * b
    return d

resultado = ejemplo_funcion2(a, b)
print(resultado)

def importa(f):
    '''Importa un archivo, toma la primera columna como indice y la convierte a date time. 
    Regresa el promedio diario de cada columna'''
    df = pd.read_csv(f,index_col=0,parse_dates=True).resample("2h").mean()
    return df

f = "../data/Cuernavaca_1dia_comas.csv"
cuerna_mean = importa(f)
print(cuerna_mean)