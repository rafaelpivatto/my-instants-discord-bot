import os

from discord.ext import commands
from loguru import logger

from bot.client import InstantClient
from bot.exceptions import MissingBotToken


bot = commands.Bot(command_prefix=commands.when_mentioned_or(">"),
                   description='Play audio from myinstants')


@bot.event
async def on_ready():
    logger.debug(f'Logged in as: {bot.user.name} - {bot.user.id}')

bot_token = os.getenv('MYINSTANTS_BOT_TOKEN')
if not bot_token:
    raise MissingBotToken

bot.add_cog(InstantClient(bot))
bot.run(bot_token)
