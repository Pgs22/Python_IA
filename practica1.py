import pandas as pd
import numpy as np

# Para consolidar lo aprendido, se proponen ejercicios prácticos que combinan Pandas y NumPy:

# ==========================================
## EJERCICIO 1 
# Cargar el archivo CSV de ejemplo en un DataFrame de Pandas.
# ==========================================

df = pd.read_csv('empleados.csv')

# ==========================================
## EJERCICIO 2
# Explorar el DataFrame: head(), info(), describe(). Analiza el contenido que muestra cada método.
# ==========================================

# [MÉTODO .head()]
# -------------------------------------------------------------------------
# Devuelve las 2 primeras filas añadiendo 2, si lo dejamos vacío aparecen 5 filas por defecto
# Y nos cuenta la primera fila como título sin enumerar, y 
# añadiendo los valores en columnas añadiendo una columna con el índice
# -------------------------------------------------------------------------
print(df.head(2))

# [MÉTODO .info()]
# -------------------------------------------------------------------------
# Indica el total de filas y muestra a la izquierda el índice
# La primera fila la identifica como nombre de columna y del resto comprueba si el campo es nulo y su tipo
# -------------------------------------------------------------------------
print(df.info())

# [MÉTODO .describe()]
# -------------------------------------------------------------------------
# De los valores identifica la primera fila como nombres de columnas
# Y del resto de datos, si son numéricos, muestra en una tabla los resultados de cálculos estadísticos
# en la primera columna indica el nombre de cada cálculo
# -------------------------------------------------------------------------
df.describe()

# ==========================================
## EJERCICIO 3 
# Filtrar empleados por edad, ciudad y departamento. Se tienen que hacer consultas separadas.
# ==========================================

# -------------------------------------------------------------------------
# Por edad
# -------------------------------------------------------------------------
df_mayor_30 = df[df['edad'] > 30]
print(df_mayor_30)

# -------------------------------------------------------------------------
# Por ciudad
# -------------------------------------------------------------------------
df_bcn = df[df['ciudad'] == 'Barcelona']
print(df_bcn)

# -------------------------------------------------------------------------
# Por departamento
# -------------------------------------------------------------------------
df_depart = df[df['departamento'] == 'Ventas']
print(df_depart)

# ==========================================
## EJERCICIO 4 
# Crear nuevas columnas con cálculos: salario anual y antigüedad en años.
# ==========================================

df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df['salario_anual'] = df['salario'] * 12
df['antigüedad_en_años'] = df['fecha_ingreso'].dt.year
print(df.columns)

# ==========================================
## EJERCICIO 5 
# Aplicar funciones estadísticas de NumPy: media, desviación estándar y percentiles.
# ==========================================

print("Media:", np.mean(df['salario_anual']))
#El 75% de los empleados tienen este salario anual o menos
print("Percentil 75:", np.percentile(df['salario_anual'], 75))
#Para saber la diferencia entre la media y el sueldo más alto
print("Desviación estándar:", np.std(df['salario_anual']))

# ==========================================
## EJERCICIO 6 
# Realizar agrupaciones por ciudad, departamento y rango de edad (separadas): calcular métricas resumen.
# ==========================================

# ==========================================
## EJERCICIO 7 
# Responded a las siguientes preguntas:
# ==========================================

# 7.1. Empleado más antiguo.
# 7.2. Ciudad con más empleados.
# 7.3. Departamento con mayor salario promedio.
# 7.4. Empleado con menos experiencia en la empresa.
# 7.5. Empleados de marketing, de la ciudad de Barcelona y Madrid, que tengan más de 10 años de experiencia.