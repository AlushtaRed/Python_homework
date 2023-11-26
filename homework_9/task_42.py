# Задача 42: Узнать какая максимальная households 
# в зоне минимального значения population
import pandas as pd
file = 'california_housing_train.csv'
pf = pd.read_csv(file)
pf_min_popular = pf.loc[pf.population < pf.population.quantile(0.10), ['population', 'households' ]]
print(pf_min_popular)
max_households_in_min_population = pf_min_popular.households.max()
print(max_households_in_min_population)