import pandas as pd

file_path = '../data/Cuernavaca_To_1dia_comas.csv'
cuerna = pd.read_csv(file_path, index_col=0, parse_dates=True)

print(cuerna.head())