import dis
def magic_calculation(a, b):
	a = 98
	return a ** b + a

print(dis.dis(magic_calculation))