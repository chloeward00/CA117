import sys

def main():

    evilwords = ['e', 'v', 'i', 'l']
    found = []
    for lines in sys.stdin:
        words = lines.strip().casefold()
        found = [s for s in words if s in evilwords]
        if found == evilwords:
            print(lines.strip())

if __name__ == '__main__':
    main()
