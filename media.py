# A movie class containing the properties of a movie
class Movie():
        #available ratings and genres for the movies
        RATINGS = ["G", "PG", "PG-13", "R"]
        GENRE = ["Action", "Adventure", "Comedy", "Documentary", "Drama", "Horror", "Romance", "Science Fiction", "Thriller"]

        #initialise the class variables
        def __init__(self, title, trailer_youtube_url, cover_art_url, year_released, synopsis, genre, rating):
                self.title = title
                self.trailer_youtube_url = trailer_youtube_url
                self.cover_art_url = cover_art_url
                self.year_released = year_released
                self.synopsis = synopsis
                self.GENRE = genre
                self.RATINGS = rating

        def __str__(self):
                return self.title

        



        
