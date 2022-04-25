class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2


area_circle = Circle(5)
print(area_circle.area())
