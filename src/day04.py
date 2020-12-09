#!/usr/bin/python3

import hashlib
from aoc import repres

input = 'yzbqklnj'

part2 = True

zeros = "000000" if part2 else "00000"

r = 1
while True:
	hash = hashlib.md5((input + str(r)).encode())
	if hash.hexdigest()[:len(zeros)] == zeros:
		break
	r += 1
  
repres(r, part2)
