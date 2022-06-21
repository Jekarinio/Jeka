import math
A = int(input("Введите стору A = "))
B = int(input("Введите сторону B = "))
C = int(input("Введите сторону C ="))
P = (A + B +C) / 2
S = math.sqrt(P * (P - A) * (P - B) * (P - C))
print(S)