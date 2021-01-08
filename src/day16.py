#!/snap/bin/pypy3

from aoc import repres

part2 = True

sues = {}
with open("../data/day16.txt", "rt") as file:
	for d in file.readlines():
		d = d.split(', ')
		i = d[0].index(': ')
		name = d[0][:i]
		d[0] = d[0][i+2:]
		items = {}
		for i in d:
			[iname, iq] = i.split(': ')
			items[iname] = int(iq)
		sues[name] = items

knowledge = {
	'children': lambda a : a != 3,
	'cats': lambda a : (a <= 7) if part2 else a != 7,
	'samoyeds': lambda a : a != 2,
	'pomeranians': lambda a : (a >= 3) if part2 else a != 3,
	'akitas': lambda a : a != 0,
	'vizslas': lambda a : a != 0,
	'goldfish': lambda a : (a >= 5) if part2 else a != 5,
	'trees': lambda a : (a <= 3) if part2 else a != 3,
	'cars': lambda a : a != 2,
	'perfumes': lambda a : a != 1 }

rule_out = [s for s,i in sues.items() for k,a in knowledge.items() if k in i and a(i[k])]

r = int([s for s in sues.keys() if s not in rule_out][0].split(' ')[1])

repres(r, part2)
