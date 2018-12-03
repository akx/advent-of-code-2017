from aoclib import read_input, yes, split_by_whitespace, compose, imap
from day6lib import reallocate

initial_banks = list(read_input(
    'input-d6.txt',
    record_processor=compose(split_by_whitespace, imap(int), list),
    record_postvalidator=yes,
))[0]

allocations, final_banks = reallocate(initial_banks)
first_cycle = allocations.index(tuple(final_banks))
print(first_cycle, len(allocations), len(allocations) - first_cycle)
