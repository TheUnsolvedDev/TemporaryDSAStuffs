import sys
sys.stdout = open('output.txt','wt')

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if (a > b):
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)

if __name__ == "__main__":
    
    for i in range(100):
	    print(gcd(10,13))