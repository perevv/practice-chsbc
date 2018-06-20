import datetime
import math
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Pereviznyk and Belyaev')



s = float(input("Довжина сторони: "))
n = float(input("Кількість сторон: "))
с = n*s**2
h = float(math.pi/n)
s = 4 * math.tan(h)

print ("Площа: ",s ,"см,квадрат")



