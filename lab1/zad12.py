# Napisz pogram, który dla zadanego n oraz dla listy zagnieżdżonej zawierającej liczby
# rzeczywiste o wymiarach n × n wyświetli sumę wartości liczb, które znajdują się na
# przekątnych macierzy.

from numpy import random

n = 5
s = 0
list1 = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        list1[i][j] = random.randint(3)
        if i == j:
            s += list1[i][j]

print(list1)
print(s)
