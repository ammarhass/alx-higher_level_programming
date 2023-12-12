#!/usr/bin/python3
"""define a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """intialize a new square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update method"""
        if args and len(args) != 0:
            j = 0
            for i in args:
                if j == 0:
                    if i is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = i
                elif j == 1:
                    self.size = i
                elif j == 2:
                    self.x = i
                elif j == 3:
                    self.y = i
                j = j + 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictioanry representation of a Square"""
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
