#!/usr/bin/python
from memory_profiler import profile

class Polygon:

    __max_area = 0.0

    # method to render a shape
    def render(self):
        print("Rendering Polygon...")

    def getMaxArea(self) -> float:
        return self.__max_area

    def setMaxArea(self, newPrice) -> None:
        self.__max_area = newPrice

class Square(Polygon):
    # renders Square
    def render(self):
        print("Rendering Square...")

class Circle(Polygon):
    # renders circle
    def render(self):
        print("Rendering Circle...")


class Area(Polygon):
    pass

# create an object of Square
s1 = Square()
s1.render()

s2 = Area()
s2.render()
print(" { ", s2.getMaxArea(), " } ")

s2.__max_area = 1
print(" { ", s2.getMaxArea(), " } ")

s2.setMaxArea(12)
print(" { ", s2.getMaxArea(), " } ")

# create an object of Circle
c1 = Circle()
c1.render()
