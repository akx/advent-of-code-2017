from aoclib import read_input, split_by_whitespace, compose, imap

def divide_divisible_pair(integers):
    for a in integers:
        for b in integers:
            if a > b and divmod(a, b)[1] == 0:
                return (a / b)

cksum = sum(
    divide_divisible_pair(record)
    for record in
    read_input(
        'input-d2.txt',
        record_processor=compose(split_by_whitespace, imap(int), tuple),
    )
)

print(cksum)
