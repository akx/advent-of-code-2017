from aoclib import read_input, split_by_whitespace, compose, imap

all_passphrases = list(read_input(
    'input-d4.txt',
    record_processor=compose(split_by_whitespace),
))

valid_passphrases = [
    phrase
    for phrase
    in all_passphrases
    if len(set(phrase)) == len(phrase)
]

print(len(valid_passphrases), len(all_passphrases))
