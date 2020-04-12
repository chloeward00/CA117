import sys

dictionary = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
}

def English_Irish(filename):

    Eng_Irish = {}
    with open(filename, "r") as f:
        for lines in f:
            values = lines.split()
            Eng_Irish[values[0]] = values[1]

    return Eng_Irish

def main():
    Eng_Irish = English_Irish(sys.argv[1])
    for lines in sys.stdin:
        lines = lines.split()
        the_words = []
        for number in lines:
            try:
                the_words.append(Eng_Irish[dictionary[int(number)]])
            except (ValueError, KeyError):
                the_words.append("unknown")
        print (" ".join(the_words))

if __name__ == "__main__":
    main()
