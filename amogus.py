#!/usr/bin/env python3
import discord, os
import os
from os.path import join, dirname
from dotenv import load_dotenv
 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class amogus(discord.Client):
    async def on_ready(self):
        print('Imposter:')
        print(self.user.name)
        print(self.user.id)
        print('-------------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!amogus'):
            await message.reply('When the imposter is sus!', mention_author=True)

client = amogus()
client.run(os.getenv('TOKEN'))
