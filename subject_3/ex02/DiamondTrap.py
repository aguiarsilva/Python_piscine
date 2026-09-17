from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """ 
    Concrete class to create a King character.
    It inherits from Baratheon and Lannister classes.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Concrete class constructor for the new King class.
        """
        super().__init__(first_name)
        self.is_alive = is_alive

    def set_eyes(self, eyes):
        """
        Method to set the eyes attribute of the King instance.
        """
        self._eyes = eyes

    def set_hairs(self, hairs):
        """
        Method to set the hairs attribute of the King instance.
        """
        self._hairs = hairs

    def get_eyes(self):
        """
        Method to get the eyes attribute of the King instance.
        """
        return self._eyes

    def get_hairs(self):
        """
        Method to get the hairs attribute of the King instance.
        """
        return self._hairs

    @property
    def eyes(self):
        """
        Method to get the eyes attribute of the King instance.
        """
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        """
        Method to set the eyes attribute of the King instance.
        """
        self._eyes = value

    @property
    def hairs(self):
        """
        Method to get the hairs attribute of the King instance.
        """
        return self._hairs

    @hairs.setter
    def hairs(self, value):
        """
        Method to set the hairs attribute of the King instance.
        """
        self._hairs = value