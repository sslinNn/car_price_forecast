import pandas as pd
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)
# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)
# чтение данных из CSV-файла

# data = pd.read_csv('carsDFreg28_2.csv')
df = pd.read_csv('datasets/dfAll2.csv')
df = df.drop(df.columns[df.columns.str.contains('Unnamed',case=False)],axis=1)

# Шаг 2: Предобработка данных
df.drop(['CarName', 'carPriceMin', 'defltPrice', 'removed', 'minPrice', 'CarModel'], axis=1, inplace=True)
df = pd.get_dummies(df, columns=['CarFuel', 'CarTransmission', 'CarDrive', 'highPrice', 'goodPrice'], drop_first=True)
df.dropna(inplace=True)

# Разбиение данных на обучающую и тестовую выборки
X = df.drop('carPrice', axis=1)
y = df['carPrice']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

gb = GradientBoostingRegressor(learning_rate=0.2, n_estimators=300, random_state=42)
gb.fit(X_train, y_train)


score = gb.score(X_test, y_test)
print('Score градиентного бустинга:', score)



# with open('model.pickle', 'wb') as f:
#     pickle.dump(gb, f)
# f.close()

# with open('model.pickle', 'rb') as f:
#     gb = pickle.load(f)
#
# new_data = {
#     '':''
# }
#
# prediction = gb.predict(new_data)
# print(prediction)



