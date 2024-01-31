#!/usr/bin/python3

'''Module for shapes'''

class Rectangle:
    '''Class for rectangle'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initialize a rectangle object'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Get the width attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width attribute'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Get the height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the height attribute'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''Return the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Return the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Compare two rectangles and return the one with a larger area or the first one if the areas are equal'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        area_1 = rect_1.area()
        area_2 = rect_2.area()
        return rect_1 if area_1 >= area_2 else rect_2

    @classmethod
    def square(cls, size=0):
        '''Create a new instance with height and width equal to size'''
        return cls(size, size)

    def __str__(self):
        '''Return a string representation of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ''
        return '\n'.join([str(self.print_symbol) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        '''Return a string representation of the rectangle suitable for creating a new instance'''
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        '''Decrement the number_of_instances attribute and print a message when a rectangle instance is deleted'''
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

# Example Usage:
if __name__ == "__main__":
    rect1 = Rectangle(3, 4)
    rect2 = Rectangle(2, 6)
    print(Rectangle.bigger_or_equal(rect1, rect2))

    square = Rectangle.square(5)
    print(square)
    print(f"Area of square: {square.area()}")
