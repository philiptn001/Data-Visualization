import pandas as pd
import matplotlib.pyplot as plt


def clean_city(cell):
    if "London" in cell:
        return "London"
    else:
        return cell


df = pd.read_csv("Books.csv")
print(df.to_string())
drop_columns = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver',
                'Contributors', 'Issuance type', 'Shelfmarks']
df.drop(drop_columns, axis="columns", inplace=True)
df.columns = [c.replace(" ", "_") for c in df.columns]
df["Place_of_Publication"] = df["Place_of_Publication"].apply(clean_city)
df["Place_of_Publication"].value_counts().plot.pie()
# df["Place_of_Publication"].value_counts().plot.bar()
plt.show()

