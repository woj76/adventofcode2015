#!/snap/bin/pypy3

from aoc import repres

part2 = True

with open("../data/day17.txt", "rt") as file:
	sizes = [int(x) for x in file.read().strip().split('\n')]

containers = [i for i in range(len(sizes))]

all_checked = {}

def check(used, s_used):
	load = sum([sizes[x] for x in used])
	if load == 150:
		all_checked[s_used] = True
		return
	elif load > 150:
		return
	for i in containers:
		if i in used:
			continue
		next_candidate = sorted(used + [i])
		snc = ",".join([str(x) for x in next_candidate])
		if snc in all_checked:
			break
		check(next_candidate, snc)

check([],"")

if part2:
	cnts = [s.count(',') + 1 for s in all_checked]
	r = cnts.count(min(cnts))
else:
	r = len(all_checked)

repres(r, part2)
