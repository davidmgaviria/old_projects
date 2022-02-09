# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 09:14:10 2018

@author: dgaviria6
"""

# Caesar Cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
     while True:
         print('Do you wish to encrypt or decrypt a message, or quit?')
         mode = input().lower()
         if mode in ['encrypt', 'e', 'decrypt', 'd', 'quit', 'q']:
             return mode
         else:
             print('Enter either "encrypt" or "e" or "decrypt" or "d" or "quit" or "q".')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
        else:
            print('Error: Key value is too large')

def getTranslatedMessage(mode, message, key):
     if mode[0] == 'd':
        key = -key
        translated = ''
     else:
        translated = ''

        for symbol in message:
            symbolIndex = SYMBOLS.find(symbol)
            if symbolIndex == -1: # Symbol not found in SYMBOLS.
                # Just add this symbol without any change.
                translated += symbol
            else:
                # Encrypt or decrypt.
                symbolIndex += key
   
                if symbolIndex >= len(SYMBOLS):
                    symbolIndex -= len(SYMBOLS)
                elif symbolIndex < 0:
                    symbolIndex += len(SYMBOLS)
   
                translated += SYMBOLS[symbolIndex]
        
        return translated


Running = True
while Running:
    mode = getMode()
    if mode == 'quit' or mode == 'q':
        print('Done')
        Running = False
    else:
        message = getMessage()
        key = getKey()
        print('Your translated text is:')
        print(getTranslatedMessage(mode, message, key), end='\n\n')
