import os
import disnake
from dotenv import dotenv_values
from disnake.ext import commands
from ext.logger import main_logger

config = {
    **dotenv_values(".env"),
    **os.environ,  
}


class Client(commands.InteractionBot):
    def __init__(self):
        super().__init__(intents=disnake.Intents.all())

    async def on_ready(self):
        user = bot.user
        main_logger.info("=== Bot Started ===")
        main_logger.info(f"Bot Name: {user}")
        main_logger.info(f"Bot ID: {user.id}")
        main_logger.info(f"Connected guilds: {len(bot.guilds)}")
        main_logger.info("==================")


if __name__ == '__main__':
    bot = Client()

    token = config.get('TOKEN')

    try:
        if token:
            main_logger.info('Starting bot...')
            bot.run(token)
        else:
            main_logger.critical('Missing token! Exiting!')
    except:
        main_logger.critical('Invalid Token')
