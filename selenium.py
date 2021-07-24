# EP.3 Selenium
import wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driverpath = '/Applications/chromedriver'
driverpath = '/Users/la/www/pythonBootCamp/code/chromedriver'
driver = webdriver.Chrome(driverpath)

# browser = webdriver.Chrome(executable_path='/Applications/chromedriver')
# browser.get('https://www.google.com')

url = 'http://uncle-machine.com/login/'
driver.get(url)

username = driver.find_element_by_id('username')
username.send_keys('pythonbootcamprpa@gmail.com')
password = driver.find_element_by_id('password')
password.send_keys('1234')
button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
button.click()
# password.send_keys(Keys.RETURN)

addurl = 'http://uncle-machine.com/addproduct/'
driver.get(addurl)

pdname = driver.find_element_by_id('name')
pdprice = driver.find_element_by_id('price')
pddetail = driver.find_element_by_id('detail')

pd1_name = 'Micro Python Pico'
pd1_price = 1000
pd1_detail = 'Python IoT Course with pico board'

pdname.send_keys(pd1_name)
pdprice.send_keys(pd1_price)
pddetail.send_keys(pd1_detail)

button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
button.click()
