# All the necessary used libraries
import discord
from discord.ext import commands
import random

TOKEN = "dongers" # Make sure to remove this before pushing to GitHub
description = '''This bot generates random team compositions for Overwatch. That way more people have a better time playing the game.'''
bot = commands.Bot(command_prefix='$', description=description)
client = discord.Client()

tanks = ["Hammond", "Reinhardt","Zarya","Orissa","D.Va","Winston","Roadhog"]
dps = ["Bastion","Doomfist","Genji","Hanzo","Junkrat","McCree","Mei","Pharah","Reaper","Soldier: 76","Sombra","Symmetra","Torbjorn","Tracer","Widowmaker"]
heals = ["Mercy","Zenyatta","Ana","Brigitte","Lucio","Moira"]
allClasses = tanks + dps + heals
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
    

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command(name="222",
	description="Generates a random 2 healer, 2 tank, 2 dps team composition")
async def dos_dos_dos(ctx):
	await ctx.send(nice_print(two_two_two())+random.choice(outcome))


@bot.command(name="randoms",
	description="Completely random combination of 6 unique heroes")
async def rando(ctx):
	await ctx.send(nice_print(total_random())+random.choice(outcome))


@bot.command(name="single",
	description="Spits out a single random hero")
async def solo(ctx):
	addon = random.choice(embels)
	await ctx.send(picker(allClasses)+ addon)

@bot.command(name="hellyea",
	description="DON'T YOU DARE TOUCH MY FUKIN' SISTER-WIFE YOU HEAR ME!	")
async def hell_yea(ctx):
	await ctx.send("**HELL YEA BROTHER YEE YEE**")

@bot.command(name="number",
	description="Generates as many unique random heroes as the user requests")
async def randNumb(ctx, player: int):
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

@bot.command(name="peep", pass_context=True)
async def peep(ctx):
	ctx.send("This is supposed to return a list of all the members in a voice channel but apparently thats impossible and nothing mattters so go figure.")


bot.run(TOKEN)
