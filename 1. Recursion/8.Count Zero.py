def countZero(n):
	#type 1
	num = str(n)

	if len(num) == 0:
		return 0

	lastPart = countZero(num[1:])

	if num[0]=='0':
		return 1 + lastPart
	else:
		return lastPart

print(countZero(10000))

