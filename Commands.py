import discord
import random
import asyncio
import typing
from discord.ext import commands
adminid = 375538977685372928
minutes=0
hours=0
seconds=0
days=0


class Commands:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def bothelp(self, SmileBot):
        
        await SmileBot.send("Use !!help")

    @commands.command()
    async def info(self, SmileBot):

        hembed0 = discord.Embed(

            title="SmileBot",
            color=0xff0000,
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

            name="Commands:",
            value="!!help"
        )

        hembed0.add_field(

            name="Library:",
            value="discord.py"
        )

        hembed0.add_field(

            name="Servercount:",
            value="{0}".format(len(self.bot.guilds))
        )

        hembed0.add_field(

            name="Registered users",
            value="{0}".format(len(self.bot.users))
        )

        hembed0.add_field(

            name="Ping",
            value="{0} ms".format(round(self.bot.latency*1000,0))
        )

        hembed0.add_field(

            name="Upvote",
            value="[click here](https://discordbots.org/bot/450174807368269825/vote)"
        )

        hembed0.add_field(

            name="Support",
            value="[click here](https://discord.gg/Ahf8J2c)"
        )

        hembed0.add_field(

            name="Invite",
            value="[click here](https://discordapp.com/oauth2/authorize?client_id=450174807368269825&permissions=268822598&scope=bot)"
        )

        hembed0.set_footer(

            text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author)
        )

        hembed0.add_field(

        name="dbl web",
        value="[click here](https://discordbots.org/bot/450174807368269825)"
        )
        
        try:

            await SmileBot.message.delete()
            await SmileBot.send(embed=hembed0)
            
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

#testing-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def test(self, SmileBot):
        await SmileBot.send('Bestanden!')

    @commands.command()
    async def testerror(self, SmileBot):
        await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Just4Testing")


    @commands.command()
    async def testembed(self, SmileBot):

        tembed=discord.Embed(

            title="BESTANDEN",
            color=0xff0000

        )

        await SmileBot.send(embed=tembed)

#say------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command(aliases=["write","speak"])
    async def say(self, SmileBot, *, message):
        await SmileBot.message.delete()
        guild=SmileBot.message.guild
        log=discord.utils.get(guild.text_channels, name='mod-log')
        bog=self.bot.get_channel(541307455888556042)
        try:  
            await SmileBot.send("<:smilebot_loudspeaker:521796922391003148> "+message)
            await bog.send("I had to say ```{4}``` for ``{3}`` ({0}) in {2} on {1}".format(SmileBot.message.author, guild.name, SmileBot.message.channel.name, SmileBot.message.author.mention, message))
            try:
                await log.send("I had to say ```"+message+"``` for "+SmileBot.message.author.mention+" in "+SmileBot.message.channel.mention)
            except AttributeError:
                pass
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))
            # ("+SmileBot.author.id+")

    @say.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!say ``<message>``")

