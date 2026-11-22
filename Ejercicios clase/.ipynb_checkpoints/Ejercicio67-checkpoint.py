import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("felicidad-mundial-2020.csv")
bottom_10 = df.nsmallest(10, "Ladder score")

plt.figure(figsize=(8, 6))
plt.scatter(bottom_10["Ladder score"], bottom_10["Freedom to make life choices"], color="red")
plt.title("10 países menos felices: Felicidad vs Libertad de elección")
plt.xlabel("Ladder score")
plt.ylabel("Freedom to make life choices")
plt.grid(True)
plt.tight_layout()
plt.savefig("grafica.png")
plt.show()