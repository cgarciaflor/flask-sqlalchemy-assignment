from src.models import dataBase, Movie
class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        
        allMovies = Movie.query.all()
        return allMovies

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        singleMovie = Movie.query.filter_by(movie_id=movie_id).first()

        return singleMovie

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        newMovie = Movie(title=title, director=director, rating=rating)
        dataBase.session.add(newMovie)
        dataBase.session.commit()
        return newMovie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        title = f"%{title}%"
        search = Movie.query.filter(Movie.title.like(title)).all()
        return search


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
