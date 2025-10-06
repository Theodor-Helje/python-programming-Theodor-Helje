import numpy as np
import matplotlib.pyplot as plt

class Video:
    """Class to describe a general video, used as a building block for other classes"""
    def __init__(self, title=None, genre=None, rating = None):
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
    
    @title.setter
    def title(self, title):
        self._title = title
    
    @genre.setter
    def genre(self, genre):
        self._genre = genre

    @rating.setter
    def rating(self, rating):
        self._rating = rating

    def info(self):
        return f"video with title {self.title}, genre: {self.genre}, rating {self.rating} \n"
    
class TV_serie(Video):
    """Class to describe a TV-series, uses the video class as parent"""
    def __init__(self, title=None, genre=None, rating=None, num_episodes=None):
        super().__init__(title, genre, rating)
        self.num_episodes = num_episodes
    
    @property
    def num_episodes(self):
        return self._num_episodes
    
    @num_episodes.setter
    def num_episodes(self, num_episodes):
        self._num_episodes = num_episodes
    
    def info(self):
        return f"TV-series, title: {self.title}, genre: {self.genre}, rating: {self.rating}, episodes: {self.num_episodes} \n"

class Movie(Video):
    """Class to describe a movie, uses the video class as parent"""
    def __init__(self, title=None, genre=None, rating=None, duration=None):
        super().__init__(title, genre, rating)
        self.duration = duration
    
    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, duration):
        self._duration = duration
    
    def info(self):
        return f"Movie, title: {self.title}, genre: {self.genre}, rating: {self.rating}, duraition: {self.duration} \n"
    
class Documentary(Video):
    """Class to describe a documentary, uses the video class as parent"""
    def __init__(self, title=None, genre=None, rating=None):
        super().__init__(title, genre, rating)

pokemon = TV_serie("Pokemon", "Cartoon", 4.5, 550)
titanic = Movie("Titanic", "Romance", 4.7, 194)
code = Documentary("The Code", "Math", 4)

for video in tuple((pokemon, titanic, code)):
    print(video.info())

class frac:
    def __init__(self, nominator=None, denominator=None):
        self.nominator = nominator
        self.denominator = denominator
    
    @property
    def nominator(self):
        return self._nominator
    
    @property
    def denominator(self):
        return self._denominator
    
    @nominator.setter
    def nominator(self, nominator):
        self._nominator = nominator
    
    @denominator.setter
    def denominator(self, denominator):
        self._denominator = denominator