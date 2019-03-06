import discord
import random
import asyncio
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

        hembed0.set_footer(

            text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author.name)
        )

        hembed0.add_field(

        name="dbl web",
        value="[CLICK HERE](https://discordbots.org/bot/450174807368269825)"
        )
        
        try:

            await SmileBot.message.delete()
            await SmileBot.send(embed=hembed0)
            
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

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

    @commands.command()
    async def say(self, SmileBot, *, message):
        await SmileBot.message.delete()
        guild=SmileBot.message.guild
        log=discord.utils.get(guild.text_channels, name='mod-log')
        bog=self.bot.get_channel(541307455888556042)
        try:  
            await SmileBot.send("<:smilebot_loudspeaker:521796922391003148> "+message)
            await bog.send("I had to say ```"+message+"``` for "+SmileBot.message.author.name+" in "+SmileBot.message.channel.mention+" ("+SmileBot.message.channel.name+") on "+guild.name)
            try:
                await log.send("I had to say ```"+message+"``` for "+SmileBot.message.author.mention+" in "+SmileBot.message.channel.mention)
            except AttributeError:
                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Log not found: Cannot log commands! Please create a channel named ``mod-log``")
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @say.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!say ``message``")

    @commands.command()
    async def embed(self, SmileBot, title, description):

        try:
            eembed=discord.Embed(
                title=title,
                color=0x00ff00,
                description=description
            )

            eembed.set_footer(

                text="Sent by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author.name)
            )

            await SmileBot.message.delete()
            await SmileBot.send(embed=eembed)

        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @embed.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!embed ``title`` ``description``")


    @commands.command()
    async def vote(self, SmileBot, *, question):
        
        try:
        
            vembed = discord.Embed(

                title="VOTE",
                color=0xffff00,
                description=question
            )

            vembed.set_footer(

                text="Vote by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author.name)
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
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!vote ``question``")

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
        
                

    @commands.command()
    async def speak(self, SmileBot, *, arg1):
        
        try:
            if SmileBot.message.author.id == adminid:
                await SmileBot.send(arg1)
                await SmileBot.message.delete()
            else:
                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: ``Bot-Owner``")
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))
    @commands.command()
    async def users(self, SmileBot):
        await SmileBot.send("{0} registered users".format((len(self.bot.users))))

    @commands.command()
    async def servers(self, SmileBot):
        await SmileBot.send("On {0} servers".format((len(self.bot.guilds))))

    @commands.command()
    async def support(self, SmileBot):
        try:
            sembed = discord.Embed(
                title=None,
                color=0xff0000,
                description="[Join the supportserver](https://discord.gg/Ahf8J2c)"
            )
            sembed.set_footer(

                text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author.name)
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

                text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author.name)
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

                text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author.name)
            )
            await SmileBot.send(embed=uvembed)
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

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
                text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author.name)
            )

            await SmileBot.message.delete()
            await SmileBot.send(embed=sembed)
            
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

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

    @commands.command()
    async def user(self, SmileBot, member: discord.Member):

        try:

            userjoinedat = str(member.joined_at).split('.', 1)[0]

            usercreatedat = str(member.created_at).split('.', 1)[0]

            nickname = str(member.nick).split('.',1)[0]



            userembed = discord.Embed(

                title="Userinfo about:",
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
                text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author.name)
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
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!user ``@user``")

    @commands.command()
    async def server(self, SmileBot):
        
        try:

            guild=SmileBot.message.guild

            server_create_dat = str(guild.created_at).split('.', 1)[0]
            server_member_count = str(guild.member_count).split('.', 1)[0]
    
            serverembed=discord.Embed(
                title="Information about: "+guild.name,
                color=0xffff00,
            )
            serverembed.add_field(
                name="Owner:",
                value=guild.owner,
            )
            serverembed.add_field(
                name="Created at:",
                value=guild.created_at.strftime("%d %b %Y %H:%M"),
            )
            serverembed.add_field(
                name="Membercount:",
                value=server_member_count,
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

                value="{0} ({1} text;{2} voice)".format(len(SmileBot.guild.text_channels+SmileBot.guild.voice_channels), (len(SmileBot.guild.text_channels)), (len(SmileBot.guild.voice_channels)))
            )
            serverembed.add_field(
                name="Verification level:",
                  value=guild.verification_level,
            )
            serverembed.set_footer(
                text="Requested by {0} || Bot by Saaaga_Gamez#4206".format(SmileBot.message.author.name)
            )
            await SmileBot.message.delete()
            await SmileBot.send(embed=serverembed)
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))
    
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def goodbye(self, SmileBot):
        await SmileBot.message.delete()
        guild=SmileBot.message.guild
        bog=self.bot.get_channel(541307455888556042)
        try:
           
            await SmileBot.send("Bye! Was a nice time on your server!")
            await SmileBot.message.guild.leave()
            await bog.send("I just left "+guild.name)
            
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @goodbye.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``manage_server`` to perform this command!")
            

    @commands.command()
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
            await bog.send("New notification from "+guild.name+" by "+SmileBot.message.author.name)
            await bog.send(embed=nembed)
            
        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @notification.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``administrator`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!notification ``message``")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick (self, SmileBot, member: discord.Member, *, arg):
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
                        await log.send("WARNING! I couldn't send a message to "+member.name)
                    except AttributeError:
                        await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Log not found: Cannot log commands! Please create a channel named ``mod-log``")
                await SmileBot.guild.kick(member)
                await SmileBot.send("<:smilebot_check_mark:521789345426964490> Successfully kicked "+member.name+" => **"+arg+"**")
                try:
                    await log.send(embed=kembed)
                except AttributeError:
                    await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Log not found: Cannot log commands! Please create a chanel named ``mod-log``")
            

            except Exception as error:

                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @kick.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``kick_members`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!kick ``@user`` ``reason``")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban (self, SmileBot, member: discord.Member, *, args):
        guild=SmileBot.message.guild
        log=discord.utils.get(guild.text_channels, name='mod-log')
        bembed=discord.Embed(
            title="Moderation [ban]",
            color=0xff0000,
            description=member.mention+" got banned by "+SmileBot.message.author.mention+" because of **"+arg+"**"
            )
        if SmileBot.author==member:
            await SmileBot.send("<:smilebot_thinking:521809127954055191> I don't think you really want to ban yourself...")
        else:
            try:
                SmileBot.message.delete()
                try:
                    await member.send("You just got banned from "+SmileBot.message.guild.name+" because of: "+arg)
                except:
                    try:
                        await log.send("WARNING! I couldn't send a message to "+member.name)
                    except AttributeError:
                        await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Channel not found: Please create a channel named ``mod-log``")
                reason = args
                await SmileBot.guild.ban(member, reason = reason)
                await SmileBot.send("<:smilebot_check_mark:521789345426964490> Successfully banned "+member.name+" => **"+arg+"**")
                try:
                    await log.send(embed=bembed)
                except AttributeError:
                    await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Log not found: Cannot log commands! Please create a channel named ``mod-log``")
            

            except Exception as error:

                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @ban.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``ban_members`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!ban ``@user`` ``reason``")
        if isinstance(error, commands.self.bot.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: I need the ``ban_members`` permission to ban this user!")

    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def edit (self, SmileBot, mid, *, arg):
        await SmileBot.message.delete()
        try:

            medit=SmileBot.get_message(mid)
            await medit.edit(arg)

        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @edit.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``manage_messages`` to perform this command!")

    
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn (self, SmileBot, member: discord.Member, *, arg):
        guild=SmileBot.message.guild
        log=discord.utils.get(guild.text_channels, name='mod-log')
        wembed=discord.Embed(
            title="Moderation [warn]",
            color=0xff0000,
            description=member.mention+" got warned by "+SmileBot.message.author.mention+" for **"+arg+"**"
            )
        if SmileBot.author==member:
            await SmileBot.send("<:smilebot_thinking:521809127954055191> I don't think you really want to warn yourself...")
        else:
            try:
                await SmileBot.message.delete()
                try:
                    await member.send("You just got warned on "+SmileBot.message.guild.name+" because of: "+arg)
                except:
                    try:
                        await log.send("WARNING! I couldn't send a message to "+member.name)
                    except AttributeError:
                        await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Log not found: Cannot log commands! Please create a channel named ``mod-log``")
                await SmileBot.send("<:smilebot_check_mark:521789345426964490> Successfully warned "+member.name+" => **"+arg+"**")
                try:
                    await log.send(embed=wembed)
                except AttributeError:
                    await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Channel not found: Please create a channel named ``mod-log``")

            except Exception as error:

                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @warn.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``manage_messages`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!warn ``@user`` ``reason``")
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute (self, SmileBot, member: discord.Member, *, arg):
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
                try:
                    await member.add_roles(mrole)
                    try:
                        await member.send("You just got muted on "+SmileBot.message.guild.name+" because of: "+arg)
                    except:
                        try:
                            await log.send("WARNING! I couldn't send a message to "+member.name)
                        except AttributeError:
                            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Log not found: Cannot log commands! Please create a channel named ``mod-log``")
                    await SmileBot.send("<:smilebot_check_mark:521789345426964490> Successfully muted "+member.name+" => **"+arg+"**")
                    await log.send(embed=wembed)
                except AttributeError:
                    await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Role not found: Please create a role named ``Muted``")
            

            except Exception as error:

                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @mute.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``kick_members`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!mute ``@user`` ``reason``")

    
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
            try:
                await member.remove_roles(mrole)
                await SmileBot.send("<:smilebot_check_mark:521789345426964490> Successfully unmuted "+member.name)
                try:
                    await log.send(embed=wembed)
                except AttributeError:
                    await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Log not found: Cannot log commands! Please create a channel named ``mod-log``")
            except AttributeError:
                await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Role not found: Please create a role named ``Muted``")
            

        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @unmute.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``kick_members`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!unmute ``@user``")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def tempmute (self, SmileBot, member: discord.Member, seconds, *, arg):
        guild=SmileBot.message.guild
        log=discord.utils.get(guild.text_channels, name='mod-log')
        mrole=discord.utils.get(guild.roles, name='Muted')
        wembed=discord.Embed(
            title="New moderation action",
            color=0xff0000,
            description=member.mention+" got tempmuted by "+SmileBot.message.author.mention+" for "+seconds+" seconds because of **"+arg+"**"
            )
        await SmileBot.message.delete()
        try:
            await member.add_roles(mrole)
            await member.send("You just got tempmuted on "+SmileBot.message.guild.name+" for "+seconds+" seconds because of: "+arg)
            await SmileBot.send("<:smilebot_check_mark:521789345426964490> Successfully muted "+member.name)
            await log.send(embed=wembed)
            await asyncio.sleep(seconds)
            await member.remove_roles(mrole)
            

        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @tempmute.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``kick_members`` to perform this command!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def tempban (self, SmileBot, member: discord.Member, seconds, *, arg):
        guild=SmileBot.message.guild
        log=discord.utils.get(guild.text_channels, name='mod-log')
        mrole=discord.utils.get(guild.roles, name='Muted')
        wembed=discord.Embed(
            title="New moderation action",
            color=0xff0000,
            description=member.mention+" got tempbanned by "+SmileBot.message.author.mention+" for "+seconds+" seconds because of **"+arg+"**"
            )
        await SmileBot.message.delete()
        try:
            await SmileBot.guild.ban(member)
            await member.send("You just got tempbanned on "+SmileBot.message.guild.name+" for "+seconds+" seconds because of: "+arg)
            await SmileBot.send("<:smilebot_check_mark:521789345426964490> Successfully banned "+member.name+" => **"+arg+"**")
            await log.send(embed=wembed)
            await asyncio.sleep(seconds)
            await SmileBot.guild.unban(member)
            

        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @tempban.error
    async def error(self, SmileBot, error):
        if isinstance(error, commands.MissingPermissions):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``ban_members`` to perform this command!")

    @commands.command()
    async def ping(self, SmileBot):
        try:
            await SmileBot.send("**PONG** {0} ms\n".format(round(self.bot.latency*1000,0)))

        except Exception as error:

            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @commands.command()
    async def ownerdm (self, ctx, *, message):
        blocked_list="375538977685372928"
        owner=self.bot.get_user("375538977685372928")
        if message.author.id == blocked_list:
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Blocked! You are not allowed to use this command!")
        else:
            await owner.send("New DM from "+ctx.message.author.name+" ("+ctx.message.author.id+"). Content:"+message)
            await ctx.send("<:smilebot_check_mark:521789345426964490> Your message has been delivered to Saaaga_Gamez!")

    @ownerdm.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await SmileBot.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!ownerdm ``message``")
        
            
        
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
                    await member.send("You just got reported for "+args+" on "+guild.name)
                    await log.send(embed=rembed)
                    await ctx.send("<:smilebot_check_mark:521789345426964490> Successfully reported "+member.name)

                except AttributeError:
                    await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Channel not found: I couldn't report "+member.name+". Please create a channel named ``mod-log``")
                    
                except:
                    try:
                        await log.send("WARNING! I couldn't send a message to "+member.name)
                        await log.send(embed=rembed)
                        await ctx.send("<:smilebot_check_mark:521789345426964490> Successfully reported "+member.name)
                    except AttributeError:
                        await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Channel not found: I couldn't report "+member.name+". Please create a channel named ``mod-log``")
                
            
            except Exception as error:

                await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))
    @report.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!report ``user`` ``reason``")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addrole (self, ctx, member:discord.Member, *, arg):
        role=discord.utils.get(ctx.guild.roles, name=arg)
        log=discord.utils.get(ctx.guild.text_channels, name='mod-log')
        rembed=discord.Embed(
            title="Managing [addrole]",
            color=0x0000ff,
            description=ctx.author.mention+" affecting "+member.mention+" added role "+role.mention)
        try:
            await ctx.message.delete()
            try:
                await member.add_roles(role)
                await ctx.send("<:smilebot_check_mark:521789345426964490> Successfully added "+role.name+" to "+member.mention)
                try:
                    await log.send(embed=rembed)
                except AttributeError:
                    await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Log not found: Cannot log commands! Please create a channel named ``mod-log``")
            except AttributeError:
                await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Role not found: "+role.name+" not found")
            
        except Exception as error:

            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @addrole.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``manage_roles`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!addrole ``user`` ``role name``")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def removerole (self, ctx, member:discord.Member, *, arg):
        role=discord.utils.get(ctx.guild.roles, name=arg)
        log=discord.utils.get(ctx.guild.text_channels, name='mod-log')
        rembed=discord.Embed(
            title="Managing [removerole]",
            color=0x0000ff,
            description=ctx.author.mention+" affecting "+member.mention+" removed role "+role.mention)
        try:
            await ctx.message.delete()
            try:
                await member.remove_roles(role)
                await ctx.send("<:smilebot_check_mark:521789345426964490> Successfully removed "+role.name+" from "+member.mention)
                try:
                    await log.send(embed=rembed)
                except AttributeError:
                    await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Log not found: Cannot log commands! Please create a channel named ``mod-log``")
            except AttributeError:
                await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Role not found: "+role.name+" not found")
            
        except Exception as error:

            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: ``{error}``".format(error=error))

    @removerole.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing permissions: You need ``manage_roles`` to perform this command!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("<:smilebot_x:521789373319217152> **ERROR**: Missing arguments: Usage !!removerole ``user`` ``role name``") 

def setup(bot):
    bot.add_cog(Commands(bot))

