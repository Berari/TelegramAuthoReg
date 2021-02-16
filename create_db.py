import sqlite3 as sql
from datetime import date

con = sql.connect('Accounts.db')
cur = con.cursor()
def create_table(con):
    
    
    cur = con.cursor()
    cur.execute("""CREATE TABLE telegram (
        ID INTEGER PRIMARY KEY,
        PHONE TEXT,
        PASSWORD TEXT,
        API_ID TEXT,
        API_HASH TEXT,
        LITECOIN TEXT
        )

    """)
    con.commit()


def write_in_db(cur, ID, PHONE, PASSWORD, API_ID, API_HASH, LITECOIN):
    while True:
        #ID = 4
        #PHONE = input('PHONE: ')
        #PASSWORD = input('PASSWORD: ')
        #API_ID = input('API_ID: ')
        #API_HASH = input('API_HASH: ') 
        #LITECOIN = input('LITECOIN: ')


        cur.execute("""INSERT INTO telegram (
            ID,
            PHONE, 
            PASSWORD, 
            API_ID, 
            API_HASH,
            LITECOIN
            ) 
            VALUES (?,?,?,?,?,?);""", 
            (ID,PHONE, PASSWORD, API_ID, API_HASH,LITECOIN,))

        con.commit()

        print("Зарегистрированно!")

def proxy_create_db():
    
    con = sql.connect('proxy.db')
    cur = con.cursor()

    cur.execute("""CREATE TABLE proxy (
        IP TEXT,
        PORT INT
        )

    """)
    con.commit()

def proxy():

    con = sql.connect('proxy.db')
    cur = con.cursor()

    IP = '51.158.68.133'
    PORT = 8811
    
    cur.execute("""INSERT INTO proxy (
            IP,
            PORT
            ) 
            VALUES (?,?);""", 
            (IP,PORT))

    con.commit()

proxy()
#proxy_create_db()
