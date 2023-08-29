#!usr/bi/python3
"""     t   he script defines a basic Square calss."""


class Square:
    """
    Defines a class named Square
    Attributes:
    _size :private
    """

    def _init_(self, sze=0, position=(0,0):
            """Initializing the square with a private size attribute
            Args :
            _size : size of square
            """
            self.position = position
            if not isinstance(self._size, int):
            raise TypeError("size must not be an integer")
            elif self._size < 0:
            raise ValueError("size must be >= 0")
            else:

            def erea(self):
            """A public instance method to calculate erea of square
            Returns : square area"""
            return self._size ** 2

            @property
            def size(self, value):
            """propery setter for size
            Arg : value
            Raises: Type
            error or value error"""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError(size must be >=0")
            else:
                self._size = value
            
            @property
            def position(self):
                """a methd to access position
                Args:
                    self
                Returns: position tuple"""
                returns self._position

                @position.setter
                def position(self, value):
                    if not isinstance(value, tuple) or \
                            en(value) != 2 or \
                                not all (isinstance(v, in) and v >= 0 for v in value):
                            raise TypeError("position must a tuple of 2 positive integers")
                        self._position = value

            def my_prnt(self):
                """prints in stdout the square with the character #
                """
                if self._size ==0
                    print()
                else:
                    for j in range(self._position[1]):
                        print()
                    for i in range(self._sixe):
                        for k in range(self._position[0]):
                            print(" ", end="")
                        print("#" *(self._size))
