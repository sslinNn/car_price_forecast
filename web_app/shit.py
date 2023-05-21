import pandas as pd

marks = 'Марка,Acura,Alfa,Audi,BMW,BYD,Brilliance,Cadillac,Changan,Chery,Chevrolet,' \
        'Chrysler,Citroen,Daewoo,Daihatsu,Datsun,Dodge,Dongfeng,EXEED,FAW,Fiat,Ford,' \
        'Geely,Genesis,Great,Hafei,Haval,Honda,Hummer,Hyundai,Infiniti,Isuzu,JAC,Jaguar,' \
        'Jeep,Jetour,Jetta,Kia,Land,Lexus,Li,Lifan,Lincoln,MINI,Mazda,Mercedes-Benz,' \
        'Mitsubishi,Nissan,OMODA,Opel,Peugeot,Pontiac,Porsche,RAM,Ravon,Renault,Rover,' \
        'SEAT,Saab,Skoda,Smart,SsangYong,Subaru,Suzuki,Tianye,Toyota,Volkswagen,Volvo,' \
        'Vortex,Богдан,ГАЗ,ЗАЗ,ИЖ,Лада,ЛуАЗ,Москвич,Прочие'

mrk_list = marks.split(sep=',')
df = pd.read_csv(r'C:\Users\slinm\Desktop\pythonProject2\machine_learning\datasets\ready_data.csv')
df = df.drop(['CarModel', 'carPriceMin', 'highPrice', 'goodPrice', 'defltPrice', 'removed', 'minPrice'], axis=1)
df = df.drop(df.columns[df.columns.str.contains('Unnamed', case=False)], axis=1)
# print(df.head(1).to_string())

df2 = pd.read_csv(r'C:\Users\slinm\Desktop\pythonProject2\machine_learning\datasets\dfAll.csv')
df2 = df2.drop(['CarModel', 'carPriceMin', 'highPrice', 'goodPrice', 'defltPrice', 'removed', 'minPrice'], axis=1)
df2 = df2.drop(df2.columns[df2.columns.str.contains('Unnamed', case=False)], axis=1)
# print(df2.head(1).to_string())


unq = df2['CarName'].unique()

car_dict = {}

for car in unq:
    brand, model = car.split(' ', 1)
    if brand in car_dict:
        car_dict[brand].append(model)
    else:
        car_dict[brand] = [model]
