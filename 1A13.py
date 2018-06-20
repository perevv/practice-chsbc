import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Pereviznyk and Belyaev')

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
mx = max((a, b, c))
mn = min((a, b, c))
print("Max={0} \nMin={1}".format(mx, mn))
print(a+b+c-mn-mx)
