import nextcord
from nextcord import Interaction
from nextcord.ext import commands

# datetime for the terminal to print out time for reference if there's slow down or used for references
from datetime import datetime
import os
import webserver

BOT_TOKEN = os.environ["discordkey"]
GUILD_ID = os.environ["guildid"]
GAME_VC1 = os.environ["gamevc"]

# Not really sure what this do, they say its important
intents = nextcord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents  )

# Formatting date time for easy usage
def datetimeStr():
    datetimeFormat = "%Y-%m-%d %H:%M:%S"
    datetimeNow = datetime.now().strftime(datetimeFormat)
    datetimestr = f"[{datetimeNow}]"
    return datetimestr


class DiscordBot:
    def __init__(self, bot=None):
        if bot:
            self.bot = bot
        else:
            #TODO: Add a print that show how long the system run, by comparing the system uptime and the current time
            exit()

    @bot.event
    async def on_ready():
        # Sync global commands
        await bot.sync_all_application_commands() 
        print(f"{datetimeStr()}: 🟢 Logged in as {bot.user}")
        # Source - https://stackoverflow.com/a
        # Posted by Asis, modified by community. See post 'Timeline' for change history
        # Retrieved 2025-12-25, License - CC BY-SA 4.0

        channel = nextcord.utils.get(bot.get_all_channels(), id=1375791037691330640)
        await channel.connect()


    def run(self, token=None):
        if token:
            self.bot.run(token)
        else:
            #TODO: Add a print that show how long the system run, by comparing the system uptime and the current time
            exit()

# Start of the code
webserver.keep_alive()
Bot = DiscordBot(bot)

Bot.run(token=BOT_TOKEN)
