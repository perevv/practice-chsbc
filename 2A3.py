import datetime
import random
from itertools import permutations
################################################################
def printTimeStamp(name):									  ##
 print('Автор програми: ' + name)							  ##
 print('Час компіляції: ' + str(datetime.datetime.now()))	  ##
print(printTimeStamp('Beliaev and Pereviznyk'))				  ##
################################################################

ls = ['a','b','c','d']

print(ls)
otvet = ''.join(ls)
lol = random.shuffle(ls)
print(ls)
#kek = ls + lol
#for item in permutations(otvet, lol):
    #print('='.join(item))
print(lol)
