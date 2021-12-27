#!/usr/bin/python3

from aoc import repres

boss = (109, 8, 2)

part2 = True

def combinations(num_items, prev_comb, total):
	if num_items == 0:
		return prev_comb
	new_comb = []
	for i in range(0, total):
		for l in prev_comb:
			nl = l.copy()
			if i in nl:
				continue
			nl.append(i)
			new_comb.append(sorted(nl))
	return combinations(num_items-1, new_comb, total)

def combinations2(num, total):
	return set([tuple(x) for x in combinations(num, [[]], total)])

weapons = [(8, 4, 0),(10, 5, 0),(25, 6, 0),(40, 7, 0),(74, 8, 0)]
armors = [(13, 0, 1),(31, 0, 2),(53, 0, 3),(75, 0, 4),(102, 0, 5)]
rings = [(25, 1, 0),(50, 2, 0),(100, 3, 0),(20, 0, 1),(40, 0, 2),(80, 0, 3)]

configs = []

for i in range(1,2):
	for j in range(0,2):
		for k in range(0,3):
			weapon_combs = [list(x) for x in list(combinations2(i, len(weapons)))]
			armor_combs = [list(x) for x in list(combinations2(j, len(armors)))]
			ring_combs = [list(x) for x in list(combinations2(k, len(rings)))]
			for wsi in weapon_combs:
				for asi in armor_combs:
					for rsi in ring_combs:
						cst = 0
						dmg = 0
						arm = 0
						for ii in wsi:
							c,d,a = weapons[ii]
							cst += c
							dmg += d
							arm += a
						for ii in asi:
							c,d,a = armors[ii]
							cst += c
							dmg += d
							arm += a
						for ii in rsi:
							c,d,a = rings[ii]
							cst += c
							dmg += d
							arm += a
						configs.append((cst,dmg,arm))
configs.sort()

if part2:
	configs.reverse()

def try_game(p1,p2):
	h1,d1,a1 = p1
	h2,d2,a2 = p2
	while True:
		dam1 = d1 - a2
		if dam1 < 1:
			dam1 = 1
		h2 -= dam1
		if h2 <= 0:
			return True
		dam2 = d2 - a1
		if dam2 < 1:
			dam2 = 1
		h1 -= dam2
		if h1 <= 0:
			return False

for c,d,a in configs:
	gr = try_game((100,d,a),boss)
	if part2:
		gr = not gr
	if gr:
		break

repres(c, part2)
