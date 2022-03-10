# Napisz program, który połączy dwie posortowane listy w jedną, także posortowaną.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = []

for x in list1:
    list3.append(x)
    list3.sort()

for x in list2:
    list3.append(x)
    list3.sort()

print(list3)
