# All the necessary used libraries
import discord
from discord.ext import commands
import random

TOKEN = "NDcyNDAzNjc5NDc1OTI1MDAz.DkpTow.N3CziGg8TY_iUzRubDBzo5rQZcY" # Make sure to remove this before pushing to GitHub
description = '''This bot generates random team compositions for Overwatch. That way more people have a better time playing the game.'''
bot = commands.Bot(command_prefix='$', description=description)


tanks = ["Hammond", "Reinhardt","Zarya","Orissa","D.Va","Winston","Roadhog"]
dps = ["Bastion","Doomfist","Genji","Hanzo","Junkrat","McCree","Mei","Pharah","Reaper","Soldier: 76","Sombra","Symmetra","Torbjorn","Tracer","Widowmaker"]
heals = ["Mercy","Zenyatta","Ana","Brigitte","Lucio","Moira"]
allClasses = tanks + dps + heals
perfect = ["Healer","Healer","DPS","DPS","Tank","Tank"]
emptyNames = [1,2,3,4,5,6]
embels = [", you little fruity tart",
", sexy ass bitch",
", you know you want to.",
", god fuckin dammit",
", who knows you might even get a kill!",
", gg",
", oh my guuglie-schmuuglie",
", the reason Overwatch doesn't have Battle Royale"]


outcome = ["this looks so..... promising",
"LMAO WHO DID THIS",
"solid comp.",
"why'm",
"yea i just really don't give a fuck anymore",
"they need to hurry up and remove Brigitte",
"welp gg guys",
"looking good! haha",
"good luck, looks like you need it...."]

def nice_print(comp):
	total = ""
	for hero in comp:
		total = total + hero + ",   "
	return total	
def nice_print2(people,comp):
	tempstring=""
	for person, hero in zip(people, comp):
		tempstring = tempstring + " " + person + " is playing " + hero + "\n" 
	return("```"+tempstring+"```")

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

def two_two_two():
	healers = couple_picker(heals)
	damage = couple_picker(dps)
	tankers = couple_picker(tanks)
	return (healers + tankers + damage)

def total_random():
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
    
@bot.event
async def on_message(message):
	auth = (message.author.name)
	if "no u" in message.content and "OverRandom" not in auth:
		await message.channel.send("no u")
	if "subaru" in message.content.lower() and "OverRandom" not in auth and random.randint(1,5)==3:
		await message.channel.send("subaru more like - poobaru ") 
	if random.randint(1,100)==1:
		await message.channel.send("yo shut the fuck up lmao")
	if "good bot" in message.content.lower():
		await message.channel.send("(▰˘◡˘▰)")
		await message.channel.send("`*nuzzles`")
	if "gay" == message.content.lower():
		await message.channel.send("It's 2018 and your use of a homophobic slur will not be tolerated you total fucking piece of shit.")
	if "bad bot" in message.content.lower() and "OverRandom" not in auth:
		if "kahlil" in auth.lower():
			await message.channel.send("S-s-sorry papa, i aim to please...")
		else:
			await message.channel.send("you're a bad bot you fucking bitch, lose some fucking weight tubkins")
	if "nigger" in message.content.lower():
		await message.channel.send("Whoever threw that racial slur -  ya moms a hoe")
	if "f" == message.content.lower() and "Kahlil" in auth:
		await message.channel.send("F")
	if "dafran" in message.content.lower():
		await message.channel.send("*LETS GOOOO DUUUUUUUUUUUUUUUUUUUUUUUDE*")
	await bot.process_commands(message)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command(name="222",
	description="Generates a random 2 healer, 2 tank, 2 dps team composition")
async def dos_dos_dos(ctx):
	"""Generates a random 2 healer, 2 tank, 2 dps team composition"""
	await ctx.send(nice_print(two_two_two())+random.choice(outcome))


@bot.command(name="randoms",
	description="Completely random combination of 6 unique heroes")
async def rando(ctx):
	"""Generates a completely random team composition"""
	await ctx.send(nice_print(total_random())+random.choice(outcome))


@bot.command(name="single",
	description="Spits out a single random hero")
async def solo(ctx):
	"""Returns one random hero"""
	addon = random.choice(embels)
	await ctx.send(picker(allClasses)+ addon)

@bot.command(name="hellyea",
	description="DON'T YOU DARE TOUCH MY FUKIN' SISTER-WIFE YOU HEAR ME!	")
async def hell_yea(ctx):
	"""Whenever yall boys need an extra YEE YEE"""
	await ctx.send("**HELL YEA BROTHER YEE YEE**")

@bot.command(name="number",
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



@bot.command(name="channel", pass_context=True)
async def peep(ctx):
	"""Assigns a hero to all the users within the requestors voice channel"""
	author = ctx.author
	listofmembers = author.voice.channel.members
	memberInChannelNames = [member.name for member in listofmembers]
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
	

@bot.command(name="channel2", pass_context=True)
async def channelTwo(ctx):
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
@bot.command(name="dc2", pass_context=True)
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


@bot.command(name="haltthyself")
async def pleasestop(ctx, person: str, times: int):
	author = str(ctx.author)
	if times > 20:
		await ctx.send(author.lower() + " is a fucking retard")
		return 0
	if person.lower()=="kahlil":
		await ctx.send("Checkmate buddy.")
		return 0
	elif person.lower()=="@kahlil":
		await ctx.send("Checkmate buddy.")
		return 0
	for i  in range(0,times):
		await ctx.send(person.upper() + "** PLEASE STOP**")



bot.run(TOKEN)

