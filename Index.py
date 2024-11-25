import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos desde Excel
datos = pd.read_excel('rendimiento_estudiantes.xlsx')

# Mostrar los primeros registros
print("Datos cargados:")
print(datos)

# Mostrar información general
print("\nInformación general:")
print(datos.info())

# Mostrar estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(datos.describe())

#Limpieza de los datos
# Verificar valores nulos
print("\nValores nulos por columna:")
print(datos.isnull().sum())

# Elimino las filas con valores nulos
datos = datos.dropna()
print("\nValores nulos por columna después de eliminarlos:")
print(datos.isnull().sum())

# Verificar registros duplicados
print("\nNúmero de registros duplicados:")
print(datos.duplicated().sum())

# Eliminar registros duplicados
datos = datos.drop_duplicates()
print("\nNúmero de registros duplicados después de eliminarlos:")
print(datos.duplicated().sum())

#Ver datos actuales
print(datos)

#Transoformar Datos

#Agregar nueva columna Rendimiento
rendimiento=[]
for calificacion in datos['Calificacion']:
    if calificacion >= 80:
        rendimiento.append('Alto')
    else:
        rendimiento.append('Bajo')

datos['Rendimiento'] = rendimiento

print("\nDatos con nueva columna de rendimiento:")
print(datos)

# Relación entre Horas de Estudio y Calificación
plt.scatter(datos['Horas_Estudio'], datos['Calificacion'], color='blue') # Crear gráfico de dispersión
plt.title('Horas de Estudio vs Calificación') # Título del gráfico
plt.xlabel('Horas de Estudio') # Etiqueta eje X
plt.ylabel('Calificación') # Etiqueta eje Y
plt.grid(True) # Mostrar cuadrícula
plt.show() # Mostrar gráfico


# Comparación de calificaciones por género
sns.boxplot(x='Genero', y='Calificacion', data=datos)
plt.title('Calificaciones por Género')
plt.show()

# Distribución del rendimiento
sns.countplot(x='Rendimiento', hue='Genero', data=datos)
plt.title('Distribución de Rendimiento por Género')
plt.show()


