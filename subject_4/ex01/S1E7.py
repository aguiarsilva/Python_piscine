from S1E9 import Character

class Baratheon(Character):
    """
    Class Representing Baratheon family
    """

    def __init__(self, first_name, is_alive=True):
        """
        Concrete class constructor for Baratheon Class
        """
        super().__init__(first_name)
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        Implementation of the method die() required by the abstract class.
        This method changes the is_alive attr. to False.
        """
        self.is_alive = False

    def __str__(self):
        """
        String Representation for the Baratheon instance.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Representation of Baratheon instance for Debugging
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    def __init__(self, first_name, is_alive=True):
        """
        Concrete class constructor for Lannister Class
        """
        super().__init__(first_name)
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"


    def die(self):
        """
        Implementation of the method die() required by the abstract class.
        This method changes the is_alive attr. to False.
        """
        self.is_alive = False

    def __str__(self):
        """
        String representation of Lannister instance.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Representation of Baratheon instance for debugging
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Implementation of a Class method that create characters in a chain
        """
        return cls(first_name, is_alive)
        

