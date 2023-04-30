import pandas as pd
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)
# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)
# чтение данных из CSV-файла

# data = pd.read_csv('carsDFreg28_2.csv')
df = pd.read_csv('ready_data.csv')
df = df.drop(df.columns[df.columns.str.contains('Unnamed',case=False)],axis=1)

print(df.tail(10).to_string())
