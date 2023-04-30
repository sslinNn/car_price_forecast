import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder


df = pd.read_csv('datasets/ready_to_final_Preprocessing.csv')

# print(df.head().to_string())
# print(df.Mark.value_counts())
# print(df.Model.value_counts())

ohe = OneHotEncoder()

arrayMark = ohe.fit_transform(df[["Mark"]]).toarray()
labelsMark = ohe.categories_

arrayModel = ohe.fit_transform(df[["Model"]]).toarray()
labelsModel = ohe.categories_

arrayFuel = ohe.fit_transform(df[["CarFuel"]]).toarray()
labelsFuel = ohe.categories_

arrayTransmission = ohe.fit_transform(df[["CarTransmission"]]).toarray()
labelsTransmission = ohe.categories_

arrayDrive = ohe.fit_transform(df[["CarDrive"]]).toarray()
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
df = pd.concat([df, lMark], axis=1)
df = pd.concat([df, lModel], axis=1)
df = pd.concat([df, lFuel], axis=1)
df = pd.concat([df, lTransmission], axis=1)
df = pd.concat([df, lDrive], axis=1)


df = df.drop(['Mark', 'Model', 'CarFuel', 'CarTransmission', 'CarDrive'], axis=1)
print(df.tail(1).to_string())


# df.to_csv('sss.csv', index=Fa)