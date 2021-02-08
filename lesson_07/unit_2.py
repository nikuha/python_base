from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size_1=None, size_2=None):
        self.size_1 = size_1
        self.size_2 = size_2

    @abstractmethod
    def tissue(self):
        pass


class Coat(Clothes):

    @property
    def tissue(self):
        return self.size_1/6.5 + 0.5


class Suit(Clothes):

    @property
    def tissue(self):
        return 2 * self.size_2 + 0.3


my_coat = Coat(size_1=15)
print(my_coat.tissue)

my_suit = Suit(size_2=10)
print(my_suit.tissue)
