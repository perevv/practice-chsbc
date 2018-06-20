import datetime

##################################################################
def printTimeStamp(name):                                       ##
 print('Автор програми: ' + name)                               ##
 print('Час компіляції: ' + str(datetime.datetime.now()) +"\n") ##
printTimeStamp('Beliaev and Pereviznyk')                        ##
##################################################################

def print_menu():
    print('Екстрені служби: «Пожежна безпека» - 101, «Поліція» - 102, «Швидка допомога» - 103')
    print('1. Друк телефонних номерів')
    print('2. Додати номер телефону')
    print('3. Видалити номер телефону')
    print('4. Пошук контакту')
    print('5. Вийти')
    print()

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Виберіть цифру (1-5): "))
    if menu_choice == 1:
        print("Телефонні номери:")
        for x in numbers.keys():
            print("Ім'я:", x, "\tТелефон:", numbers[x])
        print()
    elif menu_choice == 2:
        print("Додати ім'я та номер")
        name = input("Ім'я: ")
        phone = input("Номер: ")
        numbers[name] = phone
        print("Додано :)")
    elif menu_choice == 3:
        print("Видалити ім'я та номер")
        name = input("Ім'я: ")
        number = input("Номер: ")
        print = input("Номер видалений")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "не знайдений")
    elif menu_choice == 4:
        print("Знайти контакт")
        name = input("Ім'я: ")
        if name in numbers:
            print("Номер телефону:", numbers[name])
        else:
            print(name, "не знайдений")
    elif menu_choice != 5:
        print_menu()
