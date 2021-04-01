import pytesseract
import cv2
from PIL import Image, ImageGrab

a = pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_file = Image.open('D:\Python Progs\TelegramAuthoReg\cache\screanshots\code_1\scr2.png')

image_file = image_file.convert('1') # convert image to black and white
image_file.save(r'D:\Python Progs\TelegramAuthoReg\cache\screanshots\result.png')
text = pytesseract.image_to_string(Image.open(r'D:\Python Progs\TelegramAuthoReg\cache\screanshots\result.png'))

class GetCodeInTg:

    def __init__(self, TesseractPath, ImagePath, TesseracConfig = ''): 
                                                                                                                     
        self.TesseractPath = TesseractPath             
        self.ImagePath = ImagePath                   
        self.TesseracConfig = TesseracConfig

        pytesseract.tesseract_cmd = self.TesseractPath


    def confert(self):
        
        img = Image.open(self.ImagePath)        #делает изобрачение черно-белым
        img.confert('1')
        img.save(self.ImagePath)
        

    def convertfile(self):           #разделит изображения на отдельные символы
        
        img = Image.open(self.ImagePath)            #работает с изображениями 97x20
        x = 0
        cord1 = 0
        cord2 = 0

       while x<=97: 
           
           for y in range(0,20)