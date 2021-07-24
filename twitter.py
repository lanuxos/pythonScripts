# EP.6 Twitter Scrapping via Selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time

path = "/Users/la/www/pythonBootCamp/code/chromedriver"
opt = webdriver.ChromeOptions()
opt.add_argument('headless')
# driver = webdriver.Chrome(path, options=opt)
driver = webdriver.Chrome(path)

def Twitter(url):
    url = url # 'https://twitter.com/bbcworld'
    driver.get(url)
    time.sleep(5)
    content = driver.page_source  # fetch html
    data = BeautifulSoup(content, 'html.parser')
    posts = data.find_all('span', {'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
    dot = False
    allpost = []
    for p in posts:
        text = p.text
        if dot == True:
            allpost.append(text)
            print(text)
            print('----------')
            dot = False
        if text == '·':
            dot = True

    driver.close()
    return allpost


bbc = Twitter('https://twitter.com/bbcworld')
# print(bbc)
