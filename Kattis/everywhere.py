t = int(input())

while(t):
	t-=1
	n = int(input())
	cities = set()
	while(n):
		n -=1
		name = input()
		if name not in cities:
			cities.add(name)
	print(len(cities))
