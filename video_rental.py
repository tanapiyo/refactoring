import os


class Movie:

    CHILDRENDS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self.__title = title
        self.__price_code = price_code

    @property
    def price_code(self):
        return self.__price_code

    @price_code.setter
    def price_code(self, price_code):
        self.__price_code = price_code

    @property
    def title(self):
        return self.__title


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
    
    def add_rental_price(self, rental):
      this_amount = 0.0
      # 一行ごとに金額を計算
      if rental.movie.price_code == Movie.REGULAR:
          this_amount += 2.0
          if rental.days_rented > 2:
              this_amount += (rental.days_rented - 2) * 1.5
      elif rental.movie.price_code == Movie.NEW_RELEASE:
          this_amount += rental.days_rented * 3
      elif rental.movie.price_code == Movie.CHILDRENDS:
          this_amount += 1.5
          if rental.days_rented > 3:
              this_amount += (rental.days_rented - 3) * 1.5
      return this_amount
    
    def add_rental_point(self, rental):
      self.frequent_renter_points += 1
      # 新作を二日以上借りた場合はボーナスポイント
      if rental.movie.price_code == Movie.NEW_RELEASE and \
              rental.days_rented > 1:
          self.frequent_renter_points += 1

    def statement(self):
        rentals = []
        for rental in self.__rentals:
            this_amount = 0.0
            this_amount = self.add_rental_price(rental)
            self.add_rental_point(rental)
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


