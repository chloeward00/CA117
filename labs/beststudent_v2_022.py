import sys

def main():
	try:
		highest = 0
		letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		f = open(sys.argv[1], 'r')
		for line in f:
			line = line.split()
			if int((line[0].strip())) > highest:
				highest = int((line[0].strip()))
				best = ' '.join(line[1:])
			if best[:2] in letters
			    print ('Invalid mark {} encountered. Exiting').format(sys.argv[1]))

		print('Best student: ' + best)
		print('Best mark: ' + str(highest))
	except FileNotFoundError:
		print('The file {} could not be found'.format(sys.argv[1]))

if __name__ == '__main__':
	main()