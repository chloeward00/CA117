import sys
import math

def Quadratic(a, b, c):
   r1 = (-b + ((b ** 2) - 4 * a * c) ** 0.5) / (2 * a)
   r2 = (-b - ((b ** 2) - 4 * a * c) ** 0.5) / (2 * a)

   if type(r1) == float and type(r2) == float:
      print ("r1 = {}, r2 = {}".format(r1, r2))

   else:
     print(None)

def main():
   for lines in sys.stdin:
      numbers = lines.split(" ")
      a = int(numbers[0])
      b = int(numbers[1])
      c = int(numbers[2])
      (Quadratic(a, b, c))

if __name__ == "__main__":
   main()
