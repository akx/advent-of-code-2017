from math import ceil, sqrt


def ulam_spiral(n):  # via https://math.stackexchange.com/a/163101/84804
    k = ceil((sqrt(n) - 1) / 2)
    t = 2 * k + 1
    m = t ** 2
    t = t - 1
    if n >= m - t:
        return (k - (m - n), -k)
    m = m - t
    if n >= m - t:
        return (-k, -k + (m - n))
    m = m - t
    if n >= m - t:
        return (-k + (m - n), k)
    else:
        return (k, k - (m - n - t))


def ulam_spiral_steps():  # via https://math.stackexchange.com/a/163093/84804
    c = 1
    while True:
        yield from 'r' * c
        yield from 'u' * c
        c += 1
        yield from 'l' * c
        yield from 'd' * c
        c += 1


def walk_coordinates(steps, x=0, y=0):
    yield (x, y)
    for step in steps:
        if step == 'r':
            x += 1
        elif step == 'u':
            y -= 1
        elif step == 'l':
            x -= 1
        elif step == 'd':
            y += 1
        else:
            raise NotImplementedError('...')
        yield (x, y)


def manhattan(x, y):
    return abs(x) + abs(y)
