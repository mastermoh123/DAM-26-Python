import pandas as pd

# 1. Cargar datos
df = pd.read_csv("felicidad-mundial-2020.csv")

# 2. Medias agrupadas
print(df.groupby("Regional indicator")[["Ladder score", "Healthy life expectancy"]].mean())

# 3. Nuevo DataFrame con los extremos
indices = [
    df["Ladder score"].idxmax(),
    df["Ladder score"].idxmin(),
    df["Logged GDP per capita"].idxmax(),
    df["Logged GDP per capita"].idxmin(),
    df["Generosity"].idxmax(),
    df["Generosity"].idxmin()
]
df_extremos = df.loc[indices]
print(df_extremos)