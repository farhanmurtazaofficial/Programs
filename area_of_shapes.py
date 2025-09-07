class Shape:
    def __init__(self):
        pass
    def area(self):
        pass
    def __str__(self):
        return f"The of Area of Circle is {circle_obj.area()}, Area of Rectangle is {rectangle_obj.area()} and Area of Triangle is {triangle_obj.area()}"
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5*self.base*self.height

circle_obj = Circle(5)
rectangle_obj = Rectangle(5,5)
triangle_obj =Triangle(5,6)
myshape_obj = Shape()
print(myshape_obj)