import discord
import asyncio
from discord.ext import commands
bot = commands.Bot(command_prefix='!!')
bot.remove_command("help")


cogs = [

    'Commands'
]

for cog in cogs:
    bot.load_extension(cog)

bot.remove_command("tempban")
bot.remove_command("tempmute")
bot.remove_command("ownerdm")
bot.remove_command("ban")
bot.remove_command("kick")

@bot.event
async def on_ready():

    print ('-Online-')
    print ('Logged in as:')
    print ('SmileBot | Beta')
    print ('Servercount:')
    print (len(bot.guilds))
    print ('Registered users:')
    print (len(bot.users))

@bot.event
async def error():
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await self.bot.send("<:smilebot_x:521789373319217152> Command not found!")

@bot.event
async def background_loop():
    await bot.wait_until_ready()
    while bot.is_ready():
            await bot.change_presence(activity=discord.Game(name="!!help"))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name="on {0} servers!".format(len(bot.guilds))))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name="with {0} users!".format(len(bot.users))))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name="with my raspberry pi!".format(len(bot.users))))
            await asyncio.sleep(10)

bot.loop.create_task(background_loop())


@bot.command()
async def help(ctx):
    
    adminid=375538977685372928

    hembed0 = discord.Embed(

          title="SmileBot",
           color=0x00ff00,
     )
    
    hembed0.add_field(
           
        name="Creator:",
        value="Saaaga_Gamez#4206"
    )
    hembed0.add_field(
            
        name="Hosting:",
        value="Raspberry Pi 3B+"
    )
    hembed0.add_field(
        name="Prefix:",
        value="!!"
    )

    hembed0.add_field(

        name="Library:",
        value="discord.py"
    )

    hembed0.add_field(

        name="Servercount:",
        value="{0}".format(len(bot.guilds))
    )

    hembed0.add_field(

        name="Registered users",
        value="{0}".format(len(bot.users))
    )

    hembed0.add_field(

        name="Upvote",
        value="[CLICK HERE](https://discordbots.org/bot/450174807368269825/vote)"
    )

    hembed0.add_field(

        name="Support",
        value="[CLICK HERE](https://discord.gg/Ahf8J2c)"
    )

    hembed0.add_field(

        name="Invite",
        value="[CLICK HERE](https://discordapp.com/oauth2/authorize?client_id=450174807368269825&permissions=268822598&scope=bot)"
    )

    hembed0.add_field(

        name="dbl web",
        value="[CLICK HERE](https://discordbots.org/bot/450174807368269825)"
    )

    hembed0.add_field(

        name="My commands",
        value="<> -- required\n"
                    "[] -- optional\n"
                    "~~cmd~~ -- out of function\n"

    )

    hembed0.add_field(

        name="Basic",

        value="say ``<message>`` -- None [Everything whats written over this cmd will be logged in #mod-log (if existing)] -- Let me say something with a <:smilebot_loudspeaker:521796922391003148> infront\n"
                "embed ``<title> <description>`` -- None -- Let me embed something\n"
                "notification ``<message>`` -- ``administrator`` -- Send a notification embed\n"
                 "vote ``<question>`` -- None -- Ask something to the other members\n"
                 "server -- None -- Information about the server\n"
                  "user ``<user>`` -- None -- Information about the mentioned user\n"
    )

    hembed0.add_field(

        name="Fun - Game",
         value="smile -- None -- Make me smile\n"
             "joy -- None -- Make me laugh\n"
             "think -- None -- Make me thinking\n"
             "token -- None -- My token (might include sarcasm)\n"
              "magic8ball -- None -- Ask a question to the magic 8ball\n"
              "coinflip -- None -- Flip a coin\n"

    )
    hembed0.add_field(

        name="German",
        value="schere -- None -- Spielt Schere-Stein-Papier. Du setzt: Schere\n"
                "stein -- None -- Spielt Schere-Stein-Papier. Du setzt: Stein\n"
                "papier -- None -- Spielt Schere-Stein-Papier. Du setzt: Papier\n"
    )
    hembed0.add_field(
        name="Managing",
        value="Create a channel named ``mod-log`` and SmileBot will log mod actions\n"
                "report ``<user>`` ``<reason>`` -- ``None`` -- Report a user\n"
                "addrole ``<user>`` ``<role name>`` -- ``manage_roles`` -- Add a role to a user\n"
                "removerole ``<user>`` ``<role name>`` -- ``manage_roles`` -- Remove a role from a user\n"
                "goodbye -- ``manage_server>`` -- Let me leave the current guild\n"
                "warn ``<user>`` ``<reason>`` -- ``manage_messages`` -- Warn a user\n"
                "mute ``<user>`` ``<reason>`` -- ``kick_members`` [Role needed named ``Muted``]-- Mute a user\n"
                "unmute ``<user>`` -- ``kick_members`` -- Unmute a user\n"
                "~~tempmute ``<user>`` ``<time in seconds>`` ``<reason>`` -- ``kick_members`` -- Tempmute a user~~\n"
                "~~kick ``<user>`` ``<reason>`` -- ``kick_members`` -- Kick a user~~\n"
                "~~ban ``<user>`` ``<reason>`` -- ``ban_members`` -- Ban a user~~\n"
                "~~tempban ``<user>`` ``<time in seconds>`` ``<reason>`` -- ban_members`` -- Tempban a user~~\n"
    )
    hembed0.add_field(

        name="About - Help",
        value="stats -- None -- Current stats\n"
                "ping -- None -- My ping\n"
                     "users -- None -- Amount of registered users\n"
                     "servers -- None -- Servercount\n"
                     "support -- None -- Supportserver invite\n"
                      "invite -- None -- Invite me to your server\n"
                    "upvote -- None -- Upvote SmileBot\n"
                     "info -- None -- Information about the bot\n"
    )



    try:
        await ctx.message.delete()
        await ctx.send(embed=hembed0)
    except Exception as error:
        await ctx.send("**ERROR**: ``{error}``".format(error=error))
@bot.command()
async def ban(ctx):
    await ctx.send(":warning: Because of some safety problems the ban command is disabled at the moment. For more information join the supportserver")

@bot.command()
async def kick(ctx):
    await ctx.send(":warning: Because of some safety problems the kick command is disabled at the moment. For more information join the supportserver")
                   
bot.run('TOKEN')
