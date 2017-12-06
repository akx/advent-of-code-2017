# -- encoding: UTF-8 --
def redistribute(banks, index):
    banks = banks[:]
    blocks_to_redistribute = banks[index]
    assert blocks_to_redistribute
    banks[index] = 0
    index += 1
    while blocks_to_redistribute:
        banks[index % len(banks)] += 1
        blocks_to_redistribute -= 1
        index += 1
    return banks


def reallocate(banks):
    seen = set()
    iterations = []

    while True:
        t_banks = tuple(banks)
        if t_banks in seen:
            break
        seen.add(t_banks)
        iterations.append(t_banks)
        max_index = banks.index(max(banks))
        banks = redistribute(banks, max_index)

    return (iterations, banks)
