import sys


def main():
    num = sorted(int(l.strip()) for l in sys.stdin)

    the_mean = sum(num) / len(num)
    the_median = num[len(num) // 2] if len(num) % 2 else (
        num[len(num) // 2 - 1] + num[len(num) // 2]) / 2

    print("Mean: {:.1f}\nMedian: {:.1f}".format(
        the_mean, the_median))

if __name__ == '__main__':
    main()
