from about import *
from igprocess import *
from smsprocess import *
from callprocess import *
from checkconnection import *
from wpprocess import *
import time
import platform


if platform.system() == 'Linux':
    linux = True
    pass
elif platform.system() == 'Windows':
    linux = False
    pass
else:
    print('OS not supported !')
    exit()

s1 = ''

while s1 != '6' or s1 != 'exit' or s1 != 'exit script':
    about()
    checkinternet()
    s1 = input('''
    |-PRESS---------------|
    | 1] Call Bomber      |
    | 2] SMS Bomber       |
    | 3] Instagram Bomber |
    | 4] WhatsApp Bomber  |
    | 5] About            |
    | 6] Exit Script      |
    |---------------------|
    |-> ''')

    s1 = s1.lower()

    if s1 == '6' or s1 == 'exit' or s1 == 'exit script':
        exit()

    elif s1 == '3' or s1 == 'instagram bomber':
        if linux:
            igbombinglinux()
        elif linux == False:
            igbombingwin()
        time.sleep(2)
    
    elif s1 == '5' or s1 == 'about':
        pass
    
    elif s1 == '4' or s1 == 'whatsapp bomber':
        if linux:
            wpbombinglinux()
        elif linux == False:
            wpbombingwin()
        time.sleep(2)

    elif s1 == '2' or s1 == 'sms bomber':
        if linux:
            smsbombinglinux()
        elif linux == False:
            smsbombingwin()
        time.sleep(2)

    elif s1 == '1' or s1 == 'call bomber':
        callbombing()
        time.sleep(2)

    else:
        print("    |-} Sorry I didn't get it !")
        time.sleep(2)
