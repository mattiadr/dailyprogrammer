#!/bin/python

from sys import argv

if len(argv) != 3:
	print("Usage: \"" + argv[0] + " [word] [n_rem]\"")
	exit()

dictionary = {}

with open("dictionary.txt") as file:
	for l in file:
		l = l[0:-1]
		i = len(l)
		if i in dictionary:
			dictionary[i].append(l)
		else:
			dictionary[i] = [l]

def is_inside(small, big, n_rem):
	s, b = 0, 0
	while (s < len(small) or b < len(big)):
		if s < len(small) and b < len(big) and small[s] == big[b]:
			s += 1
			b += 1
		else:
			if n_rem > 0:
				b += 1
				n_rem -= 1
			else:
				return False
	return n_rem >= 0

def check_smaller(word, n_rem):
	size = len(word)
	best = 1
	for i in range(1, n_rem + 1):
		if (size - i) in dictionary:
			for w in dictionary[size - i]:
				if is_inside(w, word, n_rem):
					best = max(best, check_smaller(w, n_rem) + 1)
		
	return best

print(argv[1] + " => " + str(check_smaller(argv[1], int(argv[2]))))