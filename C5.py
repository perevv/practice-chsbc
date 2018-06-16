import datetime
import random
################################################################
def printTimeStamp(name):									  ##
 print('Автор програми: ' + name)							  ##
 print('Час компіляції: ' + str(datetime.datetime.now()))	  ##
print(printTimeStamp('Beliaev and Pereviznyk'))				  ##
################################################################

 
num1 = random.randrange(1,6)
num2 = random.randrange(1,6)
num3 = random.randrange(1,6)
num4 = random.randrange(1,6)
num5 = random.randrange(1,6)
num6 = random.randrange(1,6)

ls = (num1,num2,num3,num4,num5,num6)
print(ls)
