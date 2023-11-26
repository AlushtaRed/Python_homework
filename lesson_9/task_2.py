import pandas as pd
file = 'california_housing_train.csv'
df = pd.read_csv(file)
# Задача №61. Решение в группах
# 1. Определить какое максимальное и минимальное
# значение median_house_value
print(df.median_house_value.max())
print(df[['median_house_value']].max())
print(df[['median_house_value']].min())
print(df[['median_house_value']].mean())

# 2. Показать максимальное median_house_value, где
# median_income = 3.1250
print(df.loc[df.median_income == 3.1250, ['median_house_value']].max())
# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_value
print(df.median_house_value.quantile(0.05))
print(df.loc[df.median_house_value < df.median_house_value.quantile(0.05), ['median_house_value', 'population']])
df_quantile = df.loc[df.median_house_value < df.median_house_value.quantile(0.05)]
print(df_quantile.population.max())