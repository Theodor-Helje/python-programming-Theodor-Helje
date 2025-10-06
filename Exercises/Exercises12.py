import numpy as np
import matplotlib.pyplot as plt

class Video:
    def __init__(self, title=None, genre=None, rating = .0, type=None):
        self.title = title
        self.genre = genre
        self.rating = rating
    
    @property
    def title(self):
        return self._title
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def rating(self):
        return self._rating
    
    @property
    def type(self):
        return self._type
    
    @title.setter
    def title(self, title):
        self._title = title
    
    @genre.setter
    def genre(self, genre):
        self._genre = genre

    @rating.setter
    def rating(self, rating):
        self._rating = rating

    @type.setter
    def type(self, type):
        self._type = type

    def info(self):
        return f"{self.type} with title {self.title}, genre: {self.genre}, rating {self.rating}"