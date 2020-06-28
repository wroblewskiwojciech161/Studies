import numpy as np
import pandas as pd

"""Wojciech Wroblewski lista5 zad2 kwjp"""

np.seterr(divide='ignore', invalid='ignore')

"""funkcja pobiera dane z plikow do list"""


def get_data():
    data_ratings_csv = pd.read_csv("ratings.csv")
    data_ratings = np.array(data_ratings_csv.query("movieId <= 10000"))
    data_movies = pd.read_csv("movies.csv")
    movies = np.array(data_movies.query("movieId <= 10000"))
    data_ratings = np.array(data_ratings)

    # count distinct people id  #610
    count_dist_people = data_ratings_csv.groupby('userId').nunique()
    # get last movie id in given range  (up to 10000)  #9018
    last_movie_id = data_movies.query("movieId <= 10000")["movieId"].iloc[-1]

    # fill matrix  611x9019
    ratings = np.zeros((len(count_dist_people) + 1, last_movie_id + 1))
    for element in data_ratings:
        ratings[int(element[0]), int(element[1])] = element[2]

    return movies, ratings


def recommendation(x, y):
    z = np.dot(np.nan_to_num(x / np.linalg.norm(x, axis=0)), np.nan_to_num(y / np.linalg.norm(y)), )
    X = np.nan_to_num(x / np.linalg.norm(x, axis=0))
    Z = np.nan_to_num(z / np.linalg.norm(z))

    return np.dot(X.T, Z)


"""funkcja na podstawie rekomendacji zwraca filmy i ich dane charakterystyczne"""


def get_recommended_movies(ratings_data, movies_data, own_marks):
    get_recommended_movies = []
    recommendations = recommendation(ratings_data, own_marks)

    for m in movies_data:
        get_recommended_movies.append((recommendations[m[0]][0], m[0], m[1]))

    get_recommended_movies = np.array(get_recommended_movies)

    """wynik posortowany rosnaco ze wzgl na wynik rekomendacji"""

    return get_recommended_movies[np.argsort(get_recommended_movies[:, 0])]


data = get_data()
ratings_data = data[1]
movies_data = data[0]

own_marks = np.zeros((9019, 1))
own_marks[2571] = 5
own_marks[32] = 4
own_marks[260] = 5
own_marks[1097] = 4
own_marks[1097] = 4

recommendation = get_recommended_movies(ratings_data, movies_data, own_marks)

"""wyswietlam top 9 rekomendacji """
for r in recommendation[:-10:-1]:
    print(r[0], "  ", r[1], " ", r[2])
