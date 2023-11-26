# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
import pandas as pd
file = 'california_housing_train.csv'
df = pd.read_csv(file)
df_popular = df.loc[df.population < 500, ['median_house_value', 'population']]
print(df_popular)
avg = df_popular.median_house_value.mean()
print(avg)