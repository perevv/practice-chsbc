import datetime
from collections import defaultdict
import re
################################################################
def printTimeStamp(name):									  ##
 print('Автор програми: ' + name)							  ##
 print('Час компіляції: ' + str(datetime.datetime.now()))	  ##
print(printTimeStamp('Beliaev and Pereviznyk'))				  ##
################################################################

words = "Yan Vlad Serega Yan Yan Yan Serega Alex Alex Alex Alex Alex Alex " # Елементи 

# Рахує скільки в рядку елементів повторюються
d = defaultdict(int)    
for word in words.split(): 
    d[word] += 1

# Кількість повторів записав у список
string = str(d.values()) 
lol = re.findall('(\d+)', string) 
xex = len(lol) # Скільки елементів(ці самі повтори) знаходяться у списку 

i = 0 
ls = [] # Пустий список, в який плануємо закинути елементи, які потрапляють у діапозон від 1 до 5 повторів

# Цикл який закидує елементи в список з діапозоном 1-5
while i <xex:
    if int(lol[i]) >= 1 and int(lol[i]) <= 5:
    	ls.append(lol[i]) # Додає у список елемент, якщо від входить у діапозон 1-5
    i +=1
                                       # Кількість елементів у списку(ls)
print('Скільки повторів з діапозоном: ',len(ls))

# Навсяк 
d = str(d) # Перемінну d в рядок
vasa = d.replace("defaultdict(<class 'int'>,", '') # Видалити defaultdict...
vasa = vasa.replace(')', '') and vasa.lstrip() # Видалити ')' та пробіл в началі 
print('Всі елементи з кількістю повторів: \n', vasa)







