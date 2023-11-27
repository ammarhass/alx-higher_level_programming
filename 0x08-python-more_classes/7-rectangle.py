
#!/usr/bin/python3
""" class """


class Rectangle:
    """ a Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """define a Rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        l = []
        for i in range(self.__height):
            for j in range(self.__width):
                l.append(str(self.print_symbol))
            if i != self.__height - 1:
                l.append('\n')
        return ("".join(l))

    def __repr__(self):
        l = "Rectangle(" + str(self.__width)
        l += ", " + str(self.__height) + ")"
        return l

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
