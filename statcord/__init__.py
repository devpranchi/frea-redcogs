from pathlib import Path

from redbot.core.bot import Red

with open(Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]

from .statcord import StatcordPost


async def setup(bot: Red) -> None:
    bot.add_cog(statcord(bot))
    
bot.load_extension("cogs/stat")
