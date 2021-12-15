#!/usr/bin/env python3

directions = open("input.txt", "r")

horizontal = 0
depth = 0
aim = 0
for move in directions:
	move = move.strip('\n')
	# split into direction and amount
	direction, amount = move.split(" ")
	if direction == "forward":
		horizontal += int(amount)
		depth = depth + (aim * int(amount))
	elif direction == "down":
		aim += int(amount)
	elif direction == "up":
		aim -= int(amount)
	else:
		print("Unexpected input")
		exit()
print("Total horizontal: " + str(horizontal) + " - Depth: " + str(depth))
print("Challenge 2 answer: " + str(horizontal * depth))
