import datetime
import time
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Pereviznyk and Belyaev")

t = time.localtime()
print ("Поточний час : ",time.asctime(t))


