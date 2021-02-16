import os
import pyautogui
from time import sleep


def create_file(ip, port):

    f = open(r'D:\Python Progs\TelegramAuthoReg\.reg files\connection_prox.reg', 'r')

    a = f'"ProxyServer"="http://{ip}:{port}"'

    lines = f.readlines()
    lines[8] = a

    f.close()

    f = open(r'D:\Python Progs\TelegramAuthoReg\.reg files\connection_prox.reg', 'w')
 
    f.writelines(lines)

    f.close()


def conn_proxy():

    os.startfile(r'D:\Python Progs\TelegramAuthoReg\bat files\conn_proxy.bat')
    
    sleep(0.25)
    pyautogui.press('enter')

    sleep(0.190)
    pyautogui.press('enter')

    sleep(0.25)
    os.startfile(r'C:\Program Files\Internet Explorer\iediagcmd.exe')

    sleep(6)

def off_proxy():

    os.startfile(r'D:\Python Progs\TelegramAuthoReg\bat files\off_proxy.bat')
    
    sleep(0.25)
    pyautogui.press('enter')

    sleep(0.190)
    pyautogui.press('enter')

    sleep(0.25)
    os.startfile(r'C:\Program Files\Internet Explorer\iediagcmd.exe')

    sleep(6)

#Diagnostics utility for Internet Explorer