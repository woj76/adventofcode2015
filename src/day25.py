#!/usr/bin/python3

from aoc import repres

row=2947
column=3029

pos = 1
step = 2

for i in range(column-1):
	pos += step
	step += 1

step -= 1
for i in range(row-1):
	pos += step
	step += 1

code = 20151125

for _ in range(pos-1):
	code *= 252533
	code %= 33554393

repres(code, False)
