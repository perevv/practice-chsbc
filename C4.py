import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Pereviznyk and Belyaev")

plan = input('Введіть свій тарифний план: ')
MB = float(input('Введіть кількість використаних МБ: '))
dmb1 = 0.05
dmb2 = 0.04
dmb5 = 0.02
 
if plan == '1000':

	if MB <= 1000 :

		print('20 грн')
	else:
		a = ((MB-1000)*0.05)
		print (a + 20)
		a1 = ((MB-1000)*0.04)
		print("Як би ви перейшли на тарифний план 2000\nви б сплачували 35 грн за 2000 Мб\nта позатарифно 1 Мб = 0.04 грн\nЗа",MB,"MB ви б сплатили за додаткові Мб",a1,"грн" )

	

if plan == '2000':

	if MB <= 2000:

		print ("35 грн")

	else:
		a = ((MB-2000)*0.04)
		print (a + 35)
		a1 = ((MB-2000)*0.02)
		print("Як би ви перейшли на тарифний план 5000\nви б сплачували 85 грн за 5000 Мб\nта позатарифно 1 Мб = 0.02 грн\nЗа",MB,"MB ви б сплатили за додаткові Мб",a1,"грн" )	

if plan == '5000':

	if MB <= 5000:

		print ("85 грн")

	else:
		a = ((MB-5000)*0.02)
		print (a + 85)	


