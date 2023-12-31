import discord
import asyncio
from discord import app_commands
from key import token
TOKEN = token.get('TOKEN')

intents = discord.Intents.default()
intents.members = True

id_do_servidor =  815714353793466448
marketOn = False

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await clients.sync(guild = discord.Object(id=id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
            print(f"Entramos como {self.user}.")
            mercadao = aclient.get_channel(1141895078298783778)
            while(self.synced == True):
                if(marketOn == True): #Só funcionar quando usar o comando "/start" e parar quando for usado o "/stop"
                    mensagem = await mercadao.send("test")
                    await asyncio.sleep(10)
                    await mensagem.delete()
                await asyncio.sleep(1) 

aclient = client()
clients = app_commands.CommandTree(aclient)

@clients.command(guild = discord.Object(id=id_do_servidor), name = 'market', description='Visualiza como está o mercado!') #Comando específico para seu servidor
async def market(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá!", ephemeral = False) 

@clients.command(guild = discord.Object(id=id_do_servidor), name = 'balance', description='Mostra o seu saldo atual!') #Comando específico para seu servidor
async def balance(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá {interaction.user.mention} Seu saldo é: ", ephemeral = False)

@clients.command(guild = discord.Object(id=id_do_servidor), name = 'start', description='Inicia o mercado de ações') #Comando específico para seu servidor
async def start(interaction: discord.Interaction):
    global marketOn
    marketOn = True
    await interaction.response.send_message(f"Olá {interaction.user.mention}, Você acabou de iniciar a atualização de mercado", ephemeral = False)

@clients.command(guild = discord.Object(id=id_do_servidor), name = 'stop', description='Desliga o mercado de ações') #Comando específico para seu servidor
async def stop(interaction: discord.Interaction):
    global marketOn
    marketOn = False
    await interaction.response.send_message(f"Olá {interaction.user.mention}, Você acabou de desligar a atualização de mercado", ephemeral = False)

aclient.run(TOKEN)