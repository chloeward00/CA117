import sys

def main():
    try:
        highestmark = 0
        f = open(sys.argv[1], 'r')
        for line in f:
            line = line.split()
            if int((line[0].strip())) > highestmark:
                highestmark = int((line[0].strip()))
                bestmark = ' '.join(line[1:])
        print('Best student: ' + bestmark)
        print('Best mark: ' + str(highestmark))
    except FileNotFoundError:
        print('The file {} could not be found'.format(sys.argv[1]))


if __name__ == '__main__':
    main()
