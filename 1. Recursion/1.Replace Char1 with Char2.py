'''
		Q: define funtion which convert char1 from string to char2
		ip:
			string = abcba
			char1 = b
			char2 = #
		op:
			a#c#a

'''


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
	char1 = 'b'
	char2 = '#'

	result = replaceChar(string,char1,char2)
	print(result)