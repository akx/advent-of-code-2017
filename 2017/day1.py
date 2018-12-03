from aoclib import read_input, read_chars, identity

inp = list(read_input('input-d1.txt', records_iterator=read_chars, record_processor=identity))

def p1(inp, step):
	s = 0

	for i in range(len(inp)):
		ni = int((i + step) % len(inp))
		if inp[i] == inp[ni]:
			s += int(inp[i])

	print(s)	

if __name__ == '__main__':
	p1(inp, len(inp) / 2)