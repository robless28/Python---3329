# implement 3 classes that inherit from the "shape" class 
    # Rectangle 
    # circle 
    # square (inherits from rectangle)

##### First...
from baseShape import Shape

class Rectangle(Shape):
    # overwrite contructor?
    def __init__(self, x = 0, y = 0, w = 10, l = 20):
        super().__init__(x, y)
        # add a lenght and width
        self.width = w
        self.lenght = l

    # add a string method to print the details of this shape nicely 
    def __str__(self):
        details = "This is a rectangle: \n"
        details += f"Attributes \n coordinates: ({self.x}, {self.y})\n"
        details += f"size: (w: {self.width}, l: {self.lenght}, area: 
        return details

    #overwrite getShape?

myRect = Rectangle()

print(myRect)