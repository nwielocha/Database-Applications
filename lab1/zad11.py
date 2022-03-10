# Napisz program, który dla listy składającej się z n list (każda z m elementów) wyświetli
# zawartość każdego wiersza w odwrotnej kolejności.

from numpy import random

list1 = []
list2 = []
n = 3
m = 4

for i in range(m):
    x = random.randint(100)
    list2.append(x)

for i in range(n):
    print(list2)
    list2.reverse()
    list1.append(list2)

print(list1)
