#!/usr/bin/python3

from aoc import repres

file = open("../data/day23.txt", "rt")
data = [x for x in file.read().strip().split('\n') if x != '']
file.close()

part2 = True

regs = {'a' : 1 if part2 else 0, 'b' : 0}

ip = 0
while ip < len(data):
	d = data[ip].split(' ')
	if d[0] == 'hlf':
		regs[d[1]] //= 2
		ip += 1
	elif d[0] == 'tpl':
		regs[d[1]] *= 3
		ip += 1
	elif d[0] == 'inc':
		regs[d[1]] += 1
		ip += 1
	elif d[0] == 'jmp':
		if d[1] in regs:
			v = regs[d[1]]
		else:
			if d[1][0] == '+':
				d[1] = d[1][1:]
			v = int(d[1])
		ip += v
	else:
		if d[2] in regs:
			v = regs[d[2]]
		else:
			if d[2][0] == '+':
				d[2] = d[2][1:]
			v = int(d[2])
		if d[0] == 'jie':
			if regs[d[1][0]] % 2 == 0:
				ip += v
			else:
				ip += 1
		elif d[0] == 'jio':
			if regs[d[1][0]] == 1:
				ip += v
			else:
				ip += 1

repres(regs['b'], part2)
