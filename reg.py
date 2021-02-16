from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from telethon import TelegramClient, events, sync
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs4
from time import sleep

import requests
import sqlite3
import pyautogui

import proxy_parser
import create_session
import SmsActiveAPI


class GetApiData:

    def __init__(self,phone):
        
        self.phone = phone


class DataBase:

    def __init__(self, con):
        
        self.con = con
        self.cursorObj = self.con.cursor()


    def number_of_entries(self): #возвращает кол во записей в дб
        
        self.cursorObj.execute('SELECT * FROM telegram')

        rows = self.cursorObj.fetchall()
        
        number_of_entries = len(rows)

        return number_of_entries

    def write_in_db(self, ID, PHONE, PASSWORD, API_ID, API_HASH, LITECOIN):

        self.cursorObj.execute("""INSERT INTO telegram (
            ID,
            PHONE, 
            PASSWORD, 
            API_ID, 
            API_HASH,
            LITECOIN
            ) 
            VALUES (?,?,?,?,?,?);""", 
            (ID,PHONE, PASSWORD, API_ID, API_HASH,LITECOIN,))

        self.con.commit()



class Telegram:

    def __init__(self, api_key):
        self.api_key = api_key
        self.sms = SmsActiveAPI.SmsActive(api_key)

    def reg(self, phone, id):          #работает если в клиенте 1 аккаунт
    
        pyautogui.click(29, 93)
        sleep(0.25)
        pyautogui.click(243, 166)
        sleep(0.25)
        pyautogui.click(58, 257)
        sleep(0.25)
        pyautogui.click(968, 733)
        sleep(0.25)

        phone = phone[1 : 11]

        pyautogui.typewrite (phone)
        sleep(0.25)
        pyautogui.click(903, 662)

        self.sms.changing_activation_status(id = id, status = 1)

        sleep(10)

        code = sms.get_full_sms(id).split('code')[1].split(' ')[1]
        print(code)
        pyautogui.typewrite(code)

    def exit(self):         #работает если в клиенте 2 аккаунта
    
        pyautogui.click(29, 93)
        sleep(0.25)
        pyautogui.click(48, 517)
        sleep(0.25)
        pyautogui.click(1074, 138)
        sleep(0.25)
        pyautogui.click(1015, 254)
        sleep(0.25)
        pyautogui.click(1055, 606)


if __name__ == '__main__':
    sleep(3)
    api_key = 'b720Af9f1b59bf58ebbc91f8b5404A77'
    tele = Telegram(api_key)
    a = True
    #tele.exit()

    sms = SmsActiveAPI.SmsActive(api_key)
 
    #con.conn(proxy_port = '8080', proxy_id = '1234.56')
    #con.conn(proxy_id = '4534.665', proxy_port = '8081')
    #while a == True:

        #data = sms.get_phone_number(service = 'tg')

        #if data == 'NO_NUMBERS':
            #pass

        #else:
       
            #id = data[0]
            #phone = data[1]
            #a = False
            #tele.reg(phone, id)


