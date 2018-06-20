import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Pereviznyk and Belyaev')

i1 = float(input("Введіть довжину 1 сторони: "))
i2 = float(input("Введіть довжину 2 сторони: "))
i3 = float(input("Введіть довжину 3 сторони: "))
if i1 == i2 and i1==i3 and i3==i2:
	print ("Цей трикутник рівносторонній")
elif i1 == i2 or i1==i3 or i3==i2:
	print ("Цей трикутник рівнобедрений")
else:
	print("Цей трикутник нерівносторонній")