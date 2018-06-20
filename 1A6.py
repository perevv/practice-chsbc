import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Pereviznyk and Belyaev')

i = float(input("Введіть вартіть страв: "))
p = 18%i
ch = 14%i
z = i + p + ch
print ("Податок становить : ", p)
print ("Чайові: ", ch)
print ("Загальна сума до сплати: ", z)