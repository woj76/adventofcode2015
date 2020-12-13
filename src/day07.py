#!/usr/bin/python3

from aoc import repres

file = open("../data/day07.txt", "rt")
data = [tuple(x.split(' -> ')) for x in file.read().strip().split('\n')]
file.close()

part2 = False

connections = {}
values = {}

for x, y in data:
	connections[y] = x.split(' ')

r = None

def get_value(symb):
	if part2 and symb == 'b' and not r is None:
		return r
	if symb in values.keys():
		return values[symb]
	d = connections[symb]
	l = len(d)
	if l == 1:
		v = int(d[0]) if d[0].isnumeric() else get_value(d[0])
	elif l == 2:
		v = ~get_value(d[1])
	else:
		op = d[1]
		v1 = int(d[0]) if d[0].isnumeric() else get_value(d[0])
		v2 = int(d[2]) if d[2].isnumeric() else get_value(d[2])
		if op == 'AND':
			v = (v1 & v2)
		elif op == 'OR':
			v = (v1 | v2)
		elif op == 'LSHIFT':
			v = (v1 << v2)
		elif op == 'RSHIFT':
			v = (v1 >> v2)
	values[symb] = v
	return v

r = get_value('a')
repres(r, part2)

part2 = True 
values = {}

repres(get_value('a'), part2)
