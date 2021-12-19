from redbot.core import commands
import discord

class vote(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.bot_has_guild_permissions(send_messages=True)
    async def vote(self,ctx):
        em = discord.Embed(description=" ",color=discord.Color.purple())
        em.add_field(name="⏫ Vote Elixir:-",value=f"[**Vote**](https://top.gg/bot/732916004656513077/vote)",inline=False)
        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/732916004656513077/8636fca205b8c8eb71cd5f1c5ec91cd9.png?size=256")
        em.set_image(url="https://cdn.discordapp.com/attachments/847072756025655318/847072882356912128/unknown.gif")
        await ctx.send(embed=em)
