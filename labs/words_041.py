import sys
import string

def mydictionary():
    dictionary = {}
    for line in sys.stdin:
        thewords = line.lower().strip().split()
        for aword in thewords:
            aword = aword.strip(string.punctuation)
            if aword == '':
                continue
            if aword not in dictionary:
                dictionary[aword] = 1
            else:
                dictionary[aword] += 1
    return dictionary

def main():
    dictionary = mydictionary()
    for (x, y) in sorted(dictionary.items()):
        print('{} : {}'.format(x, y))


if __name__ == '__main__':
    main()
