import discord
from discord.ext import commands
import random

TOKEN = "NDcyNDAzNjc5NDc1OTI1MDAz.Dkpk_g.4FBulS2MAMiX5_GeDkvLI2d92Yk" # Make sure to remove this before pushing to GitHub
description = '''This bot generates random team compositions for Overwatch. That way more people have a better time playing the game.'''
bot = commands.Bot(command_prefix='$', description=description)


tanks = ["Hammond", "Reinhardt","Zarya","Orissa","D.Va","Winston","Roadhog"]
dps = ["Bastion","Doomfist","Genji","Hanzo","Junkrat","McCree","Mei","Pharah","Reaper","Soldier: 76","Sombra","Symmetra","Torbjorn","Tracer","Widowmaker"]
heals = ["Mercy","Zenyatta","Ana","Brigitte","Lucio","Moira"]
allClasses = tanks + dps + heals
perfect = ["Healer","Healer","DPS","DPS","Tank","Tank"]
emptyNames = [1,2,3,4,5,6]

# Random little quips added to the end of the single command only
embels = [", you little fruity tart",
", sexy ass bitch",
", you know you want to.",
", god fuckin dammit",
", who knows you might even get a kill!",
", gg",
", oh my guuglie-schmuuglie",
", the reason Overwatch doesn't have Battle Royale"]

# Random little quips added to the end of team comps, used for 222 and randoms
outcome = ["this looks so..... promising",
"LMAO WHO DID THIS",
"solid comp.",
"why'm",
"yea i just really don't give a fuck anymore",
"they need to hurry up and remove Brigitte",
"welp gg guys",
"looking good! haha",
"good luck, looks like you need it...."]

def nice_print(comp): #Nicely formats random comps for 222 and randoms
	total = ""
	for hero in comp:
		total = total + hero + ",   "
	return total	
def nice_print2(people,comp): #Nicely formats for dc2, channel, and channel2
	tempstring=""
	for person, hero in zip(people, comp):
		tempstring = tempstring + " " + person + " is playing " + hero + "\n" 
	return("```"+tempstring+"```")

def picker(heroCat): #randomly chooses a hero from the given category
	return heroCat[random.randint(0,len(heroCat)-1)]

def couple_picker(heroCat): #Picks two random unique heroes from the same category
	couple = []
	couple.append(heroCat[random.randint(0,len(heroCat)-1)])
	while len(couple) < 2:
		holder = heroCat[random.randint(0,len(heroCat)-1)]
		if holder != couple[0]:
			couple.append(holder)
	return couple

def two_two_two(): #Generates a random 2-2-2 meta and returns it as a list
	healers = couple_picker(heals)
	damage = couple_picker(dps)
	tankers = couple_picker(tanks)
	return (healers + tankers + damage)

def total_random(): #Generates a completely random comp and returns it as a list
	team = []
	while len(team) != 6:
		randomHero = picker(allClasses)
		if randomHero not in team:
			team.append(randomHero)
	return team


@bot.event 
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name="222", #Creates the bot command $222 that generates a random 2-2-2 meta
	description="Generates a random 2 healer, 2 tank, 2 dps team composition")
async def dos_dos_dos(ctx):
	"""Generates a random 2 healer, 2 tank, 2 dps team composition"""
	await ctx.send(nice_print(two_two_two())+random.choice(outcome))


@bot.command(name="randoms", #Creates the bot command $randoms that generates a random comp
	description="Completely random combination of 6 unique heroes")
async def rando(ctx):
	"""Generates a completely random team composition"""
	await ctx.send(nice_print(total_random())+random.choice(outcome))


@bot.command(name="single", #Creates the bot command to randomly select a single hero
	description="Spits out a single random hero")
async def solo(ctx):
	"""Returns one random hero"""
	addon = random.choice(embels)
	await ctx.send(picker(allClasses)+ addon)

@bot.command(name="number", #Randomly generates N number of heroes, all unique
	description="Generates as many unique random heroes as the user requests")
async def randNumb(ctx, player: int):
	"""Generates a N random heroes, all unique"""
	player = int(player)
	if player > len(allClasses):
		await ctx.send(f"Yea bud there's only {len(allClasses)} unique heroes in Overwatch. Try again.")
		return None
	selection = []
	while len(selection) < player:
		tempHero = picker(allClasses)
		if tempHero not in selection:
			selection.append(tempHero)
	players = nice_print(selection) + random.choice(outcome)
	print(players)
	await ctx.send(players)



@bot.command(name="channel", pass_context=True) #Assigns a completely random hero to everyone in the requestors voice channel
async def peep(ctx):
	"""Assigns a hero to all the users within the requestors voice channel"""
	author = ctx.author
	listofmembers = author.voice.channel.members
	memberInChannelNames=[]
	for member in listofmembers:
		if member.bot == False:
			memberInChannelNames.append(member.name)
	if len(memberInChannelNames) > 28:
		await ctx.send("It's really amazing that you have more than 28 people in a channel at a single time but now I'm nervous")
		await ctx.send("Please have less people")
		return 0
	selection = []
	while len(selection) < len(memberInChannelNames):
		tempHero = picker(allClasses)
		if tempHero not in selection:
			selection.append(tempHero)
	await ctx.send(nice_print2(memberInChannelNames,selection))
	

@bot.command(name="channel2", pass_context=True) #Only runs when 6 people are in the requestors voice channel, bots ignored, and assigns a random 2-2-2 meta
async def channelTwo(ctx):
	"""Only runs when 6 people are in the requestors voice channel, and assigns a random 2-2-2 meta"""
	author = ctx.author
	listofmembers = author.voice.channel.members
	memberInChannelNames=[]
	for member in listofmembers:
		if member.bot == False:
			memberInChannelNames.append(member.name)
	if len(memberInChannelNames) != 6:
		await ctx.send("This is meant for *6* people only")
		await ctx.send("Please fix urself")
		return None
	selection = two_two_two()
	random.shuffle(selection)
	await ctx.send(nice_print2(memberInChannelNames,selection))

@bot.command(name="dc2", pass_context=True) #Assigns a random 2-2-2 meta role to members of the requestors voice channel. 
async def dc2(ctx):
	"""This is dealers choice. Assigns a role to people in your voice channel. Only works for 6 people since it's based on 2-2-2 meta"""
	author = ctx.author
	listofmembers = author.voice.channel.members
	memberInChannelNames=[]
	for member in listofmembers:
		if member.bot == False:
			memberInChannelNames.append(member.name)
	if len(memberInChannelNames) != 6:
		await ctx.send("This is meant for *6* people only")
		await ctx.send("Please fix urself")
		return None
	selection = perfect
	random.shuffle(selection)
	tempstring=""
	await ctx.send(nice_print2(memberInChannelNames,selection))

@bot.command(name="donate", pass_context=True)
async def donate(ctx):
	"""Help keep this bot running"""
	await ctx.send("```This bot is currently running on my own server. It costs money to host but the benefits will be felt worldwide by everyone using the bot.\n"
		+"If you can please donate -  all donations go directly to paying for hosting and coffee \n"
		+ "\n"
		+"Bitcoin: 3KgHjmRgtPxKGfGj5wVVwfqUQhwretKjke \n"
		+ "\n"
		+"Thanks! ```")

if __name__ == "__main__":
	bot.run(TOKEN)
