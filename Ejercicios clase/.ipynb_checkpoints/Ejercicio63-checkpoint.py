import pandas as pd

# 1. Cargar datos
df = pd.read_csv("felicidad-mundial-2020.csv")

# 2. Cinco países con menor esperanza de vida saludable
peores_salud = df.nsmallest(5, "Healthy life expectancy")[["Country name", "Healthy life expectancy"]]
print(peores_salud)

# 3. Estadísticas (media, mínimo, máximo)
columnas = ["Ladder score", "Freedom to make life choices", "Perceptions of corruption"]
df_stats = df[columnas].agg(["mean", "min", "max"])
print(df_stats)