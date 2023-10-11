# Discord bot import
import discord
from discord.ext import commands
from discord import app_commands

# My program import
from Cogs.CommandPrograms.trpg_dice import dice

class trpg(app_commands.Group):
    def __init__(self, bot: commands.Bot, **kwargs):
        super().__init__(**kwargs)
        self.bot = bot
    
    # /trpg *
    # /trpg dice
    @app_commands.command(name="dice",description="ダイスを振ります。")
    @app_commands.guild_only()
    @app_commands.choices(secret=[discord.app_commands.Choice(name="on",value="on"),discord.app_commands.Choice(name="off",value="off")])
    async def trpg_dice_command(self, interaction: discord.Interaction, secret:str, args:str):

        await dice().trpg_dice(interaction, secret, args)

async def setup(bot: commands.Bot):
    bot.tree.add_command(trpg(bot, name="trpg"))