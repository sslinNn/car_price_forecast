import pandas as pd
import pickle
# import numpy as np

""" Загружаем данные и обученную модель """
df = pd.read_csv('datasets/ready_data.csv')
data = df.drop(df.columns[df.columns.str.contains('Unnamed', case=False)], axis=1)
data = data.drop(['CarModel'], axis=1)


"""  Создаю шаблон DF для того чтобы в будующем подставлять в него новые значения для поска 'predict'  """
data_test = data.iloc[0:1]
dff = pd.DataFrame(data_test).drop(['carPrice', 'carPriceMin'], axis=1)
df = dff


"""Очищаем DF от значений для последующего ввода новых"""
for i in df:
    for j in df[f'{i}']:
        df[f'{i}'] = 0

"""Сохраняем пустой датасет"""
df.to_csv('datasets/df_for_predict.csv', index=False)
