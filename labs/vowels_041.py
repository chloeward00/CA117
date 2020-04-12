import sys

the_vowels = "aeiou"
dictionary = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

def sort(j):
    return j[1]

def vowelcount(s):
    for vowel in the_vowels:
        dictionary[vowel] += s.count(vowel)
    return dictionary

def main():
    for lines in sys.stdin:
        lines = lines.strip().casefold()
        dictionary = vowelcount(lines)
    width = len(str(max(dictionary.values())))
    for (x, y) in sorted(dictionary.items(), key=sort, reverse=True):
        print("{:s} : {:>{}d}".format(x, y, width))

if __name__ == '__main__':
    main()
