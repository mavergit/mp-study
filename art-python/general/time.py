import time
import datetime

# для расширенной цветовой палитры терминала можно использовать библиотеку rich
# установка с помощью команды
# pip install rich
# если этой библиотеки нет, закомментируйте (#) её вызов
from rich import print

import turtle

turtle.colormode(255)
t0=turtle.Turtle()
t0.speed(0); t0.color('red');t0.width(3)

t0.fd(260);t0.lt(90);t0.circle(260,180);t0.lt(90);t0.fd(260)

time.sleep(0.7)
t0.color('black')

t0.write("Я черепашка и я умею рисовать и печатать",align='center',font=('Arial', 18,'normal'))
t0.up();t0.rt(90);t0.fd(60);t0.lt(90);t0.down()
t0.color(0,230,230)
time.sleep(0.7)

t0.write("В консоли я вычисляю, сколько секунд прошло с начала года",align='center',font=('Arial', 18,'normal'))
time.sleep(0.7)
t0.fd(260);t0.rt(90);t0.circle(-260,180);t0.rt(90);t0.fd(260)

t=time.time()
print("Функция time() отсчитала ", t, "секунд")

#считаем, сколько секунд в дне, году, високосном году, 4 годах подряд
daysec=24*60*60
yearsec=365*daysec
#leapyearsec=yearsec+daysec
fouryearsec=4*yearsec+daysec
print("Секунд в обычном году -- ", yearsec)

# считаем, сколько прошло 4-летних циклов, и какой остаток в секундах
leapcycles=int(t//fouryearsec)
remainder=t%fouryearsec
print("Целое число 4летних циклов с нулевого момента функции time() -- ", leapcycles)
print("Остаток в секундах",remainder,", это ", int(remainder//yearsec), "полных лет")

# Сегодняшняя дата
today=datetime.datetime.now()
print("Сегодня ", today)

# считаем месяцы, дни, часы, минуты, секунды с начала года
months=int(today.strftime("%m"))-1
days=int(today.strftime("%d"))-1
hours=int(today.strftime("%H"))
mins=int(today.strftime("%M"))
secs=int(today.strftime("%S"))
secsthisyear=secs+60*(mins+60*(hours+24*(days+30*months)))
print("Прошло секунд с начала года --", secsthisyear)

# сравниваем секунды с начала года и остаток секунд от начала отсчета функции time()
# по модулю одного года. Нам повезло, что в текущем году прошло целое число 4летних циклов
# с момента начала отсчета. Иначе пришлось бы делать уточнения на расположение високосного года
# внутри цикла
delta=secsthisyear-remainder

# переведем разницу в часы, минуты и секунды
dh=int(delta//3600)
dm=int(delta//60-60*dh)
ds=delta-60*(dm+60*dh)

# округлим секунды до сотых
ds=round(ds,2)
print("Округленная разница между двумя остатками секунд -- ", dh, "час", dm, "мин", ds, "сек")
print("Что же это за разница?")

turtle.update()
turtle.mainloop()

