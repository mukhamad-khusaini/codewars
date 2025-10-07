class Cube(object):
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    __side=0

    def __init__(self, inte=0):
        self.__side = abs(inte)

    def get_side(self):
        """Return the side of the Cube"""
        return self.__side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self.__side = abs(new_side)
