import pandas as pd
import numpy as np

df = pd.read_csv('empleados.csv')

# Calcular estadísticas usando NumPy sobre columnas de DataFrame
df['edad_media'] = np.mean(df['edad'])
df['edad_max'] = np.max(df['edad'])
df['edad_min'] = np.min(df['edad'])

# Nota avanzada: 
# Para datasets muy grandes, se recomienda usar operaciones NumPy directamente para optimizar memoria y velocidad