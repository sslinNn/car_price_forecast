import pandas as pd

# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)
# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)
# Сброс переноса
pd.options.display.expand_frame_repr = False

df = pd.read_csv('carsDF.csv', index_col=[0])

print(df)