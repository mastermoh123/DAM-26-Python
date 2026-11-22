import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("felicidad-mundial-2020.csv")
top_100 = df.nlargest(100, "Ladder score")

plt.figure(figsize=(8, 6))
plt.hist(top_100["Healthy life expectancy"], bins=10, edgecolor="black")
plt.title("Distribución de Esperanza de Vida Saludable (Top 100 Felicidad)")
plt.xlabel("Healthy life expectancy")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("grafica.png")
plt.show()