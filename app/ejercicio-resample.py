import pandas as pd

f = "../data/Cuernavaca_1dia_comas.csv"
df = pd.read_csv(f, parse_dates=["tiempo"])

def importa(df, periodo="A"):
    #Importa un archivo, toma la primera columna como indice y la convierte a date time. 
    #Regresa la desviación estándar de cada columna para el periodo especificado (por defecto anual)'''
    df = df.set_index("tiempo").resample(periodo).std()
    return df

print(importa(df, "ME"))