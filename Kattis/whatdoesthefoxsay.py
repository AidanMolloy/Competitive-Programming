n = int(input())

while n:
	n -=1
	dict = []
	foxSays = input()
	for sound in foxSays.split():
		dict.append(sound)

	while True:
		otherSounds = input()
		if otherSounds == "what does the fox say?":
			break

		for otherSound in otherSounds.split():
			while otherSound in dict:
				dict.remove(otherSound)

	for everySound in dict:
		print(everySound, end=" ")

