#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        # Initialize width and height attributes
        self.width = width
        self.height = height

    @property
    def width(self):
        # Getter method for retrieving width
        return self.__width

    @width.setter
    def width(self, value):
        # Setter method for setting width
        # Check if value is an integer
        if not isinstance(value, int):
            # Raise TypeError if not an integer
            raise TypeError("width must be an integer")
        # Check if value is non-negative
        elif value < 0:
            # Raise ValueError if negative
            raise ValueError("width must be >= 0")
        else:
            # Set width if it meets conditions
            self.__width = value

    @property
    def height(self):
        # Getter method for retrieving height
        return self.__height

    @height.setter
    def height(self, value):
        # Setter method for setting height
        # Check if value is an integer
        if not isinstance(value, int):
            # Raise TypeError if not an integer
            raise TypeError("height must be an integer")
        # Check if value is non-negative
        elif value < 0:
            # Raise ValueError if negative
            raise ValueError("height must be >= 0")
        else:
            # Set height if it meets conditions
            self.__height = value

