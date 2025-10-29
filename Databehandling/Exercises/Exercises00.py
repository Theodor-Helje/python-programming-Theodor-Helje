import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
show_plots = True
#jag har väldigt medvetet valt att återanvända viss kod (som t.ex. barplots) för enkelheten
#jag är smått missnöjd över hur lång rader jag har skrivit men det är för enkelt och tidskrävande att skriva allt mindre och i funktioner
#också onöjd med att jag använder "" föt DF och inte ''

def read_komtopp50(sheet=0):
    name_list = ["Rang 2020", "Rang 2019", "Kommun", "Folkmängd 2020", "Folkmängd 2019", "förändring"]
    return pd.read_excel("Data/komtopp50_2020.xlsx", names=name_list, sheet_name=sheet, skiprows=6)
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
cities_sweden = read_komtopp50(1)
print(f"2a, b: Cleaned data\n{cities_sweden.head()}\n")
print(f"2c: Sorted after population\n{cities_sweden.sort_values(by="Rang 2020")}\n")
print(f"2d: The five smallest cities\n{cities_sweden.sort_values(by="Rang 2020", ascending=False).head()}\n")
print(f"2e: Swedens population 2019, 2020\n{cities_sweden["Folkmängd 2019"].sum()}, {cities_sweden["Folkmängd 2020"].sum()}\n")

if show_plots:
    fig, axes = plt.subplots(1, 2, figsize=(11,5))
    sns.barplot(data=cities_sweden.head(5), x="Kommun", y="Folkmängd 2020", palette='pastel', ax=axes[0])
    axes[0].set_title("2f: Sveriges 5 största kommuner 2020")
    sns.barplot(data=cities_sweden.tail(5), x="Kommun", y="Folkmängd 2020", palette='pastel', ax=axes[1])
    axes[1].set_title("2f: Sveriges 5 minsta kommuner 2020")
    plt.show()

#3
cities_sweden_female, cities_sweden_male = read_komtopp50(2), read_komtopp50(3)
cities_sweden_female["Kön"], cities_sweden_male["Kön"] = "Kvinna", "Man"
print(f"3a: female\n{cities_sweden_female.head()}\n")
print(f"3a: male\n{cities_sweden_male.head()}\n")

cities_gender_merged = pd.concat([cities_sweden_female, cities_sweden_male])
del cities_gender_merged["Rang 2020"], cities_gender_merged["Rang 2019"]
print(f"3b: merged male / female\n{cities_gender_merged}\n")

del cities_sweden["Rang 2020"], cities_sweden["Rang 2019"]
cities_sweden.columns = ["Kommun", "Total Pop 2020", "Total Pop 2019", "Total förändring"]
print(f"3c: modified total\n{cities_sweden.head()}\n")

cities_sweden_final = pd.merge(cities_gender_merged.set_index("Kommun"), cities_sweden.set_index("Kommun"), on="Kommun").sort_values(by="Total Pop 2020", ascending=False)
print(f"3d: merged total and merged male / female\n{cities_sweden_final}\n")

if show_plots:
    fig, axes = plt.subplots(1, 2, figsize=(12,5))

    sns.barplot(data=cities_sweden_final.sort_values("Total Pop 2020").head(10), x="Folkmängd 2020", y="Kommun", palette='pastel', hue="Kön", ax=axes[0])
    axes[0].set_title("3e: Sveriges 10 största kommuner 2020")

    sns.barplot(data=cities_sweden_final.sort_values("Total Pop 2020", ascending=True).tail(10), x="Folkmängd 2020", y="Kommun", palette='pastel', hue="Kön", ax=axes[1])
    axes[1].set_title("3e: Sveriges 10 minsta kommuner 2020")

    plt.show()

    plt.pie([cities_sweden_final.loc[cities_sweden_final["Kön"] == "Man", "Folkmängd 2020"].sum(), cities_sweden_final.loc[cities_sweden_final["Kön"] == "Kvinna", "Folkmängd 2020"].sum()], 
            labels=["Män", "Kvinnor"], 
            startangle=90, 
            autopct='%1.1f%%'
            )
    plt.title("3f: Könsfördelning i Sveriga 2020")
    plt.show()

    sns.barplot(data=pd.DataFrame({"gender difference": abs(cities_sweden_final.loc[cities_sweden_final["Kön"] == "Man", "Folkmängd 2020"] / cities_sweden_final.loc[cities_sweden_final["Kön"] == "Kvinna", "Folkmängd 2020"])})) #LIST COMPREHENSION