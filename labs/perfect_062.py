import sys


def sumFac(n):
    return sum([i for i in range(1, (n // 2) + 1) if not n % i])


def Perfect(n):
    return n == sumFac(n)


def main():
    for line in sys.stdin:
        print(Perfect(int(line.strip())))

if __name__ == '__main__':
    main()
