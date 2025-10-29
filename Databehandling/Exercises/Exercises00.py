import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#1
cities_and_population = pd.DataFrame({
    'kommun': ['Malmö', 'Stockholm', 'Uppsala', 'Göteborg'],
    'Population': [347949, 975551, 233839, 583056]
    })
print(f"A: Hela DataFrame:\n{cities_and_population}\n")
print(f"B: Bara städer:\n{cities_and_population['kommun']}\n")
print(f"C: Bara rad med Göteborg:\n{cities_and_population[cities_and_population['kommun'] == 'Göteborg']}\n")
print(f"D: Tre största:\n{cities_and_population.sort_values('Population', ascending=False).head(3)}\n")

#E
cities_and_population['Population (%)'] = round((cities_and_population['Population'] / 10379295)*100, 1)
print(f"E: Andel befolkning i %\n{cities_and_population}\n")

#2
print(f"Sheet names:\n{pd.ExcelFile("Data/komtopp50_2020.xlsx").sheet_names}\n")
name_list = ["Rang 2020", "Rang 2019", "Kommun", "Folkmängd 2020", "Folkmängd 2019", "förändring"]
cities_sweden = pd.read_excel("Data/komtopp50_2020.xlsx", names=name_list, sheet_name=1, skiprows=6).sort_values(by="Rang 2020")
print(f"2a, b: Cleaned data\n{cities_sweden.head()}\n")
print(f"2c: Sorted after population\n{cities_sweden.sort_values(by="Rang 2020")}\n")
print(f"2d: The five smallest cities\n{cities_sweden.sort_values(by="Rang 2020", ascending=False).head()}\n")
print(f"2e: Swedens population 2019, 2020\n{cities_sweden["Folkmängd 2019"].sum()}, {cities_sweden["Folkmängd 2020"].sum()}\n")

fig, axes = plt.subplots(1, 2, figsize=(11,5))
sns.barplot(data=cities_sweden.head(5), x="Kommun", y="Folkmängd 2020", palette='pastel', ax=axes[0])
axes[0].set_title("2f: Sveriges 5 största kommuner 2020")
sns.barplot(data=cities_sweden.tail(5), x="Kommun", y="Folkmängd 2020", palette='pastel', ax=axes[1])
axes[1].set_title("2f: Sveriges 5 minsta kommuner 2020")
plt.show()

#3