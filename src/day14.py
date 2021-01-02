#!/snap/bin/pypy3

from aoc import repres

with open("../data/day14.txt", "rt") as file:
	data = [[int(y) if i>0 else y for (i,y) in enumerate(x.split(' ')) if i in [0, 3, 6, 13]] for x in file.read().strip().split('\n')]

part2 = True

target_time = 2503

if part2:
	scores = {}
	for d in data:
		scores[d[0]] = 0

for t in range(1, target_time+1) if part2 else range(target_time, target_time+1):
	distances = []
	for d in data:
		[name, speed, time, rest] = d
		distance = (t // (time + rest)) * time * speed + min(t % (time + rest), time) * speed
		distances.append((distance, name))
	if part2:
		distances.sort()
		distances.reverse()
		for n in [n for (s,n) in distances if s == distances[0][0]]:
			scores[n] += 1

if part2:
	r = max(scores.values())
else:
	r = max([d for d,n in distances])

repres(r, part2)
