from video_rental import ChildrenMovie
from video_rental import RegularMovie
from video_rental import NewReleaseMovie
from video_rental import Rental
from video_rental import Customer


def execute():
    customer = Customer('TestCustomer')
    customer.add_rental(Rental(ChildrenMovie('child1', 2), 5))# 数字いらなかった（2とか0とか）
    customer.add_rental(Rental(ChildrenMovie('child2', 2), 2))
    customer.add_rental(Rental(RegularMovie('regular', 0), 3))
    customer.add_rental(Rental(NewReleaseMovie('new1', 1), 3))
    customer.add_rental(Rental(NewReleaseMovie('new2', 1), 4))
    print(customer.calc_status())


if __name__ == "__main__":
    execute()
