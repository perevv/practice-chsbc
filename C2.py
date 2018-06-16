import datetime
import re
################################################################
def printTimeStamp(name):									  ##
 print('Автор програми: ' + name)							  ##
 print('Час компіляції: ' + str(datetime.datetime.now()))	  ##
print(printTimeStamp('Beliaev and Pereviznyk'))				  ##
################################################################


path = input('Введіть дату по шаблону (рік-місяць-день):  \n')
path = re.split(r'-', path)
year = int(path[0])
month = int(path[1])
day = int(path[2])


print(year)
print(month)
print(day)
print('          ')

def Time(year, month, day):
	if day > 1 and day < 31:
		return day +1

	elif day == 31 :
		return day = 1
print(Time(year, month, day))





