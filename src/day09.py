#!/usr/bin/python3

import itertools
from aoc import repres

file = open("../data/day09.txt", "rt")
data = [x for x in file.read().strip().split('\n')]
file.close()

part2 = True

graph = {}
verts = []

for d in data:
	[v1, _, v2, _, dist] = d.split(' ')
	dist = int(dist)
	graph[(v1,v2)] = dist
	verts.extend([x for x in [v1, v2] if x not in verts])

r = float('-inf' if part2 else 'inf')

for route in itertools.permutations(verts):
	connections = []
	all_there = True
	for i in range(0, len(route) - 1):
		r1, r2 = route[i], route[i+1]
		if not (r1, r2) in graph.keys() and not (r2, r1) in graph.keys():
			all_there = False
			break
		else:
			connections.append((r1,r2) if (r1,r2) in graph.keys() else (r2,r1))
	if not all_there:
		continue
	l = sum([graph[c] for c in connections])
	r = (max if part2 else min)(r, l)

repres(r, part2)
