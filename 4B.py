import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Pereviznyk and Belyaev")

hv1 = float(input("Скільки хвилин використано: "))
sms1 = float(input("Скільки смс використано: "))
hv = 200
sms = 50
dhv = 0.17
dsms = 0.15
vnesok = 0.44
tarif = 15
baz = tarif


if hv1 > 200:
	hv = (hv1 - hv)*dhv
	baz = tarif + hv 

elif sms1 > 50:
	sms = (sms1 - sms) *dsms
	baz = 15 + sms
if hv1 > 200 and sms1 > 50:
	hv = (hv1 - hv)*dhv
	sms = (sms1 - sms) *dsms
	baz = 15 + sms + hv
else:
	tarif == 15
	baz == 15



podatoc = 5%baz
zagal = podatoc + vnesok + baz
print ("Базова плата становить: ", baz)
print ("Загальна плата становить ", zagal)
