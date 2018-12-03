from aoclib import read_input, yes

instructions = list(read_input(
    'input-d5.txt',
    record_processor=int,
    record_postvalidator=yes,
))

ic = 0
ic_history = []


while True:
    ic_history.append(ic)
    offset = instructions[ic]
    instructions[ic] += 1
    ic += offset

    if ic < 0 or ic >= len(instructions):
        break

print(len(ic_history))
