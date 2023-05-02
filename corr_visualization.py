import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ready_data.csv')
data = df.drop(df.columns[df.columns.str.contains('Unnamed', case=False)], axis=1)
data = data.drop(['CarModel'], axis=1)

print(data.head().to_string())

'''Корреляция по carPrice, бензин, гибрид, дизель'''
mask = np.zeros_like(data[['carPrice', 'бензин',  'гибрид',  'дизель']].corr())
triangle_indices = np.triu_indices_from(mask)
mask[triangle_indices] = True
# print(mask)

plt.figure(figsize=(15, 10))
sns.heatmap(data[['carPrice', 'бензин',  'гибрид',  'дизель']].corr(), mask=mask, annot=True, annot_kws={'size': 14})
sns.set_style('white')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

'''Корреляция по carPrice, автомат, вариатор, механика, робот'''
mask = np.zeros_like(data[['carPrice', 'автомат',  'вариатор',  'механика',  'робот']].corr())
triangle_indices = np.triu_indices_from(mask)
mask[triangle_indices] = True
# print(mask)

plt.figure(figsize=(15, 10))
sns.heatmap(data[['carPrice', 'автомат',  'вариатор',  'механика',  'робот']].corr(), mask=mask, annot=True, annot_kws={'size': 14})
sns.set_style('white')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

'''Корреляция по carPrice, 4WD, задний, передний'''
mask = np.zeros_like(data[['carPrice', '4WD',  'задний',  'передний']].corr())
triangle_indices = np.triu_indices_from(mask)
mask[triangle_indices] = True
# print(mask)

plt.figure(figsize=(15, 10))
sns.heatmap(data[['carPrice', '4WD',  'задний',  'передний']].corr(), mask=mask, annot=True, annot_kws={'size': 14})
sns.set_style('white')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()
