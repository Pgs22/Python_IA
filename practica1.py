import pandas as pd
import numpy as np

# 1. Cargar datos desde CSV
df = pd.read_csv('empleados.csv')

# Para consolidar lo aprendido, se proponen ejercicios prácticos que combinan Pandas y NumPy:

# 1 Cargar el archivo CSV de ejemplo en un DataFrame de Pandas.
df = pd.read_csv('empleados.csv')

# 2 Explorar el DataFrame: head(), info(), describe(). Analiza el contenido que muestra cada método.
print(df.head())

# 3 Filtrar empleados por edad, ciudad y departamento. Se tienen que hacer consultas separadas.
# 4 Crear nuevas columnas con cálculos: salario anual y antigüedad en años.
# 5 Aplicar funciones estadísticas de NumPy: media, desviación estándar y percentiles.
# 6 Realizar agrupaciones por ciudad, departamento y rango de edad (separadas): calcular métricas resumen.
# 7 Responded a las siguientes preguntas:
# 7.1. Empleado más antiguo.
# 7.2. Ciudad con más empleados.
# 7.3. Departamento con mayor salario promedio.
# 7.4. Empleado con menos experiencia en la empresa.
# 7.5. Empleados de marketing, de la ciudad de Barcelona y Madrid, que tengan más de 10 años de experiencia.