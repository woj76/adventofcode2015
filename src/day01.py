#!/usr/bin/python3

from aoc import repres

file = open("../data/day01.txt", "rt")
data = [x for x in file.readline() if x == '(' or x == ')']
file.close()

part2 = True

r = 0

for i, d in enumerate(data):
	if d == '(':
		r += 1
	else:
		r -= 1
	if part2 and r == -1:
		r = i + 1
		break

repres(r, part2)