#embed-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def embed(self, SmileBot, title = "title", description = "description"):

        try:
            eembed=discord.Embed(
                title=title,
                color=0x00ff00,
                description=description
            )

            eembed.set_footer(

                text="Sent by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author)
            )

            await SmileBot.message.delete()
            await SmileBot.send(embed=eembed)

        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @embed.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!embed ``[title]`` ``[description]``")
        if isinstance(error, commands.BadArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Bad argument(s): Pls enter a valid title/description")
        if isinstance(error, commands.TooManyArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Too many arguments: Usage !!embed ``title`` ``description``")

#vote----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command(aliases=["poll"])
    async def vote(self, SmileBot, *, question):
        
        try:
        
            vembed = discord.Embed(

                title="VOTE",
                color=0xffff00,
                description=question
            )

            vembed.set_footer(

                text="Vote by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author)
            )

            await SmileBot.message.delete()
            question = await SmileBot.send(embed=vembed)
            await question.add_reaction(":smilebot_check_mark:521789345426964490")
            await question.add_reaction(":smilebot_o:521789361663115295")
            await question.add_reaction(":smilebot_x:521789373319217152")
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @vote.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!vote ``<question>``")

#emojis---------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def smile(self, SmileBot):
        await SmileBot.message.delete()
        await SmileBot.send("<:smilebot01:516242239220088863>")

    @commands.command()
    async def think(self, SmileBot):
        await SmileBot.message.delete()
        await SmileBot.send("<:smilebot_thinking:521809127954055191>")

    @commands.command()
    async def joy(self, SmileBot):
        await SmileBot.message.delete()
        await SmileBot.send(":joy:")

#coinflip--------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def coinflip(self, SmileBot):

        try:

            choice=random.randint(1,2)

            if choice == 1:

                await SmileBot.message.add_reaction(":smilebot_head:521795295533858836")

            if choice == 2:

                await SmileBot.message.add_reaction(":smilebot_one:521791962324402191")

        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

#ssp------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def schere(self, SmileBot):

        choice = random.randint(1, 3)

        if choice == 1:
            await SmileBot.send("Schere")

        if choice == 2:
            await SmileBot.send("Papier")

        if choice == 3:
            await SmileBot.send("Stein")

    @commands.command()
    async def stein(self, SmileBot):

        choice = random.randint(1, 3)

        if choice == 1:
            await SmileBot.send("Schere")

        if choice == 2:
            await SmileBot.send("Papier")

        if choice == 3:
            await SmileBot.send("Stein")

    @commands.command()
    async def papier(self, SmileBot):

        choice = random.randint(1, 3)

        if choice == 1:
            await SmileBot.send("Schere")

        if choice == 2:
            await SmileBot.send("Papier")

        if choice == 3:
            await SmileBot.send("Stein")

#msg------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def msg(self, SmileBot, member: discord.Member, *, arg1):
        dmembed=discord.Embed(
            title="<:smilebot_check_mark:521789345426964490> DM gesendet!",
            color=0x00ff00,
            description="Inhalt:\n"+arg1)
        
        
        try:
        
            
            if SmileBot.message.author.id == adminid:
                await member.send(arg1)
                await SmileBot.message.author.send(embed=dmembed)
                await SmileBot.message.delete()

            else:
                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: ``Bot-Owner``")
        except:
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Unable to dm user: I cannot send a dm to the mentioned user")

#stats-------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def users(self, SmileBot):
        await SmileBot.send("{0} registered users".format((len(self.bot.users))))

    @commands.command()
    async def servers(self, SmileBot):
        await SmileBot.send("On {0} guilds".format((len(self.bot.guilds))))

#links--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def support(self, SmileBot):
        try:
            sembed = discord.Embed(
                title=None,
                color=0xff0000,
                description="[Join the supportserver](https://discord.gg/Ahf8J2c)"
            )
            sembed.set_footer(

                text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author)
            )
            await SmileBot.send(embed=sembed)
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @commands.command()
    async def invite(self, SmileBot):
        try:
            
            iembed = discord.Embed(
                title=None,
                color=0xff0000,
                description="[Invite me to your server](https://discordapp.com/oauth2/authorize?client_id=450174807368269825&permissions=268822598&scope=bot)"
            )
            iembed.set_footer(

                text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author)
            )
            await SmileBot.send(embed=iembed)
            
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

            

    @commands.command()
    async def upvote(self, SmileBot):
        
        try:
            
            uvembed = discord.Embed(
                title=None,
                color=0xff0000,
                description="[Upvote SmileBot](https://discordbots.org/bot/450174807368269825/vote)"
            )
            uvembed.set_footer(

                text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author)
            )
            await SmileBot.send(embed=uvembed)
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

#token-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def token(self, SmileBot):
        
        try:
        
            choice = random.randint(1, 4)
        
            uvembed1 = discord.Embed(
                title="My token...",
                color=0xff0000,
                description="...is a secret!<:smilebot_thinking:521809127954055191>"
            )
            uvembed2 = discord.Embed(
                title="My token...",
                color=0xff0000,
                description="...is under your bed!:bed:"
            )
            uvembed3 = discord.Embed(
                title="My token...",
                color=0xff0000,
                description="...is at the moon!:full_moon_with_face:"
            )
            uvembed4 = discord.Embed(
                title="My token...",
                color=0xff0000,
                description="...is in the rubish!:wastebasket:"
            )
            await SmileBot.message.delete()
            if choice == 1:
                await SmileBot.send(embed=uvembed1)
            if choice == 2:
                await SmileBot.send(embed=uvembed2)
            if choice == 3:
                await SmileBot.send(embed=uvembed3)
            if choice == 4:
                await SmileBot.send(embed=uvembed4)
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

#stats--------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def stats(self, SmileBot):
        
        try:
            
            sembed = discord.Embed(

                title="Stats",
                color=0xffff00,
            )
            sembed.add_field(

                name="Servercount",

                   value="{0}".format((len(self.bot.guilds)))
            )
    
            sembed.add_field(

                name="Registered users",
    
                value="{0}".format((len(self.bot.users)))
            )

            sembed.add_field(

                name="Ping",
    
                value="{0} ms".format(round(self.bot.latency*1000,0))
            )
            sembed.set_footer(
                text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author)
            )

            await SmileBot.message.delete()
            await SmileBot.send(embed=sembed)
            
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

