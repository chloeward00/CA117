class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return ('{} goal(s) and {} point(s)').format(self.goals, self.points)

    def __lt__(self, obj):
        if (self.goals + (self.points // 3)) < (obj.goals + (obj.points // 3)):
            return True
        else:
            return False

    #def __gt__(self, n):
        #if (self.goals + (self.points // 3)) >= (n.goals + (n.points // 3 )):
            #return True
        #else:
            #return False

    def __eq__(self, other):
        if (self.goals + (self.points // 3)) == other.goals +(other.points // 3):
            return True
        else:
            return False

    def __add__(self,  others):
        add = (self.goals + others.goals) + (self.points + others.points)
        return ('{} goal(s) and {} point(s)').format(self.goals+others.goals, self.points+others.points)

    def __sub__(self, otherss):
        subgoals = (self.goals - otherss.goals) 
        subpoints = (self.points - otherss.points)
        return ('{} goal(s) and {} points(s)').format(subgoals, subpoints)

    def __iadd__(self, newother):

        s2alias = Score(self.goals + newother.goals, self.points + newother.points)
        return s2alias
        #if (s2alias > newother):
            #return True
        #else:
            #r#eturn False


    #def equal_to(self, score3):
        #if (self.goals + (self.points // 3)) == int(score3.goals + (score3.points // 3)):
            #return True
        #else:
            #returnFalse
