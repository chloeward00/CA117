import sys

contacts = {}


def main():
    with open(sys.argv[1], 'r') as f:
        for lines in f:
            [persons_name, persons_number, persons_email] = lines.strip().split()
            contacts[persons_name] = (persons_number, persons_email)

    for lines in sys.stdin:
        persons_name = lines.strip()
        print('Name: {}'.format(persons_name))
        try:
            print('Phone: {}'.format(contacts[persons_name][0]))
            print('Email: {}'.format(contacts[persons_name][1]))
        except KeyError:
            print('No such contact')

if __name__ == '__main__':
    main()