#magic8ball----------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def magic8ball(self, SmileBot):

        answer = random.randint(1, 5)

        if answer == 1:
            await SmileBot.send("Ask google")

        if answer == 2:
            await SmileBot.send("Yes")

        if answer == 3:
            await SmileBot.send("No")

        if answer == 4:
            await SmileBot.send("Maybe")

        if answer == 5:
            await SmileBot.send("I don't know... Try again later!")

#user---------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command(aliases=["user-info","userinfo"])
    async def user(self, SmileBot, member: discord.Member):

        try:

            userjoinedat = str(member.joined_at).split('.', 1)[0]

            usercreatedat = str(member.created_at).split('.', 1)[0]

            nickname = str(member.nick).split('.',1)[0]



            userembed = discord.Embed(

                title="Userinfo",
                color=0xffff00,
                description=member.mention

            )

            userembed.add_field(

                name="Username:",

                value=member.name

            )

            userembed.add_field(

                name="Nickname:",

                value=nickname

            )

            userembed.add_field(

                name="User ID:",

                value=member.id

            )

            userembed.add_field(

                name="Joined the server at:",

                value=member.joined_at.strftime("%d %b %Y %H:%M")

            )

            userembed.add_field(

                name="User registered at:",

                value=member.created_at.strftime("%d %b %Y %H:%M")

            )

            userembed.set_footer(
                text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author)
            )



            await SmileBot.send(embed=userembed)
            await SmileBot.message.delete()

        except IndexError:

            embed = discord.Embed(
                title="ERROR",
                color=0xffff00,
                description="I couldn't find a user. Pls try again."
            )

            await SmileBot.send(embed=embed)


        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

         

        finally:

            pass

    @user.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!user ``<user>``")
        if isinstance(error, commands.BadArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Bad argument(s): Pls enter a valid user")

#Server--------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command(aliases=["server-info","serverinfo"])
    async def server(self, SmileBot):

        guild=SmileBot.message.guild

        try:
            bans = len(await guild.bans())
        except discord.Forbidden:
            bans = "**Forbidden**\nI need ``ban_members`` to fetch bans"
        
        try:

            server_create_dat = str(guild.created_at).split('.', 1)[0]
            server_member_count = str(guild.member_count).split('.', 1)[0]
    
            serverembed=discord.Embed(
                title="Serverinfo",
                color=0xffff00,
                description=guild.name
            )
            serverembed.add_field(
                name="Owner:",
                value="{0}\n({1})".format(guild.owner.mention, guild.owner),
            )
            serverembed.add_field(
                name="Created at:",
                value=guild.created_at.strftime("%d %b %Y %H:%M"),
            )
            serverembed.add_field(
                name="Membercount:",
                value="{0}".format(server_member_count)
            )
            serverembed.add_field(
                name="Bans:",
                value=bans
            )
            serverembed.add_field(

                name="Region:",
                value=guild.region
            )
            serverembed.add_field(
                name="Roles:",
                value="{0}".format(len(guild.roles)),
            )
            serverembed.add_field(

                name="Channels:",

                value="{0} ({1} categories;{2} text;{3} voice)".format(len(SmileBot.guild.text_channels+SmileBot.guild.voice_channels+SmileBot.guild.categories),len(SmileBot.guild.categories), (len(SmileBot.guild.text_channels)), (len(SmileBot.guild.voice_channels)))
            )
            serverembed.add_field(
                name="Verification level:",
                  value=guild.verification_level,
            )
            serverembed.set_footer(
                text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author)
            )
            await SmileBot.message.delete()
            await SmileBot.send(embed=serverembed)
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

#goodbye-------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    @commands.command()
    async def goodbye(self, SmileBot):
        
        guild=SmileBot.message.guild
        bog=self.bot.get_channel(541307455888556042)
        try:
           if SmileBot.message.author == SmileBot.message.guild.owner:
                await SmileBot.message.delete()
                await SmileBot.send("Bye! Was a nice time on your server!")
                await SmileBot.message.guild.leave()
                await bog.send("I just left "+guild.name)
           else:
                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You have to be owner of this guild to perform this command!")
            
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

