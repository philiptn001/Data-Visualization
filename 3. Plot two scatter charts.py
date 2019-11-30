import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")
print(df.to_string())
virginica = df.query("species == 'virginica'")
setosa = df.query("species == 'setosa'")
versicolor = df.query("species == 'versicolor'")

ax = virginica.plot.scatter(x="sepal_length", y= "sepal_width", c="red")
ax = setosa.plot.scatter(x="sepal_length", y= "sepal_width", ax=ax, c="blue")
versicolor.plot.scatter(x="sepal_length", y= "sepal_width", ax=ax, c="green")

ax2 = virginica.plot.scatter(x="petal_length", y= "petal_width", c="red")
ax2 = setosa.plot.scatter(x="petal_length", y= "petal_width", ax=ax2, c="blue")
versicolor.plot.scatter(x="petal_length", y= "petal_width", ax=ax2, c="green")

plt.show()

