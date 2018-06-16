print("Введіть суму")
a = int(input())
a1 = a * 0.14
b1 = (a+a1)
a2 = (a+a1) * 0.14
b2 = (b1+a2)
a3 = (a+a2) * 0.14
b3 = (b2+a3)
print("Рік 1 - {:.2f}".format(b1))
print("Рік 2 - {:.2f}".format(b2))
print("Рік 3 - {:.2f}".format(b3))

