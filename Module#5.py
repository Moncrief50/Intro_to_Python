# Import python graphics library into environment
from graphics import *

# Create class point defining coordinates of a rectangle
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
         return "({}, {})".format(self.x, self.y)

# Create class rectangle to manufacture rectangle objects
class Rectangle:
    """ A class to manufacture rectangle objects """
    # Create Rectangle
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

# Now that we have created our rectangle object we can test it
# Create a rectangle
def create_rectangle(x, y, width, height):
    return Rectangle(Point(x, y), width, height)

# Return rectangle as a string
def str_rectangle(self):
    return str(self)

# Shift rectangle
def shift_rectangle(self, dx,dy):
    ix = self.corner.x
    iy = self.corner.y
    self.corner.x += dx
    self.corner.y += dy

 # Offset Rectangle
def offset_rectangle(self, dx, dy):
    iy, ix = self.corner.x, self.corner.y
    return Rectangle(Point(ix + dx, iy + dy), self.width, self.height)

# Testing the class rectangle
r1 = create_rectangle(10, 20, 30, 40)
print("Str Rectangle")
print(str_rectangle(r1))

shift_rectangle(r1, -10, -20)
print("Shift Rectangle")
print(str_rectangle(r1))

r2 = offset_rectangle(r1, 100, 100)
print("Offset Rectangles")
print(str_rectangle(r1))
print(str_rectangle(r2))