#notification--------------------------------------------------------------------------------------------------------------------------------------------------------          

    @commands.command(aliases=["announcement"])
    @commands.has_permissions(administrator=True)
    async def notification(self, SmileBot, *, arg1):
        nembed=discord.Embed(
            title="Notification :bell:",
            color=0x00ff00,
            description=arg1
            )
        await SmileBot.message.delete()
        guild=SmileBot.message.guild
        bog=self.bot.get_channel(541307455888556042)
        try:
            await SmileBot.send(embed=nembed)
            await bog.send("New notification from "+guild.name+" by {0}".format(SmileBot.message.author))
            await bog.send(embed=nembed)
            
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @notification.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``administrator`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!notification ``<message>``")

#kick----------------------------------------------------------------------------------------------------------------------------------------------------------------


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick (self, SmileBot, member: discord.Member, *, arg = "unspecified"):
        guild=SmileBot.message.guild
        log=discord.utils.get(guild.text_channels, name='mod-log')
        kembed=discord.Embed(
            title="Moderation [kick]",
            color=0xff0000,
            description=member.mention+" got kicked by "+SmileBot.message.author.mention+" because of **"+arg+"**"
            )
        if SmileBot.author==member:
            await SmileBot.send("<:smilebot_thinking:521809127954055191> I don't think you really want to kick yourself...")
        else:
            try:
                await SmileBot.message.delete()
                try:
                    await member.send("You just got kicked from "+SmileBot.message.guild.name+" because of: "+arg)
                except:
                    try:
                        await log.send("WARNING! I couldn't send a message to {0}".format(member))
                    except AttributeError:
                        pass
                await SmileBot.guild.kick(member)
                await SmileBot.send("<:smilebot_check_mark:521789345426964490> Successfully kicked {0} => **{1}**".format(member, args))
                try:
                    await log.send(embed=kembed)
                except AttributeError:
                    pass            

            except Exception as error:

                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @kick.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``kick_members`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!kick ``<@user>`` ``[reason]``")
        if isinstance(error, commands.BadArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Bad argument(s): Pls enter a valid user")

#Ban----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban (self, SmileBot, member: discord.Member, *, args = "unspecified"):
        guild=SmileBot.message.guild
        log=discord.utils.get(guild.text_channels, name='mod-log')
        bembed=discord.Embed(
            title="Moderation [ban]",
            color=0xff0000,
            description=member.mention+" got banned by "+SmileBot.message.author.mention+" because of **"+args+"**"
            )
        if SmileBot.author==member:
            await SmileBot.send("<:smilebot_thinking:521809127954055191> I don't think you really want to ban yourself...")
        else:
            try:
                await SmileBot.message.delete()
                try:
                    await member.send("You just got banned from "+SmileBot.message.guild.name+" because of: "+args)
                except:
                    try:
                        await log.send("WARNING! I couldn't send a message to {0}".format(member))
                    except AttributeError:
                        pass
                grund="{0} > by {1}".format(args, SmileBot.message.author)
                await SmileBot.guild.ban(member, reason = grund)
                await SmileBot.send("<:smilebot_check_mark:521789345426964490> Successfully banned {0} => **{1}**".format(member, args))
                try:
                    await log.send(embed=bembed)
                except AttributeError:
                    pass
            

            except Exception as error:

                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @ban.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``ban_members`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!ban ``<user>`` ``[reason]``")
        if isinstance(error, commands.BadArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Bad argument(s): Pls enter a valid user")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban (self, SmileBot, member: discord.Member):
        guild=SmileBot.message.guild
        log=discord.utils.get(guild.text_channels, name='mod-log')
        bembed=discord.Embed(
            title="Moderation [unban]",
            color=0xff0000,
            description="{0} unbanned {1}.".format(ctx.message.author.mention, member)
            )
        if SmileBot.author==member:
            await SmileBot.send("<:smilebot_thinking:521809127954055191> How is this possible?")
        else:
            try:
                SmileBot.message.delete()
                await SmileBot.guild.unban(member)
                await SmileBot.send("<:smilebot_check_mark:521789345426964490> Successfully unbanned {0}".format(member))
                try:
                    await log.send(embed=bembed)
                except AttributeError:
                    pass
            

            except Exception as error:

                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @unban.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``ban_members`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!unban ``<user>``")
        if isinstance(error, commands.BadArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Bad argument(s): Pls enter a valid user")
            

#warn------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn (self, SmileBot, member: discord.Member, *, reason = "unspecified"):
        guild=SmileBot.message.guild
        log=discord.utils.get(guild.text_channels, name='mod-log')
        wembed=discord.Embed(
            title="Moderation [warn]",
            color=0xff0000,
            description=member.mention+" got warned by "+SmileBot.message.author.mention+" for **"+reason+"**"
            )
        if SmileBot.author==member:
            await SmileBot.send("<:smilebot_thinking:521809127954055191> I don't think you really want to warn yourself...")
        else:
            try:
                await SmileBot.message.delete()
                try:
                    await member.send("You just got warned on "+SmileBot.message.guild.name+" because of: "+reason)
                except:
                    try:
                        await log.send("WARNING! I couldn't send a message to {0}".format(member))
                    except AttributeError:
                        pass
                await SmileBot.send("<:smilebot_check_mark:521789345426964490> Successfully warned {0} => **{1}**".format(member,reason))
                try:
                    await log.send(embed=wembed)
                except AttributeError:
                    pass

            except Exception as error:

                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @warn.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``manage_messages`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!warn ``@user`` ``reason``")
        if isinstance(error, commands.BadArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Bad argument(s): Pls enter a valid user")

#Mute------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute (self, SmileBot, member: discord.Member, *, arg="unspecified"):
        guild=SmileBot.message.guild
        log=discord.utils.get(guild.text_channels, name='mod-log')
        mrole=discord.utils.get(guild.roles, name='Muted')
        wembed=discord.Embed(
            title="Moderation [mute]",
            color=0xff0000,
            description=member.mention+" got muted by "+SmileBot.message.author.mention+" because of **"+arg+"**"
            )
        if SmileBot.author==member:
            await SmileBot.send("<:smilebot_thinking:521809127954055191> I don't think you really want to mute yourself...")
        else:
        
            try:
                await SmileBot.message.delete()
                await member.add_roles(mrole)
                try:
                    await member.send("You just got muted on "+SmileBot.message.guild.name+" because of: "+arg)
                except:
                    try:
                        await log.send("WARNING! I couldn't send a message to {0}".format(member))
                    except AttributeError:
                        pass
                await SmileBot.send("<:smilebot_check_mark:521789345426964490> Successfully muted {0} => **{1}**".format(member,arg))
                try:
                    await log.send(embed=wembed)
                except AttributeError:
                    pass
            except Exception as error:

                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @mute.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``kick_members`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!mute ``@user`` ``reason``")
        if isinstance(error, commands.BadArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Bad argument(s): Pls enter a valid user")
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute (self, SmileBot, member: discord.Member):
        guild=SmileBot.message.guild
        log=discord.utils.get(guild.text_channels, name='mod-log')
        mrole=discord.utils.get(guild.roles, name='Muted')
        wembed=discord.Embed(
            title="Moderation [unmute]",
            color=0xff0000,
            description=member.mention+" got unmuted by "+SmileBot.message.author.mention
            )
        await SmileBot.message.delete()
        try:
                await member.remove_roles(mrole)
                await SmileBot.send("<:smilebot_check_mark:521789345426964490> Successfully unmuted {0}".format(member))
                try:
                    await log.send(embed=wembed)
                except AttributeError:
                    pass

        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @unmute.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``kick_members`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!unmute ``@user``")
        if isinstance(error, commands.BadArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Bad argument(s): Pls enter a valid user")

#Ping-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def ping(self, SmileBot):
        try:
            await SmileBot.send("**PONG** {0} ms\n".format(round(self.bot.latency*1000,0)))

        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))
        
#Report----------------------------------------------------------------------------------------------------------------------------------------------------------------------            
        
    @commands.command()
    async def report (self, ctx, member:discord.Member, *, args):
        guild=ctx.message.guild
        log=discord.utils.get(guild.text_channels, name='mod-log')
        rembed=discord.Embed(
            title="Moderation [report]",
            color=0xff0000,
            description=member.mention+" got reported by "+ctx.author.mention+" because of **"+ args+"**")

        if ctx.author==member:
            await ctx.send("<:smilebot_thinking:521809127954055191> I don't think you really want to report yourself...")
        else:
            try:
                await ctx.message.delete()
                try:
                    await log.send(embed=rembed)
                    await ctx.send("<:smilebot_check_mark:521789345426964490> Successfully reported {0}".format(member))
                    await member.send("You just got reported for "+args+" on "+guild.name)

                except AttributeError:
                    await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Log not found: I couldn't report {0}. Please create a channel named ``mod-log``".format(member))
                    
                except:
                    try:
                        await log.send("WARNING! I couldn't send a message to {0}".format(member))
                        await log.send(embed=rembed)
                        await ctx.send("<:smilebot_check_mark:521789345426964490> Successfully reported {0}".format(member))
                    except AttributeError:
                        await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Channel not found: I couldn't report {0}. Please create a channel named ``mod-log``".format(member))
                
            
            except Exception as error:

                await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))
    @report.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!report ``user`` ``reason``")
        if isinstance(error, commands.BadArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Bad argument(s): Pls enter a valid user")

#Role-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addrole (self, ctx, member:discord.Member, role: discord.Role):
        log=discord.utils.get(ctx.guild.text_channels, name='mod-log')
        rembed=discord.Embed(
            title="Managing [addrole]",
            color=0x0000ff,
            description=ctx.author.mention+" affecting "+member.mention+" added role "+role.mention)
        try:
            await ctx.message.delete()
            await member.add_roles(role)
            await ctx.send("<:smilebot_check_mark:521789345426964490> Successfully added "+role.name+" to "+member.mention)
            try:
                await log.send(embed=rembed)
            except AttributeError:
                pass
            
        except Exception as error:

            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @addrole.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``manage_roles`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!addrole ``user`` ``role name``")
        if isinstance(error, commands.BadArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Bad argument(s): Pls enter a valid user/role")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def removerole (self, ctx, member:discord.Member, role: discord.Role):
        log=discord.utils.get(ctx.guild.text_channels, name='mod-log')
        rembed=discord.Embed(
            title="Managing [removerole]",
            color=0x0000ff,
            description=ctx.author.mention+" affecting "+member.mention+" removed role "+role.mention)
        try:
            await ctx.message.delete()
            await member.remove_roles(role)
            await ctx.send("<:smilebot_check_mark:521789345426964490> Successfully removed "+role.name+" from "+member.mention)
            try:
                await log.send(embed=rembed)
            except AttributeError:
                pass
        except Exception as error:

            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @removerole.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``manage_roles`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!removerole ``user`` ``role name``")
        if isinstance(error, commands.BadArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Bad argument(s): Pls enter a valid user/role")
            
#Clear----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command(aliases=["purge","delete"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, arg: typing.Union[int, discord.Member]):

            

        if isinstance(arg, int):
            if arg < 1:
                return await ctx.send("<:smilebot_thinking:521809127954055191> Deleteing {0} messages is not possible...".format(arg))
            if arg > 100:
                return await ctx.send("<:smilebot_x:521789373319217152> I can't delete more than 100 messages at once!")

            deleted = await ctx.channel.purge(limit=min(arg, 100) + 1)
        elif isinstance(arg, discord.Member):
            deleted = await ctx.channel.purge(check=lambda m: m.author.id == arg.id)

        messages = len(deleted)-1
        log=discord.utils.get(ctx.guild.text_channels, name='mod-log')
        cembed=discord.Embed(
            title="Managing [purge]",
            color=0x0000ff,
            description="{0} deleted {1} messages in {2}".format(ctx.author.mention, messages, ctx.message.channel.mention)
            )
        if messages < 1:
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: I can't delete less than 1 messages")
        else:
            answer=await ctx.send("<:smilebot_check_mark:521789345426964490> Successfully deleted {0} messages!\n".format(messages), delete_after=5)
            try:
                await log.send(embed=cembed)
            except AttributeError:
                pass
                           
    @clear.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``manage_messages`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument): 
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!clear ``amount``")
        if isinstance(error, commands.BadArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Bad argument(s): Pls enter a valid amount/user")

#Sendto----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def sendto (self, ctx, Guild, Name, *, text):
        server=discord.utils.get(self.bot.guilds, name=Guild)
        channel=discord.utils.get(server.text_channels, name=Name)
        if ctx.message.author.id==adminid:
            await channel.send(text)
            await ctx.send("Message sent!")
        else:
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: ``Bot-Owner``")

#roleinfo---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command(aliases=["roleinfo","role-info"])
    async def role(selfs,ctx, role: discord.Role):

        if role.mentionable==True:
            variable1="<:smilebot_check_mark:521789345426964490>"
        else:
            variable1="<:smilebot_x:521789373319217152>"

        if role.hoist==True:
            variable2="<:smilebot_check_mark:521789345426964490>"
        else:
            variable2="<:smilebot_x:521789373319217152>"

        if role.permissions.administrator==True:
            variable3="<:smilebot_check_mark:521789345426964490>"
        else:
            variable3="<:smilebot_x:521789373319217152>"

        rembed=discord.Embed(
            title="Role",
            color=0xffff00,
        )

        rembed.add_field(

            name="Name:",
            value=role.name
        )

        rembed.add_field(

            name="ID:",
            value=role.id
        )

        rembed.add_field(

            name="Mention:",
            value="{0}\n``{1}``".format(role.mention, role.mention)
        )

        rembed.add_field(

            name="Color:",
            value=role.color
        )

        rembed.add_field(

            name="Members in this role:",
            value=len(role.members)
        )

        rembed.add_field(

            name="Created at:",
            value=role.created_at.strftime("%d %b %Y %H:%M")
        )

        rembed.add_field(

            name="Mentionable:",
            value=variable1
        )

        rembed.add_field(

            name="Hoisted:",
            value=variable2
        )

        rembed.add_field(

            name="Administrator:",
            value=variable3
        )

        rembed.set_footer(

            text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(ctx.message.author)

        )

        await ctx.message.delete()
        await ctx.send(embed=rembed)

    @role.error
    async def error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!role ``role``")
        if isinstance(error, commands.BadArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Bad argument(s): Pls enter a valid role")

#Restart------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def restart(self, ctx):

        python=sys.executable
        os.execl(python, python, *sys.argv)

        if ctx.message.author.id==adminid:
            try:
                process=self.bot.process
                for handler in process.open_files() + process.connections():
                    os.close(handler.fd)
                await ctx.send("<:smilebot_check_mark:521789345426964490> Restarting...")
            except:
                await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Something went wrong!")
        else:
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``Bot-Owner`` to perform this command!")

#Bugreport--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command(aliases=["bug","bug-report"])
    async def bugreport (self,ctx,*,bug):
        bog=self.bot.get_channel(541307455888556042)
        bembed=discord.Embed(
            title="Bugreport",
            color=0xff0000,
            description="User: {0} ({1})\nGuild: {2}\nChannel: {3} ({4})\nBug: {5}".format(ctx.message.author, ctx.message.author.id, ctx.message.guild.name, ctx.message.channel.name, ctx.message.channel.id, bug)
        )
        if ctx.message.author.id == 0:
            await ctx.send("<:smilebot_x:521789373319217152> Blocked: You are not allowed to execute this command!")
        else:
            if ctx.message.id==369824793165561857:
                await ctx.send("Moin Hirschi! Da du warscheinlich eh keinen Bug reporten willst, schreib mir doch einfach per DM.\nLG Saaaga_Gamez :joy:")
            else:
                await bog.send(embed=bembed)
                await ctx.send("<:smilebot_check_mark:521789345426964490> Bug reported! You may recieve a message via dm or this channel if the bug is fixed!")

#Help---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.command(aliases=["h","hilfe"])
    async def help(self, ctx, module):



        bembed=discord.Embed(

            title="Basic",
            color=0xffff00,
            description="say ``<message>`` -- None -- Let me say something with a <:smilebot_loudspeaker:521796922391003148> infront\n"
                        ">Aliases: ``write``;``speak``\n"
                        "embed ``[title]`` ``[description]`` -- None -- Let me embed something\n"
                        "notification ``<message>`` -- ``administrator`` -- Send a notification embed\n"
                        ">Aliases: ``announcement``\n"
                        "vote ``<question>`` -- None -- Ask something to the other members\n"
                        ">Aliases: ``poll``\n"
                        "server -- None -- Information about the server\n"
                        ">Aliases: ``serverinfo``;``server-info``\n"
                        "user ``<user>`` -- None -- Information about the mentioned user\n"
                        ">Aliases: ``userinfo``;``user-info``\n"
                        "role ``<role>`` -- None -- Information about the mentioned role\n"
                        ">Aliases: ``roleinfo``;``role-info``\n"
                        "bug ``<bug>`` -- None -- Report a bot bug\n"
                        ">Abuse may end in a block!\n"
                        ">Aliases: ``bugreport``;``bug-report``\n"
                        "\n"
                        "``<required>`` ¦ ``[optional]`` ¦ ~~out of function~~\n"
        )

        bembed.set_footer(

            text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(ctx.message.author)

        )

        fgembed = discord.Embed(

            title="Fun",
            color=0x0000ff,
            description="smile -- None -- Make me smile\n"
                        "joy -- None -- Make me laugh\n"
                        "think -- None -- Make me thinking\n"
                        "token -- None -- My token (might include sarcasm)\n"
                        "magic8ball ``[question]`` -- None -- Ask a question to the magic 8ball\n"
                        "coinflip -- None -- Flip a coin\n"
                        "\n"
                        "``<required>`` ¦ ``[optional]`` ¦ ~~out of function~~\n"
        )

        fgembed.set_footer(

            text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(ctx.message.author)

        )

        gembed = discord.Embed(

            title="German",
            color=0x00ff00,
            description="schere -- None -- Spielt Schere-Stein-Papier. Du setzt: Schere\n"
                        "stein -- None -- Spielt Schere-Stein-Papier. Du setzt: Stein\n"
                        "papier -- None -- Spielt Schere-Stein-Papier. Du setzt: Papier\n"
                        "\n"
                        "``<required>`` ¦ ``[optional]`` ¦ ~~out of function~~\n"
        )

        gembed.set_footer(

            text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(ctx.message.author)

        )

        membed = discord.Embed(

            title="Managing",
            color=0x00ffff,
            description="clear ``<amount|user>`` -- ``manage_messages`` -- Clear an amount of messages or all messages of a user\n"
                        ">Aliases: ``purge``;``delete``\n"
                        "addrole ``<user>`` ``<role>`` -- ``manage_roles`` -- Add a role to a user\n"
                        "removerole ``<user>`` ``<role>`` -- ``manage_roles`` -- Remove a role from a user\n"
                        "goodbye -- ``server_owner`` -- Let me leave the current guild\n"
                        "\n"
                        "``<required>`` ¦ ``[optional]`` ¦ ~~out of function~~\n"
                        "\n"
                        "Every use of these commands will be logged, if a channel named ``mod-log`` exists"
        )

        membed.set_footer(

            text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(ctx.message.author)

        )

        modembed = discord.Embed(

            title="Moderation",
            color=0xff0000,
            description="report ``<user>`` ``<reason>`` -- ``None`` -- Report a user\n"
                        "warn ``<user>`` ``[reason]`` -- ``manage_messages`` -- Warn a user\n"
                        "mute ``<user>`` ``[reason]`` -- ``kick_members`` [Role needed named ``Muted``]-- Mute a user\n"
                        "unmute ``<user>`` -- ``kick_members`` -- Unmute a user\n"
                        "kick ``<user>`` ``[reason]`` -- ``kick_members`` -- Kick a member\n"
                        "ban ``<user>`` ``[reason]`` -- ``ban_members`` -- Ban a member\n"
                        "~~unban ``<user>`` -- ``ban_members`` -- Unban a user~~\n"
                        "\n"
                        "``<required>`` ¦ ``[optional]`` ¦ ~~out of function~~\n"
                        "\n"
                        "Every use of these commands will be logged, if a channel named ``mod-log`` exists"
        )

        modembed.set_footer(

            text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(ctx.message.author)

        )

        aembed = discord.Embed(

            title="About",
            color=0x0000ff,
            description="info -- None -- Information about the bot\n"
                        "stats -- None -- Current stats\n"
                        "ping -- None -- My ping\n"
                        "users -- None -- Amount of registered users\n"
                        "servers -- None -- Servercount\n"
                        "support -- None -- Supportserver invite\n"
                        "invite -- None-- Invite me to your server\n"
                        "upvote -- None -- Upvote SmileBot\n"
                        "\n"
                        "``<required>`` ¦ ``[optional]`` ¦ ~~out of function~~\n"
        )

        aembed.set_footer(

            text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(ctx.message.author)

        )

        oembed = discord.Embed(

            title="Owner",
            color=0x000000,
            description="msg ``<User>`` ``<message>`` -- Owner -- Send a DM to the mentioned user\n"
                        "sendto ``<guild name>`` ``<channel name>`` ``<message>`` -- Owner -- Send a message\n"
                        "~~restart -- Owner -- Restart the bot~~\n"
                        "\n"
                        "``<required>`` ¦ ``[optional]`` ¦ ~~out of function~~\n"
        )

        oembed.set_footer(

            text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(ctx.message.author)

        )

        if module=="Basic" or module=="basic":
            await ctx.message.delete()
            await ctx.send(embed=bembed)
        else:
            if module=="Fun" or module=="fun":
                await ctx.message.delete()
                await ctx.send(embed=fgembed)
            else:
                if module=="German" or module=="german":
                    await ctx.message.delete()
                    await ctx.send(embed=gembed)
                else:
                    if module=="Managing" or module=="managing":
                        await ctx.message.delete()
                        await ctx.send(embed=membed)
                    else:
                        if module=="Moderation" or module=="moderation":
                            await ctx.message.delete()
                            await ctx.send(embed=modembed)
                        else:
                            if module=="About" or module=="about":
                                await ctx.message.delete()
                                await ctx.send(embed=aembed)
                            else:
                                if module=="Owner" or module== "owner":
                                    await ctx.message.delete()
                                    await ctx.send(embed=oembed)
                                else:
                                    await ctx.send("<:smilebot_x:521789373319217152> Module **{0}** not found.".format(module))

    @help.error
    async def error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            hembed=discord.Embed(
                title="HELP!",
                color=0xff00ff,
                description="!!help ``module``\nAliases: ``h`` ; ``hilfe``"
            )

            hembed.add_field(

                name="Modules",
                value="Basic\nFun\nGerman\nManaging\nModeration\nAbout\nOwner\n"
                      "\n"
                      "You've found a bug? Type !!bug ``<bug>`` to report it!\n"
                      "\n"
                      "[Invite](https://discordapp.com/oauth2/authorize?client_id=450174807368269825&permissions=268822598&scope=bot) | [Support](https://discord.gg/Ahf8J2c) | [DBL](https://bit.ly/SmileBot)"
            )

            hembed.set_footer(

                text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(ctx.message.author)

            )

            react=await ctx.send(embed=hembed)
            await react.add_reaction(":smilebot_letter_S:554315152112222220")
            await react.add_reaction(":smilebot_letter_m:554315151541796874")
            await react.add_reaction(":smilebot_letter_i:554315151424225280")
            await react.add_reaction(":smilebot_letter_l:554315152019816468")
            await react.add_reaction(":smilebot_letter_e:554315151998976041")
            await react.add_reaction(":smilebot_letter_B:554315152040919060")
            await react.add_reaction(":smilebot_letter_o:554315152401498132")
            await react.add_reaction(":smilebot_letter_t:554315152263086080")

def setup(bot):
    bot.add_cog(Commands(bot))

