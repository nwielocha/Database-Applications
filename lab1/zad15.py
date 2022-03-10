# Napisz program, który ostatni element listy zamieni na inną listę np dla danych [1, 3,
# 5, 7, 9, 10], [2, 4, 6, 8] wynik to [1, 3, 5, 7, 9, 2, 4, 6, 8]

a = [1, 3, 5, 7, 9, 10]
b = [2, 4, 6, 8]

a.pop(5)
a.extend(b)

print(a)
