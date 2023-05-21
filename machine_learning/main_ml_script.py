import pandas as pd
import pickle
from class__ import Car
# import numpy as np

""" Загружаем данные и обученную модель """
df = pd.read_csv(r'C:\Users\slinm\Desktop\pythonProject2\machine_learning\datasets\ready_data.csv')
data = df.drop(df.columns[df.columns.str.contains('Unnamed', case=False)], axis=1)
data = data.drop(['CarModel'], axis=1)


"""  Создаю шаблон DF для того чтобы в будующем подставлять в него новые значения для поска 'predict'  """
data_test = data.iloc[0:1]
dff = pd.DataFrame(data_test).drop(['carPrice', 'carPriceMin'], axis=1)
df = dff



with open(r'C:\Users\slinm\Desktop\pythonProject2\machine_learning\model.pkl', 'rb') as f:
    model = pickle.load(f)



def ml(car):
    """Очищаем DF от значений для последующего ввода новых"""
    for i in df:
        for j in df[f'{i}']:
            df[f'{i}'] = 0

    """ Ввод новых параметров для предикта """
    df['CarYear'] = car.CarYear
    df['EngineCapacity(l)'] = car.EngineCapacity
    df['HorsePower'] = car.HorsePower
    df['CarOdo(KM)'] = car.CarOdo

    for trns in df:
        if car.CarTrans == trns:
            df[f'{trns}'] = 1

    for futype in df:
        if car.FuelType == futype:
            df[f'{futype}'] = 1

    for drv in df:
        if car.CarDrive == drv:
            df[f'{drv}'] = 1

    mark_ = car.CarMark
    model_ = car.CarModel
    for i in df:
        if i == mark_:
            df[f'{i}'] = 1
        elif i == model_:
            df[f'{i}'] = 1

    result = model.predict(df)
    return result[0].round()


def save_object(obj, filename):
    with open(filename, 'wb') as outp:
        pickle.dump(obj, outp, -1)
