class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}
        self.race_times = 0

    def __str__(self):
        li = []
        li.append('Name: {:s}'.format(self.name))
        li.append('ID: {:d}'.format(self.tid))
        li.append('Race time: {:d}'.format(self.race_times))
        return '\n'.join(li)

    def add_time(self, d, time):
        self.times[d] = time
        self.race_times += time

    def get_time(self, d):
        return self.times[d]
