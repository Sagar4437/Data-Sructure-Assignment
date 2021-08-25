#type 3 
def checkPalindrom(s):
	if len(s)==1:
		return True

	if s[0] != s[-1]:
		return False
	
	else:
		return checkPalindrom(s[1:-1])


print(checkPalindrom('racecar'))

