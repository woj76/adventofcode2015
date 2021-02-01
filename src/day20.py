#!/snap/bin/pypy3

from aoc import repres

part2 = True

input = 29000000 // 10

sieve = {}

for i in range(1, input):
	sieve[i] = 0

for i in range(1, input):
	j = 1
	d = 0
	while j <= input and (d < 50 or not part2):
		if j > 1:
			sieve[j-1] += i
			d += 1
		j += i

for i,v in sieve.items():
	if v * (11 if part2 else 10) >= input*10:
		r = i
		break

repres(r, True)
