import datetime

################################################################
def printTimeStamp(name):									  ##
 print('Автор програми: ' + name)							  ##
 print('Час компіляції: ' + str(datetime.datetime.now()))	  ##
print(printTimeStamp('Beliaev and Pereviznyk'))				  ##
################################################################

path = input('Введіть IMEI код (14 цифр): ')
n0 = int(path[0])

 path[0]+(path[1]*2)