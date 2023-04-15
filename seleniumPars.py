from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time

useragent = UserAgent()
# options
options = webdriver.FirefoxOptions()
options.set_preference('general.useragent.override', useragent.random)
S = Service('C:\\Users\slinm\Desktop\pythonProject2\firefoxdriver\geckodriver.exe')
driver = webdriver.Firefox(service=S, options=options)


url = f'https://pikabu.ru/best'
try:
    driver.get(url=url)
    time.sleep(20)

    story = driver.find_elements(By.CLASS_NAME, 'story__main')

    all_links = {}
    for j in range(2):
        title2 = driver.find_elements(By.CLASS_NAME, 'story__title')
        for i in len(title2):
            title = driver.find_elements(By.CLASS_NAME, 'story__title')[i].text
            href = driver.find_elements(By.CLASS_NAME, 'story__title')[i].find_element(By.TAG_NAME, 'a').get_attribute('href')
            all_links[title] = [href]
            print(f'{title} : {href}')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

    print(all_links)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
