import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos de fertilidad adolescente
df = pd.read_csv('/content/AdolescentFertility.csv')
data = pd.DataFrame(df)

# Filtrar datos por años específicos
dataFilteredBy2007_2017 = data.loc[(data['2017'] == 53.46) & (data['2007'] == 63.57)]
print(dataFilteredBy2007_2017)

# Mostrar los 10 países con mayor fertilidad adolescente en 2017
print(data.sort_values(by='2017', ascending=False)[['Country Name', '2017']].head(10))

# Filtrar datos de Costa Rica
dataFiltered = data.loc[(data['Country Name'] == "Costa Rica")]
dataFiltered1 = dataFiltered.drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], axis=1)
dataFiltered2 = dataFiltered1.sum()
print(dataFiltered2.mean())

# Cargar datos de casas en Boston
datos = pd.read_csv("casasboston.csv")
print(datos)

# Seleccionar columnas específicas
df = datos[["RM", "CRIM", "MEDV", "TOWN", "CHAS"]]

# Renombrar columnas
df = datos.rename(columns={
    "TOWN": "CIUDAD",
    "CRIM": "INDICE_CRIMEN",
    "INDUS": "PCT_ZONA_INDUSTRIAL",
    "CHAS": "RIO CHARLES",
    "RM": "N_HABITACIONES_MEDIO",
    "MEDV": "VALOR_MEDIANO",
    "LSTAT": "PCT_CLASE_BAJA"
})

print(df)

# Graficar histograma del número de habitaciones
df.N_HABITACIONES_MEDIO.plot.hist()
plt.title('Histograma de frecuencias de número de habitaciones')
plt.xlabel('Número de Habitaciones Promedio')
plt.ylabel('Frecuencia')
plt.show()

# Graficar dispersión de índice de crimen y valor mediano de las casas
df.plot.scatter(x="VALOR_MEDIANO", y="INDICE_CRIMEN", alpha=1)
plt.title('Gráfico de dispersión de índice de crimen')
plt.xlabel('Valor Mediano')
plt.ylabel('Índice de Crimen')
plt.show()

# Graficar barras de las primeras 10 ciudades por valor mediano de las casas
valor_por_ciudad = df.groupby("CIUDAD")["VALOR_MEDIANO"].mean()
valor_por_ciudad.head(10).plot.barh()
plt.title('Gráfico de barras de las primeras 10 ciudades por valor mediano de las casas')
plt.xlabel('Valor Mediano')
plt.ylabel('Ciudad')
plt.show()