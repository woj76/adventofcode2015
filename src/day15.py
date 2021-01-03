#!/snap/bin/pypy3

from aoc import repres

with open("../data/day15.txt", "rt") as file:
	data = [[int(y if i == 10 else y[:-1]) for (i,y) in enumerate(x.split(' ')) if i in [2, 4, 6, 8, 10]] for x in file.read().strip().split('\n')]

part2 = True

highest_score = float('-inf')

mixtures = [[a, b, c, d] for a in range(0, 101) for b in range(0, 101) for c in range(0, 101) for d in range(0, 101) if a + b + c + d == 100]

for mixture in mixtures:
	f = [0] * 5
	for i in range(5):
		for j in range(len(data)):
			f[i] += data[j][i]*mixture[j]
	score = 1
	for i in range(0,4):
		if f[i] < 0:
			f[i] = 0
		score *= f[i]
	if score > highest_score and (f[4] == 500 or not part2):
		highest_score = score

repres(highest_score, part2)
