#!/usr/bin/python3

from aoc import repres

file = open("../data/day02.txt", "rt")
data = [[int(y) for y in x.split('x')] for x in file.read().split('\n') if x != '']
file.close()

part2 = True

r = 0

for d in data:
	d.sort()
	r += 2*d[0] + 2*d[1] + d[2]*d[1]*d[0] if part2 else 3*d[0]*d[1] + 2*d[1]*d[2] + 2*d[2]*d[0]

repres(r)
