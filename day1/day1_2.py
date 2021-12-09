#!/usr/bin/env python3

data = open("input.txt", "r")

depth_list = data.readlines()
total_increments = 0
last_sum = 0
for index, depth in enumerate(depth_list):
	depth = int(depth.strip("\n"))
	# Get the sum of current depth + the next two
	sum = int(depth_list[index]) + int(depth_list[index+1]) + int(depth_list[index+2])
	# Deal with first run, since there's nothing to compare it to
	if index == 0:
		last_sum = sum
		continue
	if sum > last_sum:
		total_increments += 1
	last_sum = sum
	# Exit loop if we're not going to have two additional values to add to it
	if index == len(depth_list) - 3:
		break
print("Total increments: " + str(total_increments))
