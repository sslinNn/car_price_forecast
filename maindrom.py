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

#IndexError
car = soup.find('div', class_='css-1nvf6xk eojktn00').findAll('div', class_='css-13ocj84 e1icyw250')[1]

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
print(data_list)

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

print(Title)
print(year)
model = ''.join(model)
if len(model) > 6:


print(model, len(model))
