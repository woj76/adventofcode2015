#!/snap/bin/pypy3

from aoc import repres
import json

with open("../data/day12.txt", "rt") as file:
	data = json.load(file)

part2 = True
r = 0

def collect_numbers(js):
	ret = []
	if isinstance(js, int):
		ret.append(js)
	elif isinstance(js, dict):
		if not (part2 and "red" in js.values()):
			for k,v in js.items():
				if isinstance(v, int):
					ret.append(v)
				elif not isinstance(v, str):
					ret.extend(collect_numbers(v))
	elif isinstance(js, list):
		for v in js:
			ret.extend(collect_numbers(v))
	return ret

repres(sum(collect_numbers(data)), part2)
