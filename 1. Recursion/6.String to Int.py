def string2int(string):
	if len(string) == 1:
		return ord(string) - ord('0')

	lastPart = string2int(string[1:])
	first = ord(string[0]) - ord('0')
	length = len(string)-1

	return first*(10**length)+lastPart
	
print(string2int('10212'))