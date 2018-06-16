import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Pereviznyk and Belyaev')

import datetime
print("довжина: ")
a = float(input())
print("Ширина: ")
b = float(input())
c = a*b
print ("площу поля в арах: ", c / 100)

print ("площу поля в гектарах:", c / 10000)