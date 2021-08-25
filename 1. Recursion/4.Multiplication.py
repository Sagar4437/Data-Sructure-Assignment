
def mult1(m,n):
	#type 1
	if n == 0:
		return 0

	first = m
	lastPart = mult1(m,n-1)

	return first + lastPart


def mult2(m,n):
	#type 2
	if n == 0:
		return 0

	firstPart = mult2(m,n-1)
	last = m

	return firstPart + last



print(mult1(6,3))