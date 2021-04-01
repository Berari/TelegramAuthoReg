

import pytesseract

from PIL import Image, ImageGrab, ImageDraw



def get_message_text(id:int):
    

    pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    #time.sleep(3)
    #pyautogui.click(35, 143)

    #image = pyautogui.screenshot(region=(322,859, 420, 876))
    #img = ImageGrab.grab( (322,859, 423, 883) )
    #img.save(f"D:\Python Progs\TelegramAuthoReg\cache\screanshots\scr{id}.png")

   

    
    text=pytesseract.image_to_string(Image.open(r'D:\Python Progs\TelegramAuthoReg\cache\screanshots\result.png'), lang='eng', config='--psm 6 -c tessedit_char_whitelist=0123456789')
    
    print(text)
    
    
get_message_text(id = 2)