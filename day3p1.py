"""
This file is messy as I had to try different approaches to get to the answer...

only to find that I had transcribed my input wrong :D
"""

from itertools import islice
import matplotlib.pyplot as plt

from aoclib import last
from day3lib import ulam_spiral, ulam_spiral_steps, walk_coordinates, manhattan


def test_svg(steps):
    path = []
    for value, (x, y) in enumerate(walk_coordinates(steps), 1):
        path.append(((x, y), value))

    coordinates, labels = zip(*path)
    xs, ys = zip(*coordinates)
    plt.ioff()

    plt.figure(figsize=(40, 40))
    plt.plot(xs, ys)
    plt.gca().invert_yaxis()
    plt.plot(0, 0, 'r+')

    plt.savefig('d3p1.svg', dpi=300)


input = 361527

steps = islice(ulam_spiral_steps(), 0, input - 1)

x, y = last(walk_coordinates(steps))
print(x, y, manhattan(x, y))

x, y = ulam_spiral(input)
print(x, y, manhattan(x, y))
