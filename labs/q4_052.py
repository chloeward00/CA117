import sys

food_calories = {}
people = {}

filename = sys.argv[1]

with open(filename, 'r') as f:
        f = f.readlines()
        for fooditem in f:
            food = fooditem.split()
            food_calories[" ".join(food[0:-1])] = int(food[-1])

for lines in sys.stdin:
    diet = lines.strip().split(',')
    name = diet[0]
    food = diet[1:]

    calories = 0
    for fooditem in food:
        if fooditem in food_calories:
            calories += food_calories[fooditem]
        else:
            calories += 100

    people[name] = calories

longest = len(max(people, key=len))
largest = len(str(people[max(people, key=people.get)]))


for k in sorted(people, key=people.get):
    print('{:>{}} : {:>{}}'.format(k, longest, people[k], largest))
