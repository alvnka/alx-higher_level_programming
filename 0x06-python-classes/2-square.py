#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """
        initialize the square with an optimal size

        :param size: size of the square
        :type size: int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
