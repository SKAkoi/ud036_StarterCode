import fresh_tomatoes
from media import Movie
import csv

# a function that grabs all the movies from a csv file passed to it
def grabmovies(filename):
    movies = []
    with open(filename, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for movie in reader:
            movies.append(Movie(title=movie['Name'], trailer_youtube_url=movie['trailer_youtube_url'], cover_art_url=movie['cover_art_url'], year_released=movie['year_released'], synopsis=movie['synopsis'], genre=movie['genre'], rating=movie['rating']))
    return movies

#gather up the list of movies into a list
movies = grabmovies('data/movies.csv')

#pass the list of movies to the function that displays it in the browser
fresh_tomatoes.open_movies_page(movies)

