import re
import pandas as pd

df = pd.read_csv('datasets/backupALL2.csv')
df = df.drop(df.columns[df.columns.str.contains('Unnamed', case=False)], axis=1)

df['CarFuel'] = df['CarFuel'].str.replace('автомат', '').str.replace('механика', '')
df['CarTransmission'] = df['CarTransmission'].str.replace('4WD', '').str.replace('АКПП', 'автомат').str.replace('передний', '')
df['CarDrive'] = df['CarDrive'].str.replace("['4', 'W', 'D']", '4WD')
for i in df['CarDrive']:
    pattern = r"^\d+$"
    result = re.search(pattern, i)
    if result:
        df['CarDrive'] = df['CarDrive'].str.replace(i, '')


df.to_csv('datasets/ready_to_final_Preprocessing.csv', encoding='utf-8', index=False)