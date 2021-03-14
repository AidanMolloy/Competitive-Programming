playerNo = int(input())
n = int(input())
timeLeft = 210
for i in range(n):
	t, z = input().split()
	t = int(t)
	timeLeft -= t
	if timeLeft <= 0:
		print(playerNo)
		break
	if z == 'T':
		playerNo += 1

	if playerNo == 9:
		playerNo = 1
