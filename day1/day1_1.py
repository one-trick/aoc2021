#!/usr/bin/env python3

data = open("input.txt", "r")

depth_list = data.readlines()
# Loop through each list item
total_increments = 0
last_depth = 0
for index, depth in enumerate(depth_list):
	depth = int(depth.strip("\n"))
	# Deal with the first line that won't have a previous depth
	if index == 0:
		last_depth = depth
		continue
	if depth > last_depth:
		total_increments += 1
	last_depth = depth

print("Total increments: " + str(total_increments))
