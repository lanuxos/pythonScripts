# EP.4 Selenium
import wikipedia, os, time
from selenium import webdriver

wikipedia.set_lang('th')

imgfile = os.listdir('../asset/')   # current directory
os.chdir('../asset/')   # go back one step
mainpath = os.path.abspath(os.curdir)   # get current file directory
# mainpath = os.getcwd()    # get current working directory || current execute directory
# print(imgfile)
wordlist = []
pathlist = []
for img in imgfile:
    if img[-3:] == 'png':
        # print(img)
        fn = img.split('.')[0]
        wordlist.append(fn)
        path = os.path.join(mainpath, img)
        # print(path)
        pathlist.append(path)

# print(wordlist)
alltitle = []
alldata = []
allprice = [1000,2000,3000]
for wl in wordlist:
    try:
        data = wikipedia.summary(wl)
        alltitle.append(wl)
        alldata.append(data)
        # print(wl, data)
        # print('----')
    except:
        alltitle.append(wl)
        alldata.append('Data not found')
driverpath = '/Users/la/www/pythonBootCamp/code/chromedriver'
driver = webdriver.Chrome(driverpath)

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

for pn, pp, pd, pt in zip(alltitle, allprice, alldata, pathlist):
    pdname = driver.find_element_by_id('name')
    pdprice = driver.find_element_by_id('price')
    pddetail = driver.find_element_by_id('detail')
    photo = driver.find_element_by_id('photo')

    # pd1_name = pn
    # pd1_price = pp
    # pd1_detail = pd
    # photopath = pt

    pdname.send_keys(pn)
    pdprice.send_keys(pp)
    pddetail.send_keys(pd)
    photo.send_keys(pt)

    time.sleep(3)

    button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
    button.click()
