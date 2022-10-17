import math

def divisors(number):
	for i in range(1,int(math.sqrt(number))+1):
		if (number % i == 0):
			print(i,number//i,':',end = ' ')
	print()

if __name__ == '__main__':
	divisors(100)