class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}

    def __str__(self):
        return 'Name: {:s}\nID: {:d}\nRace time: {:d}'.format(self.name, self.tid, self.total_time())

    def total_time(self):
        return sum(self.times.values())

    def add_time(self, sport, time):
        self.times[sport] = time

    def get_time(self, sport):
        if sport in self.times:
            return self.times[sport]
        else:
            return 'N/A'

    def __eq__(self, other):
        return(self.total_time() == other.total_time())

    def __gt__(self, other):
        return(self.total_time() > other.total_time())

    def __lt__(self, other):
        return(self.total_time() < other.total_time())

class Triathlon(object):

    def __init__(self):
        self.d = {}

    def add(self, s):
        self.d[s.tid] = s

    def remove(self, tid):
        del self.d[tid]

    def lookup(self, tid):
        if tid in self.d:
            return self.d[tid]
        else:
            return None

    def best(self):
        return min(self.d.values())

    def worst(self):
        return max(self.d.values())
