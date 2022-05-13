from redbot.core import commands
import discord

class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(aliases=["botinfo"])
    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.has_guild_permissions(send_messages=True)
    async def about(self,ctx):
        em = discord.Embed(description=" ",color=discord.Color.purple())
        em.add_field(name="Instance owned by",value="**\`sechi#0002** - Developer\n**\`yukina#8653** - Graphics Designer",inline=False)
        em.add_field(name="Hosting provider",value="Amazon AWS EC2 - Singapore server(ap-southeast1)",inline=False)
        em.add_field(name="Python",value="3.9.5",inline=True)
        em.add_field(name="discord.py",value="1.7.3",inline=True)
        em.add_field(name="Red version",value="3.4.16",inline=True)
        em.add_field(name="About Frea",value=f"This bot is an instance of [Red, an open source Discord bot](https://github.com/Cog-Creators/Red-DiscordBot) created by [Twentysix](https://github.com/Twentysix26) and [improved by many.](https://github.com/Cog-Creators)",inline=False)
        em.add_field(name="Story Behind Frea",value=f"Frea was made by Sechi, also one of Elixir's devs, and then maintained by the community.\n\n**Quick Links**\n[Status Page](https://status.pranchi.xyz) | [Support Server](https://frea.io/support) | [GitHub](https://github.com/devpranchi/frea-discord)",inline=False)
        await ctx.send(embed=em)
