n = int(input())
a = int(input())
b = int(input())
kolvo = 0
number = 1
for i in range(n):
    if number//a:
        kolvo += 1
    elif number // b and number % a != 0:
        kolvo += 1
    number += 1
print(kolvo)
