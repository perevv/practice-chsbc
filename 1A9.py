import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Pereviznyk and Belyaev')


a = float(input("Введіть роки вашого життя: "))
def age():
    if a < 1:
        print("Ви ввели від'ємне число. Будь ласка спробуйте ще раз")
        return
    else:
        a1 = 2
        a2 = a - a1
        b1 = a1 / 10.5
        b2 = a1 / 4
        b3 = a2 / 7
        b4 = b2 + b3
        b5 = b1 + b3
        print("У собачих роках вам було б: ",+ b4, "років") 
        print("У собачих роках вам було б: ",+ b5, "років")


age()