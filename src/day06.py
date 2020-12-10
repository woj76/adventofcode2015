#!/usr/bin/python3

from aoc import repres

file = open("../data/day06.txt", "rt")
data = [x for x in file.read().strip().replace(' through ', '-').replace('turn ', '').split('\n')]
file.close()

part2 = True

r = 0

grid = {}

for x in range(0, 1000):
	for y in range (0, 1000):
		grid[(x,y)] = 0

for d in data:
	[op, rng] = d.split(' ')
	[b,e] = rng.split('-')
	[x1, y1] = [int(x) for x in b.split(',')]
	[x2, y2] = [int(x) for x in e.split(',')]
	for x in range(x1, x2+1):
		for y in range(y1, y2+1):
			if part2:
				if op == "on":
					grid[(x,y)] += 1
				elif op == "off":
					grid[(x,y)] -= 1
					if grid[(x,y)] < 0:
						grid[(x,y)] = 0
				else:
					grid[(x,y)] += 2
			else:
				if op == "on":
					grid[(x,y)] = 1
				elif op == "off":
					grid[(x,y)] = 0
				else:
					grid[(x,y)] = (grid[(x,y)] + 1) % 2

r = sum(grid.values())

repres(r, part2)
