import pandas as pd


df = pd.read_csv('datasets/dfAll2.csv')
df = df.drop(df.columns[df.columns.str.contains('Unnamed', case=False)], axis=1)

# Разделяем колонку 'CarName' на 'Mark' и 'Model'
df[['Mark', 'Model']] = df['CarName'].str.split(n=1, expand=True)
df.drop('CarName', axis=1, inplace=True)

# Из колонки 'CarModel', убираем объем двигателя, т.к он и так парсится
df['CarModel'] = df['CarModel'].str.slice(start=4)

#define columns to move to front
cols_to_move = ['Mark', 'Model', 'CarModel']

#move columns to front
df = df[cols_to_move + [x for x in df.columns if x not in cols_to_move]]

print(df.head().to_string())