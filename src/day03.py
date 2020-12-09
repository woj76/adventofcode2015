#!/usr/bin/python3

from aoc import repres

file = open("../data/day03.txt", "rt")
data = [x for x in file.readline().strip()]
file.close()

part2 = True

r = 0

positions = [(0,0), (0,0)] if part2 else [(0,0)]
turn = 0
visited = set()

for d in data:
	(x,y) = positions[turn]
	visited |= {(x,y)}
	if d == '<':
		x -= 1
	elif d == '>':
		x += 1
	elif d == '^':
		y += 1
	elif d == 'v':
		y -= 1
	positions[turn] = (x,y)
	turn += 1
	turn %= len(positions)
r = len(visited)

repres(r, part2)
