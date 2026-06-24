from abc import ABC, abstractmethod

class Charachter(ABC):
    """
    Abstract class that creates a characther. It takes two parameters:
        first_name
        is_alive set default to True

    It has a method named die() that changes the is_alive status to false
    """
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name


    @abstractmethod
    def die(self):
        pass

class Stark(Charachter):
    """
    This class inherits from Charachter class.
    """

    def __init__(self, first_name, is_alive):
        super().__init__(first_name, is_alive=True)

    def die(self):
        is_alive = False

