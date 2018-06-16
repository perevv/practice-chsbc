import datetime
import math

################################################################
def printTimeStamp(name):									  ##
 print('Автор програми: ' + name)							  ##
 print('Час компіляції: ' + str(datetime.datetime.now()))	  ##
print(printTimeStamp('Beliaev and Pereviznyk'))				  ##
################################################################

t1 = int(input('Введіть першу точку широти  (в градусах): '))
g1 = int(input('Введіть першу точку довготи (в градусах): '))
t2 = int(input('Введіть другу точку широти  (в градусах): '))
g2 = int(input('Введіть другу точку довготи (в градусах): '))

t1 = math.radians(t1)
t2 = math.radians(t2)
g1 = math.radians(g1)
g2 = math.radians(g2)
vid = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print(t1)
print(g1)
print(t2)
print(g2)
vid = vid*111.3*math.cos(15)
print(vid)