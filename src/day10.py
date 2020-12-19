#!/usr/bin/python3

from aoc import repres

part2 = True

input = [int(x) for x in "1113122113"]

for _ in range(50 if part2 else 40):
	next_input = []
	i = 0
	while i < len(input):
		c = input[i]
		if i == len(input) - 1:
			next_input.append(1)
			next_input.append(c)
			i += 1
		else:
			j = i + 1
			count = 1
			while j < len(input) and input[j] == c:
				j += 1
				count += 1
			next_input.append(count)
			next_input.append(c)
			i = j
	input = next_input

repres(len(input), part2)
