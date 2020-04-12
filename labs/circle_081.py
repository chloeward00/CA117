class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        x_value = (self.x + other.x) / 2
        y_value = (self.y + other.y) / 2
        return Point(x_value, y_value)

    def __str__(self):
        return 'Centre: ({:.1f}, {:.1f})'.format(self.x, self.y)

class Circle(object):

    def __init__(self, centre=Point(0, 0), radius=0):
        self.radius = radius
        self.centre = centre

    def __str__(self):
        return "{}\nRadius: {}".format(self.centre.__str__(), self.radius)

    def __add__(self, other):
        centre_v = self.centre.midpoint(other.centre)
        radius_v = self.radius + other.radius
        return Circle(centre_v, radius_v)
