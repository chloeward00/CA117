import sys
import string

def builddictionary():
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
    dictionary = builddictionary()
    newdictionary = {}
    for (x, y) in sorted(dictionary.items()):
        if len(x) > 3 and int(y) >= 3:
            newdictionary[x] = y
    width = len(max(newdictionary.keys(), key=len))

    for (x, y) in sorted(newdictionary.items()):
        print('{:>{:d}} : {:>2d}'.format(x, int(width), y))

if __name__ == '__main__':
    main()
