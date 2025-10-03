from disnake.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(ExampleCog(bot))