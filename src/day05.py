#!/usr/bin/python3

from aoc import repres

file = open("../data/day05.txt", "rt")
data = [x for x in file.read().strip().split('\n')]
file.close()

part2 = True

r = 0

vowels = list('aeiou')
banned = ['ab', 'cd', 'pq', 'xy']

def check_nice1(word):
	if len([x for x in list(word) if x in vowels]) < 3:
		return False
	double = False
	ban = False
	for i in range(len(word)-1):
		if word[i] == word[i+1]:
			double = True
		if word[i] + word[i+1] in banned:
			ban = True
	return (not ban) and double


def check_nice2(word):
	pairs = []
	found = False
	l = len(word)
	for i in range(l-1):
		pairs.append(word[i] + word[i+1])
		if i < l-2 and word[i] == word[i+2]:
			found = True
	if not found:
		return False
	found = False
	for i in range(len(pairs)-2):
		if pairs[i] in pairs[i+2:]:
			found = True
			break
	return found
	 
for d in data:
	if (part2 and check_nice2(d)) or (not part2 and check_nice1(d)):
		r += 1

repres(r, part2)
