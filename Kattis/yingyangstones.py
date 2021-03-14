s = input()

Wcount = 0
for i in s:
	if i == 'W':
		Wcount += 1

Bcount = len(s) - Wcount

if Wcount == Bcount:
	print("1")
else:
	print("0")
