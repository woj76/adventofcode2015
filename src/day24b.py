#!/snap/bin/pypy3

from aoc import repres
from itertools import combinations


file = open("../data/day24.txt", "rt")
data = [int(x) for x in file.read().strip().split('\n') if x != '']
file.close()

chunk = sum(data) // 4

data.sort()

s = 0
max_size = 0

while s <= chunk:
	s += data[max_size]
	max_size += 1

data.reverse()

s = 0
min_size = 0

while s < chunk:
	s += data[min_size]
	min_size += 1

sizes = []

for first in range(min_size,max_size):
	for second in range(min_size,max_size):
		for third in range(min_size,max_size):
			fourth = len(data) - first - second - third
			if fourth < min_size or fourth >= max_size:
				continue
			l = sorted([first, second, third, fourth])
			if l not in sizes:
				sizes.append(l)

data=set(data)

min_qe = float('inf')
min_size = float('inf')

for s1, s2, s3, s4 in sizes:
	if s1 > min_size:
		break
	for c1 in combinations(data, s1):
		if sum(c1) != chunk:
			continue
		remains = data - set(c1)
		for c2 in combinations(remains, s2):
			if sum(c2) != chunk:
				continue
			remains = remains - set(c2)
			for c3 in combinations(remains, s3):
				if sum(c3) != chunk:
					continue
				remains = remains - set(c3)
				for c4 in combinations(remains, s4):
					if sum(c4) != chunk:
						continue
					min_size = min(min_size, s1)
					qe = 1
					for e in c1:
						qe *= e
					if qe < min_qe:
						min_qe = qe

repres(min_qe, True)
