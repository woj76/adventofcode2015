#!/snap/bin/pypy3

from aoc import repres
from itertools import permutations

with open("../data/day13.txt", "rt") as file:
	data = [x.replace('.','').replace(' would','').replace('gain ','').replace('lose ','-').replace('happiness units by sitting next to ','') for x in file.read().strip().split('\n')]

part2 = True

happy = {}
names = []

for d in data:
	[n1, p, n2] = d.split(' ')
	if n1 not in names:
		names.append(n1)
	if n2 not in names:
		names.append(n2)
	happy[(n1,n2)] = int(p)

if part2:
	for n in names:
		happy[(n,"Myself")] = 0
		happy[("Myself", n)] = 0
	names.append("Myself")

max_happy = float('-inf')

len_names = len(names)

for arrangement in permutations(names):
	happiness = 0
	for i,n in enumerate(arrangement):
		happiness += happy[(n, arrangement[(i-1) % len_names])]
		happiness += happy[(n, arrangement[(i+1) % len_names])]
	max_happy = max(max_happy, happiness)

repres(max_happy, part2)
