import discord
from discord import client
from discord.ext import commands
from webserver import keep_alive

import os


intents = discord.Intents.default()
intents.members = True
# If you have commands.Bot, add `intents = intents` in the parentheses:
client = commands.Bot(command_prefix = ".",intents = intents)

@client.event
async def on_ready():
    print('Bot online')

# def get_prefix(message):
#     prefix = "?"  # default prefix
#     if not message.guild:  # if in dms
#         return commands.when_mentioned_or(prefix)(bot, message)
#     #you can set a guild/server specific one here
#     return commands.when_mentioned_or(prefix)(bot, message)
#
#
# bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
#
# @bot.command
# async def whisperroll(ctx):
#     await ctx.author.send("some random thing")
@client.event
async def on_member_join(member):

    await member.send("Greetings from Enactus SRM. This is Amigo. Reply with 'help' to know more.")
# @client.event
# async def on_member_join(member):
#     print(f'(member) has joined the server.')

# @client.event
# async def on_member_remove(member):
#     print(f'(member) has left the server')


# @client.event
# async def send(ctx):
#     file = discord.File("C:\\Users\\Prachet Balaji\\Desktop\\DAA ELAB")
#     await ctx.send(file=file, content="Message to be sent")


@client.event
async def on_message(message):



    if message.author == client.user:
        return
    if message.content.startswith('Help') or message.content.startswith('help') :
        await message.author.send("Greetings from ENACTUS SRM .This is Amigo. Live and Stereo, ready to help you with your queries. We're here to enlighten you regarding:\nA) Discovering  Yourself: Discovering ourselves  helps us to identify our abilities, and also how we can leverage and develop them.\nB)Break the monotony: Following the same schedule, doing the same things everyday will make you trapped in a life of routines and sameness.\nC)Meaning in life: Meaning provides a purpose for our lives.\nD)Befriending Emotions: Befriending emotions is a gentle way to be mindful of what we're experiencing without judging ourselves\nE)Anchor Yourself: An anchor at sea can be life saving or life threatening. Much like a sea voyage, we need to anchor ourselves to a strong value system, with a prioritization that helps you make decisions based on what is most important.\nPick the option you want, for example: '>a' for option A")


    if not message.content.startswith(('help','Help','About','a','>a','b','>b','c','>c','d','>d','A','>A','B','>B','C','>C','D','>D','E','>E')):
        await message.channel.send("Hello {0.author.mention},This is Amigo. Live and Stereo, ready to help you with your queries. Reply with 'help' to know more".format(message))
    #when the message with help then do this
    elif message.content.startswith('About'):
        await message.channel.send('Greetings from ENACTUS SRM .This is Amigo. Live and Stereo, ready to help you with your queries.')

    if not message.guild:
       # if message.content.startswith(('hi','Hi','Hello','hello')):
       #     try:
        #        await message.channel.send("Hey there! Reply with help if you want to know more.")
        #    except discord.errors.Forbidden:
         #       pass




        if message.content.startswith(('>a','>A','a','A')):
            try:

                embed=discord.Embed(title="Discovering  Yourself",
                description="A) Discovering  Yourself : Discovering ourselves  helps us to identify our abilities, and also how we can leverage and develop them. As you can find out what you are passionate about, it's easier to grasp the concepts and accept them.\nFor more, visit https://enactussrm.netlify.app/discover_yourself.html ",
                url="https://enactussrm.netlify.app/discover_yourself.html", icon_url="https://enactus-srm.netlify.app/black.png"
                )
                #embed.set_image(url="https://www.mbs.ac.uk/media/ambs/content-assets/images/enterprise/enactus-manchester-enterprise-centre-main-1536x500.jpg")
                embed.set_thumbnail(url="https://enactus-srm.netlify.app/black.png")
                await message.channel.send(embed=embed)
                await message.channel.send('Refer the following document for more information', file=discord.File('Book.pdf'))
                await message.channel.send('', file=discord.File('Book.pdf'))
            except discord.errors.Forbidden:
                pass



        if message.content.startswith(('>b','>B','b','B')):
            try:

                embed=discord.Embed(title="Breaking the monotony",
                description="B)Break the monotony: Following the same schedule, doing the same things everyday will make you trapped in a life of routines and sameness. Unvarying events adversely affects your performance, morale, and quality of work. Breaking the monotony will give you more flexibility, new streams of creativity and make your life more exciting and interesting.\nFor more, visit https://bit.ly/breakMonotonyMeraki",
                url="https://bit.ly/breakMonotonyMeraki", icon_url="https://enactus-srm.netlify.app/black.png"
                )
                #embed.set_image(url="https://www.mbs.ac.uk/media/ambs/content-assets/images/enterprise/enactus-manchester-enterprise-centre-main-1536x500.jpg")
                embed.set_thumbnail(url="https://enactus-srm.netlify.app/black.png")
                await message.channel.send(embed=embed)
            except discord.errors.Forbidden:
                pass




        if message.content.startswith(('>c','>C','c','C')):
            try:

                embed=discord.Embed(title="Meaning in life",
                description="C)Meaning in life: Meaning serves a number of important functions in human lives Firstly, meaning provides a purpose for our lives. Secondly, it furnishes values or standards by which to judge our actions. Thirdly, it gives us a sense of control over the events in our life. Lastly, it provides us with self-worth.\nFor more, visit https://bit.ly/meaningInLifeMeraki",
                url="https://bit.ly/meaningInLifeMeraki", icon_url="https://enactus-srm.netlify.app/black.png"
                )
                #embed.set_image(url="https://www.mbs.ac.uk/media/ambs/content-assets/images/enterprise/enactus-manchester-enterprise-centre-main-1536x500.jpg")
                embed.set_thumbnail(url="https://enactus-srm.netlify.app/black.png")
                await message.channel.send(embed=embed)
            except discord.errors.Forbidden:
                pass




        if message.content.startswith(('>d','>D','d','D')):
            try:

                embed=discord.Embed(title="Befriending Emotions",
                description="D)Befriending Emotions:  Befriending emotions is a gentle way to be mindful of what we're experiencing without judging ourselves. It allows us to process feelings like anger and hate. Being gently present with how feelings are living in our body can give us some distance from them.\nFor more, visit https://bit.ly/befriendEmotionsMeraki",
                url="https://bit.ly/befriendEmotionsMeraki", icon_url="https://enactus-srm.netlify.app/black.png"
                )
                #embed.set_image(url="https://www.mbs.ac.uk/media/ambs/content-assets/images/enterprise/enactus-manchester-enterprise-centre-main-1536x500.jpg")
                embed.set_thumbnail(url="https://enactus-srm.netlify.app/black.png")
                await message.channel.send(embed=embed)
            except discord.errors.Forbidden:
                pass




        if message.content.startswith(('>e','>E','e','E')):
            try:

                embed=discord.Embed(title="Anchor Yourself",
                description="E)Anchor Yourself:  An anchor at sea can be life saving or life threatening. Much like a sea voyage, we need to anchor ourselves to a strong value system, with a prioritization that helps you make decisions based on what is most important. Super clear goals that drive your actions and habits. However, anchors can also be negative, base beliefs that propagate only material joy and determine our self worth can often be detrimental.\nFor more, visit https://bit.ly/anchorYourselfMeraki",
                url="https://bit.ly/anchorYourselfMeraki", icon_url="https://enactus-srm.netlify.app/black.png"
                )
                #embed.set_image(url="https://www.mbs.ac.uk/media/ambs/content-assets/images/enterprise/enactus-manchester-enterprise-centre-main-1536x500.jpg")
                embed.set_thumbnail(url="https://enactus-srm.netlify.app/black.png")
                await message.channel.send(embed=embed)
            except discord.errors.Forbidden:
                pass



    else:
        pass
keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET2")
OTE0MTgxMjYwMTAzMDEyMzYy.YaJTpQ.7FuOn8B8jgX8J6NyawxBfZ1aL94
client.run(TOKEN)
