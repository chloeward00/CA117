import sys

def sorter(t):
    return t[1]


def main():
    skipped = []
    studentmarks = {}
    for lines in sys.stdin:
        name = lines.strip().split(':')[0]
        marks = lines.strip().split(':')[1].split(',')

        totalmarks = 0
        try:
            for the_mark in marks:
                totalmarks += int(the_mark)
        except ValueError:
            skipped.append(name)
        else:
            studentmarks[name] = totalmarks

    for student in sorted(studentmarks.items(), key=sorter, reverse=True):
        print('{} : {}'.format(student[0], student[1]))

    print('Skipped:')
    for astudent in skipped:
        print(astudent)

if __name__ == '__main__':
    main()
