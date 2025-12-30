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

# -------------------------------------------------------------------------
# Crear el DataFrame
# -------------------------------------------------------------------------
data = {
    'nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Jorge', 'Lucia'],
    'edad': [25, 34, 42, 19, 28, 31],
    'ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Madrid', 'Barcelona'],
    'departamento': ['IT', 'Marketing', 'Ventas', 'IT', 'Marketing', 'Ventas'],
    'salario': [2500, 3200, 4000, 1800, 2800, 3000],
    'fecha_ingreso': ['2020-01-01', '2018-05-15', '2015-09-30', '2021-03-20', '2019-07-10', '2017-11-05']
}
df = pd.DataFrame(data)

# -------------------------------------------------------------------------
# AGRUPACIONES
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# Agrupación por CIUDAD y métricas
resumen_ciudad = df.groupby('ciudad')['salario'].describe()
print(resumen_ciudad)
# -------------------------------------------------------------------------
# Agrupación por DEPARTAMENTO y métricas
resumen_depto = df.groupby('departamento')['salario'].mean()
print(resumen_depto)
# -------------------------------------------------------------------------
# Agrupación por RANGO DE EDAD Senior, Adulto y Joven
#creamos un narray de edades
edades = df['edad'].values
#Multiplicamos por 6 porque tenemos 6 edades y necesitamos 6 etiquetas para duplicar el array
#Para evitar que solo deje un espacio de 12 caracteres que es lo que ocupa Senior (+36)
# se añade --> dtype=object --> con esto le prohíbes a NumPy que mida el texto
nombres_rangos = np.array(['Senior (36+)'] * len(edades), dtype=object)

# Nuevos filtros para agrupar rangos de edad Joven o adulto
es_joven = edades <= 25
es_adulto = (edades > 25) & (edades <= 35)

# Aplicamos los filtros usando INDEXACIÓN DIRECTA
nombres_rangos[es_joven] = 'Joven (hasta 25)'
nombres_rangos[es_adulto] = 'Adulto Joven (26-35)'

# Devolvemos el array al DataFrame
df['rango_edad'] = nombres_rangos

#Agrupamos
resumen_edad = df.groupby('rango_edad')['salario'].agg([np.sum, np.mean, np.std])
print("\nMétricas resumen:\n", resumen_edad)
# -------------------------------------------------------------------------


# ==========================================
## EJERCICIO 7 
# Responded a las siguientes preguntas:
# ==========================================

# 7.1. Empleado más antiguo.
# 7.2. Ciudad con más empleados.
# 7.3. Departamento con mayor salario promedio.
# 7.4. Empleado con menos experiencia en la empresa.
# 7.5. Empleados de marketing, de la ciudad de Barcelona y Madrid, que tengan más de 10 años de experiencia.

# -------------------------------------------------------------------------
# PREPARACIÓN PARA FECHAS (Punto 5.1)
# -------------------------------------------------------------------------
# Convertimos a datetime y calculamos la experiencia en años
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
fecha_actual = pd.to_datetime('2025-12-29') # Fecha de hoy
df['experiencia'] = (fecha_actual - df['fecha_ingreso']).dt.days / 365.25

# -------------------------------------------------------------------------
# RESPUESTAS
# -------------------------------------------------------------------------

# 7.1. Empleado más antiguo (El que tiene la fecha de ingreso menor)
# Usamos idxmin() que devuelve el índice del valor mínimo
empleado_antiguo = df.loc[df['fecha_ingreso'].idxmin(), 'nombre']
print(f"7.1. Empleado más antiguo: {empleado_antiguo}")

# 7.2. Ciudad con más empleados
# value_counts() cuenta repeticiones y idxmax() nos da la que más tiene
ciudad_top = df['ciudad'].value_counts().idxmax()
print(f"7.2. Ciudad con más empleados: {ciudad_top}")

# 7.3. Departamento con mayor salario promedio
# Agrupamos y buscamos el máximo
depto_top_salario = df.groupby('departamento')['salario'].mean().idxmax()
print(f"7.3. Depto con mayor salario promedio: {depto_top_salario}")

# 7.4. Empleado con menos experiencia
# idxmax() en fecha (la fecha más reciente es la menor experiencia)
empleado_novato = df.loc[df['fecha_ingreso'].idxmax(), 'nombre']
print(f"7.4. Empleado con menos experiencia: {empleado_novato}")

# 7.5. Marketing, Barcelona/Madrid y > 10 años experiencia
# Combinamos filtros usando & (AND) y | (OR) del punto 2.6
filtro_complejo = (df['departamento'] == 'Marketing') & \
                  (df['ciudad'].isin(['Barcelona', 'Madrid'])) & \
                  (df['experiencia'] > 10)

empleados_filtrados = df[filtro_complejo]
print("\n7.5. Empleados que cumplen el criterio complejo:")
print(empleados_filtrados[['nombre', 'ciudad', 'experiencia']])

#opcion 2 ejercicio 7
#punto 4
# Tomamos el año 2025 como referencia
# Usamos x[:4] para agarrar los primeros 4 caracteres de la fecha (el año)
df['experiencia'] = df['fecha_ingreso'].apply(lambda x: 2025 - int(x[:4]))

#punto 5
# Crear salario anual (Operación vectorizada de la sección 2.6 de tu teoría)
df['salario_anual'] = df['salario'] * 12

# Antigüedad simplificada (asumiendo año 2025)
# Usamos apply como sugiere tu tabla de métodos de Pandas
df['antigüedad'] = df['fecha_ingreso'].apply(lambda x: 2025 - int(x[:4]))

# Estadísticas con NumPy (Sección 2.7)
media_salarial = np.mean(df['salario'])
desviacion = np.std(df['salario'])

# Agrupación por departamento
resumen_depto = df.groupby('departamento')['salario'].mean()
print(resumen_depto)

# Filtro: Marketing Y (Madrid o Barcelona) Y antigüedad > 10
# Nota: La teoría menciona "Filtrar registros con condiciones"
filtro = (df['departamento'] == 'Marketing') & \
         (df['ciudad'].isin(['Madrid', 'Barcelona'])) & \
         (df['antigüedad'] > 10)

resultado = df[filtro]