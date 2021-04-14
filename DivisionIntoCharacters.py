import pytesseract
import cv2

from PIL import Image, ImageGrab
from time import sleep

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_file = Image.open('D:\Python Progs\TelegramAuthoReg\cache\screanshots\code_1\scr2.png')

image_file = image_file.convert('1') # convert image to black and white
image_file.save(r'D:\Python Progs\TelegramAuthoReg\cache\screanshots\result.png')
#text = pytesseract.image_to_string(Image.open(r'D:\Python Progs\TelegramAuthoReg\cache\screanshots\result.png'))

def CheckingList(list1, str1):

    a = 0
    b = 0

    for data in list1:

        if data == str1:
            a = a + 1

        else:
            b = b+1

    if a == len(list1): 
        return 'all'        #ВСЕ ЭЛЕМЕНТЫ СООТВЕТСТВУЮТ УСЛОВИЮ

    if a>0:
        return True         #ЭЛЕМЕНТ ВСТРЕТИЛСЯ
    if b == len(list1):
        return False        #ЭЛЕМЕНТ НЕ ВСТРЕТИЛСЯ


class GetCodeTg:

    def __init__(self, ImagePath, TesseracConfig = '',ImgSize = [101,24], TesseractPath = r'C:\Program Files\Tesseract-OCR\tesseract.exe'): 
                                                                                                                     
        self.TesseractPath = TesseractPath             
        self.ImagePath = ImagePath                   
        self.TesseracConfig = TesseracConfig
        self.ImgSize = ImgSize

        pytesseract.tesseract_cmd = self.TesseractPath


    def confert(self):
        
        img = Image.open(self.ImagePath)        #делает изобрачение чернобелым
        img.confert('1')
        img.save(self.ImagePath)
        

    def scanimg(self):           #вернет кортеж с кортежами в каждом из которых координаты верх.точки полосы с чер.точками и координатой нижней точки полосы с бел.пикселями
        
        img = Image.open(self.ImagePath)            #работает с изображениями 97x20
    
        self.cord = []          #координаты буквы
        self.FullCordList = []  #координаты всех букв
        colorlist = []
        last = 0
        a= 0 

        for x in range(last, self.ImgSize[0]):
           
            for y in range(0,self.ImgSize[1]):      #pix = 255 - white
                                                    #pix = 0 - black
               pix = img.load()
               pix = pix[x,y]
               
               colorlist.append(pix)

               if len(colorlist) == self.ImgSize[1]:
                    
                   
                    if a >0:
                        #print('2')
                        d = CheckingList(list1 = colorlist, str1 = 255)
                        print(d)
                        if d == 'all':
                            self.cord.append(x)
                            self.cord.append(self.ImgSize[1])
                            self.FullCordList.append(self.cord)
                            self.cord = []
                            a = 0

                    
                    else:
                        #print('3')
                        if  CheckingList(list1 = colorlist, str1 = 0):
                            self.cord.append(x-1)
                            self.cord.append(0)
                            a = a+1
                    colorlist = []
                  


            


                            
                
        return self.FullCordList
                   

g = GetCodeTg(ImagePath=r'D:\Python Progs\TelegramAuthoReg\cache\screanshots\result.png')
a = g.scanimg()
print('1')
#sleep(20)
print(a)
#for a in g:
    #print(i)