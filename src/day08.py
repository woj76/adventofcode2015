#!/usr/bin/python3

from aoc import repres

file = open("../data/day08.txt", "rt")
data = [x for x in file.read().strip().split('\n')]
file.close()

part2 = True

r = 0

for d in data:
	l = 0
	i = 0
	while i < len(d):
		if d[i] == '\"':
			l += 2 if part2 else -1
		else:
			two = d[i:i+2]
			if two == '\\\\' or two == '\\\"':
				if part2:
					l += 3
				i += 1
			elif two == '\\x':
				if part2:
					l += 1
				else:
					i += 3
		l += 1
		i += 1
	if part2:
		r += (l - len(d))
	else:
		r += (len(d) - l)

repres(r, part2)
