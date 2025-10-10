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

class Frac:
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
    
    def _simplify(self, other=None):
        i = 100
        if type(other) == Frac:
            while True:
                if other.nominator % i == 0 and other.denominator % i == 0:
                    return Frac(other.nominator // i, other.denominator // i)
                i -= 1

    def __str__(self, other=None):
        if other == None:
            if self.nominator == 0:
                return ""
            else:
                return f"{self._simplify(self).nominator}/{self._simplify(self).denominator}"
        elif isinstance(other, Frac):
            if other.nominator == 0:
                return ""
            else:
                return f"{other._simplify(other).nominator}/{other._simplify(other).denominator}"
        raise TypeError("Cannor represent non Frac types as str")
    
    def mixed(self, other=None):
        if object.__eq__(other, None):
            if self.nominator >= self.denominator:
                whole_numbers = self.nominator // self.denominator
                return f"{whole_numbers} {self.__str__(Frac(self.nominator - whole_numbers * self.denominator, self.denominator))}"
            else:
                return(self.__str__())
        elif isinstance(other, Frac):
            if other.nominator >= other.denominator:
                whole_numbers = other.nominator // other.denominator
                return f"{whole_numbers} {self.__str__(Frac(other.nominator - whole_numbers * other.denominator, other.denominator))}"
            else:
                return(self.__str__(other))
        raise TypeError("Cannot perform function on non Frac type")
    
    def _get_common_denominator(self, other):
        if type(other) == type(self):
            first_nominator = int(self.nominator * other.denominator)
            second_nominator = int(other.nominator * self.denominator)
            common_denominator = int(self.denominator * other.denominator)
            return first_nominator, second_nominator, common_denominator
        raise TypeError(f"Cannot find common denominator with non Frac types")
    
    def __eq__(self, other):
        if isinstance(other, Frac):
            a, b = self._get_common_denominator(other)
            return a == b
    
    def __add__(self, other):
        if type(other) == type(self):
            a_nominator, b_nominator, denominator = self._get_common_denominator(other)
            return Frac(a_nominator + b_nominator, denominator)
        elif isinstance(other, int):
            return Frac(self.nominator + self.denominator, self.denominator)
        raise TypeError(f"Can only perform mathematical operation with Frac or int types")
    
    def __sub__(self, other):
        if type(other) == type(self):
            a_nominator, b_nominator, denominator = self._get_common_denominator(other)
            return Frac(a_nominator - b_nominator, denominator)
        elif isinstance(other, int):
            return Frac(self.nominator + self.denominator, self.denominator)
        raise TypeError(f"Can only perform mathematical operation with Frac or int types")
    
    def __mul__(self, other):
        if isinstance(other, int):
            return Frac(self.nominator * other, self.denominator)
        raise TypeError("Cannot perform __mul__ with non int types")
    
    def __rmul__(self, other):
        return Frac(self.__mul__(other))
    
    def __truediv__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if type(other) == type(self):
            return Frac(self.nominator * other.denominator, self.denominator * other.nominator)
        raise type("Cannot perform mathematical operation with non Frac type")
    
a = Frac(1, 2)
b = Frac(1, 7)
print(a + b)
c = Frac(1, 3)
for i in range(1, 11):
    c.nominator = i
    print(c.mixed())
c = Frac(10, 20)
print(c)