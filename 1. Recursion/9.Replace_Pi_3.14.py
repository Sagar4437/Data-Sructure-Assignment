def replacePi(s):
	if len(s) <= 1:
		return s

	if s[0:2] != 'pi':
		return s[0] + replacePi(s[1:])
	else:
		return '3.14' + replacePi(s[2:])

print(replacePi('pi_pic'))