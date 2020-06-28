#zad1

macierz = [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]]

for row in macierz:
    print(row)

#transpozycja
trans = [[macierz[j][i] for j in range(len(macierz))] for i in range(len(macierz[0]))]

print("\n")
for row in trans:
    print(row)
