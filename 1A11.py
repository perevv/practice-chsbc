import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Pereviznyk and Belyaev')

i = input('Введіть ваш зріст в см: ')
i1 = (int(i)%30.48)//2.54 
i2 = int(i)//30.48
print(i1, "Дюймів")
print(i2, "Футів")