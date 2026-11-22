import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("felicidad-mundial-2020.csv")
conteo_regiones = df["Regional indicator"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(conteo_regiones, labels=conteo_regiones.index, autopct="%1.1f%%", startangle=140)
plt.title("Número de países por región")
plt.tight_layout()
plt.savefig("grafica.png")
plt.show()