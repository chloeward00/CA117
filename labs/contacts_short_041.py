#!/usr/bin/env python

import sys


def main():
    with_numbers = sys.argv[1]
    contacts = {}
    with open(with_numbers, 'r') as f:
        contacts_info = f.readlines()
    for i in range(len(contacts_info)):
        persons_name, phone_number = contacts_info[i].split()
        contacts[persons_name] = phone_number.strip()

    for persons_name in sys.stdin:
        persons_name = persons_name.strip()
        if persons_name in contacts.keys():
            print('Name: {}'.format(persons_name))
            print('Phone: {}'.format(contacts[persons_name]))
        else:
            print('Name: {}'.format(persons_name))
            print('No such contact')

if __name__ == '__main__':
    main()
