animalSounds = input()
soundList = animalSounds.split()
for item in soundList:
	if(item == "Rawr"):
		print("Tiger", end=" ")
	elif(item == "Chirp"):
		print("Bird", end=" ")
	elif(item == "Ssss"):
		print("Snake", end=" ")
	elif(item == "Grr"):
		print("Lion", end=" ")