#  Napisz program, który realizuje mnożenie macierzy przez skalar,
# np WEJSCIE [[1,2,4,6],[2,3,4,5],[12,3,4,5]], 3
# WYJSCIE:[[3,6,12,18],[6,9,12,15],[36,9,12,15]]
import numpy as np

a = np.array([[1, 2, 4, 6], [2, 3, 4, 5], [12, 3, 4, 5]])
s = 3

print(np.multiply(a, s))
