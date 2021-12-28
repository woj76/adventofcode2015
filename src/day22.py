#!/usr/bin/python3

from aoc import repres

part2 = True

# Hit Points: 71
# Damage: 10

game_state = {
	'boss_hit' : 71,
	'boss_damage' : 10,
	'player_hit' : 50,
	'player_mana' : 500,
	'player_armor' : 0,
	'next_turn' : 'player',
	'missle_counter' : 0,
	'drain_counter' : 0,
	'shield_counter' : 0,
	'poison_counter' : 0,
	'recharge_counter': 0}

effect_spells = ['shield','poison','recharge']

def cast_spell(gs,spell):
	if spell in effect_spells and gs[spell+'_counter']:
		return None, None
	counter = None
	if spell == 'missle':
		cost = 53
	elif spell == 'drain':
		cost = 73
	elif spell == 'shield':
		cost = 113
		counter = 6
	elif spell == 'poison':
		cost = 173
		counter = 6
	elif spell == 'recharge':
		cost = 229
		counter = 5
	if gs['player_mana'] < cost:
		return None, None
	gs['player_mana'] -= cost
	if spell in effect_spells:
		gs[spell+'_counter'] = counter
	else:
		if spell == 'missle':
			gs['boss_hit'] -= 4
		elif spell == 'drain':
			gs['boss_hit'] -= 2
			gs['player_hit'] += 2
	gs['next_turn'] = 'boss'
	return gs,cost

def execute_effects(gs):
	gs['player_armor'] = 0
	for sp in effect_spells:
		if gs[sp+'_counter']:
			gs[sp+'_counter'] -= 1
			if sp == 'shield':
				gs['player_armor'] = 7
			elif sp == 'poison':
				gs['boss_hit'] -= 3
			elif sp == 'recharge':
				gs['player_mana'] += 101

min_cost = float('inf')

def try_game(gs,current_cost):
	global min_cost
	if current_cost >= min_cost:
		return
	if part2 and gs['next_turn'] == 'player':
		gs['player_hit'] -= 1
		if gs['player_hit'] <= 0:
			return
	execute_effects(gs)
	if gs['boss_hit'] <= 0:
		if current_cost < min_cost:
			min_cost = current_cost
		return
	if gs['next_turn'] == 'boss':
		damage = gs['boss_damage'] - gs['player_armor']
		if damage < 1:
			damage = 1
		gs['player_hit'] -= damage
		gs['next_turn'] = 'player'
		if gs['player_hit'] <= 0:
			return
		try_game(gs, current_cost)
	elif gs['next_turn'] == 'player':
		for spell in ['missle','drain','shield','poison','recharge']:
			ngs = gs.copy()
			ngs,cst = cast_spell(ngs,spell)
			if ngs == None:
				continue
			if ngs['boss_hit'] <= 0:
				if current_cost + cst < min_cost:
					min_cost = current_cost + cst
				return
			try_game(ngs,current_cost+cst)

try_game(game_state, 0)

repres(min_cost, part2)
