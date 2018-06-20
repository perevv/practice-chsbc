import copy
import datetime
from itertools import groupby 
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Pereviznyk and Belyaev")


i = ['h', 'e', 'l', 'l', 'o','w','o','r','d'] 
i1 = list(set(i)) 
nlist = copy.deepcopy(i1) 
nlist.remove(nlist[0]) 
nlist.remove(nlist[2]) 
nlist.remove(nlist[3]) 
print(nlist)