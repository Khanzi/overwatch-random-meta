import random
import os

tanks = ["Hammond", "Reinhardt","Zarya","Orissa","D.Va","Winston","Roadhog"]
dps = ["Bastion","Doomfist","Genji","Hanzo","Junkrat","McCree","Mei","Pharah","Reaper","Soldier: 76","Sombra","Symmetra","Torbjorn","Tracer","Widowmaker"]
heals = ["Mercy","Zenyatta","Ana","Brigitte","Lucio","Moira"]
allClasses = tanks + dps + heals
emptyNames = [1,2,3,4,5,6]
def picker(heroCat):
	return heroCat[random.randint(0,len(heroCat)-1)]

def couple_picker(heroCat):
	couple = []
	couple.append(heroCat[random.randint(0,len(heroCat)-1)])
	while len(couple) < 2:
		holder = heroCat[random.randint(0,len(heroCat)-1)]
		if holder != couple[0]:
			couple.append(holder)
	return couple

def total_random():
	team = []
	while len(team) != 6:
		randomHero = picker(allClasses)
		if randomHero not in team:
			team.append(randomHero)
	return team


def two_two_two():
	healers = couple_picker(heals)
	damage = couple_picker(dps)
	tankers = couple_picker(tanks)
	return (healers + tankers + damage)

def who_is_playing():
	teamsize = int(input("How many people are playing?")) 
	players = []
	for i in range(0,teamsize):
		players.append(input(f"Player {i+1}: "))
	return players

def options_print():
	print("")
	print("=======================================")
	print("")
	print("1: Two Two Two")
	print("2: Total Randomness")
	print("3: Enter Player Names")
	print("")
	print("=======================================")
	print("")

def team_print(heroes,emptyNames):
		random.shuffle(heroes)
		for i in range(0,len(emptyNames)):
			print(f"{emptyNames[i]} is playing {heroes[i]}")
def clear():
    os.system( 'cls' )

def menu():
	global emptyNames
	doneWithMe = True
	while doneWithMe:
		options_print()
		userChoice = int(input("What would you like to do: "))
		if userChoice == 1:
			clear()
			team_print(two_two_two(),emptyNames)
		elif userChoice == 2:
			clear()
			team_print(total_random(),emptyNames)
		elif userChoice == 3:
			clear()
			emptyNames = who_is_playing()
			print(emptyNames)
		else:
			Print("m8 thats not even an option")



menu()