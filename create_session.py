from telethon import TelegramClient, sync
import sqlite3
import time




db = sqlite3.connect('Accounts.db')
cur = db.cursor()



def create_session(cur, x):
    print("Очередь аккаунта № " + str(x))
    cur.execute(f"SELECT PHONE FROM telegram WHERE ID = '{x}'")
    time.sleep(0.2)
    Phone = str(cur.fetchone()[0])
    print("Входим в аккаунт: " + Phone)
    cur.execute(f"SELECT PASSWORD FROM telegram WHERE ID = '{x}'")
    time.sleep(0.2)
    password = str(cur.fetchone()[0])
    print(password)
    cur.execute(f"SELECT API_ID FROM telegram WHERE ID = '{x}'")
    time.sleep(0.2)
    api_id = str(cur.fetchone()[0])
    cur.execute(f"SELECT API_HASH FROM telegram WHERE ID = '{x}'")
    time.sleep(0.2)
    api_hash = str(cur.fetchone()[0])
    session = str("sessions/anon" + str(x))
    client = TelegramClient(session, api_id, api_hash)
    client.start()