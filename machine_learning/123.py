import pandas as pd
import pickle

df = pd.read_csv('datasets/df_for_predict.csv')

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

""" Ввод новых параметров для предикта """
df['CarYear'] = 2005
df['EngineCapacity(l)'] = 2.5
df['HorsePower'] = 165
df['CarOdo(KM)'] = 222
df['бензин'] = 1
df['автомат'] = 1
df['4WD'] = 1
df['Subaru'] = 1
df['Outback'] = 1


a = 'Audi'
b = 'BMW'
for i in df:
    if i == a:
        df[f'{i}'] = 1
    elif i == b:
        df[f'{i}'] = 1


result = model.predict(df)
print(df.head().to_string())
print('Price - ', result[0].round())
