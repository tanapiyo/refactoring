from video_rental import Movie
from video_rental import Rental
from video_rental import Customer


def execute():
    customer = Customer('TestCustomer')
    customer.add_rental(Rental(Movie('child1', 2), 5))
    customer.add_rental(Rental(Movie('child2', 2), 2))
    customer.add_rental(Rental(Movie('regular', 0), 3))
    customer.add_rental(Rental(Movie('new1', 1), 3))
    customer.add_rental(Rental(Movie('new2', 1), 4))
    print(customer.statement())


if __name__ == "__main__":
    execute()
