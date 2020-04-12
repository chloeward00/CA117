#!/usr/bin/env python3

import sys


def main():
    try:
        file = sys.argv[1]
        highestlinesmarks = []
        lines = []
        with open(file, 'r') as f:
            for line in f:
                lines.append(line.strip())
            highestmark = 0

            for line in lines:
                try:
                    if highestmark < int(line[:2]):
                        highestmark = int(line[:2])
                except ValueError:
                    print('Invalid mark {} encountered. Skipping.'.format(line[:2]))

            for line in lines:
                if int(line[:2]) == highestmark:
                    highestlinesmarks.append(line[3:])

        beststudentmark = highestmark
        beststudents = ', '.join(highestlinesmarks)
        print('Best student(s): {}'.format(beststudents))
        print('Best mark: {}'.format(beststudentmark))
    except FileNotFoundError:
        print('The file {} could not be opened.'.format(file))

if __name__ == '__main__':
    main()
