#!/usr/bin/python

# A script that acts as the GTS, for sending and receiving pokemon between a
# retail cart and a PC. Credit goes to LordLandon and his sendpkm script, as
# well as the description of the GTS protocol from
# http://projectpokemon.org/wiki/GTS_protocol
#
# - Infinite Recursion

from aux import gtsvar
from aux.pokehaxlib import initServ
from aux.getpkm import getpkm
from aux.sendpkm import sendpkm
from platform import system
from sys import argv, exit
from time import sleep
import os

s = system()
if s == 'Darwin' or s == 'Linux':
    if os.getuid() != 0:
        print 'Program must be run as superuser. Enter your password below',
        print 'if prompted.'
        os.system('sudo ' + argv[0] + ' root')
        exit(0)

print gtsvar.version

initServ()
sleep(1)

done = False
while True:
    print 'Choose an option:'
    print 's - send pkm to game', 'r - receive pkm from game'
    print 'm - receive multiple pkms from game', 'q - quit'
    option = raw_input().strip().lower()

    if option.startswith('s'): sendpkm()
    elif option.startswith('r'): getpkm()
    elif option.startswith('m'):
        print 'Press ctrl + c to return to main menu'
        while True:
            try: getpkm()
            except KeyboardInterrupt: break
    elif option.startswith('q'):
        print 'Quitting program'
        break
    else:
        print 'Invalid option, try again'
        continue

    print 'Returning to main menu'
