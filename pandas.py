import pandas as pd

# 1. Cargar datos desde CSV
df = pd.read_csv('empleados.csv')

# Mostrar primeras filas para verificar que por defecto son 5 filas
# print(df.head())

# # 2. Selección de columnas
print(df['nombre'])              # Columna unidimensional (Series)
print(df[['nombre','salario']])  # Selección de varias columnas

# 3. Filtrado de filas
df_mayor_30 = df[df['edad'] > 30]
print(df_mayor_30)

# 4. Crear nuevas columnas
df['salario_anual'] = df['salario'] * 12
df['edad_en_dias'] = df['edad'] * 365

# 5. Manejo de fechas
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df['año_ingreso'] = df['fecha_ingreso'].dt.year
df['mes_ingreso'] = df['fecha_ingreso'].dt.month
df['dia_ingreso'] = df['fecha_ingreso'].dt.day

# Buenas prácticas:
# - Siempre revisar tipos de datos: df.dtypes
# - Comprobar nulos: df.isnull().sum()
# - Evitar bucles usando operaciones vectorizadas
# - Documentar columnas nuevas y transformaciones


