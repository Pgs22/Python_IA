import pandas as pd

# 1. Cargar datos desde CSV
df = pd.read_csv('empleados.csv')

# Mostrar primeras filas para verificar que por defecto son 5 filas
# print(df.head())

# # 2. Selección de columnas
print(df['nombre'])              # Columna unidimensional (Series)
print(df[['nombre','salario']])  # Selección de varias columnas