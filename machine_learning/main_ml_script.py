import pandas as pd
import pickle
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


def ml(car_year=int,
       engine_capacity=float,
       horse_power=int,
       car_odo=int,
       car_trans=str,
       fuel_type=str,
       car_drive=str,
       car_mark=str,
       car_model=str
       ):
    """Очищаем DF от значений для последующего ввода новых"""
    for i in df:
        for j in df[f'{i}']:
            df[f'{i}'] = 0

    """ Ввод новых параметров для предикта """
    df['CarYear'] = car_year
    df['EngineCapacity(l)'] = engine_capacity
    df['HorsePower'] = horse_power
    df['CarOdo(KM)'] = car_odo

    for trns in df:
        if car_trans == trns:
            df[f'{trns}'] = 1

    for futype in df:
        if fuel_type == futype:
            df[f'{futype}'] = 1

    for drv in df:
        if car_drive == drv:
            df[f'{drv}'] = 1

    mark_ = car_mark
    model_ = car_model
    for i in df:
        if i == mark_:
            df[f'{i}'] = 1
        elif i == model_:
            df[f'{i}'] = 1

    result = model.predict(df)
    return result[0].round()
