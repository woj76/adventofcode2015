#!/snap/bin/pypy3

from aoc import repres

part2 = True

def check_pw(s):
	if 'i' in s or 'l' in s or 'o' in s:
		return False
	straight = False
	for i in range(len(s)-2):
		if ord(s[i+2]) == ord(s[i]) + 2 and ord(s[i+1]) == ord(s[i]) + 1:
			straight = True
			break
	if not straight:
		return False
	pairs = []
	i = 0
	while i < len(s) - 1:
		if s[i] == s[i+1]:
			i += 1
			if pairs and not s[i] in pairs:
				return True
			pairs.append(s[i])
		i += 1
	return False


def inc_str(s):
	s = list(s)
	for i in range(len(s)-1, -1, -1):
		if s[i] == 'z':
			s[i] = 'a'
		else:
			s[i] = chr(ord(s[i]) + 1)
			break
	return "".join(s)

input = "vzbxkghb"

while not check_pw(input):
	input = inc_str(input)

if part2:
	input = inc_str(input)
	while not check_pw(input):
		input = inc_str(input)

repres(input, part2)
