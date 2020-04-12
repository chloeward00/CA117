class MP3Track(object):

    def __init__(self, title, duration, by=[]):
        self.title = title
        self.duration = duration
        self.by = by

    def __str__(self):
        return'Title: {}\nBy: {}\nDuration: {:}'.format(self.title, ', '.join(self.by), self.duration)

    def __gt__(self, other):
        if (self.duration > other.duration):
            return 'True'
        else:
            return 'False'
