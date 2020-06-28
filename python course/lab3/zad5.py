# zad5
def power_set(tab):
    if len(tab) == 0:
        return [{}]
    first = tab[0]
    rest = tab[1:]

    return power_set(rest) + list(map(lambda subset: {first, *subset}, power_set(rest)))


tab = [1, 2, 3, 4, 5]
print(power_set(tab))
