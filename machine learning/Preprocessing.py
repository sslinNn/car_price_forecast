import re
import pandas as pd
import numpy as np
import pathlib
import pathlib as pathlib
from sklearn.preprocessing import OneHotEncoder


# # Сброс ограничений на количество выводимых рядов
# pd.set_option('display.max_rows', None)
# # Сброс ограничений на число столбцов
# pd.set_option('display.max_columns', None)
# # Сброс ограничений на количество символов в записи
# pd.set_option('display.max_colwidth', None)

# чтение данных из CSV-файла
data = pd.read_csv('datasets/dfAll.csv')
# data = data.drop(data.columns[data.columns.str.contains('Unnamed', case=False)], axis=1)

# создание маски
date_regex = r'\d\.\d'
mask = data['EngineCapacity(l)'].str.match(date_regex)
data = data.loc[mask]

date_regex2 = r'\d'
mask2 = data['HorsePower'].str.match(date_regex2)
data = data.loc[mask2]

date_regex3_1 = r'\d\d\d'
date_regex3_2 = r'\d\d'
date_regex3_3 = r'\d'
combined_regex = f"({date_regex3_1})|({date_regex3_2})|({date_regex3_3})"

data['CarOdo(KM)'].fillna(value='0', inplace=True)
mask3 = data['CarOdo(KM)'].str.match(combined_regex)
data = data.loc[mask3]

# функция для удаления букв из каждой ячейки данных
def remove_letters(s):
    return re.sub('[^0-9]+', '', s)

# применение функции к каждой ячейке данных с помощью applymap()
data['CarOdo(KM)'] = data['CarOdo(KM)'].apply(remove_letters)
data['HorsePower'] = data['HorsePower'].str.replace('2 л', '0')


# Разделяем колонку 'CarName' на 'Mark' и 'Model'
data[['Mark', 'Model']] = data['CarName'].str.split(n=1, expand=True)
data.drop('CarName', axis=1, inplace=True)

# Из колонки 'CarModel', убираем объем двигателя, т.к он и так парсится
data['CarModel'] = data['CarModel'].str.slice(start=4)

#define columns to move to front
cols_to_move = ['Mark', 'Model', 'CarModel']

#move columns to front
data = data[cols_to_move + [x for x in data.columns if x not in cols_to_move]]

data.to_csv('ready_data 0_5.csv', index=False)
data = pd.read_csv('ready_data 0_5.csv')


data['CarFuel'] = data['CarFuel'].str.replace('автомат', '').str.replace('механика', '')
data['CarTransmission'] = data['CarTransmission'].str.replace('4WD', '').str.replace('АКПП', 'автомат').str.replace('передний', '')
data['CarDrive'] = data['CarDrive'].str.replace("['4', 'W', 'D']", '4WD')
for i in data['CarDrive']:
    pattern = r"^\d+$"
    result = re.search(pattern, i)
    if result:
        data['CarDrive'] = data['CarDrive'].str.replace(i, '')


ohe = OneHotEncoder()
# data['EngineCapacity(l)'] = pd.to_numeric(data['EngineCapacity(l)'])
# data['HorsePower'] = pd.to_numeric(data['HorsePower'])
# data['CarOdo(KM)'] = pd.to_numeric(data['CarOdo(KM)'])


arrayMark = ohe.fit_transform(data[["Mark"]]).toarray()
labelsMark = ohe.categories_

arrayModel = ohe.fit_transform(data[["Model"]]).toarray()
labelsModel = ohe.categories_

arrayFuel = ohe.fit_transform(data[["CarFuel"]]).toarray()
labelsFuel = ohe.categories_

arrayTransmission = ohe.fit_transform(data[["CarTransmission"]]).toarray()
labelsTransmission = ohe.categories_

arrayDrive = ohe.fit_transform(data[["CarDrive"]]).toarray()
labelsDrive = ohe.categories_

labelsMark = np.array(labelsMark, dtype='object').ravel()
labelsModel = np.array(labelsModel, dtype='object').ravel()
labelsFuel = np.array(labelsFuel, dtype='object').ravel()
labelsTransmission = np.array(labelsTransmission, dtype='object').ravel()
labelsDrive = np.array(labelsDrive, dtype='object').ravel()


# print(labelsMark)
# print(labelsModel)

lMark = pd.DataFrame(arrayMark, columns=labelsMark)
lModel = pd.DataFrame(arrayModel, columns=labelsModel)
lFuel = pd.DataFrame(arrayFuel, columns=labelsFuel)
lTransmission = pd.DataFrame(arrayTransmission, columns=labelsTransmission)
lDrive = pd.DataFrame(arrayDrive, columns=labelsDrive)


#Присоединяем то, что наВанХотЕнкодерили
data = pd.concat([data, lMark], axis=1)
data = pd.concat([data, lModel], axis=1)
data = pd.concat([data, lFuel], axis=1)
data = pd.concat([data, lTransmission], axis=1)
data = pd.concat([data, lDrive], axis=1)

data = data.drop(['Mark', 'Model', 'CarFuel', 'CarTransmission', 'CarDrive'], axis=1)

data.to_csv('datasets/ready_data.csv', index=False)
file = pathlib.Path("ready_data 0_5.csv")
file.unlink()