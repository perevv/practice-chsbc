import datetime
print("сантиметрах: ")
a = float(input())

print ("футах: ", a * 12)
print ("дюймах:", a * 2.54 )
name = "Serga i Yan"
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp(name)
