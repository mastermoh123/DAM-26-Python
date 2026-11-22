import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("felicidad-mundial-2020.csv")
df_ordenado = df.sort_values(by="Ladder score", ascending=False)
seleccion = pd.concat([df_ordenado.head(3), df_ordenado.tail(3)])

seleccion.plot(
    x="Country name",
    y=["Ladder score", "Logged GDP per capita"],
    kind="bar",
    figsize=(10, 6)
)
plt.title("Top 3 y Bottom 3 países: Felicidad vs Renta per cápita")
plt.ylabel("Valor")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafica.png")
plt.show()