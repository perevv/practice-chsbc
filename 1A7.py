import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

x = input('Введіть температуру в Цельсіях:')
k = 273
f = 32
print ((k) + int(x))
print ((f) + int (x)* 1.8)
printTimeStamp('Pereviznyk and Belyaev')