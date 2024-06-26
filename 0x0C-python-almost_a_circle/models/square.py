#!/usr/bin/python3
""" Module for Square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class representing a square, inheriting from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a square instance """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter method for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter method for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Updates attributes based on the arguments """
        if args:
            arg_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary representation of the square """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }


if __name__ == "__main__":
    pass  # You can add tests here if needed
