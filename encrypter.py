# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:58:34 2018

@author: dgaviria6
"""

                                                                                
#%%


def encode(char):
    if char == 'a' or char == 'A':
        return '$'
    elif char == 'b' or char == 'B':
        return 'Π'
    elif char == 'c' or char == 'C':
        return 'Ψ'
    elif char == 'd' or char == 'D':
        return 'Ϋ'
    elif char == 'e' or char == 'E':
        return 'Φ'
    elif char == 'f' or char == 'F':
        return 'β'
    elif char == 'g' or char == 'G':
        return 'ζ'
    elif char == 'h' or char == 'H':
        return 'Ϫ'
    elif char == 'i' or char == 'I':
        return 'ѝ'
    elif char == 'j' or char == 'J':
        return 'Ѩ'
    elif char == 'k' or char == 'K':
        return 'Ѯ'
    elif char == 'l' or char == 'L':
        return 'Ӿ'
    elif char == 'm' or char == 'M':
        return 'Ӟ'
    elif char == 'n' or char == 'N':
        return '@'
    elif char == 'o' or char == 'O':
        return 'ƣ'
    elif char == 'p' or char == 'P':
        return '%'
    elif char == 'q' or char == 'Q':
        return '§'
    elif char == 'r' or char == 'R':
        return 'µ'
    elif char == 's' or char == 'S':
        return 'Æ'
    elif char == 't' or char == 'T':
        return 'Ð'
    elif char == 'u' or char == 'U':
        return '+'
    elif char == 'v' or char == 'V':
        return '£'
    elif char == 'w' or char == 'W':
        return '¢'
    elif char == 'x' or char == 'X':
        return 'ñ'
    elif char == 'y' or char == 'Y':
        return 'Ķ'
    elif char == 'z' or char == 'Z':
        return 'Ɣ'
    elif char == ' ':
        return '_'
    elif char == '.':
        return '.'
    elif char == ':':
        return ':'
    elif char == '!':
        return '!'
    elif char == '?':
        return '?'
    elif char == ',':
        return ','
    elif char == "'":
        return "'"
    elif char == '"':
        return '"'
    elif char == '0':
        return 'Ͳ'
    elif char == '1':
        return 'Δ'
    elif char == '2':
        return 'Ό'
    elif char == '3':
        return 'ί'
    elif char == '4':
        return 'ῢ'
    elif char == '5':
        return 'ῷ'
    elif char == '6':
        return 'ф'
    elif char == '7':
        return 'Ѧ'
    elif char == '8':
        return 'Ѹ'
    elif char == '9':
        return 'ҏ'   
    else:
        return '|'

def decode(char):
    if char == '$':
        return 'a'
    elif char == 'Π':
        return 'b'
    elif char == 'Ψ':
        return 'c'
    elif char == 'Ϋ' :
        return 'd'
    elif char == 'Φ':
        return 'e'
    elif char == 'β':
        return 'f'
    elif char == 'ζ':
        return 'g'
    elif char == 'Ϫ':
        return 'h'
    elif char == 'ѝ':
        return 'i'
    elif char == 'Ѩ':
        return 'j'
    elif char == 'Ѯ':
        return 'k'
    elif char == 'Ӿ':
        return 'l'
    elif char == 'Ӟ':
        return 'm'
    elif char == '@':
        return 'n'
    elif char == 'ƣ':
        return 'o'
    elif char == '%':
        return 'p'
    elif char == '§':
        return 'q'
    elif char == 'µ':
        return 'r'
    elif char == 'Æ':
        return 's'
    elif char == 'Ð':
        return 't'
    elif char == '+':
        return 'u'
    elif char == '£':
        return 'v'
    elif char == '¢':
        return 'w'
    elif char == 'ñ':
        return 'x'
    elif char == 'Ķ':
        return 'y'
    elif char == 'Ɣ':
        return 'z'
    elif char == '_':
        return ' '
    elif char == '.':
        return '.'
    elif char == ':':
        return ':'
    elif char == '!':
        return '!'
    elif char == '?':
        return '?'
    elif char == ',':
        return ','
    elif char == "'":
        return "'"
    elif char == '"':
        return '"'
    elif char == 'Ͳ':
        return '0'
    elif char == 'Δ':
        return '1'
    elif char == 'Ό':
        return '2'
    elif char == 'ί':
        return '3'
    elif char == 'ῢ':
        return '4'
    elif char == 'ῷ':
        return '5'
    elif char == 'ф':
        return '6'
    elif char == 'Ѧ':
        return '7'
    elif char == 'Ѹ':
        return '8'
    elif char == 'ҏ':
        return '9'     
    else:
        return ' '



print('This is an encoding and decoding machine.\n\n'
      'To encode something, enter "encode"\n'  
      'To decode something, enter "decode"\n' 
      'To quit process, enter "quit"')

started=True
while started:
    goal = input('\nCommand: ')
    if goal == 'encode':
        keyword = input('Phrase to encode: ')
        for letter in keyword:
            char = encode(letter)
            print(char, end='')
    elif goal == 'decode':
        keyword = input('Phrase to decode: ')
        for letter in keyword:
            char = decode(letter)
            print(char, end='')
    elif goal == 'quit':
        print('Done')
        started=False
    else:
        print('Unknown command, please enter either "encode", "decode", or "quit"')




    

