from aoclib import read_input, yes, split_by_whitespace, compose, imap
from day6lib import reallocate

initial_banks = list(read_input(
    'input-d6.txt',
    record_processor=compose(split_by_whitespace, imap(int), list),
    record_postvalidator=yes,
))[0]

allocations, final_banks = reallocate(initial_banks)
print(len(allocations))
