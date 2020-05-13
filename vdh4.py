import math
print(" Nhap a: ")
a = int(input())
print(" Nhap b: ")
b = int(input())
print("  Nhap c ")
c = int(input())
deltha = b ** 2 - 4 * a * c
if deltha < 0:
    print(" Phuong trinh vo nghiem ")
elif deltha == 0:
    print(" Phuong trình có nghiem kep ")
    x = -b / 2 * a
    print(x)
else:
    print(" Phuong trinh co hai nghiem phan biet ")
x1 = (-b - (math.sqrt(deltha))) / (2 * a)
print(" Nghiem x1: ")
print(x1)
x2 = (-b + (math.sqrt(deltha))) / (2 * a)
print(" Nghiem x2: ")
print(x2)
© 2020 GitHub, Inc.
