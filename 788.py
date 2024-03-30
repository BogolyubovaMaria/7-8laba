#7 ЛАБОРАТОРНАЯ
from PIL import Image
def zd1():
     image = Image.open('cat.jpg')
     image.show()
# инфо о размере,формате,цветовой модели изображения:
     width,height = image.size
     print("Размер изображения: ",width,"x",height)
     format = image.format
     print("Формат изображения: ",format)
     cvetmodel=image.mode
     print("Цветовая модель изображения: ", cvetmodel)
def zd2():
     image = Image.open("cat.jpg")
     image.show()
     #зеркалим горизонтальное фото
     povorot = image.rotate(180)
     povorot.show()
     mirrorgoriz = povorot.transpose(Image.FLIP_LEFT_RIGHT)
     mirrorgoriz.show()
     #уменьшаем в три раза
     cot1=image.reduce(3)
     cot1.show()
     #поворачиваем изначальный вариант в вертикальный(90 град против часовой)
     rotatevert = image.rotate(90)
     rotatevert.show()
     #вертикально-отзеркаленное
     mirrorvert = rotatevert.transpose(Image.FLIP_LEFT_RIGHT)
     mirrorvert.show()

     image.save('cat1.jpg')
     povorot.save('mirrorgoriz.jpg')
     cot1.save('3raz.jpg')
     rotatevert.save('90gr.jpg')
     mirrorvert.save('mirror90.jpg')

def zd3():
     from PIL import Image,ImageFilter
     images1 = ["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg"]
     for x in images1:
          a = Image.open(x)
          d = a.filter(ImageFilter.EDGE_ENHANCE) #Усиление контраста на границах объектов
          a.show()
          d.save('3zdpy/' + str("novo" + x))
def zd4():
     image = ["rose.jpg","rose2.jpg","rose3.jpg","rose4.jpg"]
     position=(0,0)
     #добавляем водяной знак
     for x in image:
          a = Image.open(x)
          c = Image.open('wat.png')
          a.paste(c,(0,0), mask = c)
          a.show()
          a.save('3zdpy/' + str("watermark" + x))
#8 ЛАБОРАТОРНАЯ
def zd18():
     from PIL import Image, ImageFilter
     image = Image.open("zd18.jpg")
     image.show()
     #text
     croptext=image.crop((0,1600,1122,1754))
     croptext.save('3zdpy/' + str("text.jpg"))
     croptext.show()
     #flowers
     cropflow = image.crop((0, 0, 1122, 1600))
     cropflow.save('3zdpy/' + str("flow.jpg"))
     cropflow.show()
def zd28():
     h = {"Новый год": "zd28.jpg","Пасха": "zd288.jpg","Праздник весны": "zd18.jpg"}
     a = input("Напишите праздник,к которому нужна открытка: ")
     if a in h:
          c = h[a]
          img = Image.open(c)
          img.show()
     else:
          print("Такой открытки у нас нет...")
def zd38():
     from PIL import Image, ImageDraw, ImageFont
     h = {"Новый год": "zd28.jpg", "Пасха": "zd288.jpg", "Праздник весны": "zd18.jpg","Масленница": "zd2888.jpg"}
     a = input("Напишите праздник,к которому нужна открытка: ")
     if a in h:
          c = h[a]
          img = Image.open(c)
          img.show()
          d = input("Введите имя человека,которого вы хотите поздравить: ")
          t = f"{d},с праздником тебя!!!"
          w = ImageDraw.Draw(img)
          font = ImageFont.truetype("arial.ttf", 60 )  # выбираем шрифт и размер
          w.text(((img.width/2-img.height/2),0),t, (0,255,255), font = font,stroke_width=2) #голубой шрифт
          #+ обводка(stroke_width=2)=это жирный формат текста
          img.show()
          img.save('textovi.png')
     else:
          print("Такой открытки у нас нет...")
zd2()