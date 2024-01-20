import time
from telethon.sync import TelegramClient, events
import re
import random

API_ID = 21870863
API_HASH = 'bf696e0beb52bb6084bb2262b3e6def2'
SEND_ID = -1002000028646  # Your group ID
SEND_ID2 = -1002085105108  # Your group ID

client = TelegramClient('session', API_ID, API_HASH)

# Existing channels for regular message handling
chats_to_scrape = [
    '@kurumichks',
    '@Sscrapper_CC',
    '@JohnnySinsChat',
    '@thePremiumBinsStore',
    '@ccxenchat',
    '@ApprovedCCSChat',
    '@botsakuraa',
    '@JulietteCC',
    '@finnBotChat',
    '@CRACKXCC',
    '@yatogamiiccs',
    '@nomorebins',
    '@fbcharged',
    '@ccnkiller',
    '@VepexChats',
    '@ChatKurama',
    '@TeamPLUTO',
    '@OnlyApproverd',
    '@PeezyChat',
    '@delta_free_users',
    '@KiraAccountsGrupo',
    '@sunchk1',
    '@Bins_Club',
    '@thePremiumBinsStore',
    '@ArthurChkGroup',
    '@Waste_Scrap',
    '@TechzillaChkChat',
    '@OficialScorpionsGrupo',
    '@RemChatChk',
    '@ReiAyanamiChat',
    '@KiraAccountsGrupo',
    '@BuddyXChatts',
    '@unknownstuffs',
    '@persian_cc_checker',
    '@professordonho',
    't.me/+1HB97b0UQQwyMzRl',
    '@D3MON_Giveaway',
    '@animeworldkkk',
    '@mibtw',
    '@liveccschat',
    '@CCSLIVES0',
    '@Outbullet',
    't.me/+ikk0HPeFDyRlZWQ1',
    'https://t.me/raven_ccs',
    '@OficialScorpionsGrupo'
]

# Additional channels for Auto Chk


keywords = ['Approved', '𝑨𝒑𝒑𝒓𝒐𝒗𝒆', 'Succeeded', 'Live CC', 'Charged', '𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝', 'CCN Live', 'Insufficient funds', 'Card Issuer Declined CVV', 'Gateway Rejected: cvv', '𝗽𝘂𝗿𝗰𝗵𝗮𝘀𝗲𝗱 𝗳𝗼𝗿 𝟬.𝟬𝟭$', 'CVV2/VAK Failure', '𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱', '𝐀𝐩𝐩𝐫𝐨𝐆𝐞𝐭𝐎𝐮𝐭𝐭𝐚', '𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫', 'Authenticate Successfu', 'Payment Successfull']

# Keep track of sent posts
sent_posts = set()

@client.on(events.NewMessage(chats=chats_to_scrape))
async def new_message_handler(event):
    print('New message event triggered')
    await process_message(event)

@client.on(events.MessageEdited(chats=chats_to_scrape))
async def edited_message_handler(event):
    print('Edited message event triggered')
    await process_message(event)

async def process_message(event):
    try:
        cleaned_text = event.raw_text
        
        # Check if any keyword is present in the text
        if any(keyword.upper() in cleaned_text.upper() for keyword in keywords):
            # Remove unwanted content (usernames, links, etc.)
            cleaned_text = re.sub(r'@\w+|http\S+', '', cleaned_text)
            
            # Check if the post has already been sent
            if cleaned_text not in sent_posts:
                # Send the approved post along with the "Checked By @C0LL_BR0KEN" message
                combined_message = f'{cleaned_text}\nChecked By @C0LL_BR0KEN'
                await client.send_message(SEND_ID, combined_message)
                await client.send_message(SEND_ID2, combined_message)

                
                # Add the post to the set of sent posts
                sent_posts.add(cleaned_text)
                
                print('Found Approved Card:', cleaned_text)
    except Exception as e:
        print(f"Error processing message: {e}")

client.start()
client.run_until_disconnected()
