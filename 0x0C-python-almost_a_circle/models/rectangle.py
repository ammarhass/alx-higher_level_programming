#!/usr/bin/python3
"""Define a Rectangle class"""
from models.base import Base

class Rectangle(Base):
    """a Rectanble class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value\

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints "#" in the stdout"""
        [print("") for l in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for z in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print("")

    def __str__(self):
        """magic method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update the class instance attribute"""
        if args and len(args) != 0:
            j = 0
            for i in args:
                if j == 0:
                    if i is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = i
                elif j == 1:
                    self.width = i
                elif j == 2:
                    self.height = i
                elif j == 3:
                    self.x = i
                elif j == 4:
                    self.y = i
                j = j + 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                     self.y = value

    def to_dictionary(self):
        """method that returns the dictionay representation of a Rectangle"""
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width' :self.width
                }
