def palindrome_check(string,start,end):
	if start < end:
		if string[start] == string[end]:
			palindrome_check(string,start+1,end-1)
		else:
			return False
	return True

if __name__ == "__main__":
	string = 'racecars'
	print(palindrome_check(string,0,len(string)-1))