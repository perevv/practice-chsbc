import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
max_ = max((a, b, c))
min_ = min((a, b, c))
print("Max={0} \n Min={1}".format(max_, min_))
print(a+b+c-min_-max_)
printTimeStamp("Віталій")
