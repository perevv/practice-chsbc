import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Pereviznyk and Belyaev')

i = input ("Введіть ваше ім'я: ")
print ("Привіт", i, "!")