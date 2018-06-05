import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Pereviznyk and Belyaev')

i = int (input('Введіть чотирьохзначне число:'))
b = len(i)
#i = int(i)

#if b == 3:
print (b[0] + b[1] + b[2] + b[3])

#b = map(int, str(i))
#print (b)