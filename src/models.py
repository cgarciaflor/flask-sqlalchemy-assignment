# TODO - Create SQLAlchemy dataBase and Movie model
from flask_sqlalchemy import SQLAlchemy

dataBase = SQLAlchemy()

class Movie(dataBase.Model):
    movie = dataBase.Column(dataBase.Integer, primary_key=True, nullable=False)
    title = dataBase.Column(dataBase.String(255), nullable=False)
    director = dataBase.Column(dataBase.String(255), nullable=False)
    rating = dataBase.Column(dataBase.Integer, nullable=False)  