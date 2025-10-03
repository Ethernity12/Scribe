import os
import disnake
from cogs.test_cogs import ExampleCog
from dotenv import dotenv_values
from disnake.ext import commands
from ext.logger import main_logger
from typing import List

config = {
    **dotenv_values(".env"),
    **os.environ,  
}


class Client(commands.InteractionBot):
    def __init__(self):
        super().__init__(intents=disnake.Intents.all())
        self.cog_list: List[commands.Cog] = [
            ExampleCog(self)
        ]
        self.cog_loader()

    async def on_ready(self):
        user = self.user
        main_logger.info("=== Bot Started ===")
        main_logger.info(f"Bot Name: {user}")
        main_logger.info(f"Bot ID: {user.id}")
        main_logger.info(f"Connected guilds: {len(bot.guilds)}")
        main_logger.info("==================")

    def cog_loader(self):
        for cog in self.cog_list:
            self.add_cog(cog)
            main_logger.info(f"Cog loaded: {cog.__class__.__name__}")
        


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
