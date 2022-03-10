#  Napisz program, który z podanej listy napisów utworzy inną listę zawierającą pary
# (napis, długoscnapisu).

list1 = ["one", "two", "three"]
list2 = []
length = 0

for i in range(len(list1)):
    length = len(list1[i])
    print(length)
    list2.append(list1[i])
    list2.append(length)

print(list2)
