from aoclib import read_input, split_by_whitespace, compose, imap

cksum = sum([
    (max(record) - min(record))
    for record in
    read_input(
        'input-d2.txt',
        record_processor=compose(split_by_whitespace, imap(int), tuple),
    )
])
print(cksum)
