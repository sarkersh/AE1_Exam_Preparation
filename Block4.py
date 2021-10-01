from abc import ABC, abstractmethod

class Shape2D(ABC):

    def __init__(self, name):
        self.name = name
        self.FAMILY = '2D'

    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape2D):
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    def __repr__(self):
        return self.FAMILY

    def __str__(self):
        return self.name

    def calculate_area(self):
        return self.length * self.width


class Triangle(Shape2D):
    def __init__(self, name, base, height):
        self.name = name
        self.base = base
        self.height = height

    def __repr__(self):
        return self.FAMILY

    def __str__(self):
        return self.name

    def calculate_area(self):
        return self.base * self.height / 2


class Square(Rectangle):
   def __init__(self, name, length):
      self.name = name
      self.length = length

   def __repr__(self):
       return self.FAMILY

   def __str__(self):
       return self.name

   def calculate_area(self):
      return self.length * self.length

r = Rectangle('rec1',10,20)
print ('rectngle area: ',r.calculate_area())

tri = Triangle('triangle1',10,20)
print ('triangle area: ',tri.calculate_area())

s = Square('square',10)
print ('square area: ',s.calculate_area())

# class Shape2D(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def calculate_area(self):
#         pass
#
# class Rectangle(Shape2D):
#     def __init__(self, name, length, width):
#         super().__init__(name)
#
#     def __repr__(self):
#         return
#
#     def __str__(self):
#         return
#
#     def calculate_area(self, length, width):
#         self.length = float(length)
#         self.width = float(width)
#
#
#
# class Triangle(Shape2D):
#     def __init__(self, name, base, height):
#         self.base = float(base)
#         self.height = float(height)
#         super().__init__(name)
#
#     def __repr__(self):
#         return
#
#     def __str__(self):
#         return
#
#     def calculate_area(self, base, height):
#         def calculate_area(self, base, height):
#             self.base = float(base)
#             self.height = float(height)
#
#
# class Square(Rectangle):
#     def __init__(self, name, length):
#
#     def __repr__(self):
#         return
#
#     def __str__(self):
#         return
