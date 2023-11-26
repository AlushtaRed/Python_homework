import pandas as pd
file = 'california_housing_train.csv'
# file_upd = "california_housing_train_upd.csv"
# Задача №57. Общее обсуждение

# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
df = pd.read_csv(file)
# df1 = pd.read_csv(file_upd)
# print(df.head())

# 2. Посмотреть сколько в нем строк и столбцов
print(df.shape)

# 3. Определить какой тип данных имеют столбцы
print(df.dtypes)

# Задача №59. Решение в группах
# 1. Проверить есть ли в файле пустые значения
print(df.isnull().sum())


# 2. Показать median_house_value где median_income < 2
print(df.loc[df.median_income < 2, ["median_income", "median_house_value"]])

# 3. Показать данные в первых 2 столбцах
print(df[['longitude', 'latitude']])
print(df.iloc[:, 0:2])

# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
print(df.loc[(df.housing_median_age < 20) & (df.median_house_value > 70000)])
# df2 = df.iloc[:, 0:2]
# print(df2.head())
# print(df2.shape)
