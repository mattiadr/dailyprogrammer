#!/bin/python

from sys import argv

if len(argv) != 2:
	print("Usage: \"" + argv[0] + " [file]\"")
	exit()

well = []

with open(argv[1]) as file:
	lines = file.readlines()
	rows, cols = (int(s) for s in lines[0].split())
	for line in lines[1:-1]:
		well.append([int(s) for s in line.split()])
	target = int(lines[-1])

for i in range(rows):
	if 1 in well[i]:
		sr, sc = i, well[i].index(1)      # source row and col
	if target in well[i]:
		tr, tc = i, well[i].index(target) # target row and col

target += 1

def dfs(r, c, visited, min, minDepth):
	if visited[r][c]:
		return
	visited[r][c] = True

	if well[r][c] == min[0]:
		minDepth.append((r, c))
	elif well[r][c] < min[0]:
		min[0] = well[r][c]
		minDepth.clear()
		minDepth.append((r, c))
	else:
		return

	# 4 directions
	if r > 0:      dfs(r-1, c, visited, min, minDepth)
	if r < rows-1: dfs(r+1, c, visited, min, minDepth)
	if c > 0:      dfs(r, c-1, visited, min, minDepth)
	if c < cols-1: dfs(r, c+1, visited, min, minDepth)
	# 8 directions
	#for i in range(r-1, r+2):
	#	for j in range(c-1, c+2):
	#		if i >= 0 and i < rows and j >= 0 and j < cols and (i != r or j != c):
	#			dfs(i, j, visited, min, minDepth)


def findMin():
	visited = [[False] * cols for i in range(rows)]
	minDepth = []
	dfs(sr, sc, visited, [well[sr][sc]], minDepth)
	return minDepth

def fillNext():
	minDepth = findMin()
	for pos in minDepth:
		well[pos[0]][pos[1]] += 1

	return len(minDepth)

def printWell():
	for l in well:
		for d in l:
			if d == well[sr][sc]:
				d = str(d).zfill(2)
				d = "\033[92m" + d + "\033[0m"
			else:
				d = str(d).zfill(2)
			print(d, end = " ")
		print()
	print()

time = 0

#printWell()

while well[tr][tc] < target:
	time += fillNext()
	#printWell()
	#input()

print("Total time: " + str(time))