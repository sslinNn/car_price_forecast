import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)
# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

carTitle = []
carYear = []
carModel = []
carEc = []
carHp = []
carFuel = []
carTransm = []
carDrive = []
carOdo = []
carPrice_ = []
carPriceMin_ = []
highPrice_ = []
goodPrice_ = []
defltPrice_ = []
removed_ = []
minPrice_ = []
i = 0
n = 0

for i in range(2):
    url = f'https://auto.drom.ru/all/page{i}/'
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

# with open('index.html', 'w') as file:
#     file.write(response.text)
#
# with open('index.html') as file:
#     src = file.read()
# soup = BeautifulSoup(src, 'lxml')

    for n in range(20):
        time.sleep(1)
        car = soup.find('div', class_='css-1nvf6xk eojktn00').findAll('div', class_='css-13ocj84 e1icyw250')[n]
        data_list = []
        for data_elem in car:
            try:
                price = data_elem.text.replace(' ', '')
            except AttributeError:
                price = None
            if '.css' in price:
                pass
            else:
                data_list.append(price)

        strg = ' '.join(data_list)


        Title = []
        for symbol in strg:
            if symbol != ',':
                Title.append(symbol)
            else:
                break
        Title = ''.join(Title)



        strg = strg[len(Title) + 2::]
        year = strg[0:4]
        strg = strg[len(year)::]



        symbol = ''
        model = []
        for symbol in strg:
            model.append(symbol)
            if 'л' in symbol:
                break
        model = ''.join(model)[:-2:]



        if len(model) > 6:
            eC = model[:3:]
            model = model[0:-4:]
            strg = strg[len(eC) + len(model) + 2::]
        else:
            eC = model[1::]
            model = None
            strg = strg[len(eC) + 2::]



        hp = []
        symbol = ''
        for symbol in strg:
            hp.append(symbol)
            if ')' in symbol:
                break


        strg = strg[len(hp)+2::]
        hp = ''.join(hp)[3:6]


        fuel = []
        symbol = ''
        for symbol in strg:
            fuel.append(symbol)
            if ',' in symbol:
                break
        strg = strg[len(fuel)+1::]
        fuel = ''.join(fuel)[:-1:]

        trans = []
        symbol = ''
        for symbol in strg:
            trans.append(symbol)
            if ',' in symbol:
                break
        strg = strg[len(trans)+1::]
        trans = ''.join(trans)[:-1:]

        drive = []
        symbol = ''
        for symbol in strg:
            drive.append(symbol)
            if ',' in symbol:
                strg = strg[len(drive) + 1::]
                drive = ''.join(drive)[:-1:]
                break
            elif ' ' in symbol:
                strg = strg[len(drive)::]
                drive = ''.join(drive)[:-1:]
                break

        if strg == 'новый':
            odo = 0
        else:
            odo = strg.replace('тыс. км', '').replace(' ', '').replace('отсобственника', '')

        """------------------------------------------------------------------------------------------------------"""

        car = soup.find('div', class_='css-1nvf6xk eojktn00').findAll('div', class_='css-1dkhqyq e1f2m3x80')[n]

        priceList = []
        for price_elem in car:
            try:
                price = price_elem.text.replace(' ', '')
            except AttributeError:
                price = None
            if '.css' in price:
                pass
            else:
                priceList.append(price)


        priceSTR = ' '.join(priceList)

        carPrice = []
        symbol = ''
        for symbol in priceSTR:
            carPrice.append(symbol)
            if '₽' in symbol:
                break

        priceSTR = priceSTR[len(carPrice)::]
        carPrice = ' '.join(carPrice).replace(' ', '')[:-1:]


        if priceSTR[:3:] == 'выс':
            priceSTR = priceSTR[13::]
            highPrice = 1
        else:
            highPrice = 0

        if priceSTR[:3:] == 'хор':
            priceSTR = priceSTR[13::]
            goodPrice = 1
        else:
            goodPrice = 0

        if priceSTR[:3:] == 'нор':
            priceSTR = priceSTR[16::]
            defltPrice = 1
        else:
            defltPrice = 0

        if priceSTR[:3:] == 'отл':
            priceSTR = priceSTR[14::]
            greatPrice = 1
        else:
            greatPrice = 0

        if priceSTR[:3:] == 'сня':
            priceSTR = priceSTR[15::]
            removed = 1
        else:
            removed = 0

        if priceSTR[:3:] == 'мин':
            strrr = priceSTR[16::]
            carPriceMin = []
            symbol = ''
            for symbol in strrr:
                carPriceMin.append(symbol)
                if '₽' in symbol:
                    break
            carPriceMin = ' '.join(carPriceMin).replace(' ', '')[:-1:]
            minPrice = 1
        else:
            carPriceMin = None
            minPrice = 0

        carTitle.append(Title)
        carYear.append(year)
        carModel.append(model)
        carEc.append(eC)
        carHp.append(hp)
        carFuel.append(fuel)
        carTransm.append(trans)
        carDrive.append(drive)
        carOdo.append(odo)
        carPrice_.append(carPrice)
        carPriceMin_.append(carPriceMin)
        highPrice_.append(highPrice)
        goodPrice_.append(goodPrice)
        defltPrice_.append(defltPrice)
        removed_.append(removed)
        minPrice_.append(minPrice)


        # print(f'{Title} * {year} * {model} * {eC} * {hp} * {fuel} * {trans} * {drive} * {odo} * price - {carPrice} * minCarPrice - {carPriceMin} * highPrice - {highPrice} * goodPrice - {goodPrice} * defltPrice - {defltPrice} * removed - {removed} * minPrice - {minPrice}')

    df = pd.DataFrame({
        'CarName': carTitle,
        'CarYear': carYear,
        'CarModel': carModel,
        'EngineCapacity(l)': carEc,
        'HorsePower': carHp,
        'CarFuel': carFuel,
        'CarTransmission': carTransm,
        'CarDrive': carDrive,
        'CarOdo(KM)': carOdo,
        'carPrice': carPrice_,
        'carPriceMin': carPriceMin_,
        'highPrice': highPrice_,
        'goodPrice': goodPrice_,
        'defltPrice': defltPrice_,
        'removed': removed_,
        'minPrice': minPrice_,
    })


    print(f'Страница - {i}')

df.to_csv('carsDF.csv', encoding='utf-8')

print(df)
