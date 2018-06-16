import math
import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Pereviznyk and Belyaev")

d = float(input("Введіть кількість днів: "))
h = float(input("Введіть кількість годин: "))
m = float(input("Введіть кількість минут: "))
s = float(input("Введіть кількість секунд: "))
d1 = 86400 
g1 = 3600
m1 = 60
s1 = 1
print (int(d*d1 + h*g1 + m*m1+ s))
