from telethon import TelegramClient, events
from telethon.tl.functions.users import GetFullUserRequest
from dotenv import load_dotenv
import os
import re


load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client = TelegramClient('session_name', api_id, api_hash)
client.start()

lista_users = ["DollarDreamYT","fullmetalcrypto","ShreksOfficiaL", "FrontMaLee", "ttarded", "bogdump"]
#squidlounge -1001661707644
#add more group ids in the list. Remember that the channel ids need the -100 code added while group ids don't.
groups = [-1001661707644]

contract_regex = r'0x[\w\d]{40}'

@client.on(events.NewMessage(chats = groups))

#These 2 commented lines  of code is for using the user_id to recognize more than one user
#target_user_id = [5017980027]  #Replace with the specific user ID
#@client.on(events.NewMessage(chats=groups, from_users=target_user_id))



async def main(event):
    user = await event.get_sender()
    match = re.search(contract_regex, event.message.message)
    
    if event.message.sender.username in lista_users:
        if event.message.sender.username == "ttarded":
            await event.forward_to(-1001803658184) 
    
        if match:
            matched_pattern = match.group()
            message = await client.send_message(-1001803658184, "Contract posted by: " + event.message.sender.username + " " + matched_pattern)
            #-1001803658184
            await client.pin_message(-1001803658184, message, notify=True)
        
with client:
    client.run_until_disconnected()

