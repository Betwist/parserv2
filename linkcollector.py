from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = f'https://sbermarket.ru/magnit_express/'
s = Service(executable_path=r'C:\Users\Betwist\PycharmProjects\parserv2\chromedriver\chromedriver.exe')
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(service=s, options=options)

categoriesLinks = []
try:
    #driver.maximize_window()
    driver.get(url=url)
    time.sleep(10)
    for _ in range(3):
        try:
            driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
            time.sleep(2)
        except:
            print('Кнопки или страниц больше нет')
    cats = driver.find_elements(By.CLASS_NAME, 'CategoryCard_root__LiY3P')
    for i in range(8, len(cats)):
        print(cats[i].text)
        cats[i].click()

        time.sleep(3)
        for _ in range(3):
            try:
                driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
                time.sleep(5)
            except:
                print('ниже некуда')
        catsIn = driver.find_elements(By.CLASS_NAME, 'LinkButton_smSize__Pm2CT')
        for z in catsIn:
             #link = z.find_element(By.TAG_NAME, 'href')
            print(z.get_attribute('href'))
            categoriesLinks.append(z.get_attribute('href'))
        driver.back()
        time.sleep(2)
        for _ in range(3):
            try:
                driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
                time.sleep(2)
            except:
                print('Кнопки или страниц больше нет')
        cats = driver.find_elements(By.CLASS_NAME, 'CategoryCard_root__LiY3P')
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
print(categoriesLinks)