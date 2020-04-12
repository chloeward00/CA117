from collections import namedtuple

Module = namedtuple('Module', 'code title ects')

CA1_MODULES = {'CA103': Module('CA103', 'Computer Systems', 5),
               'CA106': Module('CA106', 'Web Design', 5),
               'CA115': Module('CA115', 'Digital Innovation', 5),
               'CA116': Module('CA116', 'Computer Programming I', 10),
               'CA117': Module('CA117', 'Computer Programming II', 10),
               'CA169': Module('CA169', 'Networks and Internet', 5),
               'CA170': Module('CA170', 'Operating Systems', 5),
               'CA172': Module('CA172', 'Problem Solving', 5),
               'MS121': Module('MS121', 'IT Mathematics', 10)}

class Student(object):

    def __init__(self, idnum, surname, firstname):
        self.idnum = idnum
        self.surname = surname
        self.firstname = firstname
        self.mods = CA1_MODULES
        self.marks = {code: 0 for code in self.mods.keys()}

    def __str__(self):
        name = '{} : {} {}'.format(self.idnum,
                                   self.firstname,
                                   self.surname)
        unline = '-' * len(name)
        the_results = '\n'.join(
            [code + ' : ' + self.mods[code].title + ' : ' + str(
                self.marks[code]) for code in sorted(self.mods.keys())])

        passmark = 'Precision mark: {:.2f}'.format(self.precision_mark())
        if self.passed():
            the_outcome = 'Pass'
        elif self.passed_by_compensation():
            the_outcome = 'Pass by compensation'
        else:
            the_outcome = 'Fail'

        return '\n'.join([name, unline, the_results, passmark, the_outcome])

    def add_mark(self, module, grade):
        self.marks[module] = grade

    def precision_mark(self):
        the_total = 0
        the_count = 0
        for k in self.marks.keys():
          if k in self.mods.keys():
            weight = self.mods[k][-1]
            if weight == 10:
              the_total += self.marks[k] * 2
              the_count += 2
            else:
              the_total += self.marks[k]
              the_count += 1

        return the_total / the_count

    def passed(self):
        return len([m for m in self.marks.values() if m < 40]) == 0

    def passed_by_compensation(self):
        failed = [(mod, mark) for mod, mark in self.marks.items() if mark < 40]
        total_credits = sum([m[2] for m in self.mods.values()])

        b0 = self.precision_mark() >= 45
        b1 = len([mark for mod, mark in failed if mark < 35]) == 0
        b2 = total_credits / 6 >= sum([self.mods[mod][2] for mod, mark in failed])

        return b0 and b1 and b2
