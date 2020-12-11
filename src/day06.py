#!/usr/bin/python3

from aoc import repres

file = open("../data/day06.txt", "rt")
data = [x for x in file.read().strip().replace(' through ', '-').replace('turn ', '').split('\n')]
file.close()

part2 = True

r = 0

grid = [ [0] * 1000 for y in range(1000)]

for d in data:
	[op, rng] = d.split(' ')
	[b,e] = rng.split('-')
	[x1, y1] = [int(x) for x in b.split(',')]
	[x2, y2] = [int(x) for x in e.split(',')]
	for y in range(y1, y2+1):
		for x in range(x1, x2+1):
			if part2:
				if op == "on":
					grid[y][x] += 1
				elif op == "off":
					grid[y][x] -= 1
					if grid[y][x] < 0:
						grid[y][x] = 0
				else:
					grid[y][x] += 2
			else:
				if op == "on":
					grid[y][x] = 1
				elif op == "off":
					grid[y][x] = 0
				else:
					grid[y][x] = (grid[y][x] + 1) % 2

r = sum([sum(x) for x in grid])

repres(r, part2)
