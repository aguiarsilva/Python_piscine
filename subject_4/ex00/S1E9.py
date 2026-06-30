from abc import ABC, abstractmethod

class Charachter(ABC):
    """
    Abstract class that creates a characther. It takes two parameters:
        first_name
        is_alive set default to True

    It has a method named die() that changes the is_alive status to false
    """
    def __init__(self, first_name):
        """
        Class Constructor
        """
        self.first_name = first_name

    @abstractmethod
    def die(self):
        """
        Abstract method that should be fulfilled by the concrete classes    
        """
        pass

class Stark(Charachter):
    """
    This class inherits from Charachter class.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Concrete class constructor
        """
        super().__init__(first_name)
        self.is_alive = is_alive
        

    def die(self):
        """
        Implementation of the method die() required by the abstract class. This
        method changes de boolean from is_alive to False
        """
        self.is_alive = False

