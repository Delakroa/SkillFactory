class Rectangle:
    """Клас прямоугольник"""

    def __init__(self, width, height):
        """Определяем атрибуты класса прямоугольника"""
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getArea(self):
        """Метод расчитывающий площадь"""
        return self.width * self.height
