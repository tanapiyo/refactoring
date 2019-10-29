import os
from abc import ABCMeta, abstractmethod

class Movie(metaclass=ABCMeta):
    def __init__(self, title, price_code):
        self.__title = title
        self.__price_code = price_code

    @abstractmethod
    def calc_amount(self, days_rented):
      pass
    
    @abstractmethod
    def add_rental_point(self, days_rented):
      pass

    @property
    def price_code(self):
        return self.__price_code

    @price_code.setter
    def price_code(self, price_code):
        self.__price_code = price_code

    @property
    def title(self):
        return self.__title

class RegularMovie(Movie):
  def calc_amount(self, days_rented):
      add_amount = 2.0
      if days_rented > 2:
          add_amount += (days_rented - 2) * 1.5
      return add_amount
  
  def add_rental_point(self, days_rented):
    return 1

class ChildrenMovie(Movie):
  def calc_amount(self, days_rented):
      add_amount = 1.5
      if days_rented > 3:
          add_amount += (days_rented - 3) * 1.5
      return add_amount
      
  
  def add_rental_point(self, days_rented):
    return 1

class NewReleaseMovie(Movie):
  def calc_amount(self, days_rented):
      return days_rented * 3
  
  def add_rental_point(self, days_rented):
    if days_rented > 1:
      return 2
    return 1


class Rental:
    def __init__(self, movie, days_rented):
        self.__movie = movie
        self.__days_rented = days_rented

    @property
    def movie(self):
        return self.__movie

    @property
    def days_rented(self):
        return self.__days_rented

    def add_rental_point(self):
        return self.movie.add_rental_point(self.days_rented)
    
    def calc_amount(self):
        return self.movie.calc_amount(self.days_rented)


class Customer:

    __rentals = []

    def __init__(self, name):
        self.__name = name
        self.total_amount = 0.0
        self.frequent_renter_points = 0

    def add_rental(self, rental):
        self.__rentals.append(rental)

    @property
    def name(self):
        return self.__name
    
    def calc_status(self):
        rentals = []
        for rental in self.__rentals:
            self.frequent_renter_points += rental.add_rental_point()
            this_amount = rental.calc_amount()
            self.total_amount += this_amount
            rentals.append({'rental': rental, 'this_amount': this_amount})
        return self.return_result(rentals)
    
    def return_result(self, rentals):
      result = ""
      result += "Rental Record for " + self.name + os.linesep
      for rental in rentals:
        result += '\t' + rental['rental'].movie.title + \
                '\t' + str(rental['this_amount']) + os.linesep
      result += "Amount owed is " + str(self.total_amount) + os.linesep
      result += "You earned " + str(self.frequent_renter_points) + \
            " frequent renter points"
      return result


