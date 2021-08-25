def pairStar(s):
	if len(s) == 1:
		return s 


	elif s[0] != s[1]:
		return s[0] + pairStar(s[1:])

	else:
		return s[0]+'*'+ pairStar(s[1:])

print(pairStar('aaaa'))
