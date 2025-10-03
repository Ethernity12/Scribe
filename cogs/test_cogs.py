from disnake.ext import commands
from ext.logger import command_logger

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @command_logger()
    async def ping(self, inter):
        await inter.response.send_message("Pong!")