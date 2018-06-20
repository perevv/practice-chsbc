import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Pereviznyk and Belyaev')

i1 = float(input("Привіт! Яка зараз година? \n"))
i2 = input("Чи говорить папуга? \n")
if  i2 == "Так" and (i1 <= 8 or i1 == 22 or i1 == 23 or i1 == 24):
	print ("Накрити ковдрою")
else:
	print("Не накривати ковдрою")

