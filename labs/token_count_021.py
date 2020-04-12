#!/usr/bin/env python


import sys

def main():
    j = []
    for lines in sys.stdin:
       j.append(len(lines.split()))

    count = 0
    i = 0
    while i < len(j):
        count = count + j[i]
        i = i + 1
    print (count)


if __name__ == '__main__':
    main()
