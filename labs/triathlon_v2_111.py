class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return 'Name: {:s}\nID: {:d}'.format(self.name, self.tid)

def sort_on(s):
    return s.name

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

    def __str__(self):

        n = ['{}'.format(s) for s in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(n)
