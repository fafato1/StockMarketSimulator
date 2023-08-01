import discord
from discord.ext import commands
from key import token

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
TOKEN = token.get('TOKEN')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.find("mercado hoje"):
        async def slash2(interaction: discord.Interaction):
            await interaction.response.send_message(f'Olá, {message.author}, o mercado hoje se encontra vareando!', ephemeral = True)

client.run(TOKEN)