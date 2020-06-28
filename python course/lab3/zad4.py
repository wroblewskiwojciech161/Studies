# zad4
def quick_sort(o):
    return o and (quick_sort([i for i in o[1:] if i < o[0]])
                  + [o[0]]
                  + quick_sort([i for i in o[1:] if i >= o[0]]))


data = [12, 43, 5, 2, 5, 3, 7, 6, 5, 4, 3, 65, 76, 200, 7]
print(quick_sort(data))
