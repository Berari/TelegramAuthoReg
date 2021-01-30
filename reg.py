from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from telethon import TelegramClient, events, sync
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs4

import requests
import sqlite3


class DataBase:

    def __init__(self, con):
        
        self.con = con
        self.cursorObj = self.con.cursor()


    def number_of_entries(self): #возвращает кол во записей в дб
        
        self.cursorObj.execute('SELECT * FROM telegram')

        rows = self.cursorObj.fetchall()
        
        number_of_entries = len(rows)

        return number_of_entries


class SmsActive:
    pass

class reg:
    
    def __init__(self, bot_id, phone):
        pass
