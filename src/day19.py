#!/snap/bin/pypy3

from aoc import repres

part2 = True

with open("../data/day19.txt", "rt") as file:
	[reps, st] = file.read().strip().split('\n\n')
	reps = [tuple(x.split(' => ')) for x in reps.split('\n')]

collect = {}

for (s,r) in reps:
	i = 0
	while True:
		try:
			i = st.index(s, i)
			ns = st[:i] + r + st[i+len(s):]
			i += 1
			collect[ns] = True
		except:
			break

repres(len(collect), False)

steps = 0

while st != 'e':
	for (s,r) in reps:
		c = st.count(r)
		if c:
			st = st.replace(r, s)
			steps += c

repres(steps, True)
