#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """We define modules for class Square"""
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

    def area(self):
        """
        calculate the area of a square given the dimensions

        :return: area of the square
        :Return type: int
        """
        return self.__size ** 2
