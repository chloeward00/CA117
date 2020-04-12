import sys

def seconds(t):
    (x, y) = t.split(':')
    total = int(x) * 60 + int(y)
    return(total)

def sorter(t):
    return seconds(t[1])

def main():
    d = {}
    for lines in sys.stdin:
        try:
            lines = lines.split()
            d[lines[0]] = min(lines[1:], key=seconds)
        except ValueError:
            continue

    the_winner = min(d.items(), key=sorter)
    print('{} : {}'.format(the_winner[0], the_winner[1]))


if __name__ == '__main__':
    main()
