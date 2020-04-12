
class Weight(object):

    OUNCES_PER_POUND = 16

    def __init__(self, pounds=0, ounces=0):
        self.pounds = pounds
        self.ounces = ounces

    def __str__(self):
        return '{} pound(s) and {} ounce(s)'.format(self.pounds, self.ounces)

    @classmethod
    def from_ounces(cls, amount):
        ounces = amount // 16
        pounds = amount % 16
        return cls(ounces, pounds)

    def __eq__(self, other):
        return (self.pounds, self.ounces) == (other.pounds, other.ounces)

    def __lt__(self, other):
        return (self.pounds, self.ounces) < (other.pounds, other.ounces)

    def __ge__(self, other):
        return (self.pounds, self.ounces) >= (other.pounds, other.ounces)

    def __add__(self, other):
        return Weight((self.pounds + other.pounds), (self.ounces + other.ounces))

    def __iadd__(self, other):
        self.ounces += other.ounces
        self.pounds += other.pounds
        return self

    def __mul__(self, t=3):
        o = self.ounces * t
        p = self.pounds * t
        return Weight(p, o)
