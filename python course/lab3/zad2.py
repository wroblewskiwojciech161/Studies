# zad2
def flatten(x):
    types = (list, tuple)
    if isinstance(x, types):
        for value in x:
            for y in flatten(value):
                yield y
    else:
        yield x


l = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]]

print(list(flatten(l)))
