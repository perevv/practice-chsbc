import datetime
print("Введіть першу сторону")
a1 = int(input())
print("Введіть другу сторону")
b1 = int(input())
print("Введіть третю сторону")
c1 = int(input())

def rovno():
    if a1 == b1 == c1:
        print("Він рівносторонній")
    elif a1 == b1 != c1:
        print("Він рівнобедренний")
    elif a1 != b1 != c1:
        print("Нерівносторонній")
    else:
        print("Невідомо")
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Ян Яворский i Seroja Butenko"

rovno()
printTimeStamp(name)
