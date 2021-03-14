def sumDigits(a):
	sum = 0
	a = str(a)
	for b in a:
		sum += int(b)
	return sum

l = int(input())
d = int(input())
x = int(input())

for y in range(l, d+1, 1):
	if(sumDigits(y) == x):
		print(y)
		break

for z in range(d, l-1, -1):
	if(sumDigits(z) == x):
		print(z)
		break
