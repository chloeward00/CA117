import sys

scoress = []
players = []
totals = []

def main():
	for lines in sys.stdin:
		lines = lines.split()
		if lines.isalpha():
			lines.append(players)
		scores = lines[-1]+ lines[-2]+ lines[-3]
		scores = list(scores)
		totalscores = int(lines[-1]) + int(lines[-2]) + int(lines[-3])
		totals.append(totalscores)
		print(lines)

if __name__ == '__main__':
	main()