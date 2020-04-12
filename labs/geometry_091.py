class Point(object):

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

class Shape(object):

    def __init__(self, points=[]):
        self.points = points

    def sides(self):
        lis = []
        i = 0
        while i < len(self.points) - 1:
            new = Point.distance(self.points[i], self.points[i + 1])
            lis.append(new)
            i += 1

        last = Point.distance(self.points[0], self.points[-1])
        lis.append(last)

        return lis

    def perimeter(self):
        return sum(self.sides())

class Triangle(Shape):

    def area(self):
        from math import sqrt
        a = self.sides()[0]
        b = self.sides()[1]
        c = self.sides()[-1]

        s = (a + b + c) / 2

        area = sqrt(s * (s - a) * (s - b) * (s - c))
        return area

class Square(Shape):

    def area(self):
        return self.sides()[0] ** 2
