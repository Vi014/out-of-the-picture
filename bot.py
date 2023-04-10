import discord
import os

# Specify the user ID and server ID you want to delete messages in
TOKEN = "lol no token 4 u"

intents = discord.Intents.default()
intents.members = True

# Set up the bot client
client = discord.Client(intents=intents)

# Define the on_ready event handler
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
    mode = input("S to activate server-wide deletion, anything else to activate per-channel deletion: ")    
    
    if mode.lower() == 's':
        # Prompt the user to input the user ID and server ID
        user_id = input("Enter the user ID to delete messages from: ")
        server_id = input("Enter the server ID to delete messages in: ")
        # Get the specified server
        server = client.get_guild(int(server_id))
        if server is None:
            print(f"Error: server with ID {server_id} not found.")
            return
        # Loop through all text channels in the server and delete the user's messages
        for channel in server.text_channels:
            print(f"Deleting messages from user with ID {user_id} in channel {channel.name.encode('utf-8')}...")
            # Retrieve the message history
            messages = channel.history(limit=None)
            async for message in messages:
                if str(message.author.id) == user_id:
                    await message.delete()
            print(f"Finished deleting messages from user with ID {user_id} in channel {channel.name.encode('utf-8')}.")
        print("Finished deleting messages from user in all text channels in the server.")
    else:
        user_id = input("Enter the user ID to delete messages from: ")
        channel_id = input("Enter the channel ID to delete messages in: ")
        # Get the specified channel
        channel = client.get_channel(int(channel_id))
        if channel is None:
            print(f"Error: channel with ID {channel_id} not found.")
            return
        # Retrieve the message history
        messages = channel.history(limit=None)
        async for message in messages:
            if str(message.author.id) == user_id:
                await message.delete()
        print(f"Finished deleting messages from user {user_id} in channel {channel.name.encode('utf-8')}.")

# Start the bot
client.run(TOKEN)