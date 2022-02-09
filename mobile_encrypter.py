#Encryption key
############################
a = 'Δ'
b = 'µ'
c = 'Ӟ'
d = 'Ķ'
e = 'Ͳ'
f = 'ñ'
g = '$'
h = 'Ɣ'
i = 'Ϫ'
j = 'ф'
k = '%'
l = 'ѝ'
m = 'Π'
n = 'β'
o = 'Ϋ'
p = '¢'
q = 'ҏ'
r = 'ζ'
s = '£'
t = '@'
u = 'Ό'
v = 'Ѩ'
w = 'Ѧ'
x = 'ῢ'
y = 'Ӿ'
z = 'ƣ'
zero = '§'
one = 'ί'
two = 'Ð'
three = 'ῷ'
four = 'Ψ'
five ='Æ'
six = 'Φ'
seven = '+'
eight = 'Ѯ'
nine = 'Ѹ'
###############################


def encode(char):
    if char == 'a' or char == 'A':
        return a
    elif char == 'b' or char == 'B':
        return b
    elif char == 'c' or char == 'C':
        return c
    elif char == 'd' or char == 'D':
        return d
    elif char == 'e' or char == 'E':
        return e
    elif char == 'f' or char == 'F':
        return f
    elif char == 'g' or char == 'G':
        return g
    elif char == 'h' or char == 'H':
        return h
    elif char == 'i' or char == 'I':
        return i
    elif char == 'j' or char == 'J':
        return j
    elif char == 'k' or char == 'K':
        return k
    elif char == 'l' or char == 'L':
        return l
    elif char == 'm' or char == 'M':
        return m
    elif char == 'n' or char == 'N':
        return n
    elif char == 'o' or char == 'O':
        return o
    elif char == 'p' or char == 'P':
        return p
    elif char == 'q' or char == 'Q':
        return q
    elif char == 'r' or char == 'R':
        return r
    elif char == 's' or char == 'S':
        return s
    elif char == 't' or char == 'T':
        return t
    elif char == 'u' or char == 'U':
        return u
    elif char == 'v' or char == 'V':
        return v
    elif char == 'w' or char == 'W':
        return w
    elif char == 'x' or char == 'X':
        return x
    elif char == 'y' or char == 'Y':
        return y
    elif char == 'z' or char == 'Z':
        return z
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
        return zero
    elif char == '1':
        return one
    elif char == '2':
        return two
    elif char == '3':
        return three
    elif char == '4':
        return four
    elif char == '5':
        return five
    elif char == '6':
        return six
    elif char == '7':
        return seven
    elif char == '8':
        return eight
    elif char == '9':
        return nine   
    else:
        return '|'


def decode(char):
    if char == a:
        return 'a'
    elif char == b:
        return 'b'
    elif char == c:
        return 'c'
    elif char == d :
        return 'd'
    elif char == e:
        return 'e'
    elif char == f:
        return 'f'
    elif char == g:
        return 'g'
    elif char == h:
        return 'h'
    elif char == i:
        return 'i'
    elif char == j:
        return 'j'
    elif char == k:
        return 'k'
    elif char == l:
        return 'l'
    elif char == m:
        return 'm'
    elif char == n:
        return 'n'
    elif char == o:
        return 'o'
    elif char == p:
        return 'p'
    elif char == q:
        return 'q'
    elif char == r:
        return 'r'
    elif char == s:
        return 's'
    elif char == t:
        return 't'
    elif char == u:
        return 'u'
    elif char == v:
        return 'v'
    elif char == w:
        return 'w'
    elif char == x:
        return 'x'
    elif char == y:
        return 'y'
    elif char == z:
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
    elif char == zero:
        return '0'
    elif char == one:
        return '1'
    elif char == two:
        return '2'
    elif char == three:
        return '3'
    elif char == four:
        return '4'
    elif char == five:
        return '5'
    elif char == six:
        return '6'
    elif char == seven:
        return '7'
    elif char == eight:
        return '8'
    elif char == nine:
        return '9'     
    else:
        return ' '



started=True
while started:
    goal = input('Type "encode" or "decode"')
    if goal == 'encode':
        keyword = input('Phrase to encode: ')
        for letter in keyword:
            char = encode(letter)
            print(char, end='')
        started=False
        print("\n\n  ")
    elif goal == 'decode':
        keyword = input('Phrase to decode: ')
        for letter in keyword:
            char = decode(letter)
            print(char, end='')
        started=False
        print("\n\n  ")
    else:
        pass