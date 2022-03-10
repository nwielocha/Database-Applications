# Napisz program, który uzupełni listę dwudziestoma kolejnymi liczbami naturalnymi, a
# następnie używając ciągu operacji na listach utworzy następującą listę zagnieżdżoną:
# [[1,2,...,20],[20,19,...1]]

a = []
b = []
c = []

n = 20

for i in range(n):
    a.append(i)

b = a.copy()
b.reverse()

c.append(a)
c.append(b)

print(c)
