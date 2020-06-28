import numpy as np
import pandas as pd
import scipy as scipy
from scipy.sparse import*
from scipy import *
import scipy.linalg as sla

"""Wojciech Wroblewski list5 zad2 kwjp"""




def get_data():
    data_ratings_csv = pd.read_csv("./ml-latest/ratings.csv")
    data_ratings = csc_matrix(data_ratings_csv,dtype=int32).toarray()
    data_movies = pd.read_csv("./ml-latest/movies.csv")
    movies = np.array(data_movies)

    data_ratings = csc_matrix(data_ratings,dtype=int32).toarray()

    # count distinct people id
    count_dist_people = data_ratings_csv.groupby('userId').nunique()
    # get last movie id in given range
    last_movie_id = data_movies["movieId"].iloc[-1]

    # fill matrix  611x9019
    ratings = scipy.zeros((len(count_dist_people) + 1, int((last_movie_id)/10  )+1),dtype=int8)
    print(len(count_dist_people))
    for i in range(0,int((last_movie_id)/10  )+1):
        element=data_ratings[i]
        ratings[int(element[0]), int(element[1])] = element[2]

    return movies, ratings


def recommendation(x, y):
    z = scipy.dot(scipy.nan_to_num(x / sla.norm(x, axis=0)), scipy.nan_to_num(y / sla.norm(y)), )
    X = scipy.nan_to_num(x / sla.norm(x, axis=0))
    Z = scipy.nan_to_num(z / sla.norm(z))

    return scipy.dot(X.T, Z)


def get_recommended_movies(ratings_data, movies_data, own_marks):
    get_recommended_movies = []
    recommendations = recommendation(ratings_data, own_marks)

    for m in movies_data:
        get_recommended_movies.append((recommendations[m[0]][0], m[0], m[1]))

    get_recommended_movies =np.array(get_recommended_movies)

    return get_recommended_movies[scipy.argsort(get_recommended_movies[:, 0])]

data_movies = pd.read_csv("movies.csv")
last_movie_id = data_movies["movieId"].iloc[-1]

data = get_data()
ratings_data = data[1]
movies_data = data[0]

own_marks = scipy.zeros((last_movie_id+1, 1))
own_marks[2571] = 5
own_marks[32] = 4
own_marks[260] = 5
own_marks[1097] = 4
own_marks[1097] = 4

recommendation = get_recommended_movies(ratings_data, movies_data, own_marks)
print(len(recommendation))

for r in recommendation[:-10:-1]:
    print(r[0], "  ", r[1], " ", r[2])
