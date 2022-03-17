from numpy import random

# Zad. 1a
print("Zad. 1a")
grocery = {"mleko": 1, "chleb": 2}
print(grocery)
grocery["woda"] = 5
print(grocery)
for val in grocery.values():
    print(val)
for key in grocery.keys():
    print(key)

# Zad. 1b
print("Zad. 1b")
# Ciągi znaków. Nawiasy kwadratowe mogą słóżyć do pobrania konkretnego znaku (-
# indeksuje od końca), np:
cheer = "Python rules!"
print(cheer[0])
print(cheer[7])
print(cheer[-1])
# Aby uzyskać podciąg należy umieścić wewnątrz nawiasów kwadratowych trzy zmienne,
# oddzielone dwukropkami:
# [start_index:stop_index:step]
cheer = "Python rules!"
print(cheer[2:7:1])
print(cheer[2:11:3])
print(cheer[-2:-11:-3])
# Manipulowanie wielkością znaków:
# lower() upper() swapcase() capitalize()
print(cheer.lower())
print(cheer.upper())
print(cheer.swapcase())
print(cheer.capitalize())

# Zad. 1c
print("Zad. 1c")
# Przeanalizuj kod (komentarze z #):
lyrics = "happy birthday to you happy birthday to you happy birthday dear Happy birthday to you"
counts = {}  # pusty słownik
words = lyrics.split(" ")  # pobiera listę wszystkich słów poprzez podzielenie ciągu w miejscach wystąpienia spacji
for w in words:
    w = w.lower()  # zamienia na małe litery
    if w not in counts:
        counts[w] = 1
    else:
        counts[w] += 1
print(counts)

# Zad. 1d
print("Zad. 1d")


def powtorz(napis):
    return napis + napis


print(powtorz("Hello"))

# Zad. 2
print("Zad. 2")


# Napisz funkcję ispermutation, która dla dwóch list L1 i L2 zwraca True jeżli L1 i L2
# są permutacjami siebie nawzajem w przeciwnym razie funkcja zwraca False. (L1 i L2
# składają się z tych samych elementów, ale w innej kolejności).

def is_permutation(l1, l2):
    n1 = len(l1)
    n2 = len(l2)
    if n1 != n2:
        return False

    l1 = sorted(l1)
    l2 = sorted(l2)
    for i in range(0, n1, 1):
        if l1[i] != l2[i]:
            return False

    return True


print(is_permutation("napis", "apnis"))
print(is_permutation("napis", "anis"))
print(is_permutation("napis", "napisal"))

# Zad.3
print("Zad. 3")
# Napisz program, który wykorzystuje słowniki do realizacji następującego zadania: Dany
# jest słownik zawierający tytuły piosenek oraz przyporządkowane im oceny (liczby). Wy-
# świetl tytuły piosenek, których ocena wynosi 5.

# titles = {"Back in Black": 3, "Jamming": 5, "Purple Haze": 4, "Yesterday": 5}
# titles5 = {}
# i = 0
# # przechodze przez kazda wartosc
# for val in titles.values():
#     # jezeli wartosc rowna sie 5
#     if val == 5:
#         # zapisuje tytul piosenki w nowej zmiennej
#         titles5[i] = titles[i]
#     i += 1
#
# print(titles5)

# Zad11. Mając dane trzy posortowane listy L1, L2, L3 wypisz elementy. które należą do wszystkich
# list jednocześnie. Nie korzystaj z dodatkowych list, ani innych struktur danych.
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
l3 = [3, 4, 8, 9]

print(list(set(l1) & set(l2) & set(l3)))

# Zad12. L-lista liczb całkowitych. Znajdź najmniejszą brakującą liczbę dodatnią. np dla listy
# [0,-10,1,3,-20] będzie to 2.
print("Zad. 12")
list12 = [0, -10, 1, 3, -20]
list121 = []
for i in range(len(list12)):
    if list12[i] >= 0:
        list121.append(list12[i])

print(list121)
max1 = 0
for i in range(len(list121)):
    if list121[i] > max1:
        max1 = list121[i]

print(max1 - 1)

# Zad.13 Niech dana będzie lista list n x m, składająca się z zer i jedynek. Znajź wiersz, zawierający najwięcej
# jedynek. Jeżeli w liście list znajduję się same zera program powinien wypisać -1.
print("Zad. 13")
n = 5
m = 5
list1 = [[random.randint(2) for i in range(n)] for j in range(m)]
print(list1)
counter = 0

# Zad.14 Dana jest krotka
print("Zad. 14")
tuple12 = ("Apple", [10, 20, 30], (15, 25, 35))
# Jak dosatć się do "20"? Wypisz na ekranie tylko "20" spośród całej krotki.
print(tuple12[1][1])

# Zad. 15 Dana jest krotka
print("Zad. 15")
tuple3 = (1, 2, 3, 4)
# Czy potrafisz ją "rozpakować"?
# Twój kod
a, b, c, d = tuple3
print(a)  # powinno wyświetlić 1
print(b)  # powinno wyświetlić 2
print(c)  # powinno wyświetlić 3
print(d)  # powinno wyświetlić 4

# Zad. 16 Dane są krotki
print("Zad. 16")
tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)
# Czy potrafisz je zamienić? Spodziewany wynik:
# tuple1 = (5,6,7,8)
# tuple2 = (1,2,3,4)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)

# Zad. 17 Dana jest krotka
print("Zad. 17")
aTuple = (1, 4, 3, 4, 5, 1, 6, 1)
# Ile razy "1" występuje w krotce?
print(aTuple.count(1))
