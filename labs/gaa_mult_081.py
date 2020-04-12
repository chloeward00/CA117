class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return '{} goal(s) and {} point(s)'.format(self.goals, self.points)

    def __gt__(self, others):
        return ((self.goals * 3) + self.points) > ((others.goals * 3) + others.points)

    def __lt__(self, others):
        return ((self.goals * 3) + self.points) < ((others.goals * 3) + others.points)

    def __ge__(self, others):
        return ((self.goals * 3) + self.points) >= ((others.goals * 3) + others.points)

    def __le__(self, others):
        return ((self.goals * 3) + self.points) <= ((others.goals * 3) + others.points)

    def __eq__(self, others):
      return ((self.goals * 3) + self.points) == ((others.goals * 3) + others.points)

    def __add__(self, others):
        go = (self.goals + others.goals)
        po = (self.points + others.points)
        return Score(go, po)

    def __mul__(self, s=2):
      go = (self.goals * s)
      poi = (self.points * s)
      return Score(go, poi)

    def __rmul__(self, s=2):
      go = s * self.goals
      poi = s * self.points
      return Score(go, poi)

    def __imul__(self, s=2):
      self.goals *= s
      self.points *= s
      return self

    def __sub__(self, others):
        go = (self.goals - others.goals)
        po = (self.points - others.points)
        return Score(go, po)

    def __iadd__(self, others):
       self.goals += others.goals
       self.points += others.goals
       return self

    def __isub__(self, others):
       self.goals -= others.goals
       self.points -= others.points
       return self
