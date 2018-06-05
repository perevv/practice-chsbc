import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))


i = input ('Введіть літеру:')
if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
	print ('Голосна')
 	
elif i == 'y':
	print ('Може бути приголосною або голосною')
else:
     print('Приголосна')
printTimeStamp('Pereviznyk and Belyaev')