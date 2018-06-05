import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))


i = int (input ('В чому ви хочете виміряти ІМТ?\n'
 		'Нажміть 1 - якщо в дюймах та фунтах\n'
 		'Нажміть 2 - якщо в метрах та кг\n'))
if i == 1 :
	w = float(input('Введіть вашу вагу в фунтах: '))
	h = float(input('Введіть ваш зріст в дюймах: '))
	bmi = (w * 703) / (h * h)
	print('Ваш індекс маси тіла:',(bmi))
elif i == 2 :	
	w = float(input('Введіть вашу вагу в кілограмах: '))
	h = float(input('Введіть ваш зріст в метрах: '))
	bmi = (w) / (h * h)
	print('Ваш індекс маси тіла:',(bmi))
printTimeStamp('Pereviznyk i Belyaev')
            