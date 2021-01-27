#!/snap/bin/pypy3

from aoc import repres

part2 = True

with open("../data/day18.txt", "rt") as file:
	data = [list(x) for x in file.read().strip().split('\n')]

y_size = len(data)
x_size = len(data[0])

def neigbours(x, y, xs, ys):
	return [(x+dx, y+dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx != 0 or dy != 0) and 0 <= x+dx < xs and 0 <= y+dy < ys]

counts = [[0] * x_size for _ in range(y_size)]

for reps in range(100):
	for y in range(y_size):
		for x in range(x_size):
			counts[y][x] = sum([1 if data[yy][xx] == '#' else 0 for (xx,yy) in neigbours(x,y,x_size,y_size)])
	for y in range(y_size):
		for x in range(x_size):
			if data[y][x] == '#':
				data[y][x] = '#' if 2 <= counts[y][x] <= 3 else '.'
			else:
				data[y][x] = '#' if counts[y][x] == 3 else '.'
	if part2:
		data[0][0] = data[y_size-1][0] = data[0][x_size-1] = data[y_size-1][x_size-1] = '#'

r = sum([row.count('#') for row in data])

repres(r, part2)
