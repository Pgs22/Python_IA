import numpy as np

# Crear array con datos de ingresos
ingresos = np.array([50000, 60000, 55000, 35000])

# Calcular media, percentil y desviación estándar
print("Media:", np.mean(ingresos))
print("Percentil 75:", np.percentile(ingresos, 75))
print("Desviación estándar:", np.std(ingresos))

# Buenas prácticas:
# - Usar funciones de NumPy para evitar bucles
# - Revisar outliers y distribución de los datos