import asyncio
import logging
import re
from time import sleep
import os
import sys
import random

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)



try:
   import colorama
   from colorama import Fore, Back, Style
   colorama.init(autoreset=True)
   hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
   res = Style.RESET_ALL
   abu2 = Style.DIM+Fore.WHITE
   putih = Style.RESET_ALL+Style.BRIGHT+Fore.WHITE
   ungu2 = Style.NORMAL+Fore.MAGENTA
   ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
   hijau2 = Style.NORMAL+Fore.GREEN
   yellow2 = Style.NORMAL+Fore.YELLOW
   yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
   red2 = Style.NORMAL+Fore.RED
   red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
   cyan = Style.RESET_ALL+Style.BRIGHT+Fore.CYAN
   cyan2 = Style.NORMAL+Fore.CYAN

except:
   print ("Please Install Modul Colorama!!\n\n\n")
   sys.exit()

try:
   import requests
   from bs4 import BeautifulSoup
except:
   print ("Please Install Modul Requests & BS4\n\n\n")
   sys.exit()

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 717425
api_hash = '322526d2c3350b1d3530de327cf08c07'

banner = """
\33[1;33mScript \33[31;1mwww.tuweb30.tk \33[1;33m🇵🇪Perú🇵🇪
"""
cname = '@Ethpaymnt_bot?start=1832537220'
crot = 'https://t.me/Ethpaymnt_bot'


def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

async def main():
	print (banner)
	#print(Fore.BLUE + ' \n' + Fore.RESET)
	# Check if phone number is not specified
	if len(sys.argv) < 2:
		print('Usa: python eth.py +51XXXXXXXXX')
		print('-> Ingresa tu número en formato internacional donde +51 es el codigo del pais\n')
		e = input('presiona una tecla para salir...')
		exit(1)

	phone_number = sys.argv[1]
	choice = '🎁 Claim'

	if not os.path.exists("session"):
		os.mkdir("session")
	# Connect to client
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()

	# Free_LTC_Robot
	#print_msg_time(Fore.GREEN + f'Name    : @Ethpaymnt_bot '  + Fore.RESET)
	print(f'\n')
	print_msg_time(Fore.GREEN + f'Bienvenido : {me.first_name} - {me.last_name} '  + Fore.RESET)
	print(f'\n')

	# Start command /balance

	i = 1
	while(True):
		await client.send_message(crot, choice)
		print_msg_time(Fore.GREEN + ' asistencia marcada! ' + Fore.RESET)
		sleep(3605) #waktu klik hitungan dalam detik
		i = 1

		# Message the bot
	@client.on(events.NewMessage(chats=cname, incoming=True))
	async def earned_amount(event):
		message = event.raw_text
		if 'Balance' in message:
			print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)


	await client.run_until_disconnected()

asyncio.get_event_loop().run_until_complete(main())
