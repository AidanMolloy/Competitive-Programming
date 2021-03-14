def compareNums(n1):
	x1 = str(n1)
	s1 = ''.join(sorted(x1))

	return s1
x = input()
n2 = ''.join(sorted(x))
x = int(x)
length = len(n2)

while True:
	x +=1
	f = compareNums(x)
	if n2 == f:
		print(x)
		break
	if len(f) > length:
		print("0")
		break
