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

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


def ml(car_year=int, engine_capacity=float, horse_power=int, car_odo=int):
    """ Ввод новых параметров для предикта """
    df['CarYear'] = car_year
    df['EngineCapacity(l)'] = engine_capacity
    df['HorsePower'] = horse_power
    df['CarOdo(KM)'] = car_odo
    df['бензин'] = 1
    df['автомат'] = 1
    df['передний'] = 1

    a = 'Lexus'
    b = 'LX570'
    for i in df:
        if i == a:
            df[f'{i}'] = 1
        elif i == b:
            df[f'{i}'] = 1

    result = model.predict(df)
    return result[0].round()

res = ml(car_year=2000, car_odo=243, engine_capacity=1.6, horse_power=160)
print(res)
