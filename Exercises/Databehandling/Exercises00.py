import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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