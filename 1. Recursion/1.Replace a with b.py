def replaceChar(s, a, b):
	if len(s) == 0:
		return s 

	first = s[0]
	last = replaceChar(s[1:],a,b)

	if first == a :
		return b + last
	else:
		return s[0] + last

print(replaceChar('xcx','c','x'))