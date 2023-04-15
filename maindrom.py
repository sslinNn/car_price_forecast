import requests
from bs4 import BeautifulSoup

# headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
# }
#
# url = f'https://auto.drom.ru/all/page1/'
# response = requests.get(url=url, headers=headers)
#
# with open('index.html', 'w') as file:
#     file.write(response.text)

with open('index.html') as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml')

car = soup.find('div', class_='css-1nvf6xk eojktn00').findAll('div', class_='css-13ocj84 e1icyw250')[5]

data_list = []
for data_elem in car:
    try:
        data = data_elem.text.replace(' ', '')
    except AttributeError:
        data = None
    if '.css' in data:
        pass
    else:
        data_list.append(data)

strg = ' '.join(data_list)
print(strg)


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
    odo = strg.replace('тыс. км', '').replace(' ', '')

print(f'{Title} * {year} * {model} * {eC} * {hp} * {fuel} * {trans} * {drive} * {odo} *')
