import requests
from bs4 import BeautifulSoup
import pandas as pd


# df = pd.DataFrame({
#     'Title' : [0],
#     'Href' : [0]
# })

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

i = 0
while i < 1:

    url = f'https://pikabu.ru/best'
    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        for j in range(10):
            story = soup.findAll('div', class_='story__main')[j]
            storyTitle = story.find('h2', class_='story__title').text
            storyHref = story.find('h2', class_='story__title').find('a').get('href')

            # new_row = pd.DataFrame({'Title': storyTitle, 'Href': storyHref}, index=[0])
            # df = pd.concat([new_row, df]).reset_index(drop=True)


            print(storyTitle)
            # with open('links.json', 'w', encoding='utf-8') as f:
            #     f.write(f'{storyTitle} : {storyHref}')

        i += 1
    else:
        print('Ошибка при загрузке страницы:', response.status_code)
        break