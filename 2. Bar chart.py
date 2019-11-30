import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")
print(df.to_string())
df.groupby(["species"]).mean().plot.bar()
plt.show()

