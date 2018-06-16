import datetime
import math
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Pereviznyk and Belyaev")

print("Висота з якої об’єкт було скинуто в метрах: ")
d = float(input())

a = 0
b = 2*9.8*d
x = a + b

print ("Швидкість: {:.3f}".format(math.sqrt(x)) ,"м/с")


