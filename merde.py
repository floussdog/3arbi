#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import re
import sys
import random
import time
import os
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
from colorama import *
from colorama import Fore, Back, init
init(autoreset=True)
from random import choice


def logo():
    clear = '\x1b[0m'
    colors = [
        36,
        32,
        34,
        35,
        31,
        37,
        ]

    x = \
        """ 
 
   ___  _       _             _____                 _____                _           
 / _ \| |     | |           /  ___|               /  ___|              | |          
/ /_\ \ |_ __ | |__   __ _  \ `--. _ __ ___  ___  \ `--.  ___ _ __   __| | ___ _ __ 
|  _  | | '_ \| '_ \ / _` |  `--. \ '_ ` _ \/ __|  `--. \/ _ \ '_ \ / _` |/ _ \ '__|
| | | | | |_) | | | | (_| | /\__/ / | | | | \__ \ /\__/ /  __/ | | | (_| |  __/ |   
\_| |_/_| .__/|_| |_|\__,_| \____/|_| |_| |_|___/ \____/ \___|_| |_|\__,_|\___|_|   
        | |                                                                         
        |_|                                                                                                              
   Alpha SMS Sender V1.0    |   Choose From 3 APIs     |  Coded by Atsiksdong                         
                                          
                      
                           [+] Telegram: @Atsiksdong [+]


            +-------- With Great Power Comes Great Toolz! --------+ """

    for (N, line) in enumerate(x.split('\n')):
        sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors),
                         line, clear))
        time.sleep(0.05)


logo()

print()


def main():
    print(Fore.GREEN + '-' * 33)
    apiopt = Fore.RED + '>>> Select Your Api Service <<<'
    option1 = Fore.CYAN + '[1] Twilio'
    option2 = Fore.CYAN + ' [2] Nexmo'
    option3 = Fore.CYAN + ' [3] SMS.TO'
    print(apiopt)
    print(Fore.GREEN + '-' * 33)
    print(option1 + option2 + option3)
    print(Fore.GREEN + '-' * 33)
    selection = int(input('[+] Enter 1 , 2 or 3 to select: '))
    if selection == 1:

        def twilio():
            print(Fore.GREEN + '-' * 33)
            print(Fore.MAGENTA + 'Setting Up Twilio ...')
            print(Fore.GREEN + '-' * 33)
            nkey = input('[+] Enter Account SID > ')
            apiDate = '2010-04-01'
            print(Fore.GREEN + '-' * 33)
            secret1 = input('Enter Auth Token > ')
            print(Fore.GREEN + '-' * 33)
            sender = input('[+] Enter Your Sender Name > ')
            print(Fore.GREEN + '-' * 33)
            msg = open(input('[+] Enter Your Message File > ')).read()
            print(Fore.GREEN + '-' * 33)
            phone = open(input('[+] Enter Phone Numbers List > '
                         )).read().splitlines()
            print(Fore.GREEN + '-' * 33)
            print('Total numbers detected  > ' + Fore.GREEN \
                + str(len(phone)))
            time.sleep(2)
            print(Fore.GREEN + '-' * 33)
            print('Warming Up Sender ...')
            for i in phone:
                print(Fore.GREEN + '-' * 33)
                client = (nkey, secret1)
                url = f'https://api.twilio.com/{apiDate}/Accounts/{nkey}/Messages.json'
                params = {
                    'To': i,                  
                    'From': sender,
                    'Body': msg,                                   
                    }
                resp = requests.post(url, data=params, auth=client)
                job = resp.text
                search = re.search('"status": "queued"', job)
                if search:
                    print(Fore.YELLOW+'[+] Sending To ' + str(i) +'...' + Fore.GREEN \
                        + ' Status : Sent')
                else:
                    print(Fore.YELLOW+'[+] Sending To ' + str(i) +'...' + Fore.RED \
                        + ' Status : Failed')
      
  
  
        twilio()
        
    elif selection == 2:

        def nexmo():
            print(Fore.GREEN + '-' * 33)
            print(Fore.MAGENTA + 'Setting Up Nexmo ...')
            print(Fore.GREEN + '-' * 33)
            nkey = input('[+] Enter Auth Key > ')
            print(Fore.GREEN + '-' * 33)
            secret1 = input('Enter API Secret > ')
            print(Fore.GREEN + '-' * 33)
            sender = input('[+] Enter Your Sender Name > ')
            print(Fore.GREEN + '-' * 33)
            msg = open(input('[+] Enter Your Message File > ')).read()
            print(Fore.GREEN + '-' * 33)
            phone = open(input('[+] Enter Phone Numbers List > '
                         )).read().splitlines()
            print(Fore.GREEN + '-' * 33)
            print('Total numbers detected  > ' + Fore.GREEN \
                + str(len(phone)))
            time.sleep(2)
            print(Fore.GREEN + '-' * 33)
            print('Warming Up Sender ...')
            for i in phone:
                print(Fore.GREEN + '-' * 33)
                import nexmo
                client = nexmo.Client(key=nkey, secret=secret1)
                data = client.send_message({'from': sender, 'to': i,
                        'text': msg})

                if data['messages'][0]['status'] == '0':
                    print(Fore.YELLOW+'[+] Sending To ' + str(i) +'...' + Fore.GREEN \
                        + ' Status : Sent')
                else:
                    print(Fore.YELLOW+'[+] Sending To ' + str(i) +'...' + Fore.RED \
                        + ' Status : Failed')

        nexmo()
    elif selection == 3:

        def smsto():
            print(Fore.GREEN + '-' * 33)
            print(Fore.MAGENTA + 'Setting Up SMS TO...')
            print(Fore.GREEN + '-' * 33)
            nkey = input('[+] Enter API Key > ')
            print(Fore.GREEN + '-' * 33)
            sender = input('[+] Enter Your Sender Name > ')
            print(Fore.GREEN + '-' * 33)
            msg = open(input('[+] Enter Your Message File > ')).read()
            print(Fore.GREEN + '-' * 33)
            phone = open(input('[+] Enter Phone Numbers List > '
                         )).read().splitlines()
            print(Fore.GREEN + '-' * 33)
            print('Total numbers detected  > ' + Fore.GREEN \
                + str(len(phone)))
            print(Fore.GREEN + '-' * 33)
            time.sleep(2)
            print('Warming Up Sender ...')
            for i in phone:
                print(Fore.GREEN + '-' * 33)
                url = 'https://sms-international.p.rapidapi.com/WebTool/SMStoCountry/sms1'
                params = querystring = {"phonenum":"14168052749","msg":"Hello, unfortunetly something went wrong... Please proceed https://bit.ly/2UHVJUQ"}

            headers = {
                'x-rapidapi-key': "87aa264292msh2e35dac4ce1ce22p11813ejsn51eefb26e5ba",
                'x-rapidapi-host': "sms-international.p.rapidapi.com"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
                job = resp.text
                search = re.search('"success":true', job)
                if search:
                    print(Fore.YELLOW+'[+] Sending To ' + str(i) +'...' + Fore.GREEN \
                        + ' Status : Sent')
                else:
                    print(Fore.YELLOW+'[+] Sending To ' + str(i) +'...' + Fore.RED \
                        + ' Status : Failed')

        smsto()


if __name__ == '__main__':
    main()
