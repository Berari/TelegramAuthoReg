from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from time import sleep
from PIL import Image
import random, string
import pyautogui

def randomword(length):
    
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def get_code(self,mode, screanshoot):  #entrance, telegram.core
        
    def get_text():
        pass


    if mode == 'entrance':
        screen = pyautogui.screenshot('screenshot.png')

    if mode == 'telegram.core':
        pass

def Browser():

    DATA_LIST = []

    options = Options()
    options.add_argument("user-agent=[Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36]")    #Автоизация
 
    driver = webdriver.Firefox(executable_path='D:\geckodriver-v0.29.0-win64\geckodriver.exe', options=options)
    driver.get('https://my.telegram.org/auth')
    element = driver.find_element_by_id("my_login_phone")
    element.send_keys("79995517622")
    sleep(0.5)
    #pyautogui.press('enter')

    driver.find_element_by_tag_name('body').send_keys(Keys.ENTER)
    code = str(input('code: '))
    
    element = driver.find_element_by_id("my_password")
    sleep(0.125)
    element.send_keys(code)
    sleep(0.5)
    element.send_keys(Keys.ENTER)
    sleep(0.5)
    button = driver.find_element_by_partial_link_text('API development tools')  #Создание приложения
    button.click()

    sleep(0.5)
    driver.find_elements_by_id('app_title')[0].send_keys(randomword(length = 8))
    sleep(0.25)
    driver.find_elements_by_id('app_shortname')[0].send_keys(randomword(length = 6))
    sleep(0.25)
    driver.find_element_by_id('app_save_btn').click()
    sleep(0.5)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')   

    API_ID_DATA = soup.find('div', class_ = 'container tl_page_container').find('div', class_ = 'tl_page').find('div', class_ = 'app_edit_page').find('div', class_ = 'form-group').find('div', class_ = 'col-md-7').find('span', class_='form-control input-xlarge uneditable-input')
    API_HESH_DATA = soup.find('div', class_ = 'container tl_page_container').find('div', class_ = 'tl_page').find('div', class_ = 'app_edit_page').find_all('div', class_ = 'form-group')[1].find('div', class_ = 'col-md-7').find('span', class_ = 'form-control input-xlarge uneditable-input')
    
    API_ID = str(API_ID_DATA).split('<')[2].split('>')[1]
    API_HESH = str(API_HESH_DATA).split('>')[1].split('<')[0]

    DATA_LIST.append(API_ID)
    DATA_LIST.append(API_HESH)

    

    return DATA_LIST
Browser()