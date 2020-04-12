#!/usr/bin/env python3

import sys
import calendar


thepoem = {0: 'Monday and Monday\'s child is fair of face.',
           1: 'Tuesday and Tuesday\'s child is full of grace.',
           2: 'Wednesday and Wednesday\'s child is full of woe.',
           3: 'Thursday and Thursday\'s child has far to go.',
           4: 'Friday and Friday\'s child is loving and giving.',
           5: 'Saturday and Saturday\'s child works hard for a living.',
           6: 'Sunday and Sunday\'s child is fair and wise and good in every way.',
           }

def daypoem(day, month, year):
    dayborn = calendar.weekday(year, month, day)
    return 'You were born on a {}'.format(thepoem[dayborn])


def main():
    day = int(sys.argv[1])
    month = int(sys.argv[2])
    year = int(sys.argv[3])
    print(daypoem(day, month, year))

if __name__ == '__main__':
    main()
