#!/usr/bin/python

import random
import math

check_points = {
    10:         0,
    100:        0,
    1000:       0,
    10000:      0,
    100000:     0,
    1000000:    0,
}
total_count = float(0)
in_circle = float(0)
out_circle = float(0)
for i in range(10000000):
    point = (random.uniform(-.5, .5), random.uniform(-.5, .5))
    point_magnitude = math.sqrt((point[0]**2) + (point[1]**2))
    if point_magnitude<=.5:
        in_circle+=1
    else:
        out_circle=out_circle+1
    total_count+=1
    if total_count in check_points:
        check_points[total_count] = 4*(in_circle/total_count)

print(check_points)
