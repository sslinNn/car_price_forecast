import re
import pandas as pd


# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)
# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)

# чтение данных из CSV-файла
data = pd.read_csv('carsDFreg28_2.csv')


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
