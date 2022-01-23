# 1. Proszę napisać program rozwiązujący układ równań N równań liniowych O N niewiadomych.
# Dane dla problemu należy wczytać z pliku tekstowego. W pierwszym wierszu znajduje się liczba
# równań N, kolejne wiersze zawieraja macierz współczynników oraz wyrazy wolne, na przykład plik:

# 3
# 1 2 3 7
# -1 2 4 6
# 2 1 1 13
# Odpowiada układowi 3 równań o 3 niewiadomych w postaci:
# X+2Y+3Z=7
# -X+2Y+4Z=6
# 2X+Y+Z=13
# Program powinien uwzględnić przypadki układu nieoznaczonego i sprzecznego. Wskazówka:
# rozważyć zastosowanie biblioteki numpy.

import numpy as np

with open("./za1-data.csv") as file:
    line1 = file.readline()

rows_num = int(line1)

data = np.loadtxt("./za1-data.csv", skiprows=1)
A = data[0:rows_num, 0:rows_num]
B = data[0:rows_num, rows_num]
X = np.linalg.inv(A).dot(B)

print(X)