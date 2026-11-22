import pandas as pd

# 1. Cargar datos
df = pd.read_csv("felicidad-mundial-2020.csv")

# 2. Filtro
filtro = df[(df["Logged GDP per capita"].between(10.000, 11.000)) & (df["Freedom to make life choices"] < 0.900)]
print(filtro[["Country name", "Regional indicator"]])

# 3. Agrupación por región
df_agrupado = df.groupby("Regional indicator")[
    ["Ladder score", "Healthy life expectancy", "Logged GDP per capita"]
].mean()
print(df_agrupado)