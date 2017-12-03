from itertools import islice

from day3lib import ulam_spiral_steps, walk_coordinates

input = 361527

steps = islice(ulam_spiral_steps(), 0, input - 1)
grid = {}

for x, y in walk_coordinates(steps):
    if x == 0 and y == 0:
        val = 1
    else:
        val = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                val += grid.get((x + dx, y + dy), 0)
    assert (x, y) not in grid, (x, y)
    grid[x, y] = val
    if val > input:
        print(x, y, val, input)
        break
