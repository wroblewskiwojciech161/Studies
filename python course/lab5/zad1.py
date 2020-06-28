import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""Wojciech Wroblewski zad1 lista5 kwjp.

   Po uruchomieniu  programu zostanie uruchomiona funkcja realizująca 1 podpunkt zadania.
   Po zamknięciu wykresu z podpunktu 1, zostanie uruchomiona funkcja relizująca podpunkt 2.
   
   Program dosc dlugo wczytuje dane dlatego wykresy zostaly rowniez dodane do folderu z rozwiazaniem"""



"""funkcja zwraca macierz X i wektor Y na podstawie danych z pliku csv"""


def get_ratings(m):
    data = pd.read_csv("ratings.csv")

    users = data.query('movieId == 1')["userId"]
    list_of_users = []
    Y = []
    X = []
    list_of_users = (users.tolist())

    for i in range(0, len(list_of_users)):
        toystory_user_films = data.query('userId == ' + str(list_of_users[i]))

        ratings = []
        films = (toystory_user_films).iloc[0:m, 1:3]
        counter = 1
        current = 0
        ratings = []
        # usuwamy kolumne z ocenami ToyStory wiec żeby otrzymać m opini w pętli przechodze m+1
        while counter <= m + 1:
            if films["movieId"].values[current] == counter and counter <= len(films["movieId"]):
                if current == 0:
                    Y.append(films["rating"].values[current])
                ratings.append(films["rating"].values[current])
                current += 1
            else:
                ratings.append(0)
            counter += 1
        #  usuwamy kolumnę z ocenami z ToYStory dlatego [1:]
        X.append(ratings[1:])
    return X, Y


"""funkcja minimalizujaca"""


def minimise(X, Y):
    return np.linalg.lstsq(X, Y, rcond=None)[0]


""" funkcja ktora na podstawie macierzy X oraz wspolrzynnikow minimalizacji zwraca predykcje"""


def get_prediction(coff, X):
    predictions = []
    for i in range(0, len(X)):
        mark = 0
        for j in range(len(X[i])):
            mark += X[i][j] * coff[j]
        predictions.append(mark)
    return predictions


"""funkcja zwraca wartości rzeczywiste oraz przewidziane ocen dla obciętych zbiorów i zadanego m"""


def generate_prediction_comparison(m):
    arrX = np.array(get_ratings(m)[0])
    arrY = np.array(get_ratings(m)[1])

    """tworzymy zbiór testowy"""
    X = arrX[0:200, 0:m]
    Y = arrY[0:200]
    X_to_predict = arrX[200:215, 0:m]

    """przewidujemy wynik dla pozostałych 15 osób z poza zbioru"""
    predictions = get_prediction(minimise(X, Y), X_to_predict)

    """rzeczywiste oceny"""
    real = arrY[200:215]

    return real, predictions


"""funkcja realizujaca tresc oraz wykresu do podpunktu 2 zad1"""


def podpunkt_2():
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)
    fig.suptitle("zad1 podpunkt 2. Przewidywania.")

    """generowanie przewidywań dla wycinka zbioru, m = 10"""
    real = generate_prediction_comparison(10)[0]
    predictions = generate_prediction_comparison(10)[1]

    ax1.plot(list(range(0, 15)), real, 'o', label="wartość oceny", markersize=3, color='black')
    ax1.plot(list(range(0, 15)), predictions, 'o', label='wartość przewidziana', markersize=1, color='red')
    ax1.vlines(list(range(0, 15)), real, predictions, label="błąd", colors="g", linestyles="dashed")
    ax1.set_title("m=10")
    print("m = 10")
    print("wynik prawidłowy:\n", real)
    print("predykcja:\n", predictions)
    print("\n")

    real = generate_prediction_comparison(100)[0]
    predictions = generate_prediction_comparison(100)[1]
    ax2.plot(list(range(0, 15)), real, 'o', markersize=3, color='black')
    ax2.plot(list(range(0, 15)), predictions, 'o', markersize=1, color='red')
    ax2.vlines(list(range(0, 15)), real, predictions, colors="g", linestyles="dashed")
    ax2.set_title("m=100")
    print("m = 100")
    print("wynik prawidłowy:", real)
    print("predykcja:\n", predictions)
    print("\n")

    real = generate_prediction_comparison(200)[0]
    predictions = generate_prediction_comparison(200)[1]
    ax3.plot(list(range(0, 15)), real, 'o', markersize=3, color='black')
    ax3.plot(list(range(0, 15)), predictions, 'o', markersize=1, color='red')
    ax3.vlines(list(range(0, 15)), real, predictions, colors="g", linestyles="dashed")
    ax3.set_title("m=200")
    print("m = 200")
    print("wynik prawidłowy:\n", real)
    print("predykcja:\n", predictions)
    print("\n")

    real = generate_prediction_comparison(500)[0]
    predictions = generate_prediction_comparison(500)[1]
    ax4.plot(list(range(0, 15)), real, 'o', markersize=3, color='black')
    ax4.plot(list(range(0, 15)), predictions, 'o', markersize=1, color='red')
    ax4.vlines(list(range(0, 15)), real, predictions, colors="g", linestyles="dashed")
    ax4.set_title("m=500")
    print("m = 500")
    print("wynik prawidłowy:\n", real)
    print("predykcja:\n", predictions)
    print("\n")

    real = generate_prediction_comparison(1000)[0]
    predictions = generate_prediction_comparison(1000)[1]
    ax5.plot(list(range(0, 15)), real, 'o', markersize=3, color='black')
    ax5.plot(list(range(0, 15)), predictions, 'o', markersize=1, color='red')
    ax5.vlines(list(range(0, 15)), real, predictions, colors="g", linestyles="dashed")
    ax5.set_title("m=1000")
    print("m = 1000")
    print("wynik prawidłowy:\n", real)
    print("predykcja:\n", predictions)
    print("\n")

    real = generate_prediction_comparison(10000)[0]
    predictions = generate_prediction_comparison(10000)[1]
    ax6.plot(list(range(0, 15)), real, 'o', markersize=3, color='black')
    ax6.plot(list(range(0, 15)), predictions, 'o', markersize=1, color='red')
    ax6.vlines(list(range(0, 15)), real, predictions, colors="g", linestyles="dashed")
    print("m = 10000")
    print("wynik prawidłowy:\n", real)
    print("predykcja:", predictions)
    ax6.set_title("m=10000")
    fig.legend(loc='lower left')
    plt.show()


"""funkcja realizujaca tresc oraz wykresy podpunktu 1 zad1"""


def podpunkt_1():


    fig, ((ax1), (ax2), (ax3), (ax4)) = plt.subplots(4, 1)
    fig.suptitle("zad1 podpunkt 1. Regresja liniowa.")

    arrX = np.array(get_ratings(10)[0])
    arrY = np.array(get_ratings(10)[1])

    print("Przykładowe dane dla n =215  m = 10")
    print("X \n", arrX)
    print("Y \n", arrY)

    print("""Tworzenie wykresu .... Wczytywanie danych""")

    cooficient = minimise(arrX, arrY)
    predictions = get_prediction(cooficient, arrX)
    users = [x for x in range(0, len(arrX))]

    ax1.plot(users, arrY, 'o', label="wartość oceny", markersize=3, color='black')
    ax1.plot(users, predictions, 'o', label='wartość przewidziana', markersize=1, color='red')
    ax1.vlines(users, arrY, predictions, label="błąd", colors="g", linestyles="dashed")
    ax1.set_title("m=10")

    arrX = np.array(get_ratings(100)[0])
    arrY = np.array(get_ratings(100)[1])
    cooficient = minimise(arrX, arrY)
    predictions = get_prediction(cooficient, arrX)

    ax2.plot(users, arrY, 'o', markersize=3, color='black')
    ax2.plot(users, predictions, 'o', markersize=1, color='red')
    ax2.vlines(users, arrY, predictions, colors="g", linestyles="dashed")
    ax2.set_title("m=100")

    arrX = np.array(get_ratings(1000)[0])
    arrY = np.array(get_ratings(1000)[1])
    cooficient = minimise(arrX, arrY)
    predictions = get_prediction(cooficient, arrX)

    ax3.plot(users, arrY, 'o', markersize=3, color='black')
    ax3.plot(users, predictions, 'o', markersize=1, color='red')
    ax3.vlines(users, arrY, predictions, colors="g", linestyles="dashed")
    ax3.set_title("m=1000")

    arrX = np.array(get_ratings(10000)[0])
    arrY = np.array(get_ratings(10000)[1])
    cooficient = minimise(arrX, arrY)
    predictions = get_prediction(cooficient, arrX)

    ax4.plot(users, arrY, 'o', markersize=3, color='black')
    ax4.plot(users, predictions, 'o', markersize=1, color='red')
    ax4.vlines(users, arrY, predictions, colors="g", linestyles="dashed")
    ax4.set_title("m=10000")

    fig.legend(loc='lower left')
    plt.show()


print("----Podpunkt 1----\n")
podpunkt_1()

print("\n----Podpunkt 2----\n")
podpunkt_2()
