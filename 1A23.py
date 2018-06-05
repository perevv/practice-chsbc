import datetime
import math

a = int(input('Введіть a:'))

b = int(input('Введіть b:'))


e1 = a + b
e2 = b - a
e3 = a * b
e4 = a // b
e5 = a % b
e6 = math.log10(a)
e7 = a**b


print("Сума: ", + e1)
print("Різниця b - a: ", + e2)
print("Добуток a * b: ", + e3)
print("Частка a / b: ", + e4)
print("Остача a / b: ", + e5)
print("Значення log10a: ", + e6)
print("Значення a^b: ", + e7)

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Pereviznyk and Belyaev')