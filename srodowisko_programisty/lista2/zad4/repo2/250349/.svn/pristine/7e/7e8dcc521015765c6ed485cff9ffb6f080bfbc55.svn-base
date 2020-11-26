import random
from sys import stdin
import time
import sys
from more_itertools import random_permutation
"""zadanie 2 implementacia algorytm genetyczny lista3 zad2 Wojciech Wroblewski"""

in_data = input().split()
t = int(in_data[0])
n = int(in_data[1])
s = int(in_data[2])

lines = stdin.readlines()
out = []

for line in lines:
    temp = line[0:-2]
    out.append(temp)
letters = out[:-4]
candidates = out[-4:]

dict_letter_values = {}
possible_letters = []
for e in letters:
    temp = e.split(" ")
    dict_letter_values[temp[0]] = int(temp[1])
    possible_letters.append(temp[0])

file = open("dict.txt", "r")
d = file.readlines()
qwerty = []
for i in d:
    temp = i[0:-2]
    qwerty.append(temp)

"""funkcja pomocnicza do zmaiany znaku w stringu"""


def change_char(s, p, r):
    return s[:p] + r + s[p + 1:]


def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1])
    return sub_li


"""glowna klasa symulucaja algorytm genetyczny"""


class Genetic:
    def __init__(self, population_size, letters, letter_keys, start_words, dictionary):
        self.letters = letters
        self.keys = letter_keys
        self.origin_setup = start_words
        self.max_word_length = len(letters)
        self.dictionary = dictionary
        self.best = None
        self.population_size = population_size
        self.best_word = None
        self.good = []

    """funkcja sprawdzajaca czy slowo moze zostac utworzone z zadanych liter"""

    def can_create_from_letters(self, word):
        for x in word:
            if x not in self.letters or len(word) > len(self.letters):
                return False
            else:
                if word.count(x) > self.letters.count(x):
                    return False

        return True

    """funkcja spr czy slowo zawierca sie w slowniku """

    def check_if_in_dict(self, word):
        if word in self.dictionary:
            return True
        else:
            return False

    """obliczanie funkcji celu dla slowa"""

    def get_word_value(self, word):
        sum = 0
        for i in word:
            if i not in self.keys:
                return 0
            else:
                sum += self.keys[i.lower()]
        return sum

    """tworzenie slowa o zadanej dlugosci z dostapnych liter"""

    def create_word(self, size):
        l = self.letters.copy()

        word = []
        for i in range(0, size):
            a = random.choice(l)
            word.append(a)
            l.remove(a)
        return "".join(word)

    """tworzenie poczatkowej populacji"""

    def create_population(self):

        population = []

        for e in self.origin_setup:
            population.append(e)
        while len(population) < self.population_size:
            r = random.uniform(0,1)
            if r > 0.5 :
                 population.append(self.create_word(random.randint(0, self.max_word_length)))
            else :
                 population.append(''.join(random_permutation(random.choice(self.origin_setup))))
        self.best = self.get_word_value(population[0])
        return population

    """funkcja realizujaca poczatkowa selekckcje populacji"""

    def selection(self, population):

        selection = []
        out = []

        for p in population:
            touple = []
            touple.append(p)
            touple.append(self.get_word_value(p))
            selection.append(touple)

            if self.check_if_in_dict(p):

                if self.get_word_value(p) >= self.best and self.can_create_from_letters(p):
                    if p not in out:
                        out.append(p)
                        out.append(''.join(random_permutation(p)))
                    self.best = self.get_word_value(p)
                    self.best_word = p



        Sort(selection)

        i = 0
        while len(out) < 10:
            if selection[len(selection)-i -1][0] not in out:
                out.append(selection[len(selection)-i -1][0])
            i += 1



        return out

    """cross over"""

    def crossing_over(self, population):

        while len(population) < self.population_size:

            to_reproduce = self.population_size - len(population)

            children_counter = 0
            set_of_children = []

            while children_counter < to_reproduce:
                population.sort(key=len)

                r_1 = random.randint(0, len(population) - 1)

                """if r_1 >= len(population) - 1:
                    r_2 = r_1 - 1
                else:
                    r_2 = r_1 + 1"""
                r_2 = r_1
                while r_2 == r_1:
                     r_2 = random.randint(0, len(population) - 1)

                parent_1 = population[r_1]
                parent_2 = population[r_2]

                slice1 = random.randint(0, len(parent_1))
                slice2 = random.randint(0, len(parent_2))

                value = parent_1[0:slice1] + parent_2[slice2:]

                if len(value) <= self.max_word_length and value != '' and value not in set_of_children:
                    set_of_children.append(value)
                    children_counter += 1

            temp = self.mutation(set_of_children).copy()

            for x in temp:
                population.append(x)

        return population

    """mutation"""

    def mutation(self, population):
        out = []

        for p in population:
            r = random.uniform(0, 1)
            if r < 0.3:
                temp = p
                if 0 < r < 0.1:
                    if len(temp) < self.max_word_length:

                        add = random.choice(self.letters)
                        while add not in temp:
                            add = random.choice(self.letters)
                        temp += str(add)

                elif 0.1 < r < 0.2:

                    temp = change_char(temp, random.randint(0, random.randint(0, len(temp) - 1)),
                                       random.choice(self.letters))

                elif 0.2 < r < 0.3:
                    temp = temp[:-1]


                if len(temp) < self.max_word_length and temp != '':
                    out.append(temp)
                else:
                    out.append(p)
            else:
                out.append(p)
        return out

    """glowna funkcja realizujaca algorytm genetyczny"""

    def genetic_calculation(self):

        population = self.create_population().copy()
        for p in population:
            if self.check_if_in_dict(p) and self.can_create_from_letters(p):
                self.best_word = p
                self.best = self.get_word_value(p)


        t_end = time.time() + t
        while time.time() < t_end:
            population = self.selection(population).copy()
            population = self.crossing_over(population).copy()

        print(self.best)
        print(self.best_word, file=sys.stderr)


genetic = Genetic(60, possible_letters, dict_letter_values, candidates, qwerty)
genetic.genetic_calculation()
