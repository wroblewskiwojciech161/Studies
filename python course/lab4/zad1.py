"""Lista 4 zad1 Wojciech Wroblewski"""

from time import time


def get_time(method):
    def function_wrapper(*arg, **other):
        start_var = time()
        result = method(*arg, **other)
        end_var = time()
        print("czas dzialania funkcji : {nazwa}  {czas} s".format(czas=end_var - start_var, nazwa=method.__name__))
        return result
    return function_wrapper


# przykladowe funkcje dla spr dzialania
@get_time
def count_sqrt_sequence(numbers):
    sequence = [n ** 2 for n in numbers]
    return sequence


@get_time
def count_cubed_sequence(numbers):
    sequence = [n ** 3 for n in numbers]
    return sequence


numbers = [12312, 123123, 3232, 32323, 23232, 123, 32323231]

count_sqrt_sequence(numbers)
count_cubed_sequence(numbers)
