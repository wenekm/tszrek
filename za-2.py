# 3. Palindrom to coś, co czyta się tak samo od przodu i od tyłu. Hipoteza: weź dowolną liczbę naturalną.
# Jeżeli nie jest palindromem, to zapisz ją od tyłu i dodaj obie liczby. Jeżeli wynik nadal nie jest
# palindromem, kontynuuj, traktując go jako daną. Przerwij, gdy osiągniesz palindrom, albo po 10.
# próbie. Na przykład: 78+87=165, 165+561=726, 726+627=1353, 1353+3531=4884. Napisz program
# sprawdzający hipotezę dla pierwszych 200 liczb naturalnych jako startowych. Czy zawsze osiągniemy
# palindrom?

# czy ciag zanków jest palindromem
def isPalindrom(value):
    return value == value[::-1]

# Czy liczba jest palindrom
def isNumberPalindrom(value):
    return isPalindrom(str(value))

# Jeżeli liczba nie jest palindromem, to zappisujemy ją od tyłu i dodajemy obie liczby. 
# Jeżeli wynik nadal nie jest palindromem, kontynuuj, traktując go jako daną. Przerwij, gdy osiągniesz palindrom, albo po 10 próbie.
def isPalidromInTenActions(value):
    temp = value
    for k in range(1,10):
        if isNumberPalindrom(temp):
            return True
        temp += int(str(temp)[::-1])
    return False

# czy dla listy liczb naturalnych osiągniemy palindrom?
# obliczenia przerywane są w przypadku 
def isPalindromInList(val):
    for n in val:
        b = isPalidromInTenActions(n)
        if not b:
            return False
    return True

# sprawdzenie czy uda się osiągnąć palindrom dla pierwszych 200 liczb naturalnych
szukaj_do = 70
result = isPalindromInList(range(1,szukaj_do))
print(result)

