def replaceChar(s, a, b):
	if len(s) == 0:
		return s 

	first = s[0]
	last = replaceChar(s[1:],a,b)

	if first == a :
		return b + last
	else:
		return s[0] + last

if __name__ == '__main__':

	string = 'abcbca'
	char1 = 'c'
	char2 = '#'

	result = replaceChar(string,char1,char2)
	print(result)